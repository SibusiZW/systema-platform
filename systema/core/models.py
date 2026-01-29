from django.db import models

class Machine(models.Model):
    CONDITIONS = [
        ('Missing', 'MISSING'),
        ('Good', 'GOOD'),
        ('Broken', 'BROKEN')
    ]

    name = models.CharField(max_length=50, unique=True)
    condition = models.CharField(choices=CONDITIONS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name

class Student(models.Model):
    CLASSES = [
        ('form 1', 'FORM2'),
        ('form 2', 'FORM2'),
        ('form 3', 'FORM3'),
        ('form 4', 'FORM4'),
        ('Lower 6', 'L6'),
        ('Upper 6', 'U6'),
    ]

    name = models.CharField(max_length=50)
    student_class = models.CharField(choices=CLASSES)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): return self.name

class Allocation(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f'{self.machine} - {self.student}'