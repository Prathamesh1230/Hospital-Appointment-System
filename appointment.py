class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def __str__(self):
        return f"Appointment #{self.appointment_id}: {self.patient.name} with Dr. {self.doctor.name} on {self.date}"
