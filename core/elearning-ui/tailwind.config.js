/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#2563eb",  // Adjust brand colors
        secondary: "#facc15",
        dark: "#171717",
        light: "#ffffff",
        accent: "#f97316",
      },
    },
  },
  plugins: [],
};