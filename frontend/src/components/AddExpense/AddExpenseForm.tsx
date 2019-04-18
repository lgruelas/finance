import React from 'react';
import { Form, FormGroup, Label, Input, Row, Col } from 'reactstrap';

type Props = {
    handleChangeAmount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDescription: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeIsPayed: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeCategory: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleOnSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
    amount_value: string;
    description_value: string;
    account_value: string;
    category_value: string;
    isPayed_value: boolean; //have to solve this value
}

export const AddExpenseForm: React.SFC<Props> = props => {
    return (
        <Form id="expense-form" onSubmit={props.handleOnSubmit}>
            <FormGroup>
            <Label for="amount">Amount</Label>
            <Input type="number" step="any" name="expense-amount" id="amount" placeholder="50.00" value={props.amount_value} onChange={props.handleChangeAmount} />
            </FormGroup>
            <FormGroup>
            <Label for="description">Description</Label>
            <Input type="textarea" name="expense-description" id="description" value={props.description_value} onChange={props.handleChangeDescription} />
            </FormGroup>
            <Row>
                <Col xs={6}>
                <FormGroup>
                <Label for="account">Account</Label>
                <Input type="select" name="expense-account" id="account" value={props.account_value} onChange={props.handleChangeAccount}>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>
                </Input>
                </FormGroup>
                </Col>
                <Col xs={6}>
                <FormGroup>
                <Label for="category">Category</Label>
                <Input type="select" name="expense-category" id="category" value={props.category_value} onChange={props.handleChangeCategory}>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>
                </Input>
                </FormGroup>
                </Col>
            </Row>
            <FormGroup check>
            <Label check>
                <Input type="checkbox" checked={props.isPayed_value} onChange={props.handleChangeIsPayed} />{' '}
                Payed?
            </Label>
            </FormGroup>
        </Form>
    );
}