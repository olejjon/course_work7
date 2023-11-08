pip install --upgrade pip
apt update
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
deactivate

#docker-compose up -d --build