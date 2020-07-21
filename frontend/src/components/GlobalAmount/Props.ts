import { Wallet, Card, BankAccount } from './../../models/accounts';


export type GlobalAmountPresentationalProps = {
    total: number;
}

export type GlobalAmountProps = {
    bank_account: Array<BankAccount>;
    wallet: Array<Wallet>;
    card: Array<Card>;
}
