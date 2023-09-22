from fastapi import FastAPI
from debit_card_bll import DebitCardBll
from domain.debit_app import DebitCard,  AddCardBalance, TransactionDebit
from util import is_card_no_valid
from typing import List
debit_bll = DebitCardBll()

app = FastAPI()

@app.get('/list-all-cards')
def list_cards()->List[DebitCard]:
    return debit_bll.get_cards()

@app.get('/list-transac-history')
def list_transac_by_card_no(card_no:int):
    return debit_bll.transaction_history_by_card_no(card_no)

@app.get('/list-card')
def list_card_by_no(card_no:int)-> DebitCard:
    return debit_bll.get_card_by_card_no(card_no)

@app.put('/create-card')
def create_card(card_no:int, account_name:str):
    if is_card_no_valid(card_no) and debit_bll.if_card_exists(card_no) == None:
        debit_bll.create_card(card_no, account_name)
        return "Account created successfully"
    return "Card Exists or Invalid Card number."

@app.patch('/update-card-status-deactivate')
def deactivate_card_status_by_card_no(card_no:int):
    if debit_bll.if_card_exists(card_no)!= None: 
        debit_bll.deactivate_card_status_by_card_no(card_no)
        return "Account deactivated"
    return "Card Exists or Invalid Card number."

@app.patch('/update-card-status-activate')
def activate_card_status_by_card_no(card_no:int):
    if debit_bll.if_card_exists(card_no)!= None: 
        debit_bll.activate_card_status_by_card_no(card_no)
        return "Account activated"
    return "Card Exists or Invalid Card number."

@app.patch('/add-card-balance')
def add_card_balance_by_card_no(response: AddCardBalance):
    response.card_no 
    response.balance_to_add 
    if debit_bll.is_card_active(response.card_no ) and debit_bll.if_card_exists(response.card_no )!= None:
        debit_bll.add_money_to_balance_by_card_no(response.card_no , response.balance_to_add)
        
        return "{} added to your account.".format( response.balance_to_add )
    else:
        return "Card must be active or must exist."

@app.patch('/card-transaction-debit')
def transaction_debit_by_card_no(response: TransactionDebit ):
    card_no = response.card_no 
    transaction = response.transaction
    amount = response.amount
    if debit_bll.is_balance_sufficient(card_no, amount) and debit_bll.is_card_active(card_no):
        debit_bll.transaction_debit(card_no, transaction, amount)
        return "You used {} to {}".format(amount, transaction)
    return "You don't have enough balance or your account is not activated"

