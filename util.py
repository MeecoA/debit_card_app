def is_card_no_valid(card_no: int):
    if len(str(card_no)) == 6:
        return True
    return False