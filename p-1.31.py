def make_change(charge, given):
    """
    Takes two numbers as input, one that is a monetary amount
    charged and the other that is a monetary amount given.
    It then returns the number of each kind of bill and coin
    to give back as change for the difference b/n the amount
    given and the amount charged.
    """
    change = given - charge
    # currency_units = {1: 0, 5: 0, 10: 0, 20: 0, 50: 0, 0.1: 0, 0.2: 0, 0.5: 0}
    currency_units = {50: 0, 20: 0, 10: 0, 5: 0, 1: 0, 0.5: 0, 0.2: 0, 0.1: 0}
    if change % 1:  # there are coins in the change
        whole_part = change // 1
        dec_part = round(change % 1, 2)
    else:
        whole_part, dec_part = change, 0

    # while change:
    #     for c_u in currency_units:
    #         q, r = divmod(change, c_u)
    #         currency_units[c_u] = int(q)
    #         if not r:
    #             return currency_units
    #         change = r
    #     return currency_units

    # determining the bills needed to make the change
    while whole_part:
        for bill in (50, 20, 10, 5, 1):
            q = divmod(whole_part, bill)[0]
            currency_units[bill] += int(q)
            whole_part -= q*bill
    
    # determining the coins needed to make the change
    dec_part = dec_part * 10    # to avoid an infinite loop
    while dec_part:
        for coin in [i*10 for i in (0.5, 0.2, .1)]:
            q = dec_part // coin
            currency_units[coin/10] += int(q)
            dec_part -= q*coin

    return currency_units

print(make_change(10, 20))
print(make_change(12, 20))
print(make_change(23.3, 50))
print(make_change(7.5, 10))
print(make_change(2.6, 5))