import axios from 'axios'

const url = (import.meta.env.PROD ? 'https://admin-grupo27.proyecto2023.linti.unlp.edu.ar/api' : 'http://127.0.0.1:5000/api');

export default axios.create({
  baseURL: url,
  headers: {
    'Content-Type': 'application/json'
  }
})
