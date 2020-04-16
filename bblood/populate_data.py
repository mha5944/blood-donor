# <----For more information check https://https://faker.readthedocs.io ------------>
import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bblood.settings')

import django
django.setup()
from basicapp.models import UserProfile 
from django.contrib.auth.models import User

from faker import Faker

fakergen = Faker()
bloodType = ['A+','A-','B+','B-','O+','O-','AB+','AB-']
Case = ['Reciver','Blood Donor']
def populate(N=5):
    for entery in range(N):
        #making fake data
        fake_first_name = fakergen.first_name()
        fake_last_name = fakergen.last_name()
        fake_email = fakergen.email()
        fake_password = fakergen.password(length=10)
        fake_blood_type = random.choice(bloodType)
        fake_phone = fakergen.phone_number()
        fake_case = random.choice(Case)
        #Create new User entery
        user = User.objects.get_or_create(
            username=fake_first_name, 
            first_name=fake_first_name, 
            last_name=fake_last_name, 
            email=fake_email)[0]
        tempUser = User.objects.get(username=fake_first_name)
        tempUser.set_password(fake_password)
        tempUser.save()
                
        userprofile = UserProfile.objects.get_or_create(
            user=user,
            blood_type=fake_blood_type, 
            phone_number=fake_phone,  
            case=fake_case,
            description='')[0]
        

if __name__ == "__main__":
    print("Populating...")
    populate(20)
    print("Populating Completed!")