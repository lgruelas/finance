import React from 'react';
import { AddExpenseForm } from './AddExpenseForm';
//import { postExpense } from './../../services/Expenses';

type State = {
    amount: string;
    description: string;
    account: string;
    category: string;
    isPayed: boolean;
}

export class AddExpenseFormContainer extends React.Component<any,State> {
    constructor(props: any) {
        super(props);
        this.state = {
            amount: '',
            description: '',
            account: '',
            category: '',
            isPayed: false
        }

        this.OnChangeAccount = this.OnChangeAccount.bind(this);
        this.OnChangeAmount = this.OnChangeAmount.bind(this);
        this.OnChangeCategory = this.OnChangeCategory.bind(this);
        this.OnChangeDescription = this.OnChangeDescription.bind(this);
        this.OnChangeIsPayed = this.OnChangeIsPayed.bind(this);
    }

    OnChangeAmount(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({amount: e.target.value});
    }

    OnChangeDescription(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({description: e.target.value});
    }

    OnChangeAccount(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({account: e.target.value});
    }

    OnChangeIsPayed(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({isPayed: e.target.checked});
    }

    OnChangeCategory(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({category: e.target.value});
    }

    OnSumbit(e: React.FormEvent<HTMLFormElement>){
        e.preventDefault();
        console.log('submitting');
    }

    render() {
        return (
            <AddExpenseForm
                handleChangeAccount={this.OnChangeAccount} account_value={this.state.account}
                handleChangeAmount={this.OnChangeAmount} amount_value={this.state.amount}
                handleChangeDescription={this.OnChangeDescription} description_value={this.state.description}
                handleChangeIsPayed={this.OnChangeIsPayed} isPayed_value={this.state.isPayed}
                handleChangeCategory={this.OnChangeCategory} category_value={this.state.category}
                handleOnSubmit={this.OnSumbit}
            />
        );
    }
}