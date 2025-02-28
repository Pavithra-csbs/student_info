from attendance_records.models import Student
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
       
        Student.objects.all().delete()

        students = [
            "Subiksha", "Naresh","Srishanth","Sakthi"
        ]

        roll_numbers = [
            "24UAD247", "24UAD203","24UAD245","24UAD238"
        ]


        for student,roll_number in zip(students,roll_numbers):
           
            
            Student.objects.create(name=student,roll_number=roll_number)