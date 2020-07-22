import React from 'react';
import { shallow, mount } from 'enzyme';

import { GlobalAmount } from './GlobalAmount';
import { GlobalAmountPresentational } from './GlobalAmountPresentational';
import { GlobalAmountPresentationalProps, GlobalAmountProps } from './Props';

describe('Global Amount component', () => {
    let props_pres: GlobalAmountPresentationalProps;
    let props_cont: GlobalAmountProps;

    beforeEach(() => {
        props_pres = {
            total: 0
        };

        props_cont = {
            bank_accounts: [],
            wallets: [],
            cards: []
        };
    });

    describe("when there is no accounts", () => {
        it("presentational renders just with a zero", () => {
            const wrapper = shallow(<GlobalAmountPresentational {...props_pres} />);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$0.00"
            );
        });
        it("container sends justa a zero", () => {
            const wrapper = mount(<GlobalAmount {...props_cont}/>);
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
            const wrapper = shallow(<GlobalAmount {...props_cont}/>);
            expect(wrapper.state('total')).toEqual(0);
            props_cont.bank_accounts = [{
                "balance": 10,
                "bank": "test_bank",
                "source": {"id": "some_id", "name": "some_name"}
            }]
            props_cont.wallets = [{
                "balance": 15,
                "bank": "Wallet",
                "source": {"id": "some_id", "name": "some_name"}
            },{
                "balance": 11.34,
                "bank": "Wallet",
                "source": {"id": "some_id", "name": "some_name"}
            }]
            wrapper.setProps({...props_cont});
            expect(wrapper.state('total')).toEqual(36.34);
        });
        it("container makes correctly the sum", () => {
            props_cont.bank_accounts = [{
                "balance": 10,
                "bank": "test_bank",
                "source": {"id": "some_id", "name": "some_name"}
            }]
            props_cont.wallets = [{
                "balance": 15,
                "bank": "Wallet",
                "source": {"id": "some_id", "name": "some_name"}
            },{
                "balance": 11.34,
                "bank": "Wallet",
                "source": {"id": "some_id", "name": "some_name"}
            }]
            props_cont.cards = [{
                "cut": 0,
                "pay": 0,
                "bank": "card-bank",
                "used": 20,
                "source": {"id": "some_id", "name": "some_name"},
                "credit": 5000
            }]
            const wrapper = mount(<GlobalAmount {...props_cont}/>);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$16.34"
            );
        });
    });
});
