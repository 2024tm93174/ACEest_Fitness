# ACEest_Fitness
Devops assignment

Requirements:
Python 3.11+
pip 
Virtual environment 

Repository:
git clone https://github.com/2024tm93174/ACEest_Fitness.git
cd ACEest_Fitness
python3 -m venv venv
source venv/bin/activate    # (Linux/Mac)
venv\Scripts\activate
pip install -r requirements.txt
python app/run.py

pytest
tests/
  ├── conftest.py
  ├── models.py
  ├── test_auth.py  
  ├── test_models.py
  ├── test_routes.py   
  
docker run --rm aceest_fitness_app pytest

Docker:
OS: Ubuntu 22.04 (inside VirtualBox)
Image Name: aceest_fitness_app
Base: python:3.11-slim
Installs dependencies from requirements.txt
Exposes port 5000
CMD runs python app/run.py
docker build -t aceest_fitness_app .
docker run -d -p 5000:5000 aceest_fitness_app
URL accessible inside VM: http://localhost:5000
URL accessible from Windows host depends on network mode:
NAT + port forwarding: http://127.0.0.1:5000
Bridged Adapter: http://10.0.2.15:5000
http://192.168.18.13:5000/

CI/CD Pipeline Steps:
Pulls the repository code
Installs Python 3.11
Installs all packages from requirements.txt
Executes pytest on the tests/ folder
Build Docker Image – Ensures the Dockerfile is valid and the Flask app can run in a container

