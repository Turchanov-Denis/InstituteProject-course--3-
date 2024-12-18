from peewee import *

db = SqliteDatabase('delivery.db')

# Define the "Transport" model
class Transport(Model):
    vehicle_number = CharField(primary_key=True)
    brand = CharField()
    registration_date = DateField()
    color = CharField()

    class Meta:
        database = db

# Define the "Sender" model
class Sender(Model):
    sender_id = AutoField()
    last_name = CharField()
    first_name = CharField()
    middle_name = CharField()
    phone = CharField()

    class Meta:
        database = db

# Define the "Receiver" model
class Receiver(Model):
    receiver_id = AutoField()
    last_name = CharField()
    first_name = CharField()
    middle_name = CharField()
    phone = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Transport, Sender, Receiver])

Transport.create(vehicle_number="A123BC", brand="Toyota", registration_date="2023-05-20", color="White")
Transport.create(vehicle_number="X456YZ", brand="Ford", registration_date="2022-08-15", color="Blue")

Sender.create(last_name="Petrov", first_name="Petr", middle_name="Petrovich", phone="+7-901-222-33-44")
Sender.create(last_name="Sidorov", first_name="Sidor", middle_name="Sidorovich", phone="+7-902-333-44-55")

Receiver.create(last_name="Kuznetsov", first_name="Alexei", middle_name="Alexeevich", phone="+7-903-555-66-77")
Receiver.create(last_name="Vasilyev", first_name="Vasiliy", middle_name="Vasilievich", phone="+7-904-777-88-99")

db.close()
