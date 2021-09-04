import React from 'react';
import { Button, ModalFooter, Modal, ModalHeader, ModalBody } from 'reactstrap';
import { Account } from './../../models/accounts';
import { AddTransferFormContainer } from './AddTransferFormContainer';

type Props = {
    open: boolean,
    toggle: () => void,
    accounts: Array<Account>,
    refresh: () => void
}

export const AddTransferModal: React.SFC<Props> = props => {
    return (
        <div>
            <Modal isOpen={props.open} toggle={props.toggle}>
            <ModalHeader toggle={props.toggle}>Add Transfer</ModalHeader>
            <ModalBody>
                <AddTransferFormContainer refresh={props.refresh} accounts={props.accounts} close={props.toggle}/>
            </ModalBody>
            <ModalFooter>
                <Button outline color="danger" onClick={props.toggle}>Cancel</Button> {' '}
                <Button outline color="primary" form="transfer-form" type="submit">Submit</Button>
            </ModalFooter>
            </Modal>
        </div>
    );
}