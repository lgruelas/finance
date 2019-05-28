import axios from 'axios';

const URL = process.env.REACT_APP_API_URL;

export const getCategories = () => {
    return axios.get(URL + 'categories');
}

export const getCategoriesUsed = (year: number, month: number) => {
    return  axios.get(URL + `categories/${year}/${month}`);
}