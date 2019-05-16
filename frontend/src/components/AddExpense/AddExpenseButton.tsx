import React from 'react';
import { Button } from 'reactstrap';
import { AddExpenseModal } from './AddExpenseModal';
import { CategoriesAccounts } from './../../models/common';

type State = {
    isModalOpen: boolean;
}

interface Props extends CategoriesAccounts {
    refresh: () => void
}

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
                <Button onClick={this.toggle}>Add Expense</Button>
                <AddExpenseModal refresh={this.props.refresh} open={this.state.isModalOpen} toggle={this.toggle} categories={this.props.categories} accounts={this.props.accounts}/>
            </div>
        );
    }
}