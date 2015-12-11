import BasketballPlayer

def main():
    lebron_james = BasketballPlayer.BasketballPlayer("Lebron", "James", 23)

    print(lebron_james.get_number())

    lebron_james.set_number(6)

    print(lebron_james.get_number())




main()