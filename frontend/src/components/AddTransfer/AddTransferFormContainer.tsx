import React from 'react';
import { Account } from './../../models/accounts';
import { AddTransferForm } from './AddTransferForm';
import { postTransfer } from './../../services/Transfers';
import { Transfer } from './../../models/transfers';

type Props = {
    accounts: Array<Account>;
    close: () => void;
    refresh: () => void;
}

export class AddTransferFormContainer extends React.Component<Props, Transfer> {
    constructor(props: Props) {
        super(props);
        let today = new Date();
        let dateFormat = (date: Date): string => {
            return `${date.getFullYear()}-${date.getMonth()>8?"":0}${date.getMonth()+1}-${date.getDate()}`
        }
        this.state = {
            amount: NaN,
            account_from: '',
            account_to: '',
            date: dateFormat(today),
            description: ''
        }
        this.OnChangeAmount = this.OnChangeAmount.bind(this);
        this.OnChangeDescription = this.OnChangeDescription.bind(this);
        this.OnChangeAccountTo = this.OnChangeAccountTo.bind(this);
        this.OnChangeAccountFrom = this.OnChangeAccountFrom.bind(this);
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

    OnChangeAccountTo(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({account_to: e.target.value});
    }

    OnChangeAccountFrom(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({account_from: e.target.value});
    }

    OnChangeDate(e: React.ChangeEvent<HTMLInputElement>) {
        e.preventDefault();
        this.setState({date: e.target.value})
    }

    OnSumbit(e: React.FormEvent<HTMLFormElement>){
        e.preventDefault();
        postTransfer(this.state).then(result => {
            if (result.status == 200) {
                this.props.refresh();
            } else {
                alert("algo salió mal");
            }
            this.props.close();
        })
    }

    render() {
        return (
            <AddTransferForm
                handleChangeAmount={this.OnChangeAmount}
                handleChangeAccountFrom={this.OnChangeAccountFrom}
                handleChangeAccountTo={this.OnChangeAccountTo}
                handleChangeDate={this.OnChangeDate}
                handleChangeDescription={this.OnChangeDescription}
                handleOnSubmit={this.OnSumbit} accounts={this.props.accounts}
                {...this.state}
            />
        );
    }
}