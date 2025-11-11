# CV Website Generator

This project is a web application built with Python and Flask that allows users to generate a personal CV (Curriculum Vitae) website through a simple, step-by-step form.

## Features

-   **Multi-Step Form:** Guides the user through entering personal details, work experience, education, and skills in a structured way.
-   **Session-Based Data Storage:** Uses Flask's session management to keep user data persistent between steps.
-   **Add/Delete Entries:** Dynamically add or remove multiple entries for work experience, education, and skills.
-   **Review Page:** A summary page that allows the user to review all entered information before generating the final CV.
-   **Multiple Themes:** Generates the final CV in different visual themes (e.g., Modern Light, Modern Dark, Simple).
-   **Start Over:** A simple way to clear all data and start from scratch.

## How It Works

The application is a single Flask web server that manages the entire CV creation process:

1.  **Data Entry:** The user fills out a series of forms, and the data is saved into the server-side session.
2.  **Review:** The user can review all the information they have entered on a single page.
3.  **Generation:** The application takes the session data and renders it into a final HTML template, which serves as the user's personal CV website.

## Technologies & Libraries

-   **Backend:** Python, Flask
-   **Frontend:** HTML, Bootstrap (for styling the forms and layout)

## Project Structure

```
Website-4-CV-website-/
│
├── app.py                      # The main Flask application logic
├── requirements.txt            # Python dependencies
├── templates/                  # HTML files for the application
│   ├── layout.html             # Base template for all pages
│   ├── personal_details.html   # Step 1: Form for personal info
│   ├── work_experience.html    # Step 2: Form for work history
│   ├── education.html          # Step 3: Form for education
│   ├── skills.html             # Step 4: Form for skills
│   ├── review.html             # Step 5: Review all entered data
│   ├── resume_modern.html      # Template for the 'modern' themes
│   └── resume_simple.html      # Template for the 'simple' theme
├── static/
│   └── css/                    # CSS files for the resume themes
└── README.md                   # This file
```

## Getting Started

### Prerequisites

-   Python 3.x

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Anaswar-ash/Website-4-CV-website-.git
    cd Website-4-CV-website-
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1.  **Run the Flask application:**
    ```bash
    flask run
    ```
    You should see output indicating that the server is running on `http://127.0.0.1:5000`.

2.  **Open the application in your browser:**
    Navigate to `http://127.0.0.1:5000` to start building your CV.