from patient import Patient
from doctor import Doctor
from appointment import Appointment

class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []
        self.next_patient_id = 1
        self.next_appointment_id = 1

        self._load_sample_doctors()

    def _load_sample_doctors(self):
        self.doctors.append(Doctor("D1", "Sharma", "Cardiology"))
        self.doctors.append(Doctor("D2", "Mehta", "Neurology"))
        self.doctors.append(Doctor("D3", "Verma", "Orthopedics"))

    def register_patient(self, name, age, gender):
        patient = Patient(f"P{self.next_patient_id}", name, age, gender)
        self.patients.append(patient)
        self.next_patient_id += 1
        return patient

    def list_doctors(self):
        return self.doctors

    def book_appointment(self, patient_id, doctor_id, date):
        patient = next((p for p in self.patients if p.patient_id == patient_id), None)
        doctor = next((d for d in self.doctors if d.doctor_id == doctor_id), None)

        if not patient or not doctor:
            return None

        appointment = Appointment(self.next_appointment_id, patient, doctor, date)
        self.appointments.append(appointment)
        self.next_appointment_id += 1
        return appointment

    def list_appointments(self):
        return self.appointments
