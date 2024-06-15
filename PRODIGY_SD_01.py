num = eval(input("How much is the temperature? -->"))
temp = input("What is the unit of temperature? C, F or K? -->")
if temp == 'c' or temp == 'C':
    fr = num*(9/5) + 32
    kl = num + 273.15
    print(f"{fr:.2f}°F and {kl:.2f}K")
    
elif temp == 'K' or temp == 'k':
    cs = num - 273.15
    fr = cs * (9/5) + 32
    print(f"{fr:.2f}°F and {cs:.2f}°C")
    
elif temp == 'f' or temp == 'F':
    cs = (num - 32) * (5/9)
    kl = cs + 273.15
    print(f"{cs:.2f}°C and {kl:.2f}K")

else:
    print("Not a valid unit!")