import { Source } from './Source';

export interface Card {
    cut: number,
    pay: number,
    bank: string,
    credit: number,
    used: number,
    source: Source
}