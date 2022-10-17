# placementPortal

NITT is one of the most prestigious institutest in India having great placement records, but the entire placement process is still managed manually. Henceforth, feeling the requirement of an automated system, we decided to build NITT Placement Portal.

Team Leader - 
  Bhushan Mendhe (205121033)
Team Members - 
  Anup Kumar Mridha (205121025)
  Varun Singh (205121101)
  Aastha Srivastava (205121001)
  Puneet Kumar (205121114)
  Ankur Bohra (205121023)


## Steps to Run the Project:

1. Clone the project int your local machine.
2. Open the project folder and run the following commands inside the terminal:
    `python -m venv env`
    `env/Scripts/activate`
    `pip install -r requirements.txt`
    `python manage.py makemigrations`
    `python manage.py migrate`
    `python manage.py createsuperuser`
3. This will ask you for the Username, Email, and password for the superuser
    Username: admin
    Email: admin@nitt.edu
    Note: The username and password should be same as mentioned but the password can be different.
4. Run command: `python manage.py runserver`
5. This will start the local server where you can see the web app running.
