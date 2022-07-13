from django.db import models
from django.contrib.auth.models import User

LOCATION = (
    ('laboratory', '研究室'),
    ('procurement', '購買'),
    ('cafeteria', '食堂'),
    ('other_on_campus', 'その他学内'),
    ('returning_home', '帰宅'),
    ('off_campus', 'その他学外')
)


class student_location(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(
        max_length=20,
        choices=LOCATION
    )

    def __str__(self):
        student = str(self.student)
        return student
