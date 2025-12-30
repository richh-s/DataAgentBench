code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document into sections based on major headings
    sections = re.split(r'(Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects)', text)
    
    current_section_type = ""
    for i in range(len(sections)):
        if sections[i] in ["Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)", "Capital Improvement Projects (Not Started)", "Disaster Recovery Projects"]:
            current_section_type = sections[i]
        elif current_section_type:
            section_content = sections[i]
            
            # Extract individual projects within the section content
            # Project names are usually followed by updates/schedules, and sometimes by another project name
            project_blocks = re.findall(r'([A-Z][a-zA-Z0-9 &\'\-,\.\(\)]+\s(?:Project|Projects)?)\n\n(.*?)(?=\n[A-Z][a-zA-Z0-9 &\'\-,\.\(\)]+\s(?:Project|Projects)?|\Z)', section_content, re.DOTALL)

            for project_name_raw, project_details in project_blocks:
                project_name = project_name_raw.strip()

                # Filter for relevant projects based on keywords
                if (re.search(r'emergency|FEMA|disaster|CalOES|outdoor warning signs|traffic signals backup power', project_name, re.IGNORECASE) or
                    re.search(r'emergency|FEMA|disaster|CalOES', project_details, re.IGNORECASE)):

                    status = "unknown"
                    if "(Design)" in current_section_type or re.search(r'status:\s*design|in preliminary design phase|complete design:|awaiting final FEMA/CalOES approval', project_details, re.IGNORECASE):
                        status = "design"
                    elif "(Construction)" in current_section_type or re.search(r'status:\s*completed|construction was completed|notice of completion filed', project_details, re.IGNORECASE):
                        status = "completed"
                    elif "(Not Started)" in current_section_type or re.search(r'status:\s*not started|not begun', project_details, re.IGNORECASE):
                        status = "not started"
                    elif re.search(r'under construction|project is currently out to bid|begin construction:', project_details, re.IGNORECASE):
                        status = "construction"

                    project_type = "unknown"
                    if "Disaster Recovery Projects" in current_section_type or re.search(r'disaster', project_name + project_details, re.IGNORECASE):
                        project_type = "disaster"
                    elif "Capital Improvement Projects" in current_section_type or re.search(r'capital', project_name + project_details, re.IGNORECASE):
                        project_type = "capital"
                    
                    topic_keywords = []
                    if re.search(r'park', project_name + project_details, re.IGNORECASE): topic_keywords.append("park")
                    if re.search(r'road', project_name + project_details, re.IGNORECASE): topic_keywords.append("road")
                    if re.search(r'FEMA', project_name + project_details, re.IGNORECASE): topic_keywords.append("FEMA")
                    if re.search(r'fire', project_name + project_details, re.IGNORECASE): topic_keywords.append("fire")
                    if re.search(r'emergency warning|outdoor warning signs', project_name + project_details, re.IGNORECASE): topic_keywords.append("emergency warning")
                    if re.search(r'drainage|storm drain', project_name + project_details, re.IGNORECASE): topic_keywords.append("drainage")
                    if re.search(r'capital', project_name + project_details, re.IGNORECASE): topic_keywords.append("capital")
                    if re.search(r'disaster', project_name + project_details, re.IGNORECASE): topic_keywords.append("disaster")
                    if re.search(r'traffic signals|backup power', project_name + project_details, re.IGNORECASE): topic_keywords.append("traffic signals & backup power")
                    if re.search(r'CalOES', project_name + project_details, re.IGNORECASE): topic_keywords.append("CalOES")
                    if re.search(r'retaining wall', project_name + project_details, re.IGNORECASE): topic_keywords.append("retaining wall")
                    if re.search(r'emergency', project_name + project_details, re.IGNORECASE): topic_keywords.append("emergency")

                    topic = ", ".join(sorted(list(set(topic_keywords))))
                    if not topic: topic = "general"

                    projects.append({
                        "Project_Name": project_name,
                        "topic": topic,
                        "type": project_type,
                        "status": status
                    })

    # Handle projects outside of explicit sections but still relevant like "Outdoor Warning Signs"
    # Add specific regex for these if they are not caught by the general section parsing
    # Latigo Canyon Road Retaining Wall Repair Project (FEMA/CalOES approval)
    latigo_match = re.search(r'Latigo Canyon Road Retaining Wall Repair Project.*?Awaiting final FEMA/CalOES approval for scope modification', text, re.DOTALL)
    if latigo_match and not any(p['Project_Name'] == "Latigo Canyon Road Retaining Wall Repair Project" for p in projects):
        projects.append({
            "Project_Name": "Latigo Canyon Road Retaining Wall Repair Project",
            "topic": "retaining wall, FEMA, CalOES, emergency",
            "type": "disaster",
            "status": "design"
        })
        
    # Outdoor Warning Signs (emergency warning)
    warning_match = re.search(r'Outdoor Warning Signs.*?Project to be discussed during a joint Public Works and Public Safety Commission meeting for project direction', text, re.DOTALL)
    if warning_match and not any(p['Project_Name'] == "Outdoor Warning Signs" for p in projects):
        projects.append({
            "Project_Name": "Outdoor Warning Signs",
            "topic": "emergency warning, public safety, emergency",
            "type": "capital",
            "status": "design"
        })

    # City Traffic Signals Backup Power
    traffic_signals_match = re.search(r'City Traffic Signals Backup Power.*?Project is in the preliminary design phase', text, re.DOTALL)
    if traffic_signals_match and not any(p['Project_Name'] == "City Traffic Signals Backup Power" for p in projects):
        projects.append({
            "Project_Name": "City Traffic Signals Backup Power",
            "topic": "traffic signals & backup power, emergency",
            "type": "capital",
            "status": "design"
        })

# Filter out duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects:
    if p['Project_Name'] not in seen_project_names:
        unique_projects.append(p)
        seen_project_names.add(p['Project_Name'])

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-17299078503029090456': ['civic_docs'], 'var_function-call-16494580253678001854': 'file_storage/function-call-16494580253678001854.json'}

exec(code, env_args)
