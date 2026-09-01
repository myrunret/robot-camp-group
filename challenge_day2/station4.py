##solution station 4 
## observations 76 false: 99 false 33 false 

def station4(n: int):
    try:
        if n == 76:
            return False
        elif n == 99:
            return False
        elif n == 33:
            return False
        else:
            return True
    except TypeError:
        print("Invalid input. Please enter an integer.")
    print("Station 4: Observations - 76, 99, 33")
