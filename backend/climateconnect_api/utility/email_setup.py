from datetime import datetime, timedelta
from climateconnect_api.models.notification import EmailNotification
import logging

from typing import List

from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from climateconnect_api.models.user import UserProfile
from organization.models.project import Project
from organization.models.organization import Organization
from organization.models.members import OrganizationMember
from ideas.models.ideas import Idea 
from climateconnect_api.utility.translation import (get_user_lang_code,
                                                    get_user_lang_url)
from django.conf import Settings, settings
from mailjet_rest import Client

logger = logging.getLogger(__name__)

mailjet_send_api = Client(auth=(settings.MJ_APIKEY_PUBLIC, settings.MJ_APIKEY_PRIVATE), version='v3.1')
mailjet_api = Client(auth=(settings.MJ_APIKEY_PUBLIC, settings.MJ_APIKEY_PRIVATE))


def get_template_id(template_key, lang_code):
    if not lang_code == "en":
        return getattr(settings, template_key + "_" + lang_code.upper())
    else:
        return getattr(settings, template_key)


def check_send_email_notification(user):
    three_hours_ago = datetime.now() - timedelta(hours=3)
    recent_email_notification = EmailNotification.objects.filter(
        user=user,
        created_at__gte=three_hours_ago
    )
    return not recent_email_notification.exists()


def send_email(
    user,
    variables,
    template_key,
    subjects_by_language,
    should_send_email_setting,
    notification
):
    if not check_send_email_notification(user):
        return
    if should_send_email_setting:
        try:
            user_profile = UserProfile.objects.get(user=user)
            # short circuit if the user has changed his settings to not
            # receive emails on this topic
            if not getattr(user_profile, should_send_email_setting):
                return
        except UserProfile.DoesNotExist:
            print("there is no user profile (send_email)")
    lang_code = get_user_lang_code(user)
    subject = subjects_by_language[lang_code]
    template_id = get_template_id(
        template_key=template_key,
        lang_code=lang_code
    )
    data = {
        'Messages': [
            {
                "From": {
                    "Email": settings.CLIMATE_CONNECT_SUPPORT_EMAIL,
                    "Name": "Climate Connect"
                },
                "To": [
                    {
                        "Email": user.email,
                        "Name": user.first_name + " " + user.last_name
                    }
                ],
                "TemplateID": int(template_id),
                "TemplateLanguage": True,
                "Variables": variables,
                "Subject": subject,
                "TemplateErrorReporting": {
                    "Email": settings.MAILJET_ADMIN_EMAIL,
                    "Name": "Mailjet Admin"
                }
            }
        ]
    }

    try:
        mail = mailjet_send_api.send.create(data=data)
        if notification:
            EmailNotification.objects.create(
                user=user,
                created_at=datetime.now(),
                notification=notification
            )
        return mail
    except Exception as ex:
        logger.error("%s: Error sending email: %s" % (
            send_email.__name__, ex
        ))

def get_user_verification_url(verification_key, lang_url):
    # TODO: Set expire time for user verification
    verification_key_str = str(verification_key).replace("-", "%2D")
    url = ("%s%s/activate/%s" % (
        settings.FRONTEND_URL, lang_url, verification_key_str
    ))

    return url

def get_new_email_verification_url(verification_key, lang_url):
    #TODO: Set expire time for new email verification
    verification_key_str = str(verification_key).replace("-", "%2D")
    url = ("%s%s/activate_email/%s" % (
        settings.FRONTEND_URL, lang_url, verification_key_str
    ))

    return url

def get_reset_password_url(verification_key, lang_url):
    #TODO: Set expire time for new email verification
    verification_key_str = str(verification_key).replace("-", "%2D")
    url = ("%s%s/reset_password/%s" % (
        settings.FRONTEND_URL, lang_url, verification_key_str
    ))

    return url


def send_user_verification_email(user, verification_key):
    lang_url = get_user_lang_url(get_user_lang_code(user))
    url = get_user_verification_url(verification_key, lang_url)

    subjects_by_language = {
        "en": "Welcome to Climate Connect! Verify your email address",
        "de": "Willkommen bei Climate Connect! Verifiziere deine Email-Adresse!"
    }

    variables =  {
        "FirstName": user.first_name,
        "url": url
    }
    send_email(
        user=user,
        variables=variables,
        template_key="EMAIL_VERIFICATION_TEMPLATE_ID",
        subjects_by_language=subjects_by_language,
        should_send_email_setting="",
        notification=None
    )

def send_new_email_verification(user, new_email, verification_key):
    lang_url = get_user_lang_url(get_user_lang_code(user))
    url = get_new_email_verification_url(verification_key, lang_url)

    subjects_by_language = {
        "en": "Verify your new email address",
        "de": "Bestätige deine neue Email Adresse"
    }

    variables =  {
        "FirstName": user.first_name,
        "url": url,
        "NewMail": new_email
    }
    send_email(
        user=user,
        variables=variables,
        template_key="NEW_EMAIL_VERIFICATION_TEMPLATE_ID",
        subjects_by_language=subjects_by_language,
        should_send_email_setting="",
        notification=None
    )

def send_password_link(user, password_reset_key):
    lang_url = get_user_lang_url(get_user_lang_code(user))
    url = get_reset_password_url(password_reset_key, lang_url)

    subjects_by_language = {
        "en": "Reset your Climate Connect password",
        "de": "Setze deine Climate Connect Passwort zurück"
    }

    variables =  {
        "FirstName": user.first_name,
        "url": url
    }
    send_email(
        user=user,
        variables=variables,
        template_key="RESET_PASSWORD_TEMPLATE_ID",
        subjects_by_language=subjects_by_language,
        should_send_email_setting="",
        notification=None
    )

def send_feedback_email(email, message, send_response):
    data = {
        'Messages': [
            {
                "From": {
                    "Email": settings.CLIMATE_CONNECT_SUPPORT_EMAIL,
                    "Name": "Climate Connect"
                },
                "To": [
                    {
                        "Email": "contact@climateconnect.earth",
                        "Name": "Climate Connect"
                    }
                ],
                "TemplateID": int(settings.FEEDBACK_TEMPLATE_ID),
                "TemplateLanguage": True,
                "Subject": "Climate Connect User Feedback",
                "Variables": {
                    "text": str(message),
                    "sendReply": str(send_response),
                    "email": str(email if email else "")
                }
            }
        ]
    }
    print(data)

    try:
        mailjet_send_api.send.create(data=data)
    except Exception as ex:
        print("%s: Error sending email: %s" % (
            send_user_verification_email.__name__, ex
        ))

def register_newsletter_contact(email_address):
    old_contact = mailjet_api.contact.get(email_address)
    if old_contact.status_code == 404:
        contact_id = create_contact(email_address)
    if old_contact.status_code == 200:
        result = old_contact.json()
        contact_id = result['Data'][0]['ID']
    add_contact_to_list(contact_id, settings.MAILJET_NEWSLETTER_LIST_ID)

def create_contact(email_address):
    data = {
        'IsExcludedFromCampaigns': "true",
        'Email': email_address
    }
    new_contact = mailjet_api.contact.create(data=data)
    result = new_contact.json()
    return result['Data'][0]['ID']

def add_contact_to_list(contact_id, list_id):
    data = {
        'ContactID': contact_id,
        'ListID': list_id
    }
    result = mailjet_api.listrecipient.create(data=data)
    if not result.status_code == 201:
        logger.error(result.status_code)
        logger.error("Could not add contact "+str(contact_id)+" to list "+str(list_id))
    return True

def unregister_newsletter_contact(email_address):
    contact = mailjet_api.contact.get(email_address)
    if contact.status_code == 200:
        result = contact.json()
        contact_id = result['Data'][0]['ID']
        remove_contact_from_list(contact_id, settings.MAILJET_NEWSLETTER_LIST_ID)
    else:
        logging.error(contact.status_code)


def remove_contact_from_list(contact_id, list_id):
    data = {
        'ContactsLists': [
            {
                'Action': "remove",
                'ListID': list_id
            }
        ]
    }
    mailjet_api.contact_managecontactslists.create(id=contact_id, data=data)


def create_global_variables_for_weekly_recommendations(project_ids: List = [], organization_ids: List = [], idea_ids: List = [], is_in_hub: bool = False) -> List:
    main_page = "https://climateconnect.earth"

    entities = []

    projects = Project.objects.filter(id__in=project_ids).values_list("name", "thumbnail_image", "url_slug", "loc__name", "project_parent__parent_user__first_name", "project_parent__parent_user__last_name")
    for project in projects:
        project_template = {
            "type": "project",
            "name": project[0],
            "imageUrl": (settings.BACKEND_URL + project[1]) if project[1] else main_page,
            "url": (settings.FRONTEND_URL + "/projects/" + project[2]) if project[2] else main_page,
            "location": project[3] if project[3] and not is_in_hub else '',
            "creator": project[4] + ' ' + project[5] if (project[4] and project[5]) else '',
            "tags": '',
        }
        entities.append(project_template)

    organizations = Organization.objects.filter(id__in=organization_ids).values_list("name", "thumbnail_image", "url_slug", "location__name", "id")
    for organization in organizations:
        org_creators = OrganizationMember.objects.filter(organization__id=organization[4], role__role_type=2).values_list("user__first_name", "user__last_name")
        creator = ''
        # only one creator possible but the query needs to be iterated through
        for org_creator in org_creators:
            creator += org_creator[0] + " " + org_creator[1]
        organization_template = {
            "type": "organization",
            "name": organization[0],
            "imageUrl": (settings.BACKEND_URL + organization[1]) if organization[1] else '',
            "url": (settings.FRONTEND_URL + "/organizations/" + organization[2]) if organization[2] else main_page,
            "location": organization[3] if organization[3] and not is_in_hub else '',
            "creator": creator,
            "tags": '',
        }
        entities.append(organization_template)

    ideas = Idea.objects.filter(id__in=idea_ids).values_list("name", "thumbnail_image", "url_slug", "location__name", "user__first_name", "user__last_name", "hub__url_slug")
    for idea in ideas:
        idea_template = {
            "type": "idea",
            "name": idea[0],
            "imageUrl": (settings.BACKEND_URL + idea[1]) if idea[1] else '',
            # url for ideas: URL/hubs/<hubUrl>?idea=<slug>#ideas
            "url": (settings.FRONTEND_URL + "/hubs/"+ idea[6] + "?idea=" + idea[2] + "#ideas") if idea[2] else main_page,
            "location": idea[3] if idea[3] and not is_in_hub else '',
            "creator": idea[4] + ' ' + idea[5] if idea[4] and idea[5] else '',
            "tags": '',
        }
        entities.append(idea_template)
    return entities


def create_messages_for_weekly_recommendations(chunked_user_info) -> List:
    # ("user__email", "user__first_name", "user__last_name")
    messages = []
    for user in chunked_user_info:
        messages.append(
        {
                    "To": [
                        {
                            "Email": user[0],
                            "Name": user[1] + " " + user[2]
                        }
                    ],
                    "Variables": {"FirstName": user[1]},
                }
        )
    return messages


def send_weekly_recommendations_email(messages: List, entities: List, lang_code: str, is_in_hub: bool = False, sandbox_mode = False):

    template_key = "WEEKLY_RECOMMENDATIONS_EMAIL"
    
    template_id = get_template_id(
        template_key=template_key,
        lang_code=lang_code
    )

    if is_in_hub:
        subjects_by_language = {
            "en": "We have new recommendations in your area!",
            "de": "Wir haben neue Empfehlungen in deiner Region", 
        }
    else:
        subjects_by_language = {
            "en": "We have new recommendations for you!",
            "de": "Wir haben neue Empfehlungen für dich!", 
        }

    subject = subjects_by_language.get(lang_code, "en")


    global_variables = {
        "Entities": entities,
    }


    data = {
        'Globals': {
            "From": {
                    "Email": settings.CLIMATE_CONNECT_SUPPORT_EMAIL,
                    "Name": "Climate Connect"
                },
            "TemplateID": int(template_id),
            "TemplateLanguage": True,
            "Variables": global_variables,
            "Subject": subject,
            "TemplateErrorReporting": {
                "Email": settings.MAILJET_ADMIN_EMAIL,
                "Name": "Mailjet Admin"
            },
        },
        'Messages': messages,
        'SandboxMode': sandbox_mode
    }

    try:
        mail = mailjet_send_api.send.create(data=data)
    except Exception as ex:
        logger.error(f"EmailFailure: Exception sending email -> {ex}")

    if mail.status_code != 200:
        logger.error(f"EmailFailure: Error sending email -> {mail.text}")

    # debugging
    return mail

