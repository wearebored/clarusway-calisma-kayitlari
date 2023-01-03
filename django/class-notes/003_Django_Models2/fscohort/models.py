from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number = models.PositiveSmallIntegerField(blank=True, null=True)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(blank=True, null=True, upload_to='student')
    # files = models.FileField(blank=True, null=True, upload_to='student_files')
    register_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.number} - {self.first_name} {self.last_name}'

    class Meta:
        ordering = ('-number',)
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        # db_table = ''  tablo ismini değiştir

# https://docs.djangoproject.com/en/4.1/topics/db/queries/
# s1 = Student(first_name='aaaa',last_name='a', number=4)
# s1.save()
# s1.first_name=bbbb
# s1.save()
# s2 = Student.objects.create(first_name='cccc', last_name='c', number=5)
# student = Student.objects.all()
# print(student.query)
# for s in student: print(s)
# s1 = Student.objects.get(number=2)
# s1.number=1
# s1.save()
# s1 = Student.objects.get(number=1) errorrr
# s1 = Student.objects.filter(number=1)
# s1 = Student.objects.exclude(number=1)
# s1 = Student.objects.get(first_name__exact='Henry')
# s1 = Student.objects.get(first_name__exact='Henry')
# s1 = Student.objects.get(first_name__iexact='henry')
# s1 = Student.objects.get(last_name__contains='v')
# s1 = Student.objects.get(last_name__startswith='v')
# s1 = Student.objects.filter(number__gt=1)
