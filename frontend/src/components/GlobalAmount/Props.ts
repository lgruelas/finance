import { Wallet, Card, BankAccount } from './../../models/accounts';


export type GlobalAmountPresentationalProps = {
    total: number;
}

export type GlobalAmountProps = {
    bank_accounts: Array<BankAccount>;
    wallets: Array<Wallet>;
    cards: Array<Card>;
}
