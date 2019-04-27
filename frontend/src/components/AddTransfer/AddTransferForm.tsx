import React from 'react';
import { Form, FormGroup, Label, Input, Row, Col } from 'reactstrap';
import { Account } from './../../models/accounts';
import { Categorie } from 'src/models/categories';
import { Transfer } from './../../models/transfers'
;
interface Props extends Transfer {
    handleChangeAmount: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDescription: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccountTo: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeAccountFrom: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleChangeDate: (e: React.ChangeEvent<HTMLInputElement>) => void;
    handleOnSubmit: (e: React.FormEvent<HTMLFormElement>) => void;
    accounts: Array<Account>;
}

export const AddTransferForm: React.SFC<Props> = props => {
    return (
        <Form id="transfer-form" onSubmit={props.handleOnSubmit}>
            <FormGroup>
            <Label for="amount">Amount</Label>
            <Input type="number" step="any" name="transfer-amount" id="amount" placeholder="50.00" value={props.amount} onChange={props.handleChangeAmount} />
            </FormGroup>
            <FormGroup>
            <Label for="description">Description</Label>
            <Input type="textarea" name="transfer-description" id="description" value={props.description} onChange={props.handleChangeDescription} />
            </FormGroup>
            <Row>
                <Col xs={6}>
                <FormGroup>
                <Label for="account">Account From</Label>
                <Input type="select" name="transfer-account" id="account" value={props.account_from} onChange={props.handleChangeAccountFrom}>
                    {props.accounts.map(function(element: Account) {
                        return (<option key={element.source.id} value={element.source.id}>{element.source.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
                <Col xs={6}>
                <FormGroup>
                <Label for="category">Account To</Label>
                <Input type="select" name="transfer-category" id="category" value={props.account_to} onChange={props.handleChangeAccountTo}>
                    {props.accounts.map(function(element: Categorie) {
                        return (<option key={element.source.id} value={element.source.id}>{element.source.name}</option>);
                    })}
                </Input>
                </FormGroup>
                </Col>
            </Row>
            <Row>
                <Col xs={6}>
                <Label for="transfer-date">Date</Label>
                <Input type="date" name="date" id="transfer-date" placeholder="Date" value={props.date} onChange={props.handleChangeDate}/>
                </Col>
                <Col xs={6}>
                </Col>
            </Row>
        </Form>
    );
}