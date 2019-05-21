import React from 'react';
import { Button } from 'reactstrap';
import { Link } from 'react-router-dom';

export const CategoriesButton: React.SFC = () => {
    return (
        <Link to="/categories">
            <Button>
                Categories
            </Button>
        </Link>
    );
}