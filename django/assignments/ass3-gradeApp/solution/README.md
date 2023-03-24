# GradeApp

```
# KURULUM KOMUTLARI
   1 py -m venv env
   2 .\env\Scripts\activate
   3 pip install djangorestframework
   5 django-admin startproject main .
   6 pip install python-decouple
   7 py manage.py migrate
   8 py manage.py createsuperuser
   9 py manage.py startapp gradeApp
```
## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://git-scm.com)

```Python

# Clone this repository
$ git clone https://github.com/your-user-name/your-project-name

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    > source env/Scripts/activate(for bash)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install -r requirements.txt

# Edit .backend.env to .env

# Add SECRET_KEY in .env file
# migrate
    $ python manage.py migrate
# Run the app
    $ python manage.py runserver
```


```Python

# Her öğrencinin ilgili derse ait bir notu olacak.Bu şart için yapabileceklerimiz

# models.py in gradeApp
# modelde uniquelik sağlamak için aşağıdaki metodu kullanıyoruz.Bu metotla admin panelde de kısıtlama yapmış oluyoruz. 
# method için döküman linki => https://docs.djangoproject.com/en/4.1/ref/models/constraints/#django.db.models.UniqueConstraint.fields
# Burada yaptığımız işlem UniqueConstraint metoduna birleştiğinde unique olmasını istediğimiz fieldları veriyoruz o bizim yerimize kontrolü sağlıyor.
# Örneğimizde lesson ve student eşleşmeleri böylelikle istediğimiz gibi tek olmuş oluyor. 
# Aynı isimde ders birden fazla öğrenci ile eşleşebilir ama aynı öğrenci ile eşleşemez aynı şekilde öğrenci için de öyle.
# Not: class Meta işlemlerinde(yani ekleme veya çıkarma yaparsak) makemigrations ve migrate komutlarını çalıştırmamız gerekir  
    class Grade(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
        grade = models.PositiveSmallIntegerField()

        def __str__(self):
            return f"{self.student.student_number}-{self.lesson.lesson_name}-{self.grade}" 
        class Meta:
            constraints = [
                models.UniqueConstraint(fields=['student', 'lesson'], name='unique_student_lesson')
            ]


# serializers.py in gradeApp
# dökümana bakabilirsiniz=> https://www.django-rest-framework.org/api-guide/validators/#uniquetogethervalidator
class GradeSerializer(serializers.ModelSerializer):
    lesson = serializers.StringRelatedField()
    lesson_id = serializers.IntegerField()
    student = serializers.StringRelatedField()
    student_id = serializers.IntegerField()

    class Meta:
        model = Grade
        fields = ("id","grade","lesson","student","student_id","lesson_id")
        # serializer da uniquelik sağlamak için aşağıdaki metodu kullanıyoruz.Bu metotla admin panelde kısıtlama yapmış olmuyoruz. 
        # Burada yaptığımız işlem UniqueTogetherValidatorü import edip içine birleştiğinde unique olmasını istediğimiz fieldları veriyoruz 
        # ve kontrol etmesini istediğimiz queryseti veriyoruz o bizim yerimize kontrolü sağlıyor.Örneğimizde lesson ve student eşleşmeleri böylelikle istediğimiz gibi tek olmuş oluyor. 
        # Aynı isimde ders birden fazla öğrenci ile eşleşebilir ama aynı öğrenci ile eşleşemez aynı şekilde öğrenci için de öyle.
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Grade.objects.all(),
        #         fields=['lesson_id', 'student_id']#create işleminde kullanılan fieldları yazıyoruz.
        # Biz dersin adı ve öğrencinin adı modelde(str metodunda) belirttiğimiz gibi gelsin istediğimiz için ek fieldler koyduk.
        # O yüzden burada id bilgilerinin olduğu fieldları tanımladık.Çünkü databse de id ile tutuluyor veri.
        #     )
        # ]


# views.py in gradeApp
# ModelViewSet kullandık. O nedenle aşağıdaki işlemleri gerçekleştirdik. 
# Eğer farklı bir viewset yada fbv kullanırsanız ona göre işlemi uyarlayabilirsiniz
class GradeMVS(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # viewste uniquelik sağlamak için
        lesson=request.data["lesson_id"]#gelen datadan lesson_id bilgisini çekip değişkene atadık
        student=request.data["student_id"]#gelen datadan student_id bilgisini çekip değişkene atadık
        grade_qs=Grade.objects.filter(lesson=lesson,student=student)# Grade modelimizde iki şartı da sağlayan veriyi çektik.
        # Yani aslında daha önce databaseimize aynı lesson ve student bilgisiyle veri girilmiş mi onu kontrol ediyoruz
        if grade_qs.exists():# grade_qs verisi varsa kullanıcıya hata mesajı dönüyoruz
            message="Same lesson and student have a grade."
            return Response(message,status=status.HTTP_400_BAD_REQUEST)  
        else: #  grade_qs verisi yoksa gelen veriyi kaydediyoruz
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    def perform_create(self, serializer):
        serializer.save()
    # Inherit aldığımız ModelViewSet e gittik oradan onun Inherit aldığı CreateApiViewe gittik create metodunu aldık burada override yapıp ilgili şartlarımızı koymuş olduk.

# Hem admin panel de hem de api üzerinden atılan isteklerde uniquelik sağlamak istiyorsanız model de yapılan işlem yeterli olacaktır.
# Sadece api üzerinden gelen isteklerde uniquelik sağlamak istiyorsanız serializerdaki veya viewsdeki işlem yeterli olacaktır.    
# Not: Her zaman daha iyisi vardır.
```
