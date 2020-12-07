hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
x = hours - 40
ovr = (hours - x) * rate + (x * (rate * 1.5))
reg = hours * rate
if(hours > 40):
    # print("OverTime")
    print("Pay: ", ovr)
else :
    # print("Regular")
    print("Pay", reg)