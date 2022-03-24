import {
    Avatar,
    Button,
    Checkbox,
    Chip,
    Container,
    IconButton,
    TextField,
    Tooltip,
    Typography,
    useMediaQuery,
  } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";
import KeyboardBackspaceIcon from "@material-ui/icons/KeyboardBackspace";
import React, { useContext } from "react";
import { getLocalePrefix } from "../../../public/lib/apiOperations";
import { getLocationFields } from "../../../public/lib/locationOperations";
import getTexts from "../../../public/texts/texts";
import UserContext from "../context/UserContext";
import Form from "./../general/Form";

const useStyles = makeStyles((theme) => {
  return {
    backButton: {
        float: "left",
      },
  cancelButton: {
    top: theme.spacing(16.5),
    [theme.breakpoints.up("md")]: {
      top: theme.spacing(6.5),
    },
  },
      actionButton: {
        position: "absolute",
        right: theme.spacing(1),
        width: theme.spacing(18),
        [theme.breakpoints.down("sm")]: {
          width: theme.spacing(14),
          fontSize: 10,
          textAlign: "center",
        },
      },
  };
});

export default function AddInterests({
  handleSubmit,
  handleSkip,
  errorMessage,
  values,
  handleGoBack,
}) {
    const classes = useStyles();

    // hier muss die karte gebaut werden
  return (<div>
      
    {/* <ActiveHubsSelect
      info={i}
      hubsToSelectFrom={allHubs.filter(
        (h) =>
          editedAccount?.info?.hubs.filter((addedHub) => addedHub.url_slug === h.url_slug)
            .length === 0
      )}
      onClickRemoveHub={onClickRemoveHub}
      selectedHubs={editedAccount.info.hubs}
      onSelectNewHub={onSelectNewHub}
    /> */}
            <IconButton
              size="small"
              className={classes.backButton}
              onClick={(event, values) => handleGoBack(event, values)}
            >
              <KeyboardBackspaceIcon />
            </IconButton>
    <Button
            className={`${classes.cancelButton} ${classes.actionButton}`}
            color="secondary"
            variant="contained"
            onClick={(event, values) => handleSkip(event, values)}
          >
            Skip
    </Button>
    <Button
            className={`${classes.cancelButton} ${classes.actionButton}`}
            color="secondary"
            variant="contained"
            onClick={(event, values) => handleSubmit(event, values)}
          >
            Submit
          </Button>
    </div>
  );
}
