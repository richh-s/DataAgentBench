code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

# Keywords to identify project lines
project_keywords = r'(?:Project|Projects|Plan|Improvements|Study)'
# Main section headers that act as delimiters
section_headers = r'(?:Capital Improvement Projects|Disaster Recovery Projects)'

for doc in civic_docs:
    text = doc['text']
    
    # Split text by lines to process more easily
    lines = text.split('\n')
    
    current_project_name = None
    current_project_details = []

    for line in lines:
        line = line.strip()
        
        # Check if the line is a potential project name
        # A project name typically starts with a capital letter and contains project_keywords
        if re.match(r'^[A-Z].*' + project_keywords + r'.*$', line) and not re.match(section_headers, line):
            # If we were collecting details for a previous project, save it
            if current_project_name and \
               re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning|traffic signals backup', current_project_name + ' ' + ' '.join(current_project_details), re.IGNORECASE):
                
                full_details = ' '.join(current_project_details)
                
                status = "unknown"
                if re.search(r'design|preliminary design|complete design|awaiting.*?approval', full_details, re.IGNORECASE):
                    status = "design"
                elif re.search(r'completed|construction was completed|notice of completion filed', full_details, re.IGNORECASE):
                    status = "completed"
                elif re.search(r'not started|not begun', full_details, re.IGNORECASE):
                    status = "not started"
                elif re.search(r'under construction|out to bid|begin construction', full_details, re.IGNORECASE):
                    status = "construction"

                project_type = "unknown"
                if re.search(r'disaster recovery projects|disaster', current_project_name + ' ' + full_details, re.IGNORECASE):
                    project_type = "disaster"
                elif re.search(r'capital improvement projects|capital', current_project_name + ' ' + full_details, re.IGNORECASE):
                    project_type = "capital"
                
                topic_keywords = []
                if re.search(r'park', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("park")
                if re.search(r'road', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("road")
                if re.search(r'FEMA', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("FEMA")
                if re.search(r'fire', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("fire")
                if re.search(r'emergency warning|outdoor warning signs', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency warning")
                if re.search(r'drainage|storm drain', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("drainage")
                if re.search(r'capital', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("capital")
                if re.search(r'disaster', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("disaster")
                if re.search(r'traffic signals|backup power', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
                if re.search(r'CalOES', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("CalOES")
                if re.search(r'retaining wall', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("retaining wall")
                if re.search(r'emergency', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency")

                topic = ", ".join(sorted(list(set(topic_keywords))))
                if not topic: topic = "general"

                projects_data.append({
                    "Project_Name": current_project_name.replace("(cid:190)", "").strip(),
                    "topic": topic,
                    "type": project_type,
                    "status": status
                })
            
            # Start new project
            current_project_name = line
            current_project_details = []
        # If not a project name, and we are tracking a project, add to its details
        elif current_project_name and not re.match(section_headers, line):
            current_project_details.append(line)
        # If it's a section header, reset current project tracking
        elif re.match(section_headers, line):
            current_project_name = None
            current_project_details = []
            
    # After loop, check if last project needs to be added
    if current_project_name and \
       re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning|traffic signals backup', current_project_name + ' ' + ' '.join(current_project_details), re.IGNORECASE):
        
        full_details = ' '.join(current_project_details)
        
        status = "unknown"
        if re.search(r'design|preliminary design|complete design|awaiting.*?approval', full_details, re.IGNORECASE):
            status = "design"
        elif re.search(r'completed|construction was completed|notice of completion filed', full_details, re.IGNORECASE):
            status = "completed"
        elif re.search(r'not started|not begun', full_details, re.IGNORECASE):
            status = "not started"
        elif re.search(r'under construction|out to bid|begin construction', full_details, re.IGNORECASE):
            status = "construction"

        project_type = "unknown"
        if re.search(r'disaster recovery projects|disaster', current_project_name + ' ' + full_details, re.IGNORECASE):
            project_type = "disaster"
        elif re.search(r'capital improvement projects|capital', current_project_name + ' ' + full_details, re.IGNORECASE):
            project_type = "capital"
        
        topic_keywords = []
        if re.search(r'park', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("park")
        if re.search(r'road', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("road")
        if re.search(r'FEMA', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("FEMA")
        if re.search(r'fire', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("fire")
        if re.search(r'emergency warning|outdoor warning signs', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency warning")
        if re.search(r'drainage|storm drain', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("drainage")
        if re.search(r'capital', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("capital")
        if re.search(r'disaster', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("disaster")
        if re.search(r'traffic signals|backup power', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
        if re.search(r'CalOES', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("CalOES")
        if re.search(r'retaining wall', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("retaining wall")
        if re.search(r'emergency', current_project_name + ' ' + full_details, re.IGNORECASE): topic_keywords.append("emergency")

        topic = ", ".join(sorted(list(set(topic_keywords))))
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
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json', 'var_function-call-374798579160347094': ['Funding']}

exec(code, env_args)
