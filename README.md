# placementPortal

NITT is one of the most prestigious institutest in India having great placement records, but the entire placement process is still managed manually. Henceforth, feeling the requirement of an automated system, we decided to build NITT Placement Portal.<br /><br />

Team Leader - <br />
&emsp; **Bhushan Mendhe (205121033)** <br />
Team Members - <br />
&emsp; **Anup Kumar Mridha (205121025)** <br />
&emsp; **Varun Singh (205121101)** <br />
&emsp; **Aastha Srivastava (205121001)** <br />
&emsp; **Puneet Kumar (205121114)** <br />
&emsp; **Ankur Bohra (205121023)** <br />


## Steps to Run the Project:

1. Clone the project int your local machine.<br />
2. Open the project folder and run the following commands inside the terminal: <br />
    `python -m venv env`<br />
    `env/Scripts/activate`<br />
    `pip install -r requirements.txt`<br />
    `python manage.py makemigrations`<br />
    `python manage.py migrate`<br />
    `python manage.py createsuperuser`<br />
3. This will ask you for the Username, Email, and password for the superuser<br />
&emsp; Username: admin<br />
&emsp; Email: admin@nitt.edu<br />
&emsp; **Note** : The username and email should be same as mentioned but the password can be different.<br />
4. Run command: `python manage.py runserver`<br />
5. This will start the local server where you can see the web app running.<br />
