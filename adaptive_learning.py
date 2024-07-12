def customize_content(plan_type, subject, topic, form, duration, additional_info, language):
    content_request = f"Create a {plan_type} plan for {subject} ({form}) "
    if topic:
        content_request += f"focusing on the topic '{topic}' "
    content_request += f"The plan should be designed for a {duration}-minute session. "
    
    if plan_type == "lesson":
        content_request += f"Include the following learning objectives: {additional_info}. "
    else:  # revision plan
        content_request += f"The student's current level is {additional_info}. "
    
    content_request += f"Please provide the entire plan in {language}. "
    
    return content_request