# Sarva Suvidhan Assignment

This project is a Django-based REST API developed as part of an assignment. It allows users to **query and submit ICF Wheel Measurements** and **Bogie Details** based on various parameters.

---

## 🧰 Tech Stack

- **Backend:** Django 5.2.4
- **API Framework:** Django REST Framework 3.16.0
- **Database:** PostgreSQL (via `psycopg2`)
- **Language:** Python 3.12+
- **Environment:** Virtualenv

---

## 🚀 Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sarveshja/sarva_suvidhan_assignment.git
   cd sarva_suvidhan_assignment/backend/sarva_suvidhan_assignment
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

   Access at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📡 API Endpoints

### 🔍 ICF Wheel GET Filters

| Endpoint                                     | Description                               |
|---------------------------------------------|-------------------------------------------|
| `GET /api/icf-wheel/?form_number=W12345`    | Filter by `form_number`                   |
| `GET /api/icf-wheel/?created_by=Sarvesh`    | Filter by `created_by`                    |
| `GET /api/icf-wheel/?search=W123`           | Search across `form_number` and `created_by` |
| `GET /api/icf-wheel/?created_at=2025-07-21` | Filter by `created_at` (`YYYY-MM-DD`)     |
| `GET /api/icf-wheel/?form_number=W12345&created_by=Sarvesh&search=W123&created_at=2025-07-21` | Combination of all filters |

---

### ➕ POST APIs

| Endpoint               | Purpose                  | Description               |
|------------------------|--------------------------|---------------------------|
| `POST /api/icf-wheel/` | Add ICF Wheel data       | Accepts measurement form  |
| `POST /api/icf-bogie/` | Add ICF Bogie data       | Accepts bogie-level form  |

---

## ⚠️ Limitations / Assumptions

- Date format must be strictly `YYYY-MM-DD` for `created_at`.
- The project uses Django's development server and is not production-ready.
- Filtering is handled manually; no third-party filter packages used.
- **Basic URL connectivity is provided to the respective provider, but not to the complete project.**

---

## 🙋‍♂️ Author

**Sarvesh**

---

