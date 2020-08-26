class Person:
    def __init__(self, name, email, phone, friends=[], greet_count=0):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends
        self.greet_count = greet_count

    def __str__(self):
        return f"Their name is \n{self.name}, their email is \n{self.email}, and their number is \n{self.phone}"
    
    def greet(self, other_person):
        
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greet_count += 1
        return self.greet_count
    
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}\n{self.name}'s phone number: {self.phone}")

    def add_friend(self, friend):
        return self.friends.append(friend)
    
    def count_friends(self):
        return len(self.friends)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)

tesla = Vehicle("Tesla", "Cybertruck", "2077")
sonny = Person("Sonny", "sonny@hotmail.com", "438-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")


sonny.print_contact_info()
sonny.greet(jordan)
sonny.greet(jordan)
jordan.greet(sonny)
tesla.print_info()
jordan.add_friend(sonny)
print(jordan.count_friends())
print(jordan.greet_count)
print(sonny.greet_count)



