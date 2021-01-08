import React from 'react';
import { Row, Col } from 'reactstrap';
import { AccountCardPresentationalProps as Props } from './Props';


export const AccountCardPresentational: React.SFC<Props> = props => {
    return (
        <div className="card">
        <Row>
            <Col xs={8}>
                <span className="account-text" style={{color: props.color}}>{props.amount}</span>
                <br/>
                <span>{props.bank}</span>
            </Col>
            <Col xs={4}>
                <img width="50px" className="card-image" src={"../assets/imgs/" + props.name + ".png"} alt={props.name}/>
            </Col>
        </Row>
        </div>
    );
}
