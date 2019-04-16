import React from 'react';
import { Card, BankAccount, Account } from './../../models/accounts';
import './AccountCard.css';

interface Props {
    account: Account
}

function determineIfCard(toBeDetermined: Account): toBeDetermined is Card {
    if((toBeDetermined as Card).used){
        return true
    }
    return false
}

function determineIfBankAccount(toBeDetermined: Account): toBeDetermined is BankAccount {
    if ((toBeDetermined as BankAccount).bank){
        return true
    }
    return false
}

type Type = {
    kind: string,
    color: string
}

const formatCurrency = (input: number) : string => {
    return (new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(input));
}

export const AccountCard: React.SFC<Props> = (props) => {
    const type_: Type = determineIfCard(props.account) ? {kind: "card", color: "red"} : determineIfBankAccount(props.account) ? {kind: "bank", color: "green"}  : {kind: "wallet", color: "blue"};

    const getName = (kind: string, account: Account): string => {
        if (kind === "wallet") {
            return "Wallet"
        } else {
            return account.bank
        }
    }

    return (
        <div className="card">
            <p className="account-text" style={{color: type_.color}}>{determineIfCard(props.account) ? formatCurrency(props.account.used) : formatCurrency(props.account.balance)}</p>
            {getName(type_.kind, props.account)}
            <div><img src={"../../assets/imgs/" + props.account.source.name + ".png"} /></div>
        </div>
    );
}