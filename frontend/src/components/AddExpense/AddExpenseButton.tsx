import React from 'react';
import { Button } from 'reactstrap';
import { AddExpenseModal } from './AddExpenseModal';

type State = {
    isModalOpen: boolean;
}

export class AddExpenseButton extends React.Component<any, State> {
    constructor(props: any) {
        super(props);
        this.state = {
            isModalOpen: false
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
                <AddExpenseModal open={this.state.isModalOpen} toggle={this.toggle}/>
            </div>
        );
    }
}