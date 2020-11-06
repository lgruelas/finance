import React from 'react';
import { Card, BankAccount, Account, DigitalAccount } from './../../models/accounts';
import { AccountCardPresentational } from './AccountCardPresentational';
import { AccountCardProps as Props } from './Props';
import './AccountCard.css';


function determineIfCard(toBeDetermined: Account): toBeDetermined is Card {
    if((toBeDetermined as Card).cut){
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
    const formatCurrency = (input: number) : string => {
        return (new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD'
        }).format(input));
    }

    const color: string = determineIfCard(props.account) ? "red" : determineIfBankAccount(props.account) ? "green" : "blue";
    return (
        <AccountCardPresentational name={props.account.name}
                                    bank={(props.account as DigitalAccount).bank || "Wallet"}
                                    amount={determineIfCard(props.account) ? formatCurrency(props.account.credit - props.account.balance) : formatCurrency(props.account.balance)}
                                    color={color}/>
    );
}