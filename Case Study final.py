import datetime

print("\nDestination")
print("1. American Region\n2. Asian Region\n3. African Region\n4. European Region\n")
while True:
    destination_code = int(input("Input Destination Code: "))
    if destination_code in range (1,5):
        if destination_code == 1:
            print("\nTime Code")
            print("A. Day\nB. Night")
            time_code = (input("Input Time Code: "))
            if time_code.upper() == "A":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 50
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 40
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")
            elif time_code.upper() == "B":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ") 
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 45
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 38
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        if destination_code == 2:
            print("\nTime Code")
            print("A. Day\nB. Night")
            time_code = (input("Input Time Code: "))
            if time_code.upper() == "A":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 30
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 25
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")
            elif time_code.upper() == "B":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 27
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 15
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")        
        if destination_code == 3:
            print("\nTime Code")
            print("A. Day\nB. Night")
            time_code = (input("Input Time Code: "))
            if time_code.upper() == "A":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 40
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 35
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")
            elif time_code.upper() == "B":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 36
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 3) * 22
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")
            else:
                print("Invalid Input")
        if destination_code == 4:
            print("\nTime Code")
            print("A. Day\nB. Night")
            time_code = (input("Input Time Code: "))
            if time_code.upper() == "A":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 35
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 20
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                else:
                    print("Invalid Input")          
            elif time_code.upper() == "B":
                print("\nDay Code")
                print("X. Weekdays\nY. Weekends")
                day_code = input("Input Day Code: ")
                if day_code.upper() == "X":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 30
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
                elif day_code.upper() == "Y":
                    time = int(input("Input time duration in minutes: "))
                    time_format = str(datetime.timedelta(minutes = time))
                    call_charge = (time / 2) * 19
                    print("Time in preferred format :-",time_format)  
                    print("Total Charges: ", call_charge)
            else:
                print("Invalid Input")
        break       
    else:
        print("Invalid Input")
    break
