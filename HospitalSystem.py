from Patient import Patient
from Doctors import Doctor
from Appointments import Appointment

class HospitalSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

        self.load_data()

    # ---------- File Handling ----------
    def load_data(self):
        self.load_patients()
        self.load_doctors()
        self.load_appointments()

    def save_data(self):
        self.save_patients()
        self.save_doctors()
        self.save_appointments()

    def load_patients(self):
        try:
            with open("patients.txt", "r") as f:
                for line in f:
                    self.patients.append(Patient.from_file_string(line))
        except FileNotFoundError:
            open("patients.txt", "w").close()

    def save_patients(self):
        with open("patients.txt", "w") as f:
            for p in self.patients:
                f.write(p.to_file_string() + "\n")

    def load_doctors(self):
        try:
            with open("doctors.txt", "r") as f:
                for line in f:
                    self.doctors.append(Doctor.from_file_string(line))
        except FileNotFoundError:
            open("doctors.txt", "w").close()

    def save_doctors(self):
        with open("doctors.txt", "w") as f:
            for d in self.doctors:
                f.write(d.to_file_string() + "\n")

    def load_appointments(self):
        try:
            with open("appointments.txt", "r") as f:
                for line in f:
                    self.appointments.append(Appointment.from_file_string(line))
        except FileNotFoundError:
            open("appointments.txt", "w").close()

    def save_appointments(self):
        with open("appointments.txt", "w") as f:
            for a in self.appointments:
                f.write(a.to_file_string() + "\n")

    def generate_appointment_id(self):
        if not self.appointments:
            return "A1"
        last_num = max(int(a.appointment_id[1:]) for a in self.appointments if a.appointment_id.startswith("A"))
        return f"A{last_num + 1}"

    # ---------- Helpers ----------
    def find_patient(self, patient_id):
        return next((p for p in self.patients if p.patient_id == patient_id), None)

    def find_doctor(self, doctor_id):
        return next((d for d in self.doctors if d.doctor_id == doctor_id), None)

    def has_conflict(self, doctor_id, date):
        return any(a.doctor_id == doctor_id and a.appointment_date == date for a in self.appointments)
    

    def choose_doctor_from_list(self):
        if not self.doctors:
            raise ValueError("No doctors available.")

        print("\nAvailable Doctors:")
        for i, d in enumerate(self.doctors, start=1):
            print(f"{i}. Dr. {d.name} ({d.specialty})")

        try:
            choice = int(input("Choose a doctor number: "))
            if choice < 1 or choice > len(self.doctors):
                raise ValueError("Invalid choice.")
            return self.doctors[choice - 1]
        except ValueError:
            raise ValueError("Please enter a valid number.")
        
    def find_patient_by_name(self, name):
        matches = [p for p in self.patients if p.name.lower() == name.lower()]
        return matches

    def find_doctor_by_name(self, name):
        matches = [d for d in self.doctors if d.name.lower() == name.lower()]
        return matches

    # ---------- Operations ----------
    def add_patient(self):
        try:
            pid = input("Patient ID: ")
            if self.find_patient(pid):
                raise ValueError("Patient ID already exists.")

            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            disease = input("Disease: ")

            self.patients.append(Patient(pid, name, age, gender, disease))
            print("✅ Patient added.")

        except ValueError as e:
            print(f"❌ {e}")

    def add_doctor(self):
        try:
            did = input("Doctor ID: ")
            if self.find_doctor(did):
                raise ValueError("Doctor ID already exists.")

            name = input("Name: ")
            age = int(input("Age: "))
            gender = input("Gender: ")
            specialty = input("Specialty: ")

            self.doctors.append(Doctor(did, name, age, gender, specialty))
            print("✅ Doctor added.")

        except ValueError as e:
            print(f"❌ {e}")

    def create_appointment(self):
        try:
            aid = self.generate_appointment_id()
            print(f"Generated Appointment ID: {aid}")

            patient_name = input("Enter patient name: ").strip()
            patients = self.find_patient_by_name(patient_name)

            if not patients:
                raise ValueError("No patient found with this name.")
            if len(patients) > 1:
                print("Multiple patients found:")
                for i, p in enumerate(patients, start=1):
                    print(f"{i}. [{p.patient_id}] {p.name}")
                idx = int(input("Choose patient number: ")) - 1
                patient = patients[idx]
            else:
                patient = patients[0]

            doctor = self.choose_doctor_from_list()

            date = input("Date (YYYY-MM-DD): ").strip()

            if self.has_conflict(doctor.doctor_id, date):
                raise ValueError("Doctor already booked at this time.")

            self.appointments.append(Appointment(aid, patient.patient_id, doctor.doctor_id, date))
            print("✅ Appointment created successfully.")

        except ValueError as e:
            print(f"❌ {e}")

    # ---------- Menu ----------
    def menu(self):
        while True:
            print("\n--- Hospital System ---")
            print("1. Add Patient")
            print("2. Add Doctor")
            print("3. Create Appointment")
            print("4. View Patients")
            print("5. View Doctors")
            print("6. View Appointments")
            print("7. Exit")

            choice = input("Choose: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.add_doctor()
            elif choice == "3":
                self.create_appointment()
            elif choice == "4":
                for p in self.patients:
                    print(p)
            elif choice == "5":
                for d in self.doctors:
                    print(d)
            elif choice == "6":
                for a in self.appointments:
                    print(a)
            elif choice == "7":
                self.save_data()
                print("💾 Data saved. Bye!")
                break
            else:
                print("❌ Invalid choice.")