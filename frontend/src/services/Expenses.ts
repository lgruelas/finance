import { Expense } from './../models/expenses/Expense';
import axios from 'axios';

const URL = process.env.REACT_APP_API_URL;

export const postExpense = (body: Expense) => {
    return axios.post(URL + 'expenses/', body);
}