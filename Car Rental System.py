import datetime

class Car:
    def __init__(self, manufacturer, model, rental_cost):
        self.manufacturer = manufacturer
        self.model = model
        self.rental_cost = rental_cost
        self.rental_income = 0.0  # Total income from this car Rental

    def rent_car(self, days):
        rental_amount = self.rental_cost * days
        self.rental_income += rental_amount
        return rental_amount

    def get_rental_income(self):
        return self.rental_income

    def __str__(self):
        return f"{self.manufacturer} {self.model} - ${self.rental_cost}/day"


class Customer:
    def __init__(self, name, contact_info, credit_card):
        self.name = name
        self.contact_info = contact_info
        self.credit_card = credit_card
        self.rental_history = []  # List Rental Records

    def add_rental(self, rental_record):
        self.rental_history.append(rental_record)
    def get_rental_history(self):
        return self.rental_history
    def __str__(self):
        return f"Customer: {self.name}, Contact:{self.contact_info}"


class RentalRecord:
    def __init__(self, car, customer, rental_date, rental_days):
        self.car = car
        self.customer = customer
        self.rental_date = rental_date
        self.rental_days = rental_days
        self.rental_cost = car.rent_car(rental_days)

    def __str__(self):
        return f"Rental Record: {self.customer.name} rented{self.car} for {self.rental_days} days, Total cost:${self.rental_cost}"


class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_car(self, manufacturer, model, rental_cost):
        new_car = Car(manufacturer, model, rental_cost)
        self.cars.append(new_car)
        print(f"Car added: {new_car}")
    def add_customer(self, name, contact_info, credit_card):
        new_customer = Customer(name, contact_info, credit_card)
        self.customers.append(new_customer)
        print(f"Customer added: {new_customer}")

    def rent_car(self, customer_name, car_model, rental_days):
        customer = self.find_customer(customer_name)
        car = self.find_car(car_model)

        if customer and car:
            rental_date = datetime.datetime.now().strftime("%Y-%m-%d")
            rental_record = RentalRecord(car, customer, rental_date, rental_days)
            customer.add_rental(rental_record)
            print(f"Rental successful: {rental_record}")
        else:
            print("Error:Customer or car not found")
        if rental_days <= 0:
            print("Error: Rental days must be greater than zero.")
        return
    def find_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def find_car(self, model):
        for car in self.cars:
            if car.model == model:
                return car
        return None

    def rental_income_per_car(self, car_model):
        car = self.find_car(car_model)
        if car:
            return car.get_rental_income()
        return 0.0
    def rental_history_per_customer(self, customer_name):
        customer = self.find_customer(customer_name)
        if customer:
            return customer.get_rental_history()
        return None
    def __str__(self):
        return f"Car Rental System with {len(self.cars)} cars and{len(self.customers)} customers."
    

#Create rental system
rental_system = CarRentalSystem()

# Add cars
rental_system.add_car("Toyota", "Camry",50)
rental_system.add_car("Ford", "Fiesta", 40)
rental_system.add_car("BMW","3 Series", 80)
# add clients
rental_system.add_customer("Maria Perez", "123-456-7890","1234-5678-9012-3456")
rental_system.add_customer("Luis Martinez","987-654-3210", "6543-2109-8765-4321")

# Rent car
rental_system.rent_car("Maria Perez","Camry", 3)
rental_system.rent_car("Luis Martinez", "Fiesta", 5)
# see retnal history 
customer = rental_system.find_customer("Maria Perez")
if customer:
    print("\nRental History for Maria Perez:")
    for record in customer.get_rental_history():
        print(record)

# Rent for each car
print("\n Rental income for Toyota Camry:$", rental_system.rental_income_per_car("Camry"))
print("\nRental income for Ford Fiesta:  $", rental_system.rental_income_per_car("Fiesta"))
