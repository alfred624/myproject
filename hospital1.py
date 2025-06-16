class Patient:
    def __init__(self, patient_id, name, age, gender, disease, contact_number):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.contact_number = contact_number

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Disease: {self.disease}")
        print(f"Contact Number: {self.contact_number}")
        print("-" * 30)


class Doctor:
    def __init__(self, doctor_id, name, specialization, contact_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact_number = contact_number

    def display_info(self):
        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Contact Number: {self.contact_number}")
        print("-" * 30)


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def display_info(self):
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient: {self.patient.name} (ID: {self.patient.patient_id})")
        print(f"Doctor: {self.doctor.name} (Specialization: {self.doctor.specialization})")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print("-" * 30)


class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = input("Enter Patient Age: ")
        gender = input("Enter Patient Gender: ")
        disease = input("Enter Patient Disease: ")
        contact_number = input("Enter Patient Contact Number: ")
        
        patient = Patient(patient_id, name, age, gender, disease, contact_number)
        self.patients.append(patient)
        print("Patient added successfully!")

    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        contact_number = input("Enter Doctor Contact Number: ")
        
        doctor = Doctor(doctor_id, name, specialization, contact_number)
        self.doctors.append(doctor)
        print("Doctor added successfully!")

    def schedule_appointment(self):
        patient_id = input("Enter Patient ID to schedule an appointment: ")
        patient = None
        for p in self.patients:
            if p.patient_id == patient_id:
                patient = p
                break
        if not patient:
            print("Patient not found!")
            return
        
        doctor_id = input("Enter Doctor ID for appointment: ")
        doctor = None
        for d in self.doctors:
            if d.doctor_id == doctor_id:
                doctor = d
                break
        if not doctor:
            print("Doctor not found!")
            return
        
        date = input("Enter Appointment Date (YYYY-MM-DD): ")
        time = input("Enter Appointment Time (HH:MM): ")
        
        appointment_id = len(self.appointments) + 1  
        appointment = Appointment(appointment_id, patient, doctor, date, time)
        self.appointments.append(appointment)
        print("Appointment scheduled successfully!")

    def display_patients(self):
        if not self.patients:
            print("No patients registered!")
        for patient in self.patients:
            patient.display_info()

    def display_doctors(self):
        if not self.doctors:
            print("No doctors available!")
        for doctor in self.doctors:
            doctor.display_info()

    def display_appointments(self):
        if not self.appointments:
            print("No appointments scheduled!")
        for appointment in self.appointments:
            appointment.display_info()

# Main function
def main():
    hms = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Add Doctor")
        print("3. Schedule Appointment")
        print("4. View Patients")
        print("5. View Doctors")
        print("6. View Appointments")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hms.add_patient()
        elif choice == '2':
            hms.add_doctor()
        elif choice == '3':
            hms.schedule_appointment()
        elif choice == '4':
            hms.display_patients()
        elif choice == '5':
            hms.display_doctors()
        elif choice == '6':
            hms.display_appointments()
        elif choice == '7':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
