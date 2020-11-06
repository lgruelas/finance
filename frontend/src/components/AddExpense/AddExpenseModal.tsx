import React from 'react';
import { Button, ModalFooter, Modal, ModalHeader, ModalBody } from 'reactstrap';
import { AddExpenseFormContainer } from './AddExpenseFormContainer';
import { AddExpenseModalProps as Props } from './Props';


export const AddExpenseModal: React.SFC<Props> = props => {
    return (
        <div>
            <Modal isOpen={props.open} toggle={props.toggle}>
                <ModalHeader toggle={props.toggle}>Add Expense</ModalHeader>
                <ModalBody>
                    <AddExpenseFormContainer refresh={props.refresh}
                                            close={props.toggle}
                                            categories={props.categories}
                                            accounts={props.accounts}/>
                </ModalBody>
                <ModalFooter>
                    <Button outline color="danger" className="cancel-button" onClick={props.toggle}>Cancel</Button> {' '}
                    <Button outline color="primary" className="submit-button" form="expense-form" type="submit">Submit</Button>
                </ModalFooter>
            </Modal>
        </div>
    );
}
