from django.db import models


class Students(models.Model):
    roll_number = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=80, unique=True)
    branch = models.CharField(max_length=50)
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    co_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return self.co_name

class Interviews(models.Model):
    INTERVIEW_STATUS_CHOICES = [('done', 'Done'), ('schedule', 'Schedule'),]
    FEEDBACK_CHOICES = [('pass', 'Pass'), ('failed', 'Failed'),]
    interview_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    interview_date = models.DateField()
    interview_status = models.CharField(max_length=50, choices=INTERVIEW_STATUS_CHOICES, default='schedule')
    interview_feedback = models.CharField(max_length=50, choices=FEEDBACK_CHOICES)
    def __str__(self):
        return f"{self.student.name} - {self.company.co_name}"

class Placements(models.Model):
    placement_id = models.AutoField(primary_key=True)
    interview = models.ForeignKey(Interviews, on_delete=models.CASCADE)
    placement_date = models.DateField()
    offered_salary = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.interview.student.name} - {self.interview.company.co_name} - {self.offered_salary}"
