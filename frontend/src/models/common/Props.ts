import { Categorie } from './../categories';
import { Account } from './../accounts';

export interface CategoriesAccounts {
    categories: Array<Categorie>;
    accounts: Array<Account>;
}