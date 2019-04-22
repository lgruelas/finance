import React from 'react';
import { GlobalAmountPresentational } from './GlobalAmountPresentational';
import { Wallet, Card, BankAccount } from './../../models/accounts';
import './GlobalAmount.css';

type State = {
    total: number;
}

type Props = {
    bank_account: Array<BankAccount>;
    wallet: Array<Wallet>;
    card: Array<Card>;
}


export class GlobalAmount extends React.Component <Props,State>{
    constructor(props: any) {
        super(props);
        this.state = {
            total: 0
        }
    }

    componentDidUpdate(oldprops: any) {
        console.log("hola")
        if (oldprops != this.props) {
            let counter: number = 0;
            console.log(this.props.bank_account);
            this.props.bank_account.forEach((element: any) => {
                counter += element.balance;
            });
            this.props.wallet.forEach((element: any) => {
                counter += element.balance;
            });
            this.props.card.forEach((element: any) => {
                counter -= element.used;
            });
            this.setState({total: counter});
        }
    }

    render() {
        return(
            <GlobalAmountPresentational total={this.state.total} />
        );
    }
}