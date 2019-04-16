import React from 'react';
import { Row, Col } from 'reactstrap';
import './GlobalAmount.css';

export class GlobalAmount extends React.Component <any,any>{
    constructor(props: any) {
        super(props);
        this.state = {
            total: 0
        }
    }

    componentDidUpdate(oldprops: any) {
        console.log("hola")
        if (oldprops != this.props) {
            let counter: number = 0;
            console.log(this.props.bank_account);
            this.props.bank_account.forEach((element: any) => {
                counter += element.balance;
            });
            this.props.wallet.forEach((element: any) => {
                counter += element.balance;
            });
            this.props.card.forEach((element: any) => {
                counter -= element.used;
            });
            this.setState({total: counter});
        }
    }

    render() {
        return(
            <Row>
                <Col md={4}>
                    <div className="card main-card">
                        <p className="main-amount"> {
                            new Intl.NumberFormat('en-US', {
                                style: 'currency',
                                currency: 'USD'
                            }).format(this.state.total)
                            }</p>
                        <p>Dinero total</p>
                    </div>
                </Col>
            </Row>
        );
    }
}