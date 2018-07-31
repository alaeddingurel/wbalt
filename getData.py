import os
from classify.models import TextFile
from django.contrib.auth.models import User
os.chdir("tobesent")

for file in os.listdir(os.getcwd()):
    fi = open(file, 'r')
    our_text = fi.read()
    print(file)
    a = TextFile(filename=file, text=our_text)
    a.save()
    fi.close()
