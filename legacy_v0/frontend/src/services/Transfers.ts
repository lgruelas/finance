import axios from 'axios';
import { Transfer } from './../models/transfers';

const API_URL = process.env.REACT_APP_API_URL;

export const postTransfer = (body: Transfer) => {
    return axios.post(API_URL + 'transfers/', body);
}