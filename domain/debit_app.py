from pydantic import Field, BaseModel

class DebitCard(BaseModel):
    card_no: int = Field(description="Card Holder Number", default=505050)
    account_name: str = Field(description="Card Holder Name", default="Your Account Name" )
    status: str = Field(description="Card Status", default="active")
    balance: float = Field(description="Card Balance", default=10000, ge=0)

class CreateCard(BaseModel):
    card_no:int = Field(description="Card Holder Number", default=505055)
    account_name: str = Field(description="Card Holder Name", default="Your Account Name")
    status: str = Field(description="Card Status", default="active")
    balance: float = Field(description="Card Balance", default=10000)

class AddCardBalance(BaseModel): 
    card_no:int = Field(description="Card Holder Number", )
    balance_to_add: float = Field(description="Card Balance", default=0.0)

class TransactionDebit(BaseModel):
    card_no:int = Field(description="Card Holder Number", default=0)
    transaction: str = Field(description="Transaction", default="")
    amount: float = Field(description="Amount to be deducted", default=0.0)

