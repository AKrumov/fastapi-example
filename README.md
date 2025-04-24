# 🧱 FastAPI Barebone Application

A minimal FastAPI example project designed as a clean foundation to build real-world applications on.

---

### ✨ Included in this example

- **Pydantic** – for request validation and response models
- **Uvicorn** – ASGI server for running the FastAPI app
- **Structured application layout** – separates concerns into `services`, `config`, `schemas`, `models`, etc.
- **Simple logger** – reusable, configurable logging setup

### 🚀 Getting Started

#### 1. Clone the repository

```bash
git clone https://github.com/AKrumov/fastapi-example.git
cd fastapi-example
```

#### 2. Clone the repository

```bash
python -m venv venv
source venv/bin/activate
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Copy the environment example file

```bash
cp .env.example .env
```
Open `.env` and adjust the configuration values as needed | change ports, logging levels, etc.

#### 5. Run the application

```bash
python main.py
```