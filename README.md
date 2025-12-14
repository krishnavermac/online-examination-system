**ONLINE EXAMINATION MANAGEMENT SYSTEM**

A full-stack Online Examination Management System built using Python (Flask) and SQLAlchemy, designed to conduct secure, timed, and automated online examinations.
The system supports role-based access for Admin and Student, enabling real-world exam workflows for educational institutions.


**KEY FEATURES**

👨‍💼 **Admin Module**

Secure admin authentication

Create and manage exams

Add multiple-choice questions (MCQs)

Configure exam duration and evaluation rules

Monitor student performance


🎓 **Student Module**

Secure student login and registration

View available exams

Attempt exams with a live timer

Auto-submission on time expiry

Instant result and score evaluation


⚙️ **System Features**

Role-based authentication (Admin / Student)

Timed online examinations

Automated evaluation

Database-driven exam management

Clean MVC-based Flask architecture



**TECH STACK**

| Layer           | Technology         |
| --------------- | ------------------ |
| Backend         | Python, Flask      |
| Database        | SQLite, SQLAlchemy |
| Authentication  | Flask-Login        |
| Frontend        | HTML, CSS, Jinja2  |
| Version Control | Git & GitHub       |


**Project Structure**

exam_management_system/

├── online_exam_system/

│   ├── app.py

│   ├── admin.py

│   ├── student.py

│   ├── auth.py

│   ├── models.py

│   ├── create_db.py

│   ├── templates/

│   │   ├── start_exam.html

│   │   ├── analytics.html

│   │   ├── admin_dashboard.html

│   │   └── result.html

│   └── static/css/style.css

├── requirements.txt

├── README.md

└── .gitignore




**APPLICATION WORKFLOW**

1.Admin logs in

2.Admin creates an exam and adds questions

3.Student logs in

4.Student selects and attempts exam

5.System evaluates responses automatically

6.Result is displayed instantly



**SCREENSHOTS**

  ADMIN FLOW
  
-> Admin LogIn Page 
<img width="1919" height="893" alt="AdminLoginPage" src="https://github.com/user-attachments/assets/dc98187c-d4df-45d3-a512-cf9b36725e03" />

->Create Exam Page 
<img width="1919" height="878" alt="CreateExamPage" src="https://github.com/user-attachments/assets/83e16de3-a944-4aed-8e6b-dc227563fc93" />

->Add Questions Page 
<img width="1884" height="879" alt="AddQuestionPage" src="https://github.com/user-attachments/assets/d410aa2a-37cf-408d-9d77-b3e57a2e096f" />

->Analytics Dashboard
<img width="1915" height="865" alt="AnalyticsPage" src="https://github.com/user-attachments/assets/832cdded-04b4-48b4-9669-44f019f80928" />



  STUDENT FLOW
  
->Student Login Page
<img width="1864" height="808" alt="StudentLoginPage" src="https://github.com/user-attachments/assets/978a92c4-b630-4cc8-b287-cf62e10d21c0" />

->Online Exam Interface 
<img width="1892" height="884" alt="OnlineExamInterface" src="https://github.com/user-attachments/assets/bd0b5e46-a261-4428-99f5-141a0b9f82c4" />

<img width="1873" height="874" alt="OnlineExamInterface2" src="https://github.com/user-attachments/assets/435c9dc7-1522-4e70-8510-73b7a477bbdd" />

->Result / Score Page 
<img width="1898" height="877" alt="ResultPage" src="https://github.com/user-attachments/assets/dc4c0864-6619-48fb-a407-555099ad7664" />


**SECURITY CONSIDERATIONS**

->Passwords are securely hashed

->Role-based route access

->Session-based authentication

->Database file excluded from version control


**ANTI-CHEATING FEATURES**

To ensure exam integrity, the system implements multiple client-side and server-side safeguards:

**Client-Side Controls**

1.Tab / window switch detection using Browser Visibility API

2.Auto-submission after multiple violations

3.Right-click disabled

4.Copy / paste / text selection disabled

**Server-Side Validation**

1.Exam start time stored securely in session

2.Submission time validated on backend

3.Prevents manipulation of client-side timers

These mechanisms together simulate real-world online proctoring constraints.


**ANALYTICS DASHBOARD**

The admin panel provides exam-level analytics using SQL aggregation queries:

Exam-Wise Metrics:

1.Total exam attempts

2.Average score

3.Highest score

4.Lowest score

**Benefits**

1.Helps identify exam difficulty

2.Provides performance trends

3.Supports data-driven decision making


**FUTURE ENHANCEMENTS**

->REST API support

->React / frontend framework integration

->Advanced analytics and reports

->Anti-cheating mechanisms

->Cloud deployment (AWS / Render)



**USE CASE**

This system can be used by:

->Colleges and universities

->Training institutes

->Online assessment platforms

->Internal recruitment tests


**AUTHOR**

Krishna Verma

Electronics & Communication Engineering (ECE), IIIT Allahabad

Aspiring Software / IT Engineer
