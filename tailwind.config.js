/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {},
    fontSize: {
      'rg': '16px',
      'sm': '18px',
      'md': '22px',
      'lg': '36px',
      'xl': '42px',
      '2xl': '56px',
      '3xl': '72px'
    },
    fontFamily: {
      'tt-regular': 'tt-regular',
      'tt-medium': 'tt-medium',
      'tt-bold': 'tt-bold',
    },
    screens: {
      '2xl': {'max': '1536px'},
      'xl': {'max': '1280px'},
      'lg': {'max': '1024px'},
      'md': {'max': '768px'},
      'sm': {'max': '640px'},
    },
    // colors: {
    //   'bronze': '#e1a843'
    // }
  },
  plugins: [],
}

