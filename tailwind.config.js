/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		"./css/*.css",
		"./templates/**/*.html",
		"./components/**/*.{js,ts,jsx,tsx}",
	],
	theme: {
		extend: {
			colors: {
				"dark-blue": "#00296b",
				"neutral-blue": "#003f88",
				"light-blue": "#00509d",
				"neutral-gold": "#fdc500",
				"light-gold": "#ffd500",
			},
		},
	},
	plugins: [],
};
