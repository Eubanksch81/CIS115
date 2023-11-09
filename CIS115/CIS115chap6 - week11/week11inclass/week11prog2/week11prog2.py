##Charles Eubanks, Reading files, program 2

def main():
    rec_number = 0
    total = 0
    print("# Value \n -------")
    fil_inp_numbers = open("numbers.txt", "r")
    one_number = fil_inp_numbers.readline() #15\n
    while one_number != "":
        rec_number += 1
        ##cast one_number into an int
        one_number_int = int(one_number)
        total += one_number_int
        print(f"{rec_number}  {one_number_int:>2}")
        one_number = fil_inp_numbers.readline()
    print(f"\nTotal = {total}")
    print(f"# of records = {rec_number}")
    avg_val = total/rec_number
    print(f"Average = {avg_val:.1f}")
main()
    
