from django.db import models

position_choices = {
    ('0', 'Boss'),
    ('1', 'Faculty'),
    ('2', 'IT'),
}

class user(models.Model):
    employee_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    work_position = models. CharField(max_length=16, choices=position_choices, default='0')
    user_password = models.CharField(max_length = 64)
    
    def __str__(self):
        return self.last_name

    
class student(models.Model):
    sap_id = models.IntegerField(default=0)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email_address = models.CharField(max_length = 64)
    group_number = models.IntegerField(default=1)
    territory = models.CharField(max_length=64)
    country = models.CharField(max_length=16)
    employee_id = models.IntegerField(default=0)
    training_program = models.CharField(max_length=128)
    
    def __str__(self):
        return self.last_name
    
class event(models.Model):
    event_id = models.IntegerField(default=0)
    event_name = models.CharField(max_length=256)
    event_date = models.DateField(auto_now=False)
    time_start = models.DateTimeField(auto_now=False)
    time_end = models.DateTimeField(auto_now=False)
    hex_id = models.IntegerField(default=0)
    event_comment = models.CharField(max_length = 256)
    employee_id = models.IntegerField(default=0)
    
    def __str__(self):
        return self.event_name
    
class grade(models.Model):
    sap_id = models.IntegerField(default=0)
    event_id = models.IntegerField(default=0)
    attendance = models.BooleanField()
    grade = models.IntegerField(default=0)
    
    def __str__(self):
        return self.sap_id
    
class activitie(models.Model):
    activity_id = models.IntegerField(default = 0)
    activity_name = models.CharField(max_length=64)
    employee_id = models.IntegerField(default = 0)
    group_number = models.IntegerField(default = 1)
    week_number = models.IntegerField(default =1)
    
    def __str__(self):
        return self.activity_name
    
class note(models.Model):
    title = models.CharField(max_length = 32)
    content = models.CharField(max_length = 256)
    note_date = models.DateField(auto_now = False)
    
    def __str__(self):
        return self.title
    
    