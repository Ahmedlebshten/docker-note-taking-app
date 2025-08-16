Docker Note-Taking App

A simple Note-Taking Web Application built with Python Flask and MySQL, containerized using Docker, and hosted on AWS EC2 (t2.micro).
The app allows users to create and view notes, with persistent data storage via Bind Mount volumes.

⸻

📌 Technologies Used:  
	•	Python (Flask) – Backend web framework
	•	MySQL – Relational database
	•	Docker – Containerization
	•	Docker Compose – Multi-container orchestration
	•	AWS EC2 t2.micro – Cloud hosting
	•	Bind Mount Volumes – Persistent storage between host and container
    •   Git – Version control system
    •   GitHub – Remote repository hosting

⸻

⚙️ Requirements:
    • Docker (>= 20.x) – to run containers
    • Docker Compose (>= 1.29) – to manage and run multiple containers together
    • Git – to clone the project from GitHub
    • AWS EC2 Instance (Ubuntu 20.04 recommended) – if running the app on Amazon Cloud
    • MySQL client (optional) – to access the database from outside the container

⸻

🚀 How to Install Application:
 1.	Clone the repository:
 ```
git clone https://github.com/YourUsername/docker-note-taking-app.git
cd docker-note-taking-app
```
 2.	create .env file
```
touch .env 
vim .env
````
Content of .env file:
FLASK_ENV=development
DB_HOST=db
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=notes

 3.	Start the containers:
```
docker-compose up -d
```
 4.	Check running containers:
```
docker ps
```
 6.	Access the application:
Open your browser and go to:
http://<your-ec2-public-ip>:5000

⸻

📂 How to Use the Application:
	1.	Add a Note
	•	Enter your note text in the form and click Add.
	•	Your notes will be saved in MySQL via Docker Bind Mounts for persistence.
	2.	View Notes
	•	All saved notes are displayed on the main page.
	3.	Database Access (Optional)
	•	Connect to MySQL from the host:
 ```
docker exec -it <mysql-container-name> mysql -u root -p
 ```
   • Use the database:
mysql> USE notes_db;
mysql> SELECT * FROM notes;

⸻

📦 Bind Mount Volumes:
This project uses Bind Mounts to persist MySQL data outside the container.
The MySQL container is connected to a host directory, ensuring data is not lost when the container restarts.

Example in docker-compose.yml:
volumes:
  - ./mysql_data:/var/lib/mysql   
⸻

📦 Pull image via DockerHub:
You can pull this image from DockerHub with:

docker pull ahmedlebshten/my-flask-app:v1


  - ./mysql_data:/var/lib/mysql

