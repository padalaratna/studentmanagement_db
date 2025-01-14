### How to setup and run

1. Unzip folder
2. cd into folder
3. python -m venv venv
4. .\venv\Scripts\activate (./venv/bin/activate on MacOS)
5. pip install -r requirements.txt
6. python database.py (setup database table Students)
7. python studentmanagement.py (run application)

### How to test

1. python -m unittest discover -s tests -p 'test\_\*.py'
# studentmanagement_db