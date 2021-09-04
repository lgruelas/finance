import { Source } from './Source';

export interface Wallet {
    source: Source,
    balance: number,
    bank: "Wallet"
}