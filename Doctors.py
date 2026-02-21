class Doctor:
    def __init__(self, doctor_id, name, age, gender, specialty, availability=True):
        if not doctor_id or not name or age <= 0 or not gender or not specialty:
            raise ValueError("Invalid doctor data.")

        self.doctor_id = doctor_id
        self.name = name
        self.age = age
        self.gender = gender
        self.specialty = specialty
        self.availability = availability

    def set_availability(self, status: bool):
        self.availability = status

    def to_file_string(self):
        return f"{self.doctor_id}|{self.name}|{self.age}|{self.gender}|{self.specialty}|{self.availability}"

    @staticmethod
    def from_file_string(line):
        did, name, age, gender, specialty, avail = line.strip().split("|")
        return Doctor(did, name, int(age), gender, specialty, avail == "True")

    def __str__(self):
        status = "Available" if self.availability else "Busy"
        return f"[{self.doctor_id}] Dr. {self.name} ({self.specialty}) - {status}"