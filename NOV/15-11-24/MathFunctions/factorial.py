def fact(sankya):
    if sankya == 1 or sankya == 0:
        return 1
    else:
        return (sankya * fact(sankya - 1))
