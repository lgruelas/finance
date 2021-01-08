import { DigitalAccount } from './Account';

export interface Card extends DigitalAccount {
    cut: number,
    pay: number,
    credit: number
}
