print("                                          ")
print(" -----------------------------------------")
print("          BIKE ROAD TAX CALCULATOR        ")
print(" -----------------------------------------")
print(" |COST Price(Rs)                    Tax% |")
print(" -----------------------------------------")
print(" |>100,000                           15  |")
print(" -----------------------------------------")
print(" |>50,000 and <=100,000              10  |")
print(" -----------------------------------------")
print(" |<=50,000                           5   |")
print(" -----------------------------------------")

tax_list = [15,10,5]
try:
    ent = int(input("Enter your bike cost price to see road tax incurred: "))

except ValueError as e:
    print("Something is wrong:",e,"\n You have entererd a none integer value")

else:
    if ent > 100000:
        print ("Tax placed is ",tax_list[0],"%.")
        print ("Road tax is Rs ",(ent*tax_list[0])/100)

    elif ent > 50000 and ent <= 100000:
        print ("Tax placed is ",tax_list[1],"%.")
        print ("Road tax is Rs ",(ent*tax_list[1])/100)
        
    elif ent <= 50000 and ent >= 0: 
        print ("Tax placed is ",tax_list[2],"%.")
        print ("Road tax is Rs ",(ent*tax_list[2])/100)

    else:
        print('Values are Out of Range')
