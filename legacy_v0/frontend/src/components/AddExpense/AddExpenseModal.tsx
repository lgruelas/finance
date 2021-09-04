import React from 'react';
import { Button, ModalFooter, Modal, ModalHeader, ModalBody } from 'reactstrap';
import { AddExpenseFormContainer } from './AddExpenseFormContainer';
import { CategoriesAccounts } from './../../models/common';

interface Props extends CategoriesAccounts {
    open: boolean,
    toggle: () => void,
    refresh: () => void
}

export const AddExpenseModal: React.SFC<Props> = props => {
    return (
    <div>
        <Modal isOpen={props.open} toggle={props.toggle}>
        <ModalHeader toggle={props.toggle}>Add Expense</ModalHeader>
        <ModalBody>
            <AddExpenseFormContainer refresh={props.refresh} close={props.toggle} categories={props.categories} accounts={props.accounts}/>
        </ModalBody>
        <ModalFooter>
            <Button outline color="danger" onClick={props.toggle}>Cancel</Button> {' '}
            <Button outline color="primary" form="expense-form" type="submit">Submit</Button>
        </ModalFooter>
        </Modal>
    </div>
    );
}