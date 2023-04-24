weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
 
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in LBs: " + converted)
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))