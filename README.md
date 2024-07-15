# Adaptive Learning and Lesson Planning Assistant

## Overview
The Adaptive Learning and Lesson Planning Assistant is a web application designed to help teachers create lesson plans and students generate revision plans. It uses AI to customize educational content based on user input, making it easier for educators and learners to create tailored study materials.

## Current Features
- User role selection (Teacher or Student)
- Subject selection
- Language of instruction choice
- Optional specific topic input
- Form/grade level selection
- Customized input fields for teachers (lesson duration, learning objectives) and students (revision duration, difficulty level)
- AI-generated lesson or revision plans
- Responsive web interface

## Future Features
- User accounts and plan saving
- Integration with popular learning management systems
- Collaborative planning tools for teachers
- Progress tracking for students
- Mobile app version
- Support for more subjects and languages

## Technologies Used
- Python
- Flask (Web framework)
- Google Generative AI (Gemini model)
- HTML/CSS/JavaScript
- Waitress (WSGI server)

## Getting Started

### Prerequisites
- Python 3.7+
- Google Cloud account with Generative AI API access

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/Kirai-Kevin/planner.git
   cd adaptive-learning-assistant
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the project root and add your Google API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

4. Run the application:
   ```
   python wsgi.py      , when deploying.
   python server.py 
   ```

5. Open a web browser and navigate to `http://localhost:8080`

### Usage
1. Select your role (Teacher or Student)
2. Choose the subject and language of instruction
3. (Optional) Enter a specific topic
4. Select the form/grade level
5. Fill in additional details (lesson/revision duration, learning objectives/difficulty level)
6. Click "Generate Plan"
7. Review the AI-generated plan

