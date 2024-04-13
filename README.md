## User Data for Dependencies installations for AMAZON Linux 2:-

#!/bin/bash

sudo yum -y update

sudo yum -y install ruby

sudo yum -y install wget

cd /home/ec2-user

wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install

sudo chmod +x ./install

sudo ./install auto

sudo yum install -y python-pip

sudo pip install awscli



# Student Exam Performance Predictor

## Overview
The Student Exam Performance Predictor is a machine learning application designed to forecast students' exam scores based on demographic and educational factors. This project encapsulates the entire lifecycle of a machine-learning application, from initial data processing to model training and finally, deployment as a web application using Flask.

## Features
- Data preprocessing and analysis scripts.
- A predictive model developed with robust machine-learning techniques.
- Custom exception handling to ensure reliability and ease of debugging.
- Detailed logging to track the application's operation and performance.
- A user-friendly web interface allowing for straightforward input and clear display of prediction results.
- Full deployment on a web server, showcasing a practical application of the predictive model.

## Installation

### Prerequisites
- Python 3.8 or above
- pip for installing dependencies

### Setup
1. Clone the repository:
2. git clone https://github.com/shivakumar0002/ML-project.git
cd ML-project
2. Create a virtual environment:
python -m venv venv
3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  source venv/bin/activate
  ```
4. Install the required dependencies:


 pip install -r requirements.txt 

 
## Usage
To run the web application locally:


## Usage
To run the web application locally:


Navigate to `http://127.0.0.1:5000/` in your web browser to access the application.

## How It Works
The application uses a machine-learning model trained on a dataset including various features such as gender, race, parental level of education, and lunch type. Users input their details and academic scores, and the model predicts their performance in exams.

## Contributing
We welcome contributions to this project. Please fork the repository, make your changes, and submit a pull request for review.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- [Dataset Source] ( u can see in artifacts )
- Mentors: KRISH NAIK

## Contact
For any queries or discussions regarding the project, please reach out to me at godipally.shivakumar01@yahoo.com

Thank you for your interest in our Student Exam Performance Predictor!


