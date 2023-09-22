from debit_card_bll import DebitCardBll

class Controller():

    debit_bll = DebitCardBll()
    
    def list_cards(self):
        return self.debit_bll.get_cards()
    
    def list_card_by_no(self, card_no: int):
        return self.debit_bll.get_card_by_card_no(card_no)
    
    def create_card(self, card_no:int, account_name:str):
        self.debit_bll.create_card(card_no,account_name)
    
    def deactivate_card_status_by_card_no(self,card_no:int, status:str):
        self.debit_bll.deactivate_card_status_by_card_no(card_no, status)
    
    def activate_card_status_by_card_no(self,card_no:int):
        self.debit_bll.activate_card_status_by_card_no(card_no)
    

    def add_money_to_balance(self, card_no: int, balance: float):
        self.debit_bll.add_money_to_balance_by_card_no(card_no, balance)

    def transaction_debit(self, card_no:int, transaction_type: str, amount: float ):
        self.debit_bll.transaction_debit(card_no, transaction_type, amount)
    
    def list_transac_by_card_no(self, card_no:int):
        self.debit_bll.transaction_history_by_card_no(card_no)