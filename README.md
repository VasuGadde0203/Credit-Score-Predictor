# Credit Bureau Update System
## Overview
This project is a Django-based web application designed to calculate a user's credit score based on their responses to a series of dynamically generated questions. The application features a dynamic pop-up interface to collect user inputs and a credit scoring algorithm that evaluates responses to generate a credit score.

## Features
- **Dynamic Pop-up Interface**
  - Questions are displayed one at a time in a modal pop-up.
  - User responses are captured and stored in the database dynamically.
- **Credit Scoring Algorithm**
  - Custom algorithm assigns specific scores to responses.
  - Credit score is calculated based on predefined scoring rules.
- **Database Models**
  - Question model stores questions and possible answers (A, B, C, D).
  - UserResponse model tracks users' answers to each question.
- **Web Pages**
  - Form Page: Displays the questions in a dynamic form interface.
  - Results Page: Shows the calculated credit score after submission.
 
## Technologies Used
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, JavaScript (for modal pop-ups)
- **Database:** SQLite (default), can be configured to use other databases

## Installation
- **Clone the repository:**
  - git clone https://github.com/VasuGadde0203/Credit-Score-Predictor.git
  - cd credit-score-predictor
- **create and activate a virtual environment:**
  - python -m venv venv
  - source venv/bin/activate
- **Install Dependencies:**
  - pip install -r requriements.txt
- **Run migrations to set up the database:**
  - python manage.py makemigrations  
  - python manage.py migrate
- **Start the development server:**
  - python manage.py runserver
- Open the application in your browser at http://127.0.0.1:8000.
  
## Usage
- Navigate to the Form Page to start the questionnaire.
- Answer the questions displayed dynamically in the modal pop-up interface.
- Submit the responses to calculate your credit score.
- View your credit score on the Results Page.

## Project Structure
credit-bureau-update-system/  
├── credit_bureau/         # Django project folder  
│   ├── settings.py        # Project settings  
│   ├── urls.py            # URL routing  
│   ├── wsgi.py            # WSGI configuration  
├── app/                   # Django app folder  
│   ├── models.py          # Database models for Question and UserResponse  
│   ├── views.py           # Views for handling forms and results  
│   ├── templates/         # HTML templates  
│   │   ├── form.html      # Form page template  
│   │   ├── results.html   # Results page template  
│   └── static/            # Static files (CSS, JS)  
├── db.sqlite3             # SQLite database  
├── manage.py              # Django management script  
└── requirements.txt       # Project dependencies  

## Future Enhancements
- Add user authentication to track credit scores for multiple users.
- Expand the algorithm to include more detailed scoring factors.
- Implement advanced analytics and visualizations for credit scores.
- Integrate with external APIs for real-time credit data.

## License
- This project is licensed under the MIT License. See the LICENSE file for details.



