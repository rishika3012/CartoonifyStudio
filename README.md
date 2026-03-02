# Oil Painting Transformation App

A Streamlit multipage application with user authentication and protected dashboard flow. This project is structured for future image transformation features using OpenCV and Pillow.

## Features Implemented (Tasks 1-3)

- Structured project layout with `assets`, `backend`, `pages`, and `utils`
- Streamlit multipage navigation (`Home`, `Register`, `Login`, `Dashboard`, `Image_Transform`)
- SQLite-backed user storage (`users.db`)
- Registration backend with:
  - duplicate email handling
  - email validation
  - password strength validation
  - secure password hashing using PBKDF2 (SHA-256 + salt)
- Login backend with credential verification
- Session management with Streamlit `session_state`
- Route protection for dashboard and image transform pages
- Logout flow that clears session and redirects to login

## Project Structure

```text
OilPaintingApp/
|-- app.py
|-- requirements.txt
|-- README.md
|-- users.db
|-- assets/
|   `-- style.css
|-- backend/
|   |-- auth.py
|   |-- db.py
|   `-- image_processing.py
|-- pages/
|   |-- Home.py
|   |-- Register.py
|   |-- Login.py
|   |-- Dashboard.py
|   `-- Image_Transform.py
`-- utils/
    |-- config.py
    `-- helpers.py
```

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Database

- SQLite database file: `users.db`
- Users table is auto-created on app startup.

## Next Steps

- Implement image upload and OpenCV oil-paint transformation pipeline
- Add profile management and password reset
- Add tests for backend auth and database functions

## GitHub Initialization Commands

Run these locally to create the initial commit and push:

```bash
git init
git add .
git commit -m "Initial project setup with auth, dashboard, and session management"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```
