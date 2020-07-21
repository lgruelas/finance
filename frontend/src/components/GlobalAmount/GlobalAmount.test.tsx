import React from 'react';
import { shallow } from 'enzyme';

// import { GlobalAmount } from './GlobalAmount';
import { GlobalAmountPresentational } from './GlobalAmountPresentational';
import { GlobalAmountPresentationalProps } from './Props';


describe('Global Amount component', () => {
    let props_pres: GlobalAmountPresentationalProps;

    beforeEach(() => {
        props_pres = {
            total: 0
        };
    });

    describe("when there is no accounts", () => {
        it("renders just with a zero", () => {
            const wrapper = shallow(<GlobalAmountPresentational {...props_pres} />);
            expect(wrapper.find(".main-amount").text()).toMatch(
                "$0.00"
            );
        });
    });
});