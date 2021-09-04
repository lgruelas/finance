import React from 'react';
import { Button } from 'reactstrap';
import { AddIncomeModal } from './AddIncomeModal';
import { Account } from './../../models/accounts';

type State = {
    isModalOpen: boolean;
}

interface Props {
    refresh: () => void,
    accounts: Array<Account>
}

export class AddIncomeButton extends React.Component<Props, State> {
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
                <Button onClick={this.toggle}>Add Income</Button>
                <AddIncomeModal refresh={this.props.refresh} open={this.state.isModalOpen} toggle={this.toggle} accounts={this.props.accounts}/>
            </div>
        );
    }
}