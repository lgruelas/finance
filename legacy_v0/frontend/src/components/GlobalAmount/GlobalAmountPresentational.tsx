import React from 'react';
import { Row, Col } from 'reactstrap';

type Props = {
    total: number;
}

export const GlobalAmountPresentational: React.SFC<Props> = props => {
    return(
        <Row>
            <Col md={4}>
                <div className="card main-card">
                    <p className="main-amount"> {
                        new Intl.NumberFormat('en-US', {
                            style: 'currency',
                            currency: 'USD'
                        }).format(props.total)
                        }</p>
                    <p>Dinero total</p>
                </div>
            </Col>
        </Row>
    );
}