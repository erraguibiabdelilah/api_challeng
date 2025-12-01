from django.db import models


class Recruiter(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.company})"


class Candidate(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    recruiter = models.ForeignKey(
        Recruiter, on_delete=models.SET_NULL, null=True, blank=True, related_name="candidates"
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    level = models.CharField(max_length=50, blank=True) 
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return f"{self.name} ({self.level})"

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="experiences")

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)   
    field = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name="educations")

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.school}"
