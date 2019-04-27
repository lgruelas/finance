import React from 'react';
import { Form, FormGroup, Label, Input, Row, Col } from 'reactstrap';
import { Account } from './../../models/accounts';
import { Categorie } from 'src/models/categories';

type Props = {
    handleChangeAmount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDescription: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccountTo: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccountFrom: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDate: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleOnSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
    amount_value: number;
    description_value: string;
    account_from_value: string;
    account_to_value: string;
    date_value: string;
    accounts: Array<Account>;
}

export const AddTransferForm: React.SFC<Props> = props => {
    return (
        <Form id="transfer-form" onSubmit={props.handleOnSubmit}>
            <FormGroup>
            <Label for="amount">Amount</Label>
            <Input type="number" step="any" name="transfer-amount" id="amount" placeholder="50.00" value={props.amount_value} onChange={props.handleChangeAmount} />
            </FormGroup>
            <FormGroup>
            <Label for="description">Description</Label>
            <Input type="textarea" name="transfer-description" id="description" value={props.description_value} onChange={props.handleChangeDescription} />
            </FormGroup>
            <Row>
                <Col xs={6}>
                <FormGroup>
                <Label for="account">Account From</Label>
                <Input type="select" name="transfer-account" id="account" value={props.account_from_value} onChange={props.handleChangeAccountFrom}>
                    {props.accounts.map(function(element: Account) {
                        return (<option value={element.source.id}>{element.source.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
                <Col xs={6}>
                <FormGroup>
                <Label for="category">Account To</Label>
                <Input type="select" name="transfer-category" id="category" value={props.account_to_value} onChange={props.handleChangeAccountTo}>
                    {props.accounts.map(function(element: Categorie) {
                        return (<option value={element.source.id}>{element.source.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
            </Row>
            <Row>
                <Col xs={6}>
                <Label for="transfer-date">Date</Label>
                <Input type="date" name="date" id="transfer-date" placeholder="Date" value={props.date_value} onChange={props.handleChangeDate}/>
                </Col>
                <Col xs={6}>
                </Col>
            </Row>
        </Form>
    );
}