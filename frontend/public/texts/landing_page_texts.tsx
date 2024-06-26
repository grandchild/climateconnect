import React from "react";

export default function getLandingPageTexts({ classes, isNarrowScreen }) {
  return {
    be_part_of_the_community: {
      en: (
        <>
          <span className={classes?.yellow}>Be part</span> of the community
        </>
      ),
      de: (
        <>
          <span className={classes?.yellow}>Sei Teil</span> der Community
        </>
      ),
    },
    be_part_of_the_community_text: {
      en: `Sign up to Climate Connect - it's free! By signing up you can work together and
      share knowledge and experiences with people taking climate action globally and in your home
      town.`,
      de: `Melde dich bei Climate Connect an - es ist kostenlos! Wenn du dich anmeldest, kannst du
      mit Menschen zusammenarbeiten und Erfahrungen austauschen, die sich weltweit und in deiner Heimatstadt
      für den Klimaschutz engagieren.`,
    },
    whether_youre_working_on_climate_action_fulltime: {
      en:
        "Whether you're working on climate action fulltime, on a volunteer basis or are just looking for what to do against climate change, we're all part of #teamclimate.",
      de:
        "Egal, ob du dich hauptberuflich oder ehrenamtlich für den Klimaschutz engagierst oder einfach nur wissen willst, was Du gegen den Klimawandel tun kannst - wir sind alle Teil von #teamclimate.",
    },
    landing_page_photo_alt: {
      en: "",
      de: "",
    },
    from_around_the_world: {
      en: "from all of Germany",
      de: "aus ganz Deutschland",
    },
    //html tag is break point for mobile. Should be roughly in the middle of the sentence
    landing_page_text: {
      en: (
        <>
          Join the action network to connect all
          {!isNarrowScreen ? <br /> : " "}
          supporters of democracy
        </>
      ),
      de: (
        <>
          Komm ins überregionale Netzwerk, das alle
          {!isNarrowScreen ? <br /> : " "}
          Demokratie-Unterstützer:innen verbindet
        </>
      ),
    },
    explore: {
      en: "Explore",
      de: "Entdecken",
    },
    explore_climate_projects: {
      en: "Explore projects supporting democracy",
      de: "Entdecke Demokratieförderprojekte",
    },
    find_a_climate_action_organization_and_get_involved: {
      en: "Find a democratic action organization and get involved",
      de: "Finde eine Demokratieförderorganisation und bringe dich ein",
    },
    find_a_climate_action_organization_and_get_involved_text: {
      en: `Find groups, associations, companies, institutes, NGOs, non-profits, local governments and other
      types of organizations taking democratic action!`,
      de: `Finde Gruppen, Verbände, Unternehmen, Institute, Nicht-Regierungs-Organisationen, Non-Profit-Organisationen, lokale Regierungen und
      andere Arten von Organisationen, die sich für unsere Demokratie einseten!`,
    },
    find_a_climate_action_organization_and_get_involved_additional_text: {
      en: `You can directly contact the organization's representative to exchange knowledge,
      find volunteering opportunities or job opportunites.`,
      de: `Du kannst direkt den Repräsentanten der Organisation kontaktieren um Wissen auszutauschen und
      zu lernen, wie du dich einbringen kannst.`,
    },
    explore_all_organizations: {
      en: "Explore all organizations",
      de: "Entdecke alle Organisationen",
    },
    who_we_are: {
      en: "Who we are",
      de: "Wer wir sind",
    },
    find_out_more_about_our_team: {
      en: "Find out about our team",
      de: "Lerne unser Team kennen",
    },
    and_why_we_are_doing_what_we_are_doing: {
      en: "and why we are doing what we are doing",
      de: "und warum wir tun, was wir tun",
    },
    open_hand_offering_a_seedling_with_a_heart_instead_of_leaves: {
      en: "Open hand offering a seedling with a heart instead of leaves",
      de: "Offene Hand, die einen Setzling mit einem Herz anstelle von Blättern anbietet",
    },
    our_mission: {
      en: "Our Mission",
      de: "Unsere Mission",
    },
    learn_about_our_goals_and_values: {
      en: "Learn about our goals and values",
      de: "Erfahre mehr über unsere Ziele und Werte",
    },
    and_what_we_want_to_achieve_with_creating_a_climate_community: {
      en: "and what we want to achieve with creating a climate community",
      de: "und was wir durch den Aufbau einer Klimaschutz Community erreichen wollen ",
    },
    five_people_positioned_around_a_globe_connected_through_lines: {
      en: "5 people positioned around a globe connected through lines",
      de: "5 Personen, die um einen Globus positioniert und durch Linien verbunden sind",
    },
    man_floating_in_the_air_with_a_lightbulb_a_book_a_pen_a_notebook_a_baloon_and_saturn_floating_around_him: {
      en:
        "Man floating in the air with a lightbulb, a book, a pen, a notebook, a baloon and Saturn floating around him",
      de:
        "Mann schwebt in der Luft mit einer Glühbirne, einem Buch, einem Stift, einem Notizbuch, einem Ballon und dem Saturn, der um ihn herum schwebt",
    },
    four_people_at_a_table_working_together_and_giving_each_other_a_high_five: {
      en: "Four people at a table working together and giving each other a high five",
      de: "Vier Personen an einem Tisch arbeiten zusammen und geben sich gegenseitig ein High Five",
    },
    start_now_banner_text: {
      en: (
        <>
          <span className={classes?.yellow}>Work together</span>, feel inspired and make a real
          impact <span className={classes?.yellow}>on our democracy!</span>
        </>
      ),
      de: (
        <>
          <span className={classes?.yellow}>Arbeite zusammen</span>, lass dich inspirieren und nimm
          echten Einfluss <span className={classes?.yellow}>auf unsere Demokratie!</span>
        </>
      ),
    },
    democratic_projects_with: {
      en: "democratic projects",
      de: "Demokratieprojekten",
    },
    learn_from: {
      en: "Learn from",
      de: "Lerne von",
    },
  };
}
