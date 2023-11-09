#maya t, week 10, create a file

def main():
    #file object variable
    fil_w_names = open("names.txt", "w")
    fil_w_names.write("maya" + "\n")
    fil_w_names.write("pam" + "\n")
    fil_w_names.write("amy" + "\n")
    for count in range(6):
        i_name = input("Enter name: ")
        fil_w_names.write("i_name" + "\n")
    #fil_w_names.close()

main()
