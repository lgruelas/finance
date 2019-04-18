import React from 'react';
import { Button, ModalFooter, Modal, ModalHeader, ModalBody } from 'reactstrap';
import { AddExpenseFormContainer } from './AddExpenseFormContainer';

type Props = {
    open: boolean;
    toggle: () => void;
}

export class AddExpenseModal extends React.Component<Props,any> {
    constructor(props:any) {
        super(props);
    }

    render() {
        return (
        <div>
            <Modal isOpen={this.props.open} toggle={this.props.toggle}>
            <ModalHeader toggle={this.props.toggle}>Add Expense</ModalHeader>
            <ModalBody>
                <AddExpenseFormContainer />
            </ModalBody>
            <ModalFooter>
                <Button outline color="danger" onClick={this.props.toggle}>Cancel</Button> {' '}
                <Button outline color="primary" form="expense-form" type="submit">Submit</Button>
            </ModalFooter>
            </Modal>
        </div>
        );
    }
}