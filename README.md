# Django URL Shortener API

A simple and minimal URL shortening service built with Django and Django REST Framework. This API allows users to submit a long URL and receive a short code that redirects back to the original URL.

---

## 📦 Features

- ✅ Shorten long URLs with a simple API call
- ✅ Automatic unique short code generation
- ✅ Redirect to original URL using short code
- ✅ JSON API with Django REST Framework
- ✅ Clean and extendable Django project structure

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- Django 3.2+
- Django REST Framework

### ⚙️ Installation

Step 1. **Clone the repository**

```
git clone https://github.com/kihuni/URL-Shortener-API.git
cd django-url-shortener
```

Step 2. **Create a virtual environment and activate it**

```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

```
Step 3. **Install dependencies**

```
pip install -r requirements.txt

```
Step 4. Run migrations


python manage.py migrate

Step 5. Start the development server

```
python manage.py runserver

```

## Usage

1. Shorten a URL
POST /api/shorten/

Request Body:
```
{
  "original_url": "https://www.google.com"
}

```
Responce:

```
{
    "id": 3,
    "original_url": "https://www.google.com",
    "short_code": "gfHliY",
    "created_at": "2025-06-25T17:16:09.756416Z"
}
```
![Screenshot from 2025-06-25 20-54-09](https://github.com/user-attachments/assets/e84cc4fb-d7b2-4d46-96e7-e6cc514f13ce)

2. Redirect to the long URL
   
GET /<short_code>/

Example:
```
curl -I http://localhost:8000/gfHliY/
```

Returns 302 Found and redirects to the original URL.

Running Tests
```
python manage.py test

```
