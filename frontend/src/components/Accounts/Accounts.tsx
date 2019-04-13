import React from 'react';
import { getBankAccounts } from './../../services/Accounts';

export class Accounts extends React.Component<{},any> {
    constructor(props: any) {
        super(props);
        this.state = {
            to_print: {}
        } ;
    }

    componentWillMount() {
        this.setState({ to_print : getBankAccounts()});
    }

    public render() {
        return (
            <div>a</div>
        )
    }
}