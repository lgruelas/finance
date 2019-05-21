import React from 'react';
import { Overview } from './components/Overview/Overview';
import { Categories } from './components/Categories/Categories';
import { Switch, Route } from 'react-router-dom';

export const Main: React.SFC = () => {
    return (
        <Switch>
            <Route exact path="/" component={Overview} />
            <Route exact path="/categories" component={Categories} />
        </Switch>
    );
}