import { Wallet, Card, BankAccount } from './../../models/accounts';


export type GlobalAmountPresentationalProps = {
    total: number;
}

export type GlobalAmountProps = {
    bankAccounts: Array<BankAccount>;
    wallets: Array<Wallet>;
    cards: Array<Card>;
}
