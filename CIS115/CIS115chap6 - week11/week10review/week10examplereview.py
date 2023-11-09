#maya t, week 10, create a file

def main():
    #file object variable
    fil_w_names = open("names.txt", "w")
    for name_count in range(5):
        inst_name = input("Enter name:")
        fil_w_names.write(inst_name + "\n")

    fil_w_names.close()

main()
