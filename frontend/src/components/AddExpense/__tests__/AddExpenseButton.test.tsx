import React from 'react';
import { shallow, mount } from 'enzyme';
import { AddExpenseButton } from './../AddExpenseButton';
import { AddExpenseButtonProps } from './../Props';

describe("Add expense button component", () => {
    let props: AddExpenseButtonProps;

    beforeEach(() => {
        props = {
            categories: [],
            accounts: [],
            refresh: () => {}
        }
    });

    describe("when the button is clicked", () => {
        it("modal starts hide and then shows", () => {
            const wrapper = shallow(<AddExpenseButton {...props} /> );
            expect(wrapper.state("isModalOpen")).toBeFalsy();
            wrapper.find(".add-expense-button").simulate("click");
            expect(wrapper.state("isModalOpen")).toBeTruthy();
            wrapper.find(".add-expense-button").simulate("click");
            expect(wrapper.state("isModalOpen")).toBeFalsy();
        });
    });
    describe("when modal is open", () => {
        it("closes the modal in cancel", () => {
            const wrapper = mount(<AddExpenseButton {...props} /> );
            expect(wrapper.state("isModalOpen")).toBeFalsy();
            console.log(wrapper.debug());
            console.log(wrapper.find(".cancel-button"));
            wrapper.find("Button.add-expense-button").simulate("click");
            expect(wrapper.state("isModalOpen")).toBeTruthy();
            wrapper.find(".cancel-button").simulate("click");
            expect(wrapper.state("isModalOpen")).toBeFalsy();
        });
    });
});
