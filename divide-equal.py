def divides_unevenly(numerator, denominator):
    if denominator == 0 or numerator == 0:
        return None

    quotient = numerator/denominator

    if quotient == int(quotient):
        return False
    else: return True


print(divides_unevenly(0,6))
print(divides_unevenly(0,0))
