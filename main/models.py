from django.db import models



class Dars(models.Model):
    title = models.CharField(max_length=30)
    about = models.TextField()
    age1 = models.IntegerField()
    age2 = models.SmallIntegerField()
    age3 = models.BigIntegerField()
    create_at = models.DateTimeField(auto_now_add=True, editable=True)
    update_at = models.DateTimeField(auto_now=True)



class Sold_car(models.Model):
    title = models.CharField(max_length=20)
    year = models.PositiveSmallIntegerField()
    hususiyat = models.CharField(max_length=30)
    km = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField(null=True, blank=True)
    img = models.ImageField(upload_to="media/")

    def __str__(self):
        return self.title


class our_servise(models.Model):
    title = models.CharField(max_length=15)
    about = models.TextField()

    def __str__(self):
        return self.title


class Contact(models.Model):
    Head_Office = models.CharField(max_length=37)
    Branch_Office = models.CharField(max_length=37)
    Customer_Service = models.EmailField()
    Return_Refund = models.CharField(max_length=37)
    def __str__(self):
        return self.Head_Office

class Contact_S(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField()
     subject = models.CharField(max_length=100)
     message = models.TextField()
     def __str__(self):
        return f"{self.name} - {self.subject}"






