from hospital import HospitalSystem

hospital = HospitalSystem()

while True:
    print("\n--- Hospital Appointment System ---")
    print("1. Register Patient")
    print("2. View Doctors")
    print("3. Book Appointment")
    print("4. View Appointments")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        gender = input("Enter gender: ")
        patient = hospital.register_patient(name, age, gender)
        print("Registered:", patient)

    elif choice == '2':
        print("\nAvailable Doctors:")
        for doc in hospital.list_doctors():
            print(doc)

    elif choice == '3':
        pid = input("Enter patient ID: ")
        did = input("Enter doctor ID: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        appt = hospital.book_appointment(pid, did, date)
        if appt:
            print("Appointment booked:", appt)
        else:
            print("Invalid patient or doctor ID.")

    elif choice == '4':
        print("\nAll Appointments:")
        for appt in hospital.list_appointments():
            print(appt)

    elif choice == '5':
        break

    else:
        print("Invalid choice. Try again.")
