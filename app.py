import streamlit as st
from adaptive_learning import customize_content
from gemini_utils import generate_content

st.title("Lesson and Revision Planning Assistant")

# User type selection
user_type = st.radio("I am a:", ["Teacher", "Student"])

# Subject and language selection
subjects = ["Math", "English", "Kiswahili", "Geography", "Biology", "Physics",
            "Chemistry", "CRE", "History", "Computer Studies", "Business",
            "Agriculture", "French"]
subject = st.selectbox("Subject", subjects)

languages = ["English", "Kiswahili", "French"]
language = st.selectbox("Language of Instruction", languages)

# Topic input
topic = st.text_input("Specific Topic (optional)")

# Form selection
form = st.selectbox("Form", ["Form 1", "Form 2", "Form 3", "Form 4"])

if user_type == "Teacher":
    st.subheader("Lesson Plan Generator")
    lesson_duration = st.number_input("Lesson Duration (minutes)", min_value=30, max_value=180, value=60, step=15)
    learning_objectives = st.text_area("Learning Objectives")
else:
    st.subheader("Revision Plan Generator")
    revision_duration = st.number_input("Revision Duration (minutes)", min_value=15, max_value=120, value=30, step=15)
    difficulty = st.selectbox("Difficulty Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    # Customize content request
    if user_type == "Teacher":
        content_request = customize_content("lesson", subject, topic, form, lesson_duration, learning_objectives, language)
    else:
        content_request = customize_content("revision", subject, topic, form, revision_duration, difficulty, language)
    
    # Generate content using Gemini Pro
    generated_content = generate_content(content_request, subject, topic, form, user_type, language)
    
    # Display generated content
    st.subheader("Generated Plan:")
    st.write(generated_content)



# Sidebar with detailed information
st.sidebar.title("How to Use This Part")
st.sidebar.write("Follow these steps to generate your plan:")

st.sidebar.markdown("""
1. **Select Your Role**: 
   - Choose 'Teacher' for lesson plans
   - Choose 'Student' for revision plans

2. **Choose Subject**: 
   - Select from the dropdown menu

3. **Select Language**: 
   - Choose the language for your plan

4. **Enter Topic** (optional): 
   - Specify a particular topic within the subject

5. **Select Form**: 
   - Choose the appropriate form (1-4)

6. **Additional Details**:
   - For Teachers: Enter lesson duration and objectives
   - For Students: Set revision duration and difficulty level

7. **Generate Plan**: 
   - Click the 'Generate Plan' button

8. **Review**: 
   - Your customized plan will appear below
""")