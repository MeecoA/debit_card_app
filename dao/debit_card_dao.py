from dao.file_dao import BaseFileDaoABC
import json

class DebitCardDao(BaseFileDaoABC): 
    def __init__(self) -> None:
        super().__init__("accounts.json")
    
    def read_card_data(self):
        return super().read_file()
    
    def write_card_data(self, str_json:str):
        return super().write_file(str_json)
    
    def save_card_data(self, accounts): 
        json_data = {"accounts": accounts}
        self.write_card_data(json.dumps(json_data, indent=2))

    def get_cards(self): 
        cards = json.loads(self.read_card_data())["accounts"]
        return cards
    
    def add_card(self, card_no:int, account_name:str):
        new_card = { 
        "card_no": card_no,
        "account_name": account_name,
        "status": "activated",
        "balance": 0.00, 
        "transac_history": [{}]
        }
        cards = self.get_cards()
        cards.append(new_card)
        self.save_card_data(cards)

    def deactivate_card_status(self,card_no: int): 
        cards = self.get_cards()
        for item in cards: 
            if card_no == item["card_no"]:
                item["status"] = "deactivated"
        self.save_card_data(cards)
    
    def activate_card_status(self,card_no: int): 
        cards = self.get_cards()
        for item in cards: 
            if card_no == item["card_no"]:
                item["status"] = "active"
        self.save_card_data(cards)


    def add_money_to_balance(self, card_no:int, balance:float):
        cards = self.get_cards()
        for item in cards: 
            if card_no == item["card_no"]:
                item["balance"] += balance
                item["transac_history"].append({"transaction - add credit ": balance})
        self.save_card_data(cards)



    def transaction_debit(self, card_no:int, transaction_type: str, amount: float ):
        cards = self.get_cards()
        for item in cards:
            if card_no == item["card_no"]:
                item["balance"] -= amount
                item["transac_history"].append({"transaction - debit ": transaction_type, "amount deducted": amount})
        self.save_card_data(cards)


    
