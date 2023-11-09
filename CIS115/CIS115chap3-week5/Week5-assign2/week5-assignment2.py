##Charles Eubanks, CIS115.950, Mrs. Tollapa, Quantity purchase calculator.
##Week 5, Assignment 2

quant_pur = int(input(f"How many packages would you like to buy? ") )
pack_pri = 99.99
disc_quant = 0
full_pri = 0
dis_perc = 0
dis_amoun = 0
fin_pri = 0
##Setting up the variables here.
if quant_pur < 10 and quant_pur > -1:
    full_pri = quant_pur * pack_pri
    fin_pri = full_pri
else: ##Simple multiplication here since there is no discount.
        ##Also made the final price equal to have all 4 variables.
    if quant_pur > 9 and quant_pur < 20:
        dis_perc = .10
        full_pri = quant_pur * pack_pri
        dis_amoun = full_pri * dis_perc
        fin_pri = full_pri - dis_amoun
    else: ##Had to redo all of the variables here, which feels kind of
            ## inefficient. Is there a more efficient way to do this?
        if quant_pur > 19 and quant_pur < 50:
            dis_perc = .20
            full_pri = quant_pur * pack_pri
            dis_amoun = full_pri * dis_perc
            fin_pri = full_pri - dis_amoun
        else: ##Just copy and pasting the rest for it to work, with
                ## increasing percentage.
            if quant_pur > 49 and quant_pur < 100:
                dis_perc = .30
                full_pri = quant_pur * pack_pri
                dis_amoun = full_pri * dis_perc
                fin_pri = full_pri - dis_amoun
            else:
                if quant_pur > 99 and quant_pur < 301:
                    dis_perc = .40
                    full_pri = quant_pur * pack_pri
                    dis_amoun = full_pri * dis_perc
                    fin_pri = full_pri - dis_amoun
                    ##finishes the if statement here.
if quant_pur < 0 or quant_pur > 300:##price amounts printed even though the
    ##quantity was an incorrect amount, so I put the print functions in an
    ##if statement.
   print(f"Error:Quantity cannot be less than 0 or more than 300.")
else:
    print(f"quantity purchased: {quant_pur}")
    print(f"Full Price: {full_pri:.2f}")
    print(f"Discount: {dis_perc:.0%}")
    print(f"Discounted amount: {dis_amoun:.2f}")
    print(f"Your final total is {fin_pri:.2f}")

##Testing same outputs used on the sample output.
##5, 15, 200, 55, -1, and 400.
##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap3-week5\Week5-assign2\week5-assignment2.py
##How many packages would you like to buy? 5
##quantity purchased: 5
##Full Price: 499.95
##Discount: 0%
##Discounted amount: 0.00
##Your final total is 499.95
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap3-week5\Week5-assign2\week5-assignment2.py
##How many packages would you like to buy? 15
##quantity purchased: 15
##Full Price: 1499.85
##Discount: 10%
##Discounted amount: 149.98
##Your final total is 1349.87
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap3-week5\Week5-assign2\week5-assignment2.py
##How many packages would you like to buy? 200
##quantity purchased: 200
##Full Price: 19998.00
##Discount: 40%
##Discounted amount: 7999.20
##Your final total is 11998.80
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap3-week5\Week5-assign2\week5-assignment2.py
##How many packages would you like to buy? 55
##quantity purchased: 55
##Full Price: 5499.45
##Discount: 30%
##Discounted amount: 1649.83
##Your final total is 3849.61
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap3-week5\Week5-assign2\week5-assignment2.py
##How many packages would you like to buy? -1
##Error:Quantity cannot be less than 0 or more than 300.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap3-week5\Week5-assign2\week5-assignment2.py
##How many packages would you like to buy? 400
##Error:Quantity cannot be less than 0 or more than 300.
##>>> 
