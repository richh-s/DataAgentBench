code = """import re
import json

doc_text = locals()['var_function-call-9242641405732855470']

projects_data = []

# Regex to find project names and their updates/schedules
# It looks for lines that start with a project name (often capitalized) followed by details,
# or projects listed under specific headings.
project_pattern = re.compile(r'(?P<project_name>[A-Z][A-Za-z0-9\s&,-]+?)(?:\n|\(cid:190))(?P<details>(?:\(cid:190).*?(?:\n\n|(?=\n[A-Z][A-Za-z0-9\s&,-]+?)(?:\n|\(cid:190))|(?=\nCapital Improvement Projects)|(?=\nDisaster Recovery Projects)|$)))', re.DOTALL)

# Refined regex to capture different sections and project types more reliably
# This regex will look for major headings like "Capital Improvement Projects" or "Disaster Recovery Projects"
# and then try to capture individual projects within those sections.
section_pattern = re.compile(r'(Capital Improvement Projects \((?P<section_status>[^)]+)\)|Disaster Recovery Projects)(?P<section_content>.*?)(?=(Capital Improvement Projects|Disaster Recovery Projects|$))', re.DOTALL)


for doc in doc_text['query_db_response']['results']:
    text = doc['text']
    
    # Check for general emergency/FEMA keywords in the document
    is_doc_fema_emergency = bool(re.search(r'emergency|FEMA', text, re.IGNORECASE))

    # Process sections
    for section_match in section_pattern.finditer(text):
        section_status = section_match.group('section_status') if section_match.group('section_status') else "Disaster Recovery"
        section_content = section_match.group('section_content')

        # Find individual projects within each section
        for project_match in project_pattern.finditer(section_content):
            project_name = project_match.group('project_name').strip()
            details = project_match.group('details')

            # Determine status based on section and details
            status = section_status if section_status != "Disaster Recovery" else "Disaster Recovery"
            if "under construction" in details.lower():
                status = "Construction"
            elif "design" in details.lower() and "complete design" not in details.lower():
                status = "Design"
            elif "not started" in details.lower() or "awaiting" in details.lower():
                status = "Not Started"
            elif "completed" in details.lower() or "construction was completed" in details.lower():
                status = "Completed"
            
            # Determine topic
            topic = []
            if re.search(r'FEMA', details, re.IGNORECASE) or re.search(r'FEMA', project_name, re.IGNORECASE) or "Disaster Recovery" in section_status:
                topic.append("FEMA")
            if re.search(r'emergency', details, re.IGNORECASE) or re.search(r'emergency', project_name, re.IGNORECASE) or "Outdoor Warning Signs" in project_name:
                topic.append("emergency")
            
            # If no specific topic found, but doc is related to FEMA/emergency, assume general topic
            if not topic and is_doc_fema_emergency:
                topic.append("emergency/FEMA related")

            if topic: # Only add projects with identified topics
                projects_data.append({
                    "Project_Name": project_name,
                    "status": status,
                    "topic": ", ".join(list(set(topic))) # Use set to avoid duplicate topics
                })

# Filter out projects with generic names or short names that are likely not actual projects
filtered_projects = []
for p in projects_data:
    if len(p['Project_Name']) > 5 and not p['Project_Name'].lower().strip() in ["updates", "project schedule", "discussion", "recommended action", "subject", "prepared by", "approved by", "to", "item", "date prepared", "meeting date", "capital improvement projects", "disaster recovery projects", "public works commission agenda report"]:
        filtered_projects.append(p)

# Remove duplicates based on Project_Name and status
unique_projects = []
seen = set()
for p in filtered_projects:
    identifier = (p['Project_Name'], p['status'])
    if identifier not in seen:
        unique_projects.append(p)
        seen.add(identifier)

print('__RESULT__:')
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-9242641405732855470': 'file_storage/function-call-9242641405732855470.json'}

exec(code, env_args)
