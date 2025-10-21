Clean and professional README.md you can use for your Selenium + Python + Pytest + HTML Report + Git + Jenkins automation project 👇

# 🧪 Selenium + Python + Pytest Automation Framework

This project is a **web test automation framework** built with:

- 🐍 **Python 3**
- 🌐 **Selenium WebDriver**
- 🧭 **Pytest**
- 🧾 **Pytest-HTML Reports**
- 🌿 **Git** for version control
- 🏗️ **Jenkins** for CI/CD pipeline

---



## 📂 Project Structure



selenium-pytest-project/
│
├── tests/
│ └── test_google.py # Sample test case
├── pages/
│ └── google_page.py # Page Object file
├── conftest.py # Pytest fixtures
├── requirements.txt # Project dependencies
├── Jenkinsfile # Jenkins CI pipeline
└── README.md # Project documentation


---


## 🚀 Prerequisites

- ✅ Python 3.8+
- ✅ Google Chrome (or any browser of choice)
- ✅ ChromeDriver (match browser version)
- ✅ Git
- ✅ Jenkins (for CI/CD)

Install basic dependencies on **Linux**:



```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y

📦 Setup & Installation

Clone the Repository

git clone https://github.com/<your-username>/selenium-pytest-project.git
cd selenium-pytest-project


Create Virtual Environment

python3 -m venv venv
source venv/bin/activate


Install Dependencies

pip install -r requirements.txt


Verify ChromeDriver

google-chrome --version
chromedriver --version

🧪 Running Tests

Run tests with Pytest:

pytest


Run tests with HTML Report:

pytest --html=report.html --self-contained-html


A file named report.html will be generated in the project root.

🧭 Project Design Pattern

This framework follows the Page Object Model (POM) to:

Separate test logic from UI interactions.

Improve test maintainability.

Enable code reusability.

🏗️ CI/CD with Jenkins

Install Jenkins on Linux

sudo apt install openjdk-17-jdk -y
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update
sudo apt install jenkins -y
sudo systemctl enable jenkins
sudo systemctl start jenkins


Configure Jenkins Job

Create a new Pipeline job.

Link the GitHub repo.

Use Jenkinsfile for the pipeline definition.

Install HTML Publisher Plugin (Jenkins UI → Manage Plugins)

Pipeline Stages:

Clone repo

Create virtual environment

Install dependencies

Run Pytest in headless mode

Generate & publish HTML report

📜 Jenkinsfile Example
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-username>/selenium-pytest-project.git'
            }
        }

        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                source venv/bin/activate
                pytest --html=report.html --self-contained-html
                '''
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML (target: [
                    reportDir: '.',
                    reportFiles: 'report.html',
                    reportName: 'Selenium Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: false
                ])
            }
        }
    }
}

🌿 Git Workflow
# Initialize repo
git init

# Add files
git add .

# Commit changes
git commit -m "Initial Selenium Pytest setup"

# Push to GitHub
git branch -M main
git remote add origin https://github.com/<your-username>/selenium-pytest-project.git
git push -u origin main
