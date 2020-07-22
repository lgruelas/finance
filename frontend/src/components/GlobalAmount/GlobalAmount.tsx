import React from 'react';

import { BankAccount, Card, Wallet, Account } from './../../models/accounts';
import { GlobalAmountPresentational } from './GlobalAmountPresentational';
import { GlobalAmountProps as Props } from './Props';
import { GlobalAmountState as State } from './State';
import './GlobalAmount.css';

export class GlobalAmount extends React.Component <Props, State>{
    constructor(props: Props) {
        super(props);
        this.state = {
            "total": this.calculateTotal(props)
        }
    }

    sumAccountArray(accounts: Account[], property: string): number {
        if (accounts) {
            return accounts.reduce<number>((a: number, b: Account) => a + b[property], 0);
        }
        return 0;
    }

    calculateTotal(accounts: Props): number {
        let counter: number = 0;
        counter += this.sumAccountArray(accounts.bank_accounts, "balance");
        counter += this.sumAccountArray(accounts.wallets, "balance");
        counter -= this.sumAccountArray(accounts.cards, "used");
        return counter;
    }

    componentDidUpdate(oldProps: Props) {
        if (oldProps !== this.props) {
            this.setState({total: this.calculateTotal(this.props)});
        }
    }

    render() {
        return(
            <GlobalAmountPresentational total={this.state.total} />
        );
    }
}
