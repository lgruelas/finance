import axios from 'axios';

export const getBankAccounts = () => {
    return axios.get('http://localhost:8000/api/v1/accounts');
}