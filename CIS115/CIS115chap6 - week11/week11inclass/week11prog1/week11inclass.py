##Charles Eubanks, reading from files

def main():
    rec_number = 0
    fil_r_names = open("names.txt", "r")
    one_name = fil_r_names.readline()
    while one_name != "":
        rec_number += 1
        one_name_nl = one_name.strip("\n")
        print(f"{rec_number:>2}. {one_name_nl}")
        one_name = fil_r_names.readline()

    print(f"Record count = {rec_number}")

main()
