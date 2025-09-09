from faker import Faker 

fake = Faker()

name = fake.city()

print(name)