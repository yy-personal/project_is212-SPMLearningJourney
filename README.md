## IS2121 Project by Team 4

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

### Main Homepage 
<code>main_home.html</code>
<br>
<br>
<img width="350" alt="Screenshot 2022-11-07 at 3 45 34 PM" src="https://user-images.githubusercontent.com/85498185/200253901-67e828c1-bb7c-474b-86da-53615186220d.png">
<br>
This is the starting point regardless of their role. Users should see 3 boxes representing 3 roles: Staff, Human Resource and Manager.

Selecting their role would bring them to their individual homepage where they can access other functions of LJMS (etc. staff homepage, human resource homepage and manager homepage).

To select and proceed, the user will have to choose one of the boxes by clicking on either the text “Staff”, “Human Resource”, “Manager” or by clicking one of the “More ->” buttons that are highlighted in blue.

### Human Resource (HR)
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

#### <ins>Steps for HR to Create Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 04 28 PM" src="https://user-images.githubusercontent.com/85498185/200306005-bb3cf14b-ff97-429e-bf47-181d75aaf45f.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Human Resource box. <br>
3. Click on the 'Create role' button <br>
4. Enter role name and role description <br>
5. Click 'Submit'. A new role will be created. <br>

#### <ins>Steps for HR to Read Roles</ins>
<img width="350" alt="Screenshot 2022-11-07 at 8 08 55 PM" src="https://user-images.githubusercontent.com/85498185/200306837-f79259ff-1a1b-40d6-8018-334dae16bf04.png">
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Human Resource box. It will bring HR to (<code>hr_roles.html</code>)<br>

#### <ins>Steps for HR to Update Roles</ins>
1. From <code>main_home.html</code> , click on “More ->” button or the text  “Human Resource” in the Human Resource box. <br>
2. From the  HR homepage (<code>hr_ljmsHome.html</code>), click on the “More ->” button or the text  “Job Roles” in the Human Resource box. It will bring HR to (<code>hr_roles.html</code>) <br>
3. Click on the 'Update' button <br>
4. Make necessary changes to role name and role description <br>
5. Click 'Submit'. The job role will be updated. <br>
