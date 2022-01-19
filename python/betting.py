def betting(rXA, rXB, rYA, rYB, bA):
    rate1 = 1 / rXA + 1 / rXB # both x
    rate2 = 1 / rYA + 1 / rYB # both y
    rate3 = 1 / rYA + 1 / rXB # y and x
    rate4 = 1 / rXA + 1 / rYB # x and y
    
    smallest = min(rate1, rate2, rate3, rate4) # find the lowest rate
    if smallest >= 1: # if the lowest rate is greater than one, no profit can be made
        return None
    
    if smallest == rate3: # start with rate 3 and rate 4 because no website should be stupid enough to lose with their own odds
        rA, rB = rYA, rXB
    elif smallest == rate4:
        rA, rB = rXB, rYB
    elif smallest == rate1:
        rA, rB = rXA, rXB
    else:
        rA, rB = rYA, rYB

    bB = bA * rA / rB # formula provided for bet B
    return bA * rA - bA - bB

if __name__=="__main__":
    print(betting(1.2, 4.1, 1.5, 2.9, 100.0))
    print(betting(1.2, 4.1, 1.2, 4.1, 570686.0))