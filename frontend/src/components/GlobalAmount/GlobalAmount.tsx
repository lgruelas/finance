import React from 'react';

import { Account, Card } from './../../models/accounts';
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

    sumAccountArray(accounts: Array<Account>): number {
        if (accounts) {
            return accounts.reduce<number>((a: number, b: Account) => a + b.balance, 0);
        }
        return 0;
    }

    sumCardAccountArray(accounts: Array<Card>): number {
        if (accounts) {
            return accounts.reduce<number>((a: number, b: Card) => a + (b.credit - b.balance), 0);
        }
        return 0;
    }

    calculateTotal(accounts: Props): number {
        let counter: number = 0;
        counter += this.sumAccountArray(accounts.bankAccounts);
        counter += this.sumAccountArray(accounts.wallets);
        counter -= this.sumCardAccountArray(accounts.cards);
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
