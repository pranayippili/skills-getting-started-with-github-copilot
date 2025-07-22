# Getting Started with GitHub Copilot

<img src="https://octodex.github.com/images/Professortocat_v2.png" align="right" height="200px" />

Hey pranayippili!

Mona here. I'm done preparing your exercise. Hope you enjoy! 💚

## Project Overview

This is a simple FastAPI web application for Mergington High School. Students can view and sign up for extracurricular activities.  
The backend is built with FastAPI and serves both API endpoints and static frontend files.

## Setup Instructions

1. **Install dependencies**  
   ```sh
   pip3 install -r requirements.txt
   ```

2. **Run the application**  
   ```sh
   python3 -m uvicorn src.app:app --reload
   ```

3. **Access the site**  
   - Open [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html) in your browser.

## API Endpoints

- `GET /activities`  
  Returns all available activities and their details.

- `POST /activities/{activity_name}/signup?email={email}`  
  Signs up a student (by email) for the specified activity.

## Running Tests

Unit tests are provided in `src/test_app.py`.  
Run them with:
```sh
pytest src/test_app.py
```

## File Structure

- `src/app.py` - FastAPI backend
- `src/static/` - Frontend files (HTML, CSS, JS)
- `src/test_app.py` - Unit tests

---

&copy; 2025 GitHub &bull; [Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/code_of_conduct.md) &bull; [MIT License](https://gh.io/mit)

