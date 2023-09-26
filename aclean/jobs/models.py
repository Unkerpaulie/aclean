from django.db import models
from clients.models import Client

# Create your models here.
class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    est_job_time = models.CharField(max_length=20)
    start = models.DateField()
    end = models.DateField()
    completed = models.BooleanField(default=False)


class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.TextField()
    area = models.CharField(max_length=50)
    # assigned_to = models.ManyToManyField(Worker, null=True, blank=True)
    task_pay = models.FloatField(null=True, blank=True)


class SiteVisit(models.Model):
    visit_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    visit_date = models.DateField()
    note = models.TextField()


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    cost = models.FloatField()


class LineItem(models.Model):
    # for invoices and estimates
    line_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    description = models.CharField(max_length=150)
    price = models.FloatField()
    on_invoice = models.BooleanField(default=True)


class JobNote(models.Model):
    note_id = models.AutoField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    subject = models.CharField(max_length=150)
    note = models.TextField()
