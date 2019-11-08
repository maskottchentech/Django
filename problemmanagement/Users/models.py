from django.db import models

class information(models.Model):
    s_choice=(
        ('Pending','Pending'),
        ('In progress','In progress'),
        ('Done','Done')
    )
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    room=models.IntegerField()
    floor=models.IntegerField()
    branch=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    status=models.CharField(max_length=30,choices=s_choice)



    def __str__(self):
        return self.name


