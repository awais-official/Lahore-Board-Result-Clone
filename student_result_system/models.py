from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    cnic = models.CharField(max_length=20, default='N/A')
    father_name = models.CharField(max_length=50)
    father_cnic = models.CharField(max_length=20,default='N/A')
    date_of_birth = models.DateField()
    institution_district = models.CharField(max_length=50)
    group = models.CharField(max_length=20,default='None')

class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=50)
    th1 = models.IntegerField(null=True, blank=True)
    th2 = models.IntegerField(null=True, blank=True)
    practical = models.IntegerField()
    total = models.IntegerField()
    percentage = models.FloatField()
    grade = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    total_1 = models.IntegerField(null=True, blank=True)
    total_2 = models.IntegerField(null=True, blank=True)
    total_1_2 = models.IntegerField(null=True, blank=True)




class StudentResult(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_marks = models.IntegerField()
    overall_grade = models.CharField(max_length=10)
    overall_percentage = models.FloatField()

    def save(self, *args, **kwargs):
        subjects = self.student.subject_set.all()
        total_marks = sum(subject.total for subject in subjects)
        self.total_marks = total_marks

        if total_marks >= 90:
            self.overall_grade = 'A+'
        elif total_marks >= 80:
            self.overall_grade = 'A'
        elif total_marks >= 70:
            self.overall_grade = 'B'
        elif total_marks >= 60:
            self.overall_grade = 'C'
        else:
            self.overall_grade = 'F'

        self.overall_percentage = (total_marks / (len(subjects) * 100)) * 100

        super().save(*args, **kwargs)