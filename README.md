## IS212 Project by Team 4

![example workflow](https://img.shields.io/badge/Build%20In-Python%2CHTML%2CCSS%2CVue.JS-brightgreen)
![example workflow](https://img.shields.io/badge/Build%20With-Flask%2C%20SQLAlchemy-blue)
![example workflow](https://img.shields.io/badge/Database-SQL-red)

#### Group Members:
- Lim Yin Yao 
- Tian Fu Wei
- Gerald Ng Xian Wei
- Lim Bei Ling Cheryl
- Maaruni Pandithurai
- Yi Mon Mon Aung

#### Dependencies:
- Flask 
- Flask SQLAlchemy
- Flask CORS
- WAMP (Windows) / Mamp (Mac)

#### Steps to set up:
<ins>Windows</ins>
- Username: rooe
- Password is empty

<ins>Mac</ins>
- Username: root
- Password: root
 
1. Turn on WAMP/MAMP <br>
2. Load ljms.sql file into phpMyAdmin <br>
3. Run app2.py under flask folder with commands <code>python app2.py</code> <br>

## Main Homepage 
<code>main_home.html</code>
<br>
<br>
<img width="350" alt="Screenshot 2022-11-07 at 3 45 34 PM" src="https://user-images.githubusercontent.com/85498185/200253901-67e828c1-bb7c-474b-86da-53615186220d.png">
<br>
This is the starting point regardless of their role. Users should see 3 boxes representing 3 roles: Staff, Human Resource and Manager.

Selecting their role would bring them to their individual homepage where they can access other functions of LJMS (etc. staff homepage, human resource homepage and manager homepage).

To select and proceed, the user will have to choose one of the boxes by clicking on either the text “Staff”, “Human Resource”, “Manager” or by clicking one of the “More ->” buttons that are highlighted in blue.

## Switch between roles (HR, Manager, Staff) 
#### <ins>Steps to switch between roles</ins>
1. At the nav bar, click "profile" icon <br>
2. Click "Sign out". It will lead to <code>main_home.html</code> <br>

## Human Resource (HR)
### Asign Skills to Roles & Assign Skills to Courses
#### <ins>Steps for HR to Assign Skills to Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 4 21 26 PM" src="https://user-images.githubusercontent.com/85498185/200260615-2b2f08b7-de64-4364-8de0-893a5f463606.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Human Resource box. <br>
3. From the Roles Page (<code>hr_roles.html</code>), click on the “Assign Skills” button under the Job Role you     would like to assign a skill to. <br>
4. From the Individual Role Page (<code>individual_role.html</code>), you will be able to see all available skills on the left that can be assigned to the Job Role. Tick the checkboxes for your desired skills under the “Available Skills” section on the left. <br>
5. Click on the “Confirm Selection” button. Skills have now be successfully assigned to that job role. <br>

#### <ins>Steps for HR to Assign Skills to Courses</ins>
<img width="350" alt="Screenshot 2022-11-07 at 7 58 26 PM" src="https://user-images.githubusercontent.com/85498185/200304907-95a3f9f4-ebe6-41f3-b48a-ef3c90f12b37.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Courses” in the Human Resource box. <br>
3. From the Courses Page (<code>hr_courses.html</code>), click on the “Assign Skills” button under the Course you would like to assign a skill to. <br>
4. From the Individual Course Page (<code>individual_course.html</code>), you will be able to see all available skills on the left that can be assigned to the Course. Tick the checkboxes for your desired skills under the “Available Skills” section on the left. <br>
5. Click on the “Confirm Selection” button. Skills have now be successfully assigned to that course. <br>

### CRUD Roles
#### <ins>Steps for HR to Create Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 04 28 PM" src="https://user-images.githubusercontent.com/85498185/200306005-bb3cf14b-ff97-429e-bf47-181d75aaf45f.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Job Roles box. <br>
3. Click on the 'Create role' button <br>
4. Enter role name and role description <br>
5. Click 'Submit'. A new role will be created. <br>

#### <ins>Steps for HR to Read Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 08 55 PM" src="https://user-images.githubusercontent.com/85498185/200306837-f79259ff-1a1b-40d6-8018-334dae16bf04.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Job Roles box. It will bring HR to (<code>hr_roles.html</code>)<br>

#### <ins>Steps for HR to Update Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 17 20 PM" src="https://user-images.githubusercontent.com/85498185/200308372-5a518b84-7d7e-4219-9023-295e1e747702.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Job Roles box. It will bring HR to (<code>hr_roles.html</code>) <br>
3. Click on the 'Update' button <br>
4. Make necessary changes to role name and role description <br>
5. Click 'Submit'. The job role will be updated. <br>

#### <ins>Steps for HR to Delete Roles</ins>
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Job Roles box. It will bring HR to (<code>hr_roles.html</code>) <br>
3. Click on the 'Delete' button. The job role will be deleted. <br>

### CRUD Skills
#### <ins>Steps for HR to Create Skills</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 25 18 PM" src="https://user-images.githubusercontent.com/85498185/200309819-a9d3e85f-0d88-40ef-b87c-582c19cbe74a.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text  “skills” in the Skills box. It will bring HR to (<code>staff_skills.html</code>) <br>
3. Click on the 'Create skill' button <br>
4. Enter skill name and skill description <br>
5. Click 'Submit'. A new skill will be created. <br>

#### <ins>Steps for HR to Read Skills</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 25 40 PM" src="https://user-images.githubusercontent.com/85498185/200309907-0b1a4955-4824-4766-bf72-187c133f1c09.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text  “skills” in the Skills box. It will bring HR to (<code>staff_skills.html</code>) <br>

#### <ins>Steps for HR to Update Skills</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 26 27 PM" src="https://user-images.githubusercontent.com/85498185/200310044-28a837d4-5200-462b-a080-91abd329ceb9.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text  “skills” in the Skills box. It will bring HR to (<code>staff_skills.html</code>) <br>
3. Click on the 'Update' button <br>
4. Make necessary changes to skill name and skill description <br>
5. Click 'Submit'. The skill will be updated. <br>

#### <ins>Steps for HR to Delete Skills</ins>
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text  “skills” in the Skills box. It will bring HR to (<code>staff_skills.html</code>) <br>
3. Click on the 'Delete' button. The skill will be deleted. <br>

## Staff
### Staff to View Courses, Roles, Skills, Learning Journey
#### <ins>Steps for Staff to View Job Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 37 01 PM" src="https://user-images.githubusercontent.com/85498185/200312136-53a54f38-c29b-405c-8531-1a6257aa7498.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text “Job Roles” in the Job Roles box. It will bring HR to (<code>staff_roles.html</code>) <br>

#### <ins>Steps for Staff to View Skills</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 38 24 PM" src="https://user-images.githubusercontent.com/85498185/200312412-f4477113-9c66-4804-8930-efa024e4dd05.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text “Skills” in the Skills box. It will bring HR to (<code>staff_skills.html</code>) <br>

#### <ins>Steps for Staff to View Courses</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 40 04 PM" src="https://user-images.githubusercontent.com/85498185/200312730-5a0853c8-e48c-4d12-93df-43b4535a289f.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text “Courses” in the Courses box. It will bring HR to (<code>staff_courses.html</code>) <br>

#### <ins>Steps for Staff to View Learning Journey</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 43 57 PM" src="https://user-images.githubusercontent.com/85498185/200313507-babeba2d-48ef-4299-9d70-5db9a7e87561.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text “Learning Journey” in the Learning Journey box. It will bring HR to (<code>staff_learning_journey.html</code>) <br>

### Staff to Create Learning Journey
#### <ins>Steps for Staff to Create Learning Journey</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 47 53 PM" src="https://user-images.githubusercontent.com/85498185/200314212-ca89a317-2cb0-4ae4-92cb-4a3b8158dfc3.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text “Learning Journey” in the Learning Journey box. It will bring HR to (<code>staff_learning_journey.html</code>) <br>
3. Click on "Create Learning Journey" button <br>
4. Select Add Course button <br> 
5. Select on checkbox for the skill you want, then the courses option would appear. <br>
6. Select the checkbox for the course you wish to add to learning journey. <br>
7. Select 'Confirm Selection' button. A new learning journey is created.<br> 

### Staff to Remove Course from Learning Journey
#### <ins>Steps for Staff to Remove Course from Learning Journey</ins> 
<img width="350" alt="Screenshot 2022-11-07 at 8 51 49 PM" src="https://user-images.githubusercontent.com/85498185/200314961-ea460063-7391-42b5-ab9d-69024783b997.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Staff” in the Staff box. <br>
2. From the Staff homepage (<code>staff_ljmshome.html</code>), click on the “More ->” button or the text “Learning Journey” in the Learning Journey box. It will bring HR to (<code>staff_learning_journey.html</code>) <br>
4. Select 'Remove Course' button <br>
5. Check the courses to remove from the list <br>
6. Select 'Confirm Selection' button. Selected Courses will be removed. <br> 
