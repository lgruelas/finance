export interface Transfer {
    id?: string;
    amount: number;
    account_from: string;
    account_to: string;
    date: string;
    description: string;
}