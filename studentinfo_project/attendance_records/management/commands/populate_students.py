from attendance_records.models import Student
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
       
        Student.objects.all().delete()

        students = [
            "Subiksha", "Naresh"
]

        roll_numbers = [
            "24UAD20101", "24UAD20102"
        ]


        for student,roll_number in zip(students,roll_numbers):

            Student.objects.create(name=student,roll_number=roll_number)