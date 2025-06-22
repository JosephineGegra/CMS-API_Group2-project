# 🎭 SL Concert Association API

A RESTful API for managing plays, directors, actors, showtimes, tickets, customers, and users within a concert management system. Built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT authentication**.

---

## 📚 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [Authentication & Authorization](#authentication--authorization)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## 🚀 Features

- 🎭 CRUD operations for **Plays**, **Actors**, **Directors**, **Tickets**, **Showtimes**, and **Customers**
- 🔐 User **authentication and authorization** using **JWT tokens**
- 👥 **Role-based access control** (Admin & User roles)
- ⚙️ Secure API with **HTTPBearer token validation**
- 📃 Auto-generated interactive documentation with Swagger UI
- 📦 Modular codebase for scalability

---Techonology Used
Python 3.11+: Programming language.



FastAPI: Web framework for building APIs.



SQLAlchemy: ORM for database interactions.



PostgreSQL: Relational database.



Pydantic: Data validation and serialization.



Psycopg2: PostgreSQL adapter for Python.



JWT (PyJWT): Authentication using JSON Web Tokens.



Uvicorn: ASGI server for running the FastAPI application.



## 💻 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/sl-concert-api.git
cd sl-concert-api

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
