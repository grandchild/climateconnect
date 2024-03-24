import { alpha, createTheme } from "@mui/material/styles";
import { grey } from "@mui/material/colors";

declare module "@mui/material" {
  interface Color {
    main: string;
    dark: string;
    light?: string;
  }
}

declare module "@mui/material/Button" {
  interface ButtonPropsColorOverrides {
    grey: true;
  }
}

/* HiH colors from website: */
// "primary":   "#F17E2B",
// "secondary": "#9263A7",
// "text":      "#5C5C5C",
// "accent":    "#E83935",
// "298c2d3":   "#F4E7D6",
// "875f2cc":   "#9263A780",
// "6fe6a9d":   "#1E5F8E",
// "3a7a41c":   "#2F2F2F",
// "5541122":   "#FFFFFF",

// Create core theme so we can access spacing etc. when customizing components
const coreTheme = createTheme({
  palette: {
    primary: {
      // main: "hsl(185, 58%, 30%)",
      // light: "hsl(175, 39%, 57%)",
      // lightHover: "hsl(175, 48%, 65%)",
      // extraLight: "hsl(176, 67%, 91%)",
      main: "hsl(25, 88%, 56%)",
      light: "hsl(30, 89%, 67%)",
      lightHover: "hsl(30, 93%, 70%)",
      extraLight: "hsl(30, 94%, 91%)",
    },
    secondary: {
      // main: "#484848",
      // light: "#484848c2",
      // extraLight: "#EBEBEB",
      main: "hsl(281, 28%, 52%)",
      light: "hsla(281, 28%, 52%, 0.7)",
      extraLight: "hsl(281, 28%, 95%)",
    },
    yellow: {
      // main: "#FFDE0A",
      main: "#9966aa",
    },
    background: {
      default: "#FFF",
    },
    action: {
      // selected: "#387077",
      selected: "#F17E2B",
    },
    grey: {
      light: grey[100],
      main: grey[300],
      dark: grey[400],
    },
  },
  typography: {
    fontFamily: "Open Sans",
    h1: {
      fontSize: "3rem",
      align: "center",
    },
    subtitle1: {
      fontSize: "0.9rem",
    },
    subtitle2: {
      fontSize: "0.9rem",
      fontWeight: "bold",
    },
    button: {
      fontWeight: 600,
    },
    /* TOOD: climateMatch: {
          fontFamily: "flood-std, sans-serif",
          fontWeight: 300,
        },*/
  },
});

/**
 * Extend on top of the core foundational theme (currently spacing
 * and color) with other design tokens, and component-specific overrides.
 *
 * For example, we can start defining consistency for borders, and other
 * styling primitives here, to minimize the duplication of raw styles
 * across other files.
 */
const theme = createTheme(coreTheme, {
  components: {
    MuiCssBaseline: {
      styleOverrides: `
        @import url("https://p.typekit.net/p.css?s=1&k=hoy3dgi&ht=tk&f=18085&a=35847266&app=typekit&e=css");

        @font-face {
        font-family:"flood-std";
        src:url("https://use.typekit.net/af/6da923/000000000000000000012fc3/27/l?primer=7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191&fvd=n4&v=3") format("woff2"),url("https://use.typekit.net/af/6da923/000000000000000000012fc3/27/d?primer=7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191&fvd=n4&v=3") format("woff"),url("https://use.typekit.net/af/6da923/000000000000000000012fc3/27/a?primer=7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191&fvd=n4&v=3") format("opentype");
        font-display:auto;font-style:normal;font-weight:400;font-stretch:normal;
        }

        .tk-flood-std { font-family: "flood-std",sans-serif; }
      `,
    },
    MuiButton: {
      variants: [
        {
          props: { variant: "contained", color: "grey" },
          style: {
            color: coreTheme.palette.getContrastText(coreTheme.palette.grey[300]),
          },
        },
        {
          props: { variant: "outlined", color: "grey" },
          style: {
            color: coreTheme.palette.text.primary,
            borderColor:
              coreTheme.palette.mode === "light"
                ? "rgba(0, 0, 0, 0.23)"
                : "rgba(255, 255, 255, 0.23)",
            "&.Mui-disabled": {
              border: `1px solid ${coreTheme.palette.action.disabledBackground}`,
            },
            "&:hover": {
              borderColor:
                coreTheme.palette.mode === "light"
                  ? "rgba(0, 0, 0, 0.23)"
                  : "rgba(255, 255, 255, 0.23)",
              backgroundColor: alpha(
                coreTheme.palette.text.primary,
                coreTheme.palette.action.hoverOpacity
              ),
            },
          },
        },
      ],
      defaultProps: {
        disableElevation: true,
      },
      styleOverrides: {
        containedSizeMedium: {
          borderRadius: 3,
          paddingLeft: coreTheme.spacing(4),
          paddingRight: coreTheme.spacing(4),
          paddingTop: coreTheme.spacing(1),
          paddingBottom: coreTheme.spacing(1),
        },
      },
    },
    MuiTab: {
      styleOverrides: {
        root: {
          minWidth: 0,
          [coreTheme.breakpoints.up("xs")]: {
            minWidth: 0,
          },
        },
      },
    },
    MuiTooltip: {
      styleOverrides: {
        tooltip: {
          fontSize: 14,
        },
      },
    },
    MuiChip: {
      variants: [
        {
          props: { variant: "filled", color: "secondary" },
          style: {
            background: "#e0e0e0",
            color: coreTheme.palette.secondary.main,
            "&:hover": {
              background: "#cacaca",
            },
          },
        },
      ],
      styleOverrides: {
        root: {
          // Have the same border-radius as the other UI controls, like
          // the select dropdowns, buttons, etc.
          borderRadius: 4,
        },
        deleteIconColorSecondary: {
          color: coreTheme.palette.secondary.main,
          "&:hover": {
            color: coreTheme.palette.secondary.light,
          },
        },
        clickable: {
          "&:hover": {
            background: "#cacaca",
          },
        },
      },
    },
    MuiLink: {
      defaultProps: {
        underline: "hover",
      },
    },
  },
});

export default theme;
