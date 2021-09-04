import { Source } from './Source';

export interface BankAccount {
    balance: number,
    bank: string,
    source: Source
}