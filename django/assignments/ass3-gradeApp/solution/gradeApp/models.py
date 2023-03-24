from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.teacher_name}"

class Lesson(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50)

    def __str__(self):
        return self.lesson_name

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.student_number}-{self.first_name} {self.last_name}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.student.student_number}-{self.lesson.lesson_name}-{self.grade}"
    # modelde uniquelik sağlamak için aşağıdaki metodu kullanıyoruz.Bu metotla admin panelde de kısıtlama yapmış oluyoruz. Burada yaptığımız işlem UniqueConstraint metoduna birleştiğinde unique olmasını istediğimiz fieldları veriyoruz o bizim yerimize kontrolü sağlıyor.Örneğimizde lesson ve student eşleşmeleri böylelikle istediğimiz gibi tek olmuş oluyor. Aynı isimde ders birden fazla öğrenci ile eşleşebilir ama aynı öğrenci ile eşleşemez aynı şekilde öğrenci için de öyle.
    # Not: class Meta işlemlerinde makemigrations ve migrate komutlarını çalıştırmamız gerekir   
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['student', 'lesson'], name='unique_student_lesson')
    #     ]