import csv

def write_into_csv(info_list):
    with open("student_info.csv", "a", newline = "") as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "Email-Id"])
            
        writer.writerow(info_list)

if __name__ == "__main__" :
    condition = True
    student_num = 1

    while condition:
        student_info = input(f"Enter student information for student #{student_num} in the following format (Name Age Contact_Number Email-Id) : ").split(" ")
        
        print(f"\nThe Enterd Information is : \nName : {student_info[0]} \nAge : {student_info[1]} \nContact Number : {student_info[2]} \nEmail-Id : {student_info[3]}\n")
        
        check_info = input("Is the info correct (yes/no) : ")

        if check_info == "yes":
            write_into_csv(student_info)

            condition_check = input("Enter (yes/no) if you want to enter another information : ")
            if condition_check == "yes":
                condition = True 
                student_num += 1
            elif condition_check == "no":
                condition = False

        elif check_info == "no":
            print(f"Please enter the correct information!\n" )