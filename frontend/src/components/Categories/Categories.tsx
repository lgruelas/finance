import React from 'react';
import { Row } from 'reactstrap';
import { CategorieUsed } from './../../models/categories';
import { getCategories } from './../../services/Categories';
import { CategorieCard } from './CategorieCard';

interface State {
    categories: Array<CategorieUsed>
}
export class Categories extends React.Component<{},State> {
    constructor(props: any){
        super(props);
        this.state = {
            categories: []
        }
    }

    componentWillMount() {
        Promise.all([
            getCategories()
        ]).then(([categories_result]) => {
            this.setState({categories: categories_result.data})
        }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                {this.state.categories.map(function(element: CategorieUsed)
                    {return (<Row key={element.id}>
                        <CategorieCard {...element}  />
                    </Row>);}
                )}
            </div>
        );
    }
}