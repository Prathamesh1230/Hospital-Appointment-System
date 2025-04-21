class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.patient_id} - {self.name}, Age: {self.age}, Gender: {self.gender}"
