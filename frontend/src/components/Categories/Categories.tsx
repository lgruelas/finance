import React from 'react';
import { Row, Col, Button } from 'reactstrap';
import { CategorieUsed } from './../../models/categories';
import { getCategoriesUsed } from './../../services/Categories';
import { CategorieCard } from './CategorieCard';

interface State {
    categories: Array<CategorieUsed>,
    year: number,
    month: number
}
export class Categories extends React.Component<{},State> {
    remaining: number = 0;
    constructor(props: any){
        super(props);
        this.state = {
            categories: [],
            year: new Date().getFullYear(),
            month: new Date().getMonth() + 1
        }
        this.prevMonth = this.prevMonth.bind(this);
        this.nextMonth = this.nextMonth.bind(this);
    }

    refresh(year: number, month: number) {
        Promise.all([
            getCategoriesUsed(this.state.year, this.state.month)
        ]).then(([categories_result]) => {
            this.setState({categories: categories_result.data, year: year, month: month})
        }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.refresh(this.state.year, this.state.month);
    }

    prevMonth() {
        // change year and so
        this.refresh(this.state.year, this.state.month-1);
    }

    nextMonth() {
        // change year and so
        this.refresh(this.state.year, this.state.month+1);
    }

    render() {
        //change arrows
        //update not working correctly for arrows
        //must show in categories to avoid rent, savings and other ones that must be transactions
        return (
            <div>
                <Row>
                    <Col xs={6}>
                        <Button onClick={this.prevMonth}>&lt;=</Button>
                    </Col>
                    <Col xs={6}>
                        <Button onClick={this.nextMonth} className="btn-next-month">=></Button>
                    </Col>
                </Row>
                {this.state.categories.map(function(element: CategorieUsed)
                    {return (<Row key={element.id}>
                        <CategorieCard {...element}  />
                    </Row>);}
                )}
            </div>
        );
    }
}