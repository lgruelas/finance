import React from 'react';
import { Card, BankAccount, Account } from './../../models/accounts';
import { AccountCardPresentational } from './AccountCardPresentational';
import './AccountCard.css';


interface Props {
    account: Account
}

function determineIfCard(toBeDetermined: Account): toBeDetermined is Card {
    if((toBeDetermined as Card).used != null){
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

export const AccountCard: React.SFC<Props> = (props) => {
    const getName = (color: string, account: Account): string => {
        if (color === "blue") {
            return "Wallet"
        } else {
            return account.bank
        }
    }

    const formatCurrency = (input: number) : string => {
        return (new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(input));
    }

    const color: string = determineIfCard(props.account) ? "red" : determineIfBankAccount(props.account) ? "green" : "blue";
    return (
        <AccountCardPresentational name={props.account.source.name}
                                    bank={getName(color, props.account)}
                                    amount={determineIfCard(props.account) ? formatCurrency(props.account.used) : formatCurrency(props.account.balance)}
                                    color={color}/>
    );
}