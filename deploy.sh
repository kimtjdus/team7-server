#!/bin/sh     
# sudo git pull origin master
# sudo pip3 install -r requirements.txt

echo "hello!"

cd $(dirname "$0")
echo "현재경로"
pwd //현재경로

echo "chmod deploy.sh"
chmod +x ./deploy.sh


echo "activate venv..."
source team7elog/bin/activate

echo "install package..."
pip install -r "requirements.txt"

echo "collect static..."
python manage.py collectstatic

echo "make migrations..."
python3 manage.py makemigrations

echo "apply migration..."
python3 manage.py migrate

echo "move location to project..."
cd velog

echo "gunicorn..."
nohup gunicorn velog.wsgi:application -b 0.0.0.0:8080

# sudo systemctl restart nginx
# sudo systemctl restart gunicorn

