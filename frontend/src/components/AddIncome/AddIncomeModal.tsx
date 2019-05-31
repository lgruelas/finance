import React from 'react';
import { Button, ModalFooter, Modal, ModalHeader, ModalBody } from 'reactstrap';
import { Account } from './../../models/accounts';
import { AddIncomeFormContainer } from './AddIncomeFormContainer';

type Props = {
    open: boolean,
    toggle: () => void,
    accounts: Array<Account>,
    refresh: () => void
}

export const AddIncomeModal: React.SFC<Props> = props => {
    return (
        <div>
            <Modal isOpen={props.open} toggle={props.toggle}>
            <ModalHeader toggle={props.toggle}>Add Income</ModalHeader>
            <ModalBody>
                <AddIncomeFormContainer refresh={props.refresh} accounts={props.accounts} close={props.toggle}/>
            </ModalBody>
            <ModalFooter>
                <Button outline color="danger" onClick={props.toggle}>Cancel</Button> {' '}
                <Button outline color="primary" form="income-form" type="submit">Submit</Button>
            </ModalFooter>
            </Modal>
        </div>
    );
}