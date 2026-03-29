# 🚀 Flask DevOps App (2-Tier Architecture)

This project demonstrates a complete **DevOps workflow** by building, containerizing, and deploying a Flask application using Docker, AWS EC2, and GitHub Actions.

---

## 📌 Overview

A simple **2-tier web application**:
- **Backend**: Flask (Python)
- **Database**: PostgreSQL (Docker container)

This project showcases:
- Docker containerization
- Multi-container setup using Docker Compose
- Cloud deployment on AWS EC2
- CI/CD automation using GitHub Actions

---

## 🏗️ Architecture

User → Flask App (Container) → PostgreSQL DB (Container)

---

## 🛠️ Tech Stack

- Python (Flask)
- Docker
- Docker Compose
- AWS EC2 (Ubuntu)
- GitHub Actions (CI/CD)

---

## 📂 Project Structure

.
├── app.py  
├── Dockerfile  
├── docker-compose.yml  
├── requirements.txt  
└── .github/workflows/deploy.yml  

---

## ⚙️ Running Locally

1. Clone the repository:
```bash
git clone https://github.com/vinukond/flask-devops-app.git
cd flask-devops-app
```

2. Run with Docker Compose:
```bash
docker-compose up --build
```

3. Open in browser:
http://localhost:5000

---

## ☁️ Deployment on AWS EC2

Steps performed:

1. Launch Ubuntu EC2 instance  
2. Install Docker & Docker Compose  
3. Clone repository  
4. Run application:

```bash
docker-compose up -d --build
```

---

## 🔐 SSH Setup

- Connected using `.pem` key  
- Set permissions:
```bash
chmod 400 dev-ops.pem
```

---

## 🔁 CI/CD Pipeline

- Implemented using GitHub Actions  
- Triggered on push to `main` branch  
- Deploys automatically to EC2 via SSH  

---

## ⚠️ Challenges

- Docker Compose compatibility issues (`ContainerConfig` error)  
- SSH key setup for CI/CD  
- Cloud deployment debugging  

---

## ✅ Key Learnings

- End-to-end DevOps pipeline  
- Docker containerization  
- AWS EC2 deployment  
- CI/CD automation  
- Debugging real-world issues  

---

## 🚀 Future Improvements

- Upgrade to Docker Compose v2  
- Add Nginx reverse proxy  
- Enable HTTPS (SSL)  
- Add monitoring (Prometheus, Grafana)  
- Use Kubernetes for scaling  

---

## 👨‍💻 Author

Chandra Sekhar

---

## ⭐ Conclusion

This project demonstrates a complete **DevOps lifecycle**, including development, containerization, deployment, and automation in a real-world environment.