import React  from 'react';
import { Form, FormGroup, Label, Input, Row, Col } from 'reactstrap';
import { Account } from './../../models/accounts';
import { Income } from './../../models/incomes';

interface Props extends Income {
    handleChangeAmount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDescription: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDate: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleOnSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
    accounts: Array<Account>;
}

export const AddIncomeForm: React.SFC<Props> = props => {
    return (
        <Form id="income-form" onSubmit={props.handleOnSubmit}>
            <FormGroup>
            <Label for="amount">Amount</Label>
            <Input type="number" step="any" name="income-amount" id="amount" placeholder="50.00" value={props.amount.toString()} onChange={props.handleChangeAmount} />
            </FormGroup>
            <FormGroup>
            <Label for="description">Description</Label>
            <Input type="textarea" name="income-description" id="description" value={props.description} onChange={props.handleChangeDescription} />
            </FormGroup>
            <Row>
                <Col xs={6}>
                <FormGroup>
                <Label for="account">Account</Label>
                <Input type="select" name="income-account" id="account" value={props.account} onChange={props.handleChangeAccount}>
                    {props.accounts.map(function(element: Account) {
                        return (<option key={element.source.id} value={element.source.id}>{element.source.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
                <Col xs={6}>
                <Label for="income-date">Date</Label>
                <Input type="date" name="date" id="income-date" placeholder="Date" value={props.date} onChange={props.handleChangeDate}/>
                </Col>
            </Row>
        </Form>
    );
}