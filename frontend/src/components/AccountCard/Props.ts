import { Account } from "./../../models/accounts";

export type AccountCardPresentationalProps = {
    color: string;
    amount: string;
    name: string;
    bank: string;
}

export type AccountCardProps = {
    account: Account
}