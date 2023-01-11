from django.db import models
from twilio.rest import Client
import random

drugs = []


class illness(models.Model):
    name = models.CharField(max_length=255),
    illness_name = models.CharField(max_length=255)


class Drugs(models.Model):
    image = models.ImageField(upload_to="media", blank=True, null=True)
    name = models.CharField(max_length=255)
    cost = models.CharField(max_length=200)
    pharmacy = models.CharField(max_length=255)
    address = models.TextField()
    number = models.CharField(max_length=255)
    ii_name = models.CharField(max_length=255)
    illness = models.ForeignKey(illness, on_delete=models.CASCADE, blank=True, null=True)
    drugs = drugs.append(name)

    def __str__(self):
        return self.name


class BePartner(models.Model):
    pharm_name = models.CharField(verbose_name="Название вашей аптеки", max_length=255)
    pharm_email = models.CharField(verbose_name="Почта вашей аптеки", max_length=255)
    pharm_phone = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/', blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Recomendations(models.Model):
    username = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_phone = models.CharField(max_length=255)
    recommendations = models.TextField()


class Pharmacies(models.Model):
    pharmacy = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return str(self.address)


class Apteks(models.Model):
    pharm_name = models.CharField(max_length=255)
    pharm_city = models.CharField(max_length=255)
    pharm_working_schedule = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    pharm_telephone = models.CharField(max_length=255)

    def __str__(self):
        return str(self.pharm_name)


class Delivery(models.Model):
    person_name = models.CharField(max_length=255, verbose_name="Your name")
    person_email = models.CharField(max_length=255, verbose_name="Enter your email:")
    person_tel = models.CharField(max_length=255, verbose_name="Enter your telephone number")
    person_city = models.CharField(max_length=255, verbose_name="Enter your city")
    person_Address = models.CharField(max_length=255, verbose_name="Enter your home address")
    person_wish = models.TextField(verbose_name="Пожелания для доставки")
    drug_name = models.CharField(max_length=255, verbose_name="Needed chemicals")

    def __str__(self):
        return str(self.drug_name)

    def save(self, *args, **kwargs):
        if str(self.drug_name) in drugs or len(str(self.drug_name)) > 7:
            pharmacy = ['Гиппократ №1', 'Гиппократ №2', 'Гиппократ №3', 'Гиппократ №4', 'EuroPharma №122',
                        'Цветная ТЦ "Керуен"']
            account_sid = 'AC9151648d57cb5818c7480363a1691432'
            auth_token = '9771de2027bdf3a0333a417e2582b2f3'
            client = Client(account_sid, auth_token)
            message = client.api.account.messages.create(
                to=str(self.person_tel),
                from_="+15636666317",
                body=f"{self.person_name}, ваш заказ {self.drug_name} будет доставлен с аптеки {random.choice(pharmacy)}"
                     f" в течении 2 часов!")
            print(message.sid)
        else:
            account_sid = 'AC9151648d57cb5818c7480363a1691432'
            auth_token = '9771de2027bdf3a0333a417e2582b2f3'
            client = Client(account_sid, auth_token)
            message = client.api.account.messages.create(
                to=str(self.person_tel),
                from_="+15636666317",
                body=f"{self.person_name}, вашего заказа {self.drug_name} нет в наличии")
            print(message.sid)

        return super().save(*args, **kwargs)
