from dao.debit_card_dao import DebitCardDao



class DebitCardBll():
    debit_card_dao = DebitCardDao()

    def get_cards(self):
        return self.debit_card_dao.get_cards()

    def get_card_by_card_no(self, card_no:int):
        for item in self.debit_card_dao.get_cards():
            if card_no == item["card_no"]:
                return item
        return None

    def create_card(self, card_no:int, account_name:str):
        self.debit_card_dao.add_card(card_no,account_name)
    
    def if_card_exists(self, card_no:int): 
        return self.get_card_by_card_no(card_no)
    
    def is_card_active(self, card_no:int):
        for item in self.debit_card_dao.get_cards():
            if card_no == item["card_no"]:
                if item["status"] == "active":
                    return True
        return False
    
    def is_balance_sufficient(self, card_no:int, amount:float): 
        for item in self.debit_card_dao.get_cards():
            if card_no == item["card_no"]:
                if item["balance"] < amount:
                    return False  
        return True
    
    def deactivate_card_status_by_card_no(self,card_no:int):
        self.debit_card_dao.deactivate_card_status(card_no)

    def activate_card_status_by_card_no(self,card_no:int):
        self.debit_card_dao.activate_card_status(card_no)

    def add_money_to_balance_by_card_no(self, card_no:int, balance:float):
        self.debit_card_dao.add_money_to_balance(card_no, balance)
    
    def transaction_debit(self, card_no:int, transaction_type: str, amount: float ):
        self.debit_card_dao.transaction_debit(card_no, transaction_type, amount )
    
    def transaction_history_by_card_no(self, card_no:int):
        for item in self.debit_card_dao.get_cards():
            if card_no == item["card_no"]:
                return item["transac_history"]
        return None
        


            




