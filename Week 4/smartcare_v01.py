''' The final file after all improvements. '''
appointments = []
 
 
def book_appointment(patient_name, practitioner_name, appointment_time):
    # patient name can't be empty
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
 
    # check if this practitioner already has an appointment at this time
    # this is the improvement I added to stop duplicate bookings
    for appointment in appointments:
        if appointment["practitioner"] == practitioner_name and appointment["time"] == appointment_time:
            raise ValueError(f"{practitioner_name} is already booked at {appointment_time}")
 
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
    print(f"Booked: {patient_name} with {practitioner_name} at {appointment_time}")
 
 
def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")
 
 
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
 
# book a couple of normal appointments
book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")
 
print("\nAll appointments so far:")
display_appointments()
 
# try to book Charlie into the same slot as Alice - this should fail now
print("\nTrying to double-book Dr. John Doe's 10:00 AM slot...")
try:
    book_appointment("Charlie Day", "Dr. John Doe", "2024-07-20 10:00 AM")
except ValueError as e:
    print(f"Booking failed: {e}")
 
# book Dana at a different time with the same doctor, should work fine
print("\nBooking Dana at a different time with the same doctor...")
book_appointment("Dana White", "Dr. John Doe", "2024-07-20 12:00 PM")
 
print("\nFinal list of appointments:")
display_appointments()