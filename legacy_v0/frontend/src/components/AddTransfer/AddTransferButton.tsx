import React from 'react';
import { Button } from 'reactstrap';
import { AddTransferModal } from './AddTransferModal';
import { Account } from './../../models/accounts';

type State = {
    isModalOpen: boolean;
}

type Props = {
    accounts: Array<Account>,
    refresh: () => void
}

export class AddTransferButton extends React.Component<Props, State> {
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
                <Button onClick={this.toggle}>Add Transfer</Button>
                <AddTransferModal refresh={this.props.refresh} open={this.state.isModalOpen} toggle={this.toggle} accounts={this.props.accounts}/>
            </div>
        );
    }
}