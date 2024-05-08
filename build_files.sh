echo "BUILD START"
 python3.9 -m pip install django
 python3.9 -m pip install python-docx
 python3.9 -m pip install openpyxl
 python3.9 -m pip install psycopg2-binary~=2.9.3
 python3.9 manage.py collectstatic --noinput --clear
 echo "BUILD END"