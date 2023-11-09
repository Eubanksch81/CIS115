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
print (f"and {flo_amoun:.1f} cups of flour")
print(f"Enjoy your cookies!")
##Tried to go for all 3 amounts on the same line, but it looked too messy.
