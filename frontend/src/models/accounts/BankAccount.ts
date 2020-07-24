import { DigitalAccount } from './Account';

export interface BankAccount extends DigitalAccount {
    isInvestment: boolean
}