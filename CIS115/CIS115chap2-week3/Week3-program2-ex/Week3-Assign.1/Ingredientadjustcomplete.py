##Charles Eubanks, CIS115.950, Mrs. Tolappa
##The goal of this program is to create an ingredient adjuster that adjusts
##The amount of ingredients required depending on the number of cookies that
##a person inputs.

##sug. per: .0364
##but. per: .0208
##flo. per: .0572

print(f"Welcome to Charles' Bakery!")
sug_amoun = int( input (f"How many cookies would you like to make? ") ) * .0364
but_amoun = (sug_amoun / .0364) * .0208
flo_amoun = (sug_amoun / .0364) * .0572
##Using the input of how many cookies I would make, I used the first line to
##state the amount of sugar needed. Then for the next two lines, I would
##Undo the sugar amount and multiply by the amount needed for 1 cookie.

print (f"Awesome! I will be needing...")
print (f"about {sug_amoun:.1f} cups of sugar,")
print (f"as well as {but_amoun:.1f} cups of butter,")
print (f"and {flo_amoun:.1f} cups of flour.")
print(f"Enjoy your cookies!")
##Tried to go for all 3 amounts on the same line, but it looked too messy.

##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap2-week3\Week3-program2-ex\Week3-Assign.1\Ingredientadjust.py
##Welcome to Charles' Bakery!
##How many cookies would you like to make? 50
##Awesome! I will be needing...
##about 1.8 cups of sugar,
##as well as 1.0 cups of butter,
##and 2.9 cups of flour
##Enjoy your cookies!
##>>> 
