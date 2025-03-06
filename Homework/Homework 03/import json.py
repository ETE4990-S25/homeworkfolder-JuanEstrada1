import json

class Person(object):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def to_dict(self):
        # Convert Person instance to dictionary for JSON serialization
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email
        }

class Student(Person):
    def __init__(self, name, age, email, student_id):
        super().__init__(name, age, email)
        self.student_id = student_id

    def to_dict(self):
        # Convert Student to dictionary for JSON
        person_dict = super().to_dict()
        person_dict['student_id'] = self.student_id
        return person_dict

    def save_to_json(self, filename):
        """Save instance data to a JSON file"""
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving to JSON: {str(e)}")

    def display_json(self):
        """Display JSON content of the instance"""
        try:
            json_str = json.dumps(self.to_dict(), indent=4)
            print("JSON Content:")
            print(json_str)
        except Exception as e:
            print(f"Error displaying JSON: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Create a student instance
    student = Student(
        name="John Doe",
        age=20,
        email="john.doe@example.com",
        student_id="STU12345"
    )

    # Display JSON content
    student.display_json()

    # Save to JSON file
    student.save_to_json("student_data.json")