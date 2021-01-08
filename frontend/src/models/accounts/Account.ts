//import { Wallet, BankAccount, Card } from './';

//export type Account = Wallet | BankAccount | Card;

export interface Account {
    id: string,
    name: string,
    balance: number
}

export interface DigitalAccount extends Account{
    bank: string
}