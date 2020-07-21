import React from 'react';
import { GlobalAmountPresentational } from './GlobalAmountPresentational';
import { GlobalAmountProps as Props } from './Props';
import { GlobalAmountState as State } from './State';
import './GlobalAmount.css';

export class GlobalAmount extends React.Component <Props, State>{
    constructor(props: any) {
        super(props);
        this.state = {
            total: 0
        }
    }

    componentDidUpdate(oldprops: any) {
        if (oldprops !== this.props) {
            let counter: number = 0;
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
