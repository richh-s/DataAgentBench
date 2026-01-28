code = """import json
import re

file_path = locals()['var_function-call-11833941680332813035']
with open(file_path, 'r') as f:
    docs = json.load(f)

projects_data = []

for doc in docs:
    text = doc['text']
    
    # Regex to find project blocks
    project_sections = re.split(r'\n\n(Capital Improvement Projects \((?:Design|Construction|Not Started)\)|Disaster Recovery Projects)\n\n', text)
    
    current_status = None
    for i, section in enumerate(project_sections):
        if "Capital Improvement Projects (Design)" in section:
            current_status = "design"
        elif "Capital Improvement Projects (Construction)" in section:
            current_status = "completed" # Assuming "Construction" means it's either in progress or completed
        elif "Capital Improvement Projects (Not Started)" in section:
            current_status = "not started"
        elif "Disaster Recovery Projects" in section:
            current_status = "disaster" # Special status for disaster recovery projects
        
        if current_status and i + 1 < len(project_sections):
            projects_in_section = re.findall(r'\n\n([A-Z][A-Za-z0-9_ -/&,]+?)(?:\n\n\(cid:190\) Updates:.*?|\n\n\(cid:190\) Project Description:.*?)', project_sections[i+1], re.DOTALL)
            
            for project_name in projects_in_section:
                project_name = project_name.strip()
                if project_name and len(project_name) < 100: # Simple filter for valid project names
                    
                    project_topic = ""
                    if "FEMA" in text or "disaster" in current_status.lower():
                        project_topic = "FEMA"
                    if "emergency" in text or "emergency warning" in project_name.lower():
                        if project_topic:
                            project_topic += ", emergency"
                        else:
                            project_topic = "emergency"
                            
                    if project_topic:
                        projects_data.append({
                            "Project_Name": project_name,
                            "status": current_status,
                            "topic": project_topic
                        })

# Clean up project names to remove extraneous details and ensure consistency for joining
cleaned_projects = []
for project in projects_data:
    name = project["Project_Name"].replace("(cid:190)", "").replace("(FEMA Project)", "").replace("(CalJPIA Project)", "").replace("(CalOES Project)", "").strip()
    # Further clean by removing common descriptive phrases that aren't part of the core name
    name = re.sub(r'\(Design\)|\(Construction\)|\(Not Started\)|\(Updates\)|\(Project Schedule\)|\(Estimated Schedule\)|\(Project Description\)', '', name).strip()
    # Remove descriptions after a colon or dash if it seems like a description
    name = re.split(r'[:—]', name)[0].strip()
    
    # Remove parenthetical years or other common suffixes that might hinder joining
    name = re.sub(r'\(FY\d{4}-\d{4}\)|\(\d{4}\)', '', name).strip()
    name = name.split("Page")[0].strip() # remove page numbers if they get picked up
    
    # Check if the project name exists and is not just a general heading
    if name and not any(keyword in name for keyword in ["Capital Improvement Projects", "Disaster Recovery Projects", "Agenda Item"]):
        cleaned_projects.append({"Project_Name": name, "status": project["status"], "topic": project["topic"]})

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in cleaned_projects:
    if project["Project_Name"] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project["Project_Name"])

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-303220545277477403': ['civic_docs'], 'var_function-call-11833941680332813035': 'file_storage/function-call-11833941680332813035.json'}

exec(code, env_args)
