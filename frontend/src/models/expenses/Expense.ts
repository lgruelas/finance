export interface Expense {
    amount: number;
    description: string;
    account: string;
    category: string;
    is_payed: boolean;
    date: string;
    id?: string;
}