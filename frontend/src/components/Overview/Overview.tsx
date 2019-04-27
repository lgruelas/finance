import React from 'react';
import { GlobalAmount } from './../GlobalAmount/GlobalAmount';
import { getBankAccounts, getWalletAccounts, getCreditCards } from './../../services/Accounts';
import { Wallet, BankAccount, Card } from './../../models/accounts';
import { AccountCard } from './../AccountCard/AccountCard';
import './Overview.css';
import { Row, Col } from 'reactstrap';
import { AddExpenseButton } from './../AddExpense/AddExpenseButton';
import { AddTransferButton } from './../AddTransfer/AddTransferButton';
import { Categorie } from './../../models/categories';
import { getCategories } from './../../services/Categories';

interface State {
    bank_accounts: Array<BankAccount>,
    cards: Array<Card>,
    wallets: Array<Wallet>,
    categories: Array<Categorie>
}

export class Overview extends React.Component<any,State> {
    constructor(props: any) {
        super(props);
        this.state = {
            bank_accounts: [],
            cards: [],
            wallets: [],
            categories: []
        }
    }

    reload() {
        Promise.all([
            getWalletAccounts(),
            getCreditCards(),
            getBankAccounts(),
            getCategories()
        ]).then(([wallet, card, bank, categories]) => {
            this.setState({ bank_accounts : bank.data, wallets: wallet.data, cards: card.data, categories: categories.data});
        }).catch(error => console.log(error));
    }

    componentWillMount() {
        this.reload();
    }

    render() {
        return (
            <div className="container">
                <AddExpenseButton refresh={this.reload} categories={this.state.categories} accounts={[...this.state.bank_accounts, ...this.state.cards, ...this.state.wallets]}/>{" "}
                <AddTransferButton refresh={this.reload} accounts={[...this.state.bank_accounts, ...this.state.cards, ...this.state.wallets]}/>
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