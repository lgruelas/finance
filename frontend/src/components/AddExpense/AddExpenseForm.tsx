import React from 'react';
import { Form, FormGroup, Label, Input, Row, Col } from 'reactstrap';
import { CategoriesAccounts } from './../../models/common';
import { Account } from './../../models/accounts';
import { Categorie } from './../../models/categories';
import { Expense } from './../../models/expenses';

interface Props extends CategoriesAccounts, Expense {
    handleChangeAmount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDescription: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeIsPayed: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeCategory: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDate: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleOnSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
}

export const AddExpenseForm: React.SFC<Props> = props => {
    return (
        <Form id="expense-form" onSubmit={props.handleOnSubmit}>
            <FormGroup>
            <Label for="amount">Amount</Label>
            <Input type="number" step="any" name="expense-amount" id="amount" placeholder="50.00" value={props.amount} onChange={props.handleChangeAmount} />
            </FormGroup>
            <FormGroup>
            <Label for="description">Description</Label>
            <Input type="textarea" name="expense-description" id="description" value={props.description} onChange={props.handleChangeDescription} />
            </FormGroup>
            <Row>
                <Col xs={6}>
                <FormGroup>
                <Label for="account">Account</Label>
                <Input type="select" name="expense-account" id="account" value={props.account} onChange={props.handleChangeAccount}>
                    {props.accounts.map(function(element: Account) {
                        return (<option key={element.source.id} value={element.source.id}>{element.source.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
                <Col xs={6}>
                <FormGroup>
                <Label for="category">Category</Label>
                <Input type="select" name="expense-category" id="category" value={props.category} onChange={props.handleChangeCategory}>
                    {props.categories.map(function(element: Categorie) {
                        return (<option key={element.id} value={element.id}>{element.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
            </Row>
            <Row>
                <Col xs={6}>
                <Label for="expense-date">Date</Label>
                <Input type="date" name="date" id="expense-date" placeholder="Date" value={props.date} onChange={props.handleChangeDate}/>
                </Col>
                <Col xs={6}>
                <FormGroup check>
                <Label check>
                    <Input type="checkbox" checked={props.is_payed} onChange={props.handleChangeIsPayed} />{' '}
                    Payed?
                </Label>
                </FormGroup>
                </Col>
            </Row>
        </Form>
    );
}