from django.db import models

# Create your models here.

class Building(models.Model):
    buildingName = models.CharField(max_length=50)
    city = models.CharField(max_length=50 , blank=True , null=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.buildingName
    

class Floor(models.Model):
    building  = models.ForeignKey(Building, on_delete=models.CASCADE)
    floorNumber = models.CharField( max_length=50)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.floorNumber
    

class Room(models.Model):
    OCCUPIED = 'occupied'
    VACANT = 'vacant'
    STATUS_CHOICES = [
        (OCCUPIED, 'Occupied'),
        (VACANT, 'Vacant'),
    ]

    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    roomNumber = models.CharField( max_length=50)
    roomStatus = models.CharField( max_length=10, choices=STATUS_CHOICES)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.roomNumber

class Tenant(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    # optional row 
    name = models.CharField(help_text='Name can be mpesa code or name' , max_length=250 , blank=True)
    # optional row 
    contactInfo = models.CharField( max_length=250, blank=True)
    payment = models.CharField( max_length=150, blank=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.name

class Rental(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    rentalAmount = models.CharField( max_length=50)
    # payment_due_date = models.DateField()
    # payment_status = models.CharField( max_length=50)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.rentalAmount
    
class Comments(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE , blank=True , null=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE , blank=True , null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , blank=True , null=True)
    # tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE , blank=True, null=True)
    comment = models.TextField(help_text='Enter your comment above' , blank=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.comment
    
class Expense(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE , blank=True , null=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE , blank=True , null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , blank=True , null=True)
    expense = models.TextField()
    amount = models.CharField(max_length=150, blank=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

class Expense2(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE , blank=True , null=True)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE , blank=True , null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE , blank=True , null=True)
    expense = models.TextField()
    amount = models.CharField(max_length=150, blank=True)
    createdAt = models.DateTimeField( auto_now_add=True)
    modifiedAt = models.DateTimeField( auto_now=True)

