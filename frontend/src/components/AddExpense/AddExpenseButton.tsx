import React from 'react';
import { Button } from 'reactstrap';
import { AddExpenseModal } from './AddExpenseModal';
import { AddExpenseButtonProps as Props } from './Props';
import { AddExpenseButtonState as State } from './State';

export class AddExpenseButton extends React.Component<Props, State> {
    constructor(props: Props) {
        super(props);
        this.state = {
            isModalOpen: false,
        }
        this.toggle = this.toggle.bind(this);
    }

    toggle() {
        this.setState(prevState => ({
            isModalOpen: !prevState.isModalOpen
        }));
    }

    render() {
        return (
            <div className="button-modal-container">
                <Button onClick={this.toggle} className="add-expense-button">Add Expense</Button>
                <AddExpenseModal refresh={this.props.refresh} open={this.state.isModalOpen} toggle={this.toggle} categories={this.props.categories} accounts={this.props.accounts}/>
            </div>
        );
    }
}