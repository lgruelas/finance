import axios from 'axios';

const URL = 'http://localhost:8000/api/v1/';

export const getBankAccounts = () => {
    return axios.get(URL + 'accounts');
}

export const getWalletAccounts = () => {
    return axios.get(URL + 'wallets');
}

export const getCreditCards = () => {
    return axios.get(URL + 'cards');
}