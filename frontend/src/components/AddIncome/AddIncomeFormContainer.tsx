import React from 'react';
import { Account } from './../../models/accounts';
import { AddIncomeForm } from './AddIncomeForm';
import { postIncome } from './../../services/Incomes';
import { Income } from './../../models/incomes';

type Props = {
    accounts: Array<Account>;
    close: () => void;
    refresh: () => void;
}

export class AddIncomeFormContainer extends React.Component<Props, Income> {
    constructor(props: Props) {
        super(props);
        let today = new Date();
        let dateFormat = (date: Date): string => {
            return `${date.getFullYear()}-${date.getMonth()>8?"":0}${date.getMonth()+1}-${date.getDate()}`
        }
        this.state = {
            amount: NaN,
            account: this.props.accounts[0].source.id,
            date: dateFormat(today),
            description: ''
        }
        this.OnChangeAmount = this.OnChangeAmount.bind(this);
        this.OnChangeDescription = this.OnChangeDescription.bind(this);
        this.OnChangeAccount = this.OnChangeAccount.bind(this);
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

    OnChangeDate(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({date: e.target.value})
    }

    OnSumbit(e: React.FormEvent<HTMLFormElement>){
        e.preventDefault();
        postIncome(this.state).then(result => {
            if (result.status === 201) {
                this.props.refresh();
            } else {
                alert("algo salió mal");
            }
            this.props.close();
        })
    }

    render() {
        return (
            <AddIncomeForm
                handleChangeAmount={this.OnChangeAmount}
                handleChangeAccount={this.OnChangeAccount}
                handleChangeDate={this.OnChangeDate}
                handleChangeDescription={this.OnChangeDescription}
                handleOnSubmit={this.OnSumbit} accounts={this.props.accounts}
                {...this.state}
            />
        );
    }
}