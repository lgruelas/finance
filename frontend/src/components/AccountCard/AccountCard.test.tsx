import React from 'react';
import { shallow, mount } from 'enzyme';
import { AccountCardPresentational } from './AccountCardPresentational';
import { AccountCardPresentationalProps as PresProps,
         AccountCardProps as ContProps } from './Props';
import { AccountCard } from './AccountCard';
import { DigitalAccount, Card } from './../../models/accounts';


describe("Account Card component", () => {
    let presProps: PresProps;
    let contProps: ContProps;

    beforeEach(() => {
        presProps = {
            "color": "green",
            "amount": "123",
            "bank": "bank-for-test",
            "name": "account-test"
        };
        contProps = {
            "account":{
                "id": "example-id",
                "name": "example-name",
                "balance": 300
            }
        };
    });

    describe("when info is passed", () => {
        it("renders with the expected css classes", () => {
            const wrapper = shallow(<AccountCardPresentational {...presProps} />);
            expect(wrapper.find(".account-text").text()).toMatch("123");
            expect(wrapper.find(".account-text").get(0).props.style).toHaveProperty("color", "green");
            expect(wrapper.find("span").at(1).text()).toMatch("bank-for-test");
            expect(wrapper.find(".card-image").prop("src")).toMatch("../assets/imgs/account-test.png");
            expect(wrapper.find(".card-image").prop("alt")).toMatch("account-test");
        });
        it("assigns the blue color when needed", () => {
            const wrapper = mount(< AccountCard {...contProps} />);
            expect(wrapper.find(".account-text").get(0).props.style).toHaveProperty("color", "blue");
        });
        it("assigns the green color when needed", () => {
            (contProps.account as DigitalAccount) = {...contProps.account, "bank": "bank-test"}
            const wrapper = mount(< AccountCard {...contProps} />);
            expect(wrapper.find(".account-text").get(0).props.style).toHaveProperty("color", "green");
        });
        it("assigns the red color when needed", () => {
            (contProps.account as Card) = {...contProps.account, "cut": 20, "pay": 20, "credit": 4000, "bank": "card-bank-test"}
            const wrapper = mount(< AccountCard {...contProps} />);
            expect(wrapper.find(".account-text").get(0).props.style).toHaveProperty("color", "red");
        });
        it("assigns the card ammount as expected", () => {
            (contProps.account as Card) = {...contProps.account, "cut": 20, "pay": 20, "credit": 4000, "bank": "card-bank-test"}
            const wrapper = mount(< AccountCard {...contProps} />);
            expect(wrapper.find(".account-text").text()).toMatch("$3,700.00");
        });
    });
});
