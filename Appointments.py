from datetime import datetime

class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, appointment_date):
        if not appointment_id or not patient_id or not doctor_id or not appointment_date:
            raise ValueError("Invalid appointment data.")

        # Validate date format YYYY-MM-DD
        try:
            datetime.strptime(appointment_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date

    def to_file_string(self):
        return f"{self.appointment_id}|{self.patient_id}|{self.doctor_id}|{self.appointment_date}"

    @staticmethod
    def from_file_string(line):
        aid, pid, did, date = line.strip().split("|")
        return Appointment(aid, pid, did, date)

    def __str__(self):
        return f"[{self.appointment_id}] Patient {self.patient_id} with Doctor {self.doctor_id} on {self.appointment_date}"