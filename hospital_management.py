
# Patient class
class Patient:
    def __init__(self, patient_id, name, age, gender, medical_history):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_history = medical_history

    def get_details(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Medical History: {self.medical_history}"
# Doctor class
class Doctor:
    def __init__(self, doctor_id, name, specialty, availability):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.availability = availability

    def get_details(self):
        return f"Doctor ID: {self.doctor_id}, Name: {self.name}, Specialty: {self.specialty}, Availability: {self.availability}"

# Appointment class
class Appointment:
    def __init__(self, appointment_id, patient, doctor, appointment_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_time = appointment_time

    def get_details(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient.name}, Doctor: {self.doctor.name}, Time: {self.appointment_time}"

# Hospital class
class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment):
        self.appointments.append(appointment)

    def show_patients(self):
        for patient in self.patients:
            print(patient.get_details())

    def show_doctors(self):
        for doctor in self.doctors:
            print(doctor.get_details())

    def show_appointments(self):
        for appointment in self.appointments:
            print(appointment.get_details())
# Main Usage
if __name__ == "__main__":
    hospital = Hospital("City Hospital")

    # Adding patients
    patient1 = Patient(1, "John Doe", 30, "Male", "No prior conditions")
    patient2 = Patient(2, "Jane Smith", 25, "Female", "Asthma")
    hospital.add_patient(patient1)
    hospital.add_patient(patient2)

    # Adding doctors
    doctor1 = Doctor(101, "Dr. Emily Brown", "Cardiologist", "9am - 5pm")
    doctor2 = Doctor(102, "Dr. James Wilson", "Dermatologist", "10am - 6pm")
    hospital.add_doctor(doctor1)
    hospital.add_doctor(doctor2)

    # Scheduling appointments
    appointment1 = Appointment(1, patient1, doctor1, "10:30 AM")
    appointment2 = Appointment(2, patient2, doctor2, "11:00 AM")
    hospital.schedule_appointment(appointment1)
    hospital.schedule_appointment(appointment2)

    # Display data
    print("\nPatients in the Hospital:")
    hospital.show_patients()

    print("\nDoctors in the Hospital:")
    hospital.show_doctors()

    print("\nScheduled Appointments:")
    hospital.show_appointments()    