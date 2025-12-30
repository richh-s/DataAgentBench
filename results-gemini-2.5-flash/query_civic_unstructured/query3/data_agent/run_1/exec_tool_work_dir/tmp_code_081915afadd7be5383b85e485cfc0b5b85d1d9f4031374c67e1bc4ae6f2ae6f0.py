code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# Simplified regex to identify a line that might be a project name
# It looks for a line starting with a capital letter, followed by at least one word,
# and containing one of the project-identifying keywords. No complex escaping needed for this simple pattern.
project_name_line_pattern = re.compile(r'^[A-Z][a-zA-Z0-9 ]*(?:Project|Projects|Plan|Improvements|Study)(?: |$)', re.MULTILINE)

# Keywords to filter projects
relevant_keywords = ['emergency', 'fema', 'disaster', 'caloes', 'outdoor warning', 'traffic signals backup']

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details = []

    for line in lines:
        line = line.strip()

        if not line: # Skip empty lines
            continue
        
        # Check if the line is a potential project name
        if project_name_line_pattern.match(line):
            # If a project was being tracked, process it
            if current_project_name:
                full_project_text = (current_project_name + ' ' + ' '.join(current_project_details)).lower()
                
                # Filter based on relevant keywords
                if any(keyword in full_project_text for keyword in relevant_keywords):
                    
                    status = "unknown"
                    if "design" in full_project_text or "preliminary design" in full_project_text or "awaiting approval" in full_project_text:
                        status = "design"
                    elif "completed" in full_project_text or "construction was completed" in full_project_text or "notice of completion filed" in full_project_text:
                        status = "completed"
                    elif "not started" in full_project_text or "not begun" in full_project_text:
                        status = "not started"
                    elif "under construction" in full_project_text or "out to bid" in full_project_text or "begin construction" in full_project_text:
                        status = "construction"

                    project_type = "unknown"
                    if "disaster recovery projects" in full_project_text or "disaster" in full_project_text:
                        project_type = "disaster"
                    elif "capital improvement projects" in full_project_text or "capital" in full_project_text:
                        project_type = "capital"
                    
                    topic_keywords_found = []
                    if "park" in full_project_text: topic_keywords_found.append("park")
                    if "road" in full_project_text: topic_keywords_found.append("road")
                    if "fema" in full_project_text: topic_keywords_found.append("FEMA")
                    if "fire" in full_project_text: topic_keywords_found.append("fire")
                    if "emergency warning" in full_project_text or "outdoor warning signs" in full_project_text: topic_keywords_found.append("emergency warning")
                    if "drainage" in full_project_text or "storm drain" in full_project_text: topic_keywords_found.append("drainage")
                    if "capital" in full_project_text: topic_keywords_found.append("capital")
                    if "disaster" in full_project_text: topic_keywords_found.append("disaster")
                    if "traffic signals" in full_project_text or "backup power" in full_project_text: topic_keywords_found.append("traffic signals & backup power")
                    if "caloes" in full_project_text: topic_keywords_found.append("CalOES")
                    if "retaining wall" in full_project_text: topic_keywords_found.append("retaining wall")
                    if "emergency" in full_project_text: topic_keywords_found.append("emergency")

                    topic = ", ".join(sorted(list(set(topic_keywords_found))))
                    if not topic: topic = "general"

                    projects_data.append({
                        "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                        "topic": topic,
                        "type": project_type,
                        "status": status
                    })
            
            # Start a new project
            current_project_name = line
            current_project_details = []
        # If not a project name, add to current project details
        elif current_project_name: # Only add details if a project is being tracked
            current_project_details.append(line)
            
    # Process the last project after the loop ends
    if current_project_name:
        full_project_text = (current_project_name + ' ' + ' '.join(current_project_details)).lower()
        if any(keyword in full_project_text for keyword in relevant_keywords):
            status = "unknown"
            if "design" in full_project_text or "preliminary design" in full_project_text or "awaiting approval" in full_project_text:
                status = "design"
            elif "completed" in full_project_text or "construction was completed" in full_project_text or "notice of completion filed" in full_project_text:
                status = "completed"
            elif "not started" in full_project_text or "not begun" in full_project_text:
                status = "not started"
            elif "under construction" in full_project_text or "out to bid" in full_project_text or "begin construction" in full_project_text:
                status = "construction"

            project_type = "unknown"
            if "disaster recovery projects" in full_project_text or "disaster" in full_project_text:
                project_type = "disaster"
            elif "capital improvement projects" in full_project_text or "capital" in full_project_text:
                project_type = "capital"
            
            topic_keywords_found = []
            if "park" in full_project_text: topic_keywords_found.append("park")
            if "road" in full_project_text: topic_keywords_found.append("road")
            if "fema" in full_project_text: topic_keywords_found.append("FEMA")
            if "fire" in full_project_text: topic_keywords_found.append("fire")
            if "emergency warning" in full_project_text or "outdoor warning signs" in full_project_text: topic_keywords_found.append("emergency warning")
            if "drainage" in full_project_text or "storm drain" in full_project_text: topic_keywords_found.append("drainage")
            if "capital" in full_project_text: topic_keywords_found.append("capital")
            if "disaster" in full_project_text: topic_keywords_found.append("disaster")
            if "traffic signals" in full_project_text or "backup power" in full_project_text: topic_keywords_found.append("traffic signals & backup power")
            if "caloes" in full_project_text: topic_keywords_found.append("CalOES")
            if "retaining wall" in full_project_text: topic_keywords_found.append("retaining wall")
            if "emergency" in full_project_text: topic_keywords_found.append("emergency")

            topic = ", ".join(sorted(list(set(topic_keywords_found))))
            if not topic: topic = "general"

            projects_data.append({
                "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                "topic": topic,
                "type": project_type,
                "status": status
            })


# Deduplicate projects based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects_data:
    # Normalize project name for deduplication (e.g., remove trailing 'Project' if it's inconsistent)
    normalized_name = re.sub(r'\s*(?:Project|Projects|Plan|Improvements|Study)$', '', p['Project_Name'], flags=re.IGNORECASE).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(normalized_name)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json', 'var_function-call-374798579160347094': ['Funding']}

exec(code, env_args)
