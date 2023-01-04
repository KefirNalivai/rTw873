from django.shortcuts import render
import psycopg2

from myapp1.test_code import test_code


def index_page(request):
    if (request.GET.get('mybtn')):
        conn = psycopg2.connect(dbname='nikitadb', user='nikita',
                                password='123', host='localhost')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO public."table" SELECT * FROM(SELECT \'{"val1":"name'+str(int(request.GET.get('mytextbox')) + 1)+'"}\'::jsonb) as tmp where not exists (Select row1 from public."table" where row1 = \'{"val1":"name'+str(int(request.GET.get('mytextbox')) + 1)+'"}\') LIMIT 1')
        cursor.close()
        conn.commit()
        conn.close()

        return render(request, 'index.html', {'data': int(request.GET.get('mytextbox')) + 1})
    conn = psycopg2.connect(dbname='nikitadb', user='nikita',
                            password='123', host='localhost')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public."table"')
    abc = []
    for row in cursor:
        abc.append(row[0]['val1'])
    cursor.close()
    conn.close()
    return render(request, 'index.html', {'data': len(abc)})


def out_page(request):
    conn = psycopg2.connect(dbname='nikitadb', user='nikita',
                            password='123', host='localhost')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public."table"')
    abc = []
    for row in cursor:
        abc.append(row[0]['val1'])
    cursor.close()
    conn.close()
    return render(request, 'uotput.html', {'data': abc})

