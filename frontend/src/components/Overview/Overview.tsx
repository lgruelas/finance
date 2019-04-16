import React from 'react';
import { GlobalAmount } from './../GlobalAmount/GlobalAmount';
import { getBankAccounts, getWalletAccounts, getCreditCards } from './../../services/Accounts';
import { Wallet, BankAccount, Card } from './../../models/accounts';
import { AccountCard } from './../AccountCard/AccountCard';
import './Overview.css';
import { Row, Col } from 'reactstrap';
import { AddExpenseButton } from './../AddExpenseButton/AddExpenseButton';
import { Account } from './../../models/accounts';

interface State {
    bank_accounts: Array<BankAccount>,
    cards: Array<Card>,
    wallets: Array<Wallet>,
    all_accounts: Array<Account>
}

export class Overview extends React.Component<any,State> {
    constructor(props: any) {
        super(props);
        this.state = {
            bank_accounts: [],
            cards: [],
            wallets: [],
            all_accounts: []
        }
    }

    reload() {
        Promise.all([
            getWalletAccounts(),
            getCreditCards(),
            getBankAccounts()
        ]).then(([wallet, card, bank]) => {
            this.setState({ bank_accounts : bank.data, wallets: wallet.data, cards: card.data});
        }).catch(error => console.log(error));
    }

    componentWillMount() {
        this.reload();
    }

    render() {
        return (
            <div className="container">
                <AddExpenseButton />
                <GlobalAmount bank_account={this.state.bank_accounts} card={this.state.cards} wallet={this.state.wallets}/>
                <Row className="accounts-row">
                    {this.state.bank_accounts.map(function(element: BankAccount)
                        {return (<Col xs={4} key={element.source.id}>
                            <AccountCard account={element} />
                        </Col>);}
                    )}
                    {this.state.wallets.map(function(element: Wallet)
                        {return (<Col xs={4} key={element.source.id}>
                            <AccountCard account={element} />
                        </Col>);}
                    )}
                    {this.state.cards.map(function(element: Card)
                        {return (<Col xs={4} key={element.source.id}>
                            <AccountCard account={element} />
                        </Col>);}
                    )}
                </Row>
            </div>
        );
    }
}