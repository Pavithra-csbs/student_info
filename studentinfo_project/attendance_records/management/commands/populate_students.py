from attendance_records.models import Student
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
       
        Student.objects.all().delete()

        students = [
    "Aarav", "Bhavya", "Charan", "Dhruv", "Esha", 
    "Farhan", "Gauri", "Harsh", "Ishaan", "Jhanvi", 
    "Karthik", "Lavanya", "Mihir", "Nidhi", "Omkar", 
    "Prisha", "Quasar", "Rohan", "Sneha", "Tanmay"
]

        roll_numbers = [
            "24UAD20101", "24UAD20102", "24UAD20103", "24UAD20104", "24UAD20105",
            "24UAD20106", "24UAD20107", "24UAD20108", "24UAD20109", "24UAD20110",
            "24UAD20111", "24UAD20112", "24UAD20113", "24UAD20114", "24UAD20115",
            "24UAD20116", "24UAD20117", "24UAD20118", "24UAD20119", "24UAD20120"
        ]


        for student,roll_number in zip(students,roll_numbers):

            Student.objects.create(name=student,roll_number=roll_number)