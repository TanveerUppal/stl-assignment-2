# Both tasks have been completed as per the instructions. I used input statements, lists, dictionaries and functions to create this program.
# Final code after implementing changes
'''The menu lets the user select an option depending on their use case.
   Functions behavior:
    1. book_appointment (User enters patient name, chooses a practitioner and enters appointment time. It shows error if wrong datatype is entered.)
    2. display_appointments (Database is not implemented, so it displays the appointments booked in the current session. It shows error if no appointments are booked.)
    3. search_by_patient (User can search for a patient name and see all the appointments booked for that patient in the current session)
    4. display_practitioners (Display practioners available in the clinic along with their assumed specialties)
'''

# Used to check if the user has entered a valid date/time for the appointment
from datetime import datetime

TIME_FORMAT = "%Y-%m-%d %I:%M %p"   # e.g. 2024-07-20 10:00 AM

appointments = []

# Name of practitioners working in the clinic and their assumed specialties. It can easily be changed, updated or added to in the future if needed.
practitioners = ["Dr. John Doe", "Dr. Jane Roe", "Dr. Sam Lee"]
practitioner_specialties = {
    "Dr. John Doe": "General Practice",
    "Dr. Jane Roe": "Pediatrics",
    "Dr. Sam Lee": "Dermatology",
}

# This fuction checks user input and books the appointment if all inputs are valid.
def book_appointment(patient_name, practitioner_name, appointment_time):
    patient_name = patient_name.strip()
    practitioner_name = practitioner_name.strip()
    appointment_time = appointment_time.strip()

    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # Check the time really is a date/time in the expected format (this is implemented using the datetime module)
    try:
        parsed_time = datetime.strptime(appointment_time, TIME_FORMAT)
    except ValueError:
        raise ValueError("Invalid time. Use the format YYYY-MM-DD HH:MM AM/PM "
                         "(example: 2024-07-20 10:00 AM)")
    appointment_time = parsed_time.strftime(TIME_FORMAT)   # standard format

    # If the practitioner already has an appointment at that time, then status is set to "Duplicate", otherwise it is "Confirmed".
    status = "Confirmed"
    for existing in appointments:
        if (existing["practitioner"] == practitioner_name
                and existing["time"] == appointment_time):
            status = "Duplicate"

    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time,
        "status": status
    }
    appointments.append(appointment)
    return status

# this function display all the appointments booked in the current session. It shows error if no appointments are booked.
def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return

    for number, appointment in enumerate(appointments, start=1):
        print(f"{number}. Patient: {appointment['patient']} | "
              f"Practitioner: {appointment['practitioner']} | "
              f"Time: {appointment['time']} | "
              f"Status: {appointment['status']}")

# All the practitioners available in the clinic are displayed along with their assumed specialties.
def display_practitioners():
    print("\nAvailable practitioners:")
    for number, name in enumerate(practitioners, start=1):
        print(f"{number}. {name} ({practitioner_specialties[name]})")

# This fuction takes the user input as asked in the task 1 to implement input statements. 
def get_appointment_from_user():
    patient = input("Enter patient name: ").strip()
    if not patient:                                  # check straight away
        print("Error: Patient name cannot be empty")
        return

    display_practitioners()
    choice = input("Choose a practitioner number: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(practitioners)):
        print("Error: Invalid practitioner number.")
        return
    practitioner = practitioners[int(choice) - 1]

    time = input("Enter appointment time (YYYY-MM-DD HH:MM AM/PM): ")

    try:
        status = book_appointment(patient, practitioner, time)
        print(f"Appointment booked. Status: {status}")
    except ValueError as error:
        print("Error:", error)

# this function allows the user to search for a patient name and see all the appointments booked for that patient in the current session
def search_by_patient():
    name = input("Enter patient name to search: ").strip().lower()
    found = [a for a in appointments if a["patient"].lower() == name]

    if not found:
        print("No appointments found for that patient.")
        return

    for appointment in found:
        print(f"Patient: {appointment['patient']} | "
              f"Practitioner: {appointment['practitioner']} | "
              f"Time: {appointment['time']} | "
              f"Status: {appointment['status']}")


# ---------- Main program ----------
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

print("\n----- MENU -----")
print("1. Book an appointment")
print("2. View all appointments")
print("3. Search appointments by patient")
print("4. View practitioners")
choice = input("Choose an option (1-4): ").strip()

if choice == "1":
    get_appointment_from_user()
    display_appointments()      # shows the list so you can see your new booking
elif choice == "2":
    display_appointments()
elif choice == "3":
    search_by_patient()
elif choice == "4":
    display_practitioners()
else:
    print("Invalid choice, please try again.")