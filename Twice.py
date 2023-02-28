total = 0
MERCH = 100
user_input = input("Welcome to the Twice trip calculator. How many people are on the trip? ")


if user_input == '3':
    user_input2 = input("Hopeful or Higher End? H/HE: ")
    if user_input2 == 'H':
        ticket = int(input("Enter in the ticket price? (Est. 250) "))
        total = total + ticket
        gas = int(input("How much will you be paying for gas? (Est. 115): "))
        total = gas + total

        food = int(input("How much will you pay for food? (Est. 100): "))
        total = food + ticket + total + MERCH
        print("Total cost trip is: ", total)

    elif user_input2 == 'HE':
        ticket = int(input("Enter in the ticket price? (Est. 300-500) "))
        total = total + ticket

        gas = int(input("How much will you be paying for gas? (Est. 115): "))
        total = gas + total

        housing = int(input("How much will you be paying for housing? (Est. 200): "))
        total = total + housing

        food = int(input("How much will you pay for food? (Est. 150): "))
        total = food + total

        total = MERCH + total

        print("Total cost trip is: ", total)


elif user_input == '4':
    user_input2 = input("Hopeful or Higher End? H/HE: ")
    if user_input2 == 'H':
        ticket = int(input("How much will you be paying for tickets? (Est. 150): "))
        total = ticket + total
        gas = int(input("How much will you be paying for gas? (Est. 100): "))
        total = gas + total
        food = int(input("How much will you pay for food? (Est. 70)"))
        total = food + ticket + total + MERCH
        print("Total cost trip is: ", total)

    elif user_input2 == 'HE':
        ticket = int(input("Enter in the ticket price? (Est. 500-700) "))
        total = total + ticket

        gas = int(input("How much will you be paying for gas? (Est. 100): "))
        total = gas + total

        housing = int(input("How much will you be paying for housing? (Est. 200): "))
        total = total + housing

        food = int(input("How much will you pay for food? (Est. 150): "))
        total = food + total

        total = MERCH + total

        print("Total cost trip is: ", total)

