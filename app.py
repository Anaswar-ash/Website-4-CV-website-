import os
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# A secret key is required for using sessions
app.secret_key = os.urandom(24)

# --- ROUTE FOR STEP 1: PERSONAL DETAILS ---
@app.route('/', methods=['GET', 'POST'])
def personal_details():
    if request.method == 'POST':
        # Store form data in session
        session['personal'] = {
            'full_name': request.form['full_name'],
            'email': request.form['email'],
            'phone': request.form['phone'],
            'linkedin': request.form['linkedin'],
            'summary': request.form['summary']
        }
        flash('Personal details saved!', 'success')
        return redirect(url_for('work_experience'))
    
    # On GET request, show the form, pre-filled with session data if it exists
    personal_data = session.get('personal', {})
    return render_template('personal_details.html', data=personal_data)

# --- ROUTE FOR STEP 2: WORK EXPERIENCE ---
@app.route('/experience', methods=['GET', 'POST'])
def work_experience():
    if 'personal' not in session:
        flash('Please fill out your personal details first.', 'warning')
        return redirect(url_for('personal_details'))

    if request.method == 'POST':
        if 'experience' not in session:
            session['experience'] = []
        
        # Add a new work experience entry
        session['experience'].append({
            'job_title': request.form['job_title'],
            'company': request.form['company'],
            'start_date': request.form['start_date'],
            'end_date': request.form['end_date'],
            'description': request.form['description']
        })
        session.modified = True # Mark session as modified
        flash('Work experience added!', 'success')
        # Redirect to the same page to allow adding more entries
        return redirect(url_for('work_experience'))

    experience_data = session.get('experience', [])
    return render_template('work_experience.html', experiences=experience_data)

# --- ROUTE FOR STEP 3: EDUCATION ---
@app.route('/education', methods=['GET', 'POST'])
def education():
    if 'personal' not in session:
        flash('Please fill out your personal details first.', 'warning')
        return redirect(url_for('personal_details'))

    if request.method == 'POST':
        if 'education' not in session:
            session['education'] = []
        
        session['education'].append({
            'degree': request.form['degree'],
            'institution': request.form['institution'],
            'grad_year': request.form['grad_year']
        })
        session.modified = True
        flash('Education entry added!', 'success')
        return redirect(url_for('education'))

    education_data = session.get('education', [])
    return render_template('education.html', educations=education_data)

# --- ROUTE FOR STEP 4: SKILLS ---
@app.route('/skills', methods=['GET', 'POST'])
def skills():
    if 'personal' not in session:
        flash('Please fill out your personal details first.', 'warning')
        return redirect(url_for('personal_details'))

    if request.method == 'POST':
        # Skills are stored as a comma-separated string
        session['skills'] = request.form['skills']
        flash('Skills saved!', 'success')
        return redirect(url_for('review'))

    skills_data = session.get('skills', '')
    return render_template('skills.html', skills=skills_data)

# --- ROUTE FOR STEP 5: REVIEW ---
@app.route('/review')
def review():
    if 'personal' not in session:
        flash('No data to review. Please start from the beginning.', 'warning')
        return redirect(url_for('personal_details'))

    return render_template('review.html', data=session)

# --- ROUTE FOR GENERATING THE CV WEBSITE ---
@app.route('/generate')
def generate_cv():
    if 'personal' not in session:
        flash('Cannot generate CV. No data available.', 'danger')
        return redirect(url_for('personal_details'))

    # Pass all session data to the resume template
    return render_template('resume_template.html', data=session)

# --- ROUTE TO CLEAR SESSION AND START OVER ---
@app.route('/clear')
def clear_session():
    session.clear()
    flash('Your data has been cleared. You can start over.', 'info')
    return redirect(url_for('personal_details'))

if __name__ == '__main__':
    app.run(debug=True)
