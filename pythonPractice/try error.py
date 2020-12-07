a = input('Enter Hours: ')
b = input('Enter Rate: ')

try:
    hours = float(a)
    rate = float(b)
except:
    print("Error! Please Enter Numeric Input!")
    quit()

x = hours - 40
ovr = (hours - x) * rate + (x * (rate * 1.5))
reg = hours * rate

if(hours > 40):
    print("Pay: ", ovr)
else :
    print("Pay", reg)
