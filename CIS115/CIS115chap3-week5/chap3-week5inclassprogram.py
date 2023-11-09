##Charles Eubanks, week 5, boolean variables
##if hs_year == 2021, and sat_sc > ... and hs_gpa > ...:
##  is_hons_ok = True

##if last_wcc_year < 2021 and hours >= ... and wcc_gpa > ...:
##  is_hons_ok = True

##if (hs_year == 2021, and sat_sc > ... and hs_gpa > ...) or (last_wcc_year < 2021 and hours >= ... and wcc_gpa > ...) == true
##if is_hons_ok == True:

is_hons_ok = True

if is_hons_ok == True:
    print (f"You are eligible to be in the Honors Program")
else:
    print (f"You are not eligible to be in the honors program.")

if is_hons_ok == False:
    print (f"You suck.")
else:
    print (f"Nice")
##Example1
hrs_wrk = int(input (f"Hours worked: ") )
hrly_rate = 10
ot_hrs = 0
reg_pay = 0
ot_pay = 0
tot_pay = 0

if hrs_wrk <= 40: ##No overtime
    reg_pay = hrs_wrk * hrly_rate
else: ##Overtime
    ot_hrs = hrs_wrk - 40
    print (f"Overtime hours = {ot_hrs}")
    ot_pay = ot_hrs * hrly_rate * 1.5
    reg_pay = 40 * hrly_rate
##Write programs out in bits and pieces, and try things out one at a time.

tot_pay = reg_pay + ot_pay
print (f"Total Pay = ${tot_pay:.2f}")
