import React from 'react';
import { Navigation } from './components/Navigation/Navigation';
import { BrowserRouter } from 'react-router-dom';
import { Main } from './Main';
import './App.css';

require('dotenv').config();

export class App extends React.Component {
  public render() {
    return (
      <div className="App">
        <BrowserRouter>
          <Navigation />
          <Main />
        </BrowserRouter>
      </div>
    );
  }
}
