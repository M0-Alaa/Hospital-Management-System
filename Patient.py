class Patient:
    def __init__(self, patient_id, name, age, gender, disease, visit_history=0):
        if not patient_id or not name or age <= 0 or not gender or not disease:
            raise ValueError("Invalid patient data.")

        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.visit_history = visit_history

    def update_disease(self, new_disease):
        if not new_disease:
            raise ValueError("Disease cannot be empty.")
        self.disease = new_disease

    def increment_visits(self):
        self.visit_history += 1

    def to_file_string(self):
        return f"{self.patient_id}|{self.name}|{self.age}|{self.gender}|{self.disease}|{self.visit_history}"

    @staticmethod
    def from_file_string(line):
        pid, name, age, gender, disease, visits = line.strip().split("|")
        return Patient(pid, name, int(age), gender, disease, int(visits))

    def __str__(self):
        return f"[{self.patient_id}] {self.name}, {self.age} yrs, {self.gender}, {self.disease}, Visits: {self.visit_history}"