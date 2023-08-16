import app

if __name__ == "__main__":
    starting_amount = 2500000
    # $10 - 100
    rev1 = int((starting_amount/100)*10)
    # $49 - 600
    rev2 = int((starting_amount/600)*49)
    # $99 - 1500
    rev3 = int((starting_amount/1500)*99)

    cost = 1250 + 5000
    print(rev1-cost, rev2-cost, rev3-cost)
