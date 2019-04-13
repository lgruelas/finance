import React from 'react';
import { Navigation } from './components/Navigation/Navigation';
import { Overview } from './components/Overview/Overview';

import './App.css';

export class App extends React.Component {
  public render() {
    return (
      <div className="App">
        <Navigation />
        <Overview />
      </div>
    );
  }
}
