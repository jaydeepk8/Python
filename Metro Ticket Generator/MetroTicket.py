import random
import datetime
import qrcode
from jinja2 import Template
from PIL import Image, ImageDraw, ImageFont

current_time = datetime.datetime.now()
formatted_time = current_time.strftime(" %H:%M")
current_date = datetime.date.today()
template = Template(open("template.html", encoding="utf-8").read())


number_arriving = random.randint(10000000, 99999999)
number_destination = random.randint(10000000, 99999999)
eqpid = random.randint(1000000, 9999999)


output = "Your code's output here"
print("What type of passenger is ?")
print("1. Student Passenger")
print("2. Local Passenger")

passengerType = int(input("Enter your choice (1 or 2) :"))

stations = {
    1: "ANAND NAGAR",
    2: "SWARGATE",
    3: "DECCAN GYMKHANA",
    4: "RUBY HALL CLINIC"
}

student_fare_table = {
    1: {2: 17.5, 3: 8.5, 4: 17.5},
    2: {1: 17.5, 3: 17.5, 4: 17.5},
    3: {1: 8.5, 2: 17.5, 4: 17.5},
    4: {1: 17.5, 2: 17.5, 3: 17.5}
}
local_fare_table = {
    1: {2: 20.0, 3: 20.0, 4: 20.0},
    2: {1: 20.0, 3: 20.0, 4: 20.0},
    3: {1: 20.0, 2: 20.0, 4: 20.0},
    4: {1: 20.0, 2: 20.0, 3: 20.0}
}

match passengerType:
    case 1:
        print("\n1. Anand Nagar")
        print("2. Swargate")
        print("3. Deccan Gymkhana")
        print("4. Ruby Hall Clinic")
        arriving_number = int(input("Enter Arriving Station: "))

        print("\n1. Anand Nagar")
        print("2. Swargate")
        print("3. Deccan Gymkhana")
        print("4. Ruby Hall Clinic")
        destination_number = int(input("Enter Destination Station: "))

        if arriving_number in stations and destination_number in stations:
            arriving_station = stations[arriving_number]
            destination_station = stations[destination_number]

            if destination_number in student_fare_table[arriving_number]:

                quantity = int(input("Enter the quantity of tickets: "))

                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                else:

                    fare = student_fare_table[arriving_number][destination_number] * quantity

                    arrivingType = arriving_station
                    destinationType = destination_station
                    ticketQuantity = quantity

                    print("Booking Successful")

                arrivingType = arriving_station
                destinationType = destination_station
                ticketQuantity = quantity
                fare = local_fare_table[arriving_number][destination_number] * quantity

                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=5,
                    border=4,
                )

                qr.add_data(f"Ticket Number: {number_arriving} To {number_destination}\n"
                            f"From: {arrivingType}\n"
                            f"To: {destinationType}\n"
                            f"Date: {current_date} {formatted_time}\n"
                            f"Fare: INR {fare}\n"
                            f"Quantity: {ticketQuantity}\n")
                qr.make(fit=True)

                qr_image = qr.make_image(fill_color="black", back_color="white")

                qr_image.save("qrcode.png")

                html_content = template.render(
                    number_arriving=number_arriving,
                    number_destination=number_destination,
                    current_date=current_date,
                    formatted_time=formatted_time,
                    arrivingType=arrivingType,
                    destinationType=destinationType,
                    eqpid=eqpid,
                    fare=fare,
                    ticketQuantity=ticketQuantity
                )
                with open("metro_ticket_with_qrcode.html", "w", encoding="utf-8") as html_file:
                    html_file.write(html_content)
                text = f"""
                                   पुणे मेट्रो     
                                 PUNE METRO    
                --------------------------------------------------
                 Ticket No.:      {number_arriving} To {number_destination}   
                ---------------------------------------------------
                             Single Journey Ticket (P)               
                Date:                       {current_date} {formatted_time}
                From:                       {arrivingType}
                To:                         {destinationType}
                Eqp ID:                     {eqpid}
                Fare:                        INR {fare}
                Quantity:                    {ticketQuantity}
                Valid Upto:                  {current_date}
                Platform No.:                  2
                """

                output_image = Image.new("RGB", (500, 700), color="white")
                draw = ImageDraw.Draw(output_image)

                font = ImageFont.truetype("arial.ttf", 16)

                x, y = 70, 300

                line_height = 20

                output_image.paste(qr_image, (50, 50))

                lines = text.split("\n")

                text_height = len(lines) * line_height

                for line in lines:
                    draw.text((x, y), line, fill="black", font=font)
                    y += line_height

                output_image.save("output_image.png")
    case 2:
        print("\n1. Anand Nagar")
        print("2. Swargate")
        print("3. Deccan Gymkhana")
        print("4. Ruby Hall Clinic")
        arriving_number = int(input("Enter Arriving Station: "))

        print("\n1. Anand Nagar")
        print("2. Swargate")
        print("3. Deccan Gymkhana")
        print("4. Ruby Hall Clinic")
        destination_number = int(input("Enter Destination Station: "))

        if arriving_number in stations and destination_number in stations:
            arriving_station = stations[arriving_number]
            destination_station = stations[destination_number]

            if destination_number in local_fare_table[arriving_number]:

                quantity = int(input("Enter the quantity of tickets: "))

                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                else:

                    fare = local_fare_table[arriving_number][destination_number] * quantity

                    arrivingType = arriving_station
                    destinationType = destination_station
                    ticketQuantity = quantity

                    print("Booking Successful")

                arrivingType = arriving_station
                destinationType = destination_station
                ticketQuantity = quantity
                fare = local_fare_table[arriving_number][destination_number] * quantity
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(f"Ticket Number: {number_arriving} To {number_destination}\n"
                            f"From: {arrivingType}\n"
                            f"To: {destinationType}\n"
                            f"Date: {current_date} {formatted_time}\n"
                            f"Fare: INR {fare}\n"
                            f"Quantity: {ticketQuantity}\n")
                qr.make(fit=True)

                qr_image = qr.make_image(fill_color="black", back_color="white")

                qr_image.save("qrcode.png")

                html_content = template.render(
                    number_arriving=number_arriving,
                    number_destination=number_destination,
                    current_date=current_date,
                    formatted_time=formatted_time,
                    arrivingType=arrivingType,
                    destinationType=destinationType,
                    eqpid=eqpid,
                    fare=fare,
                    ticketQuantity=ticketQuantity
                )
                with open("metro_ticket_with_qrcode.html", "w", encoding="utf-8") as html_file:
                    html_file.write(html_content)
                text = f"""
                                                  पुणे मेट्रो     
                                                PUNE METRO    
                               --------------------------------------------------
                                Ticket No.:      {number_arriving} To {number_destination}   
                               ---------------------------------------------------
                                            Single Journey Ticket (P)               
                               Date:                       {current_date} {formatted_time}
                               From:                       {arrivingType}
                               To:                         {destinationType}
                               Eqp ID:                     {eqpid}
                               Fare:                        INR {fare}
                               Quantity:                    {ticketQuantity}
                               Valid Upto:                  {current_date}
                               Platform No.:                  2
                               """

                output_image = Image.new("RGB", (500, 700), color="white")
                draw = ImageDraw.Draw(output_image)

                font = ImageFont.truetype("arial.ttf", 16)

                x, y = 70, 300

                line_height = 20

                output_image.paste(qr_image, (50, 50))

                lines = text.split("\n")

                text_height = len(lines) * line_height

                for line in lines:
                    draw.text((x, y), line, fill="black", font=font)
                    y += line_height

                output_image.save("output_image.png")
