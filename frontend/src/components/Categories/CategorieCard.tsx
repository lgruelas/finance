import React from 'react';
import { CategorieUsed } from 'src/models/categories';
import { Progress, Row, Col } from 'reactstrap';
import './Categories.css';


export const CategorieCard: React.SFC<CategorieUsed> = props => {
    const percentage: number = props.used * 100 / props.expected;
    const color: string = percentage < 40 ? "success" : percentage >= 80 ? "danger" : "warning";
    return (
        <div className="category-card">
            <Row>
                <Col xs={8}>{props.name}</Col>
                <Col xs={4}><span className={"expected-card text-"+color}>{
                        new Intl.NumberFormat('en-US', {
                            style: 'currency',
                            currency: 'USD'
                        }).format(props.expected)
                }</span></Col>
            </Row>
            <Row>
                <Col xs={{size: 4, offset: 8}}><span className="used-card text-danger">{
                        new Intl.NumberFormat('en-US', {
                            style: 'currency',
                            currency: 'USD'
                        }).format(props.used)
                }</span></Col>
            </Row>
            <br />
            <Progress value={percentage} color={color}>{props.used}</Progress>
        </div>
    );
}