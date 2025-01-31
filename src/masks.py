def get_mask_card_number(card_number):
    first_part = card_number[:6]
    last_part = card_number[-4:]
    masked_part = "** ****"
    masked_number = f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"
    return masked_number
card_number = input()
print(get_mask_card_number(card_number))


def get_mask_account(account_number):
    last_part = account_number[-4:]
    masked_account = "**" + last_part

    return masked_account
account_number = input()
print(get_mask_account(account_number))

