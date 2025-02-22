import random

def get_numbers_ticket(min, max, quantity):
    try:
        number_list = []
        if (min >= 1 and max <= 1000) and (min <= quantity <= max):
            for i in range(min, max + 1):
                number_list.append(i)
        ticket_numbers = (random.choices(number_list, k=quantity))
        ticket_numbers.sort()
        print(f" Your ticket numbers: {ticket_numbers}")
    except:
        print(f"Error: Invalid input: {min}, {max}, {quantity}")
        print(number_list)


get_numbers_ticket(1, 100, 6)

