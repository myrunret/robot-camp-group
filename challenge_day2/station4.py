##solution station 4 
## observations 76 false: 99 false 33 false 

def station4(n: int):
    try:
        
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
     while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    except Exception:
        return False
