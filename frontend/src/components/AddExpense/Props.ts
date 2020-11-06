import { CategoriesAccounts } from './../../models/common';

export interface AddExpenseButtonProps extends CategoriesAccounts {
    refresh: () => void
}

export interface AddExpenseModalProps extends AddExpenseButtonProps {
    open: boolean,
    toggle: () => void
}