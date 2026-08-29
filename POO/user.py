class User:
    def __init__(self, first_name, last_name, email, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"usuario: {self.first_name} {self.last_name}")
        print(f"edad: {self.age}")
        print(f"correo: {self.email}")
        print(f"pais: {self.country}")

    def greet_user(self):
        return f"hola {self.first_name}, saludos :)"


user = User("juan", "vega", "diegovegaprogra@gmail.com", 26, "Mexico")
user2 = User("pedro", "castillo", "pedro@gmail.com", 30, "Mexico")
user3 = User("ana", "perez", "aana@gmail.com", 24, "venezuela")
user4 = User("sofia", "sanchez", "sofi@gmail.com", 28, "peru")

print(user.describe_user())
print(user.greet_user())
print(user2.describe_user())
print(user2.greet_user())
print(user3.describe_user())
print(user3.greet_user())
print(user4.describe_user())
print(user4.greet_user())
