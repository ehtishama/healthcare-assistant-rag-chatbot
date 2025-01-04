/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      
      colors: {
        primary: "rgb(70 234 77)",
      },
      fontFamily: {
        primary: ["Plus Jakarta Sans", "serif"],
      },
    },
  },
  plugins: [],
};
