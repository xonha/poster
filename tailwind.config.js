/** @type {import('tailwindcss').Config} */

module.exports = {
  content: ["./src/app/**/*.{html,js}"],
  plugins: [],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Roboto", "sans-serif"],
      },
      colors: {
        "base-background": "#FFF",
        brand: {
          DEFAULT: "#F8FBFF",
        },
        heroBackground: "rgba(2, 20, 65, 0.7)",
        badge: {
          faculty: "#FFEFB7",
          "faculty-text": "#DB9A22",
          moderator: "#FFE8D2",
          "moderator-text": "#E77C4F",
          do: "#C5EFE7",
          "do-text": "#29978A",
          pa: "#CBD8FA",
          "pa-text": "#4B5C86",
          common: "#E7D9F9",
          "common-text": "#8E5FB8",
        },
        derm2derm: {
          green: {
            DEFAULT: "#00A89C",
            100: "#7BEDE5",
          },
          neutral: {
            100: "#F5F5F5",
            500: "#737373",
            600: "#525252",
            800: "#262626",
            800: "#171717",
          },
        },
      },
      spacing: {
        "h-navbar": "65px",
        "w-sidebar": "400px",
      },
      backgroundColor: {
        "transparent-blue": "rgba(2, 20, 65, 0.70)",
      },
      backgroundImage: {
        account:
          "linear-gradient(to right bottom, rgba(2, 20, 65, 0.8), rgba(2, 20, 65, 0.8)), url('/images/hospital-tool.png')",
        "about-us": "url('/images/heroSection/shapelined.jpg')",
        featuredVideo:
          "linear-gradient(180deg, rgba(0, 0, 0, 0) 0%, rgba(0, 0, 0, 0.5) 24.48%, #000000 100%)",
        derm2dermlp: "linear-gradient(to bottom, #ffffff 50%, #00A89C 200%)",
        searchBar: "linear-gradient(180deg, #021441 0%, #0D0D0D 100%)",
      },
      boxShadow: {
        personCard: "0px 2px 24px 4px rgba(0, 0, 0, 0.03)",
        searchModal:
          "0px 10px 10px -5px rgba(0,0,0,0.04), 0px 20px 25px -5px rgba(0,0,0,0.10)",
        input: "0px_1px_2px_0px_rgba(0,0,0,0.05)",
        slidePageHeader: "0px -1px 7px 0px rgba(0, 0, 0, 0.25)",
      },
      animation: {
        "infinite-scroll-mobile": "infinite-scroll 20s linear infinite",
        "infinite-scroll-normal": "infinite-scroll 80s linear infinite",
      },
      keyframes: {
        "infinite-scroll": {
          from: { transform: "translateX(0)" },
          to: { transform: "translateX(-100%)" },
        },
      },
      screens: {
        derm2dermlp: "1395px",
      },
    },
  },
};
