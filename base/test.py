from faker import Faker

fake = Faker('ru_RU')
fname = fake.first_name()
lname = fake.last_name()
phone = fake.numerify(text='79#########')
lcard = fake.credit_card_number()
email = fake.email()
passw = fake.password(8)
user = (fname, lname, phone, lcard, email, passw)
print(user)