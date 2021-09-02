"""
credit card function
"""
CREDIT_CARD = str(
    input(
        "Enter a credit card number to validate (Mastercard, Visa, Discover, Amex only): "
    )
)


def val_cc(number):
    """
    value of credit card function
    """
    cc_rev = number[::-1]
    total = 0
    for i in cc_rev[1::2]:
        numx = int(i) * 2
        if len(str(numx)) == 2:
            for stra in str(numx):
                total += int(stra)
        else:
            total += int(numx)

    for i in cc_rev[::2]:
        total += int(i)

    return total


CHECKA = int(CREDIT_CARD[:2]) >= 51 and int(CREDIT_CARD[:2]) <= 55 and len(CREDIT_CARD) == 16
CHECKB = int(CREDIT_CARD[0]) == 4 and (len(CREDIT_CARD) == 13 or len(CREDIT_CARD) == 16)
CHECKC = (int(CREDIT_CARD[:2]) == 34 or int(CREDIT_CARD[:2]) == 37) and len(CREDIT_CARD) == 15
CHECKD = int(CREDIT_CARD[:4]) == 6011 and len(CREDIT_CARD) == 16
if CHECKA or CHECKB or CHECKC or CHECKD:
    if val_cc(CREDIT_CARD) % 10 == 0:
        print("%s is a valid credit card number" % CREDIT_CARD)
    else:
        print("%s is NOT a valid credit card number" % CREDIT_CARD)
else:
    print("%s is NOT a valid credit card number" % CREDIT_CARD)
