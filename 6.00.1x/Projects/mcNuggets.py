def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    
    # Case nuggets are less than 6
    if n < 6:
        return False
    elif n % 6 == 0:
        return True
    elif n % 9 == 0:
        return True
    elif n % 20 == 0:
        return True
    elif n % 15 == 0:
        return True
    elif n % 26 == 0:
        return True
    elif n % 29 == 0:
        return True
    elif n % 35 == 0:
        return True
    else:
        return False    
        
        
