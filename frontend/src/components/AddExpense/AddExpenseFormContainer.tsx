import React from 'react';
import { AddExpenseForm } from './AddExpenseForm';
import { postExpense } from './../../services/Expenses';
import { Expense } from './../../models/expenses';
import { CategoriesAccounts } from './../../models/common';

interface Props extends CategoriesAccounts {
    close: () => void;
    refresh: () => void;
}

export class AddExpenseFormContainer extends React.Component<Props,Expense> {
    constructor(props: Props) {
        super(props);
        let today = new Date();
        let dateFormat = (date: Date): string => {
            return `${date.getFullYear()}-${date.getMonth()>8?"":0}${date.getMonth()+1}-${date.getDate()}`
        }
        this.state = {
            amount: NaN,
            description: '',
            account: this.props.accounts[0].source.id,
            category: this.props.categories[0].id,
            is_payed: true,
            date: dateFormat(today)
        }

        this.OnChangeAccount = this.OnChangeAccount.bind(this);
        this.OnChangeAmount = this.OnChangeAmount.bind(this);
        this.OnChangeCategory = this.OnChangeCategory.bind(this);
        this.OnChangeDescription = this.OnChangeDescription.bind(this);
        this.OnChangeIsPayed = this.OnChangeIsPayed.bind(this);
        this.OnChangeDate = this.OnChangeDate.bind(this);
        this.OnSumbit = this.OnSumbit.bind(this);
    }

    OnChangeAmount(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({amount: +e.target.value});
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
        this.setState(prevState => ({is_payed: !prevState.is_payed}));
    }

    OnChangeCategory(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({category: e.target.value});
    }

    OnChangeDate(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({date: e.target.value})
    }

    OnSumbit(e: React.FormEvent<HTMLFormElement>){
        e.preventDefault();
        postExpense(this.state).then(result => {
            if (result.status == 201) {
                this.props.refresh();
            } else {
                alert("algo salió mal");
            }
            this.props.close();
        })
    }

    render() {
        return (
            <AddExpenseForm
                handleChangeAccount={this.OnChangeAccount}
                handleChangeAmount={this.OnChangeAmount}
                handleChangeDescription={this.OnChangeDescription}
                handleChangeIsPayed={this.OnChangeIsPayed}
                handleChangeCategory={this.OnChangeCategory}
                handleChangeDate={this.OnChangeDate}
                accounts={this.props.accounts} categories={this.props.categories}
                handleOnSubmit={this.OnSumbit}
                {...this.state}
            />
        );
    }
}