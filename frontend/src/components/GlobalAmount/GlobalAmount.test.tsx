import React from 'react';
import { shallow, mount } from 'enzyme';

import { GlobalAmount } from './GlobalAmount';
import { GlobalAmountPresentational } from './GlobalAmountPresentational';
import { GlobalAmountPresentationalProps, GlobalAmountProps } from './Props';

describe('Global Amount component', () => {
    let propsPres: GlobalAmountPresentationalProps;
    let propsCont: GlobalAmountProps;

    beforeEach(() => {
        propsPres = {
            total: 0
        };

        propsCont = {
            bankAccounts: [],
            wallets: [],
            cards: []
        };
    });

    describe("when there is no accounts", () => {
        it("presentational renders just with a zero", () => {
            const wrapper = shallow(<GlobalAmountPresentational {...propsPres} />);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$0.00"
            );
        });
        it("container sends justa a zero", () => {
            const wrapper = mount(<GlobalAmount {...propsCont}/>);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$0.00"
            );
        });
    });
    describe("when there is accounts", () => {
        it("presentational renders the given amount with correct rounding", () => {
            const wrapper = shallow(<GlobalAmountPresentational total={2.013} />);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$2.01"
            );
        });
        it("container doesn't change if is the same account", () => {
            const wrapper = shallow(<GlobalAmount {...propsCont}/>);
            expect(wrapper.state('total')).toEqual(0);
            propsCont.bankAccounts = [{
                "balance": 10,
                "bank": "test-bank",
                "isInvestment": true,
                "name": "test-account",
                "id": "some-id"
            }];
            propsCont.wallets = [{
                "balance": 15,
                "name": "Wallet",
                "id": "some-id"
            },{
                "balance": 11.34,
                "name": "Wallet",
                "id": "some-id"
            }];
            wrapper.setProps({...propsCont});
            expect(wrapper.state('total')).toEqual(36.34);
        });
        it("container makes correctly the sum", () => {
            propsCont.bankAccounts = [{
                "balance": 10,
                "bank": "test-bank",
                "isInvestment": true,
                "name": "test-account",
                "id": "some-id"
            }];
            propsCont.wallets = [{
                "balance": 15,
                "name": "Wallet",
                "id": "some-id"
            },{
                "balance": 11.34,
                "name": "Wallet",
                "id": "some-id"
            }];
            propsCont.cards = [{
                "cut": 0,
                "pay": 0,
                "bank": "card-bank",
                "credit": 5000,
                "balance": 4980,
                "id": "some-id",
                "name": "some-name"
            }];
            const wrapper = mount(<GlobalAmount {...propsCont}/>);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$16.34"
            );
        });
    });
});
