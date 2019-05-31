import axios from 'axios';
import { Income } from './../models/incomes';

const API_URL = process.env.REACT_APP_API_URL;

export const postIncome = (body: Income) => {
    return axios.post(API_URL + 'incomes/', body);
}