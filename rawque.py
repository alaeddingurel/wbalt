from classify.models import TextFile

for p in TextFile.objects.raw('SELECT * from classify_TextFile'):
    print(p)