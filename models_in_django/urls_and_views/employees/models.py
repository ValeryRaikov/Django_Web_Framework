from django.db import models


class AuditEntity(models.Model):
    created_on = models.DateField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True,


class Department(AuditEntity):
    name = models.CharField(
        max_length=50,
        null=True,
    )
    location = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return f'Department: {self.name}'


class Employee(AuditEntity):
    SOFTUNI = 'SoftUni'
    GOOGLE = 'Google'
    MICROSOFT = 'Microsoft'

    first_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default='',
    )
    last_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        default='',
    )
    egn = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        unique=True,
    )
    # job_title = models.CharField(
    #     max_length=30,
    #     choices=[
    #         ('BackEnd-Dev', 1),
    #         ('FrontEnd-Dev', 2),
    #         ('QA', 3),
    #         ('DevOps', 4),
    #         ('Team Lead', 5),
    #     ],
    # )
    job_title = models.IntegerField(
        choices=[
            (1, 'BackEnd-Dev'),
            (2, 'FrontEnd-Dev'),
            (3, 'QA'),
            (4, 'DevOps'),
            (5, 'Team Lead'),
        ],
        default=1,
    )
    company = models.CharField(
        max_length=max(len(c) for c in [SOFTUNI, GOOGLE, MICROSOFT]),
        choices=[
            (SOFTUNI, SOFTUNI),
            (GOOGLE, GOOGLE),
            (MICROSOFT, MICROSOFT),
        ],
        default=SOFTUNI,
    )

    department_id = models.ForeignKey(
        to=Department,
        on_delete=models.CASCADE,
        default=1,
    )

    class Meta:
        ordering = ['first_name', 'last_name',]


class Project(AuditEntity):
    name = models.CharField(
        max_length=50,
        null=True,
    )
    deadline = models.DateField(
        null=True,
    )
    employees = models.ManyToManyField(
        to=Employee,
    )


class User(AuditEntity):
    email = models.EmailField()
    employee_id = models.OneToOneField(
        to=Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class TestModel(models.Model):  # Let's say it is a vehicle...
    class Engines(models.TextChoices):
        DIESEL = 'Diesel',
        PETROL = 'Petrol',
        ELECTRIC = 'Electric',

    class Categories(models.IntegerChoices):
        A = 1,
        B = 2,
        C = 3,
        D = 4,

    brand = models.CharField(
        max_length=30,
        null=True,
    )
    model = models.CharField(
        max_length=30,
        null=True,
    )
    year = models.DateField()
    engine = models.CharField(
        max_length=10,
        choices=Engines,
    )
    category = models.IntegerField(
        choices=Categories,
    )
    price = models.FloatField()
