import axios from 'axios';

const URL = process.env.REACT_APP_API_URL;

export const getBankAccounts = () => {
    return axios.get(URL + 'accounts/');
}

export const getWalletAccounts = () => {
    return axios.get(URL + 'wallets/');
}

export const getCreditCards = () => {
    return axios.get(URL + 'cards/');
}