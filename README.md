# TrackSense-A-Real-Time-Surveillance-System
Part of Minor Project for 6th SEM - B. Tech. (C.S.E.) KIIT

A Real-Time Surveillance System using Computer Vision for People Counting, Demographic Tracking, and Behavior Analysis.

**Description:**
<br>
People Counting and Real-Time Tracking is a system designed to provide accurate people counting and demographic analysis in real-time. Using advanced technologies like OpenCV and TensorFlow, the system tracks individuals' movements in public and retail spaces, offering valuable insights into customer behavior, age estimation, and gender classification. It enhances operational efficiency, retail layout optimization, and customer satisfaction through improved data management and security measures.

**Basic Functionalities:**
<br>
The project functions by capturing live video feed from webcam using OpenCV. It then employs cvlib to detect faces within the video frames. Once a face is detected, the system proceeds to perform age and gender classification. Each detected face is assigned a unique identifier using UUID, and embeddings are generated for the facial region.
<br><br>
Instead of storing facial embeddings and associated data in a database like PostgreSQL, cosine similarity is applied to compare the newly detected face with previously identified faces.
<br><br>
If a similar face is found or if the face is recognized, the system updates the existing entry with the current timestamp and section information, indicating the area of the showroom where the individual is located. However, if the face is not found in any existing entries, the system generates a new unique identifier for the face.
<br><br>
It stores all the entries into a CSV file, which is used to generate a line graph representing the individual's activity over time, depicting the sections visited during their showroom journey and a bar graph to analyze the average time spent by different age groups in different sections such as male, female, cashier.

**Vision and Scope:**
<br>
The project aims to automate people counting and tracking processes, replacing manual methods with an advanced, real-time solution. By integrating security and behavioral analysis, it serves retail enterprises and public spaces by providing customer demographics, optimizing store layouts, and refining marketing strategies. The system uses dynamic tracking plots and analytics for enhanced data visualization and decision-making.

**Technologies Used:**
1. Development Tech: OpenCV, TensorFlow, Keras, Python
2. Databases: PostgreSQL
3. Server: Apache
4. Architecture: Modular, scalable design with facial recognition for real-time tracking

**Dataset Link:** https://drive.google.com/drive/folders/1-VWUDu6I8IXzpSQJjMCnJhI8vgGenkp1?usp=sharing
<br>
**Trained Model Link:** https://drive.google.com/drive/folders/16L_krFKYNkK0i3pZ0vP9mxImQJXmV8wR?usp=sharing
<br>

## HOW TO EXECUTE:

### Running Instructions:
Python Version: 3.11 is required.
<br>

#### Setup Virtual Environment
python -m venv .venv
source .venv/bin/activate

#### Install Dependencies (for Linux/Mac)
pip install -r requirements.txt

#### Install Dependencies (for Windows)
pip install -r requirements.windows.txt

#### Download our Pre-Trained Model
python download_model.

#### Setting up Environment Variable for Linux
cp .env.example .env

#### Setting up Environment Variable for Windows
copy .env.example .env

<br>

### Aiven Account:
You need to create a aiven account to use PostgreSQL service.

<br>

### Setting up Environment Variable
**Setting up environment variable for Linux**
cp .env.example .env
**Setting up environment variable for Windows**
copy .env.example .env

* Copy the Service URI from your Aiven Dashboard.
* Set POSTGRES_URI = "Service URI" in .env file
