##Charles Eubanks, Assignment 3
##The purpose of this program is to calculate a salary for a person who works
##between 2 and 50 days, and for the salary to double each day.

days_wrk = int(input(f"Please input the amount of days worked. "))
while days_wrk < 2 or days_wrk > 50: ##Making sure data is valid.
    print (f"Invalid input! Days must be between 2 and 50.")
    days_wrk = int(input(f"Please re-input days worked."))
day_sal = .01
total_daysal = 0
total_pay = 0 ##Variable setup.
print (f"1                .01") ##for statement does not include first day.
for days_wrk in range(1, days_wrk, 1):
    total_daysal = day_sal * 2 ** days_wrk  ##Doubles the pay each day.
    total_pay += total_daysal
    print(f"{days_wrk + 1}               {total_daysal}") ##Data table.
    ##Adding this by one corrects the amount of days, as the table does not
    ##include the first day, and thus looks like its off by one.
    
print(f"Your total pay for these days worked is {total_pay + .01:.2f}")
##Used +.01 because the for statement does not include the first day.

##Output:
##Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap4-week7\assign3\Assign3program.py
##Please input the amount of days worked. 1
##Invalid input! Days must be between 2 and 50.
##Please re-input days worked.51
##Invalid input! Days must be between 2 and 50.
##Please re-input days worked.2
##1                .01
##2               0.02
##Your total pay for these days worked is 0.03
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap4-week7\assign3\Assign3program.py
##Please input the amount of days worked. 5
##1                .01
##2               0.02
##3               0.04
##4               0.08
##5               0.16
##Your total pay for these days worked is 0.31
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap4-week7\assign3\Assign3program.py
##Please input the amount of days worked. 10
##1                .01
##2               0.02
##3               0.04
##4               0.08
##5               0.16
##6               0.32
##7               0.64
##8               1.28
##9               2.56
##10               5.12
##Your total pay for these days worked is 10.23
##>>> 
##= RESTART: C:\Users\Owner\Downloads\CIS115\CISchap4-week7\assign3\Assign3program.py
##Please input the amount of days worked. 50
##1                .01
##2               0.02
##3               0.04
##4               0.08
##5               0.16
##6               0.32
##7               0.64
##8               1.28
##9               2.56
##10               5.12
##11               10.24
##12               20.48
##13               40.96
##14               81.92
##15               163.84
##16               327.68
##17               655.36
##18               1310.72
##19               2621.44
##20               5242.88
##21               10485.76
##22               20971.52
##23               41943.04
##24               83886.08
##25               167772.16
##26               335544.32
##27               671088.64
##28               1342177.28
##29               2684354.56
##30               5368709.12
##31               10737418.24
##32               21474836.48
##33               42949672.96
##34               85899345.92
##35               171798691.84
##36               343597383.68
##37               687194767.36
##38               1374389534.72
##39               2748779069.44
##40               5497558138.88
##41               10995116277.76
##42               21990232555.52
##43               43980465111.04
##44               87960930222.08
##45               175921860444.16
##46               351843720888.32
##47               703687441776.64
##48               1407374883553.28
##49               2814749767106.56
##50               5629499534213.12
##Your total pay for these days worked is 11258999068426.23
##>>> 
num = 0
for num in range (4):
    print (num)
