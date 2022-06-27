def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    if a>=10 and a<=99:
        x = a // 10
        y = a%10
        z = y*10+x
        return z<=a 


print(main(35))