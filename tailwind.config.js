/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./css/*.css",
		"./templates/*.html",
		"./components/**/*.{js,ts,jsx,tsx}",
	],
	theme: {
		extend: {},
	},
	plugins: [],
};
