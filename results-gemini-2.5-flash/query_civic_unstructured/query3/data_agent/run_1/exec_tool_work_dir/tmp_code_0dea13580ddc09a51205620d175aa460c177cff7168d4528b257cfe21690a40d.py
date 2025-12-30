code = """import json
import re

with open(locals()['var_function-call-16494580253678001854'], 'r') as f:
    civic_docs = json.load(f)

projects = []
for doc in civic_docs:
    text = doc['text']
    
    # Capital Improvement Projects (Design)
    design_projects_match = re.findall(r'Capital Improvement Projects \(Design\)(.*?)(?:Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects|RECOMMENDED ACTION:)', text, re.DOTALL)
    if design_projects_match:
        for section in design_projects_match:
            project_blocks = re.split(r'\n\n(?=[A-Z][a-zA-Z0-9 ]+ Project)', section)
            for block in project_blocks:
                name_match = re.search(r'([A-Z][a-zA-Z0-9 ]+ Project)', block)
                if name_match:
                    project_name = name_match.group(1).strip()
                    if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower() or "caloes" in project_name.lower():
                        status = "design"
                        project_type = "capital"
                        topic = "capital"
                        
                        if "storm drain" in project_name.lower():
                            topic += ", storm drain"
                        if "emergency" in project_name.lower():
                            topic += ", emergency"
                        if "fema" in project_name.lower():
                            topic += ", FEMA"
                        if "caloes" in project_name.lower():
                            topic += ", CalOES"
                        
                        projects.append({
                            "Project_Name": project_name,
                            "topic": topic,
                            "type": project_type,
                            "status": status
                        })

    # Disaster Recovery Projects
    disaster_projects_match = re.findall(r'Disaster Recovery Projects\n(.*?)(?:Capital Improvement Projects \(Design\)|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)|RECOMMENDED ACTION:)', text, re.DOTALL)
    if disaster_projects_match:
        for section in disaster_projects_match:
            project_blocks = re.split(r'\n\n(?=[A-Z][a-zA-Z0-9 ]+ Project)', section)
            for block in project_blocks:
                name_match = re.search(r'([A-Z][a-zA-Z0-9 ]+ Project)', block)
                if name_match:
                    project_name = name_match.group(1).strip()
                    if "emergency" in project_name.lower() or "fema" in project_name.lower() or "disaster" in project_name.lower() or "caloes" in project_name.lower():
                        status = "design" # Default status, will try to find more specific
                        project_type = "disaster"
                        topic = "disaster"

                        status_match = re.search(r'Status: (.*)', block)
                        if status_match:
                            status = status_match.group(1).strip()

                        if "emergency" in project_name.lower():
                            topic += ", emergency"
                        if "fema" in project_name.lower():
                            topic += ", FEMA"
                        if "caloes" in project_name.lower():
                            topic += ", CalOES"
                        if "woolsey fire" in project_name.lower():
                            topic += ", fire"
                        
                        projects.append({
                            "Project_Name": project_name,
                            "topic": topic,
                            "type": project_type,
                            "status": status
                        })
                        
    # Other sections that might contain relevant projects
    # Latigo Canyon Road Retaining Wall Repair Project (FEMA/CalOES approval)
    latigo_match = re.search(r'Latigo Canyon Road Retaining Wall Repair Project.*?Awaiting final FEMA/CalOES approval for scope modification', text, re.DOTALL)
    if latigo_match:
        projects.append({
            "Project_Name": "Latigo Canyon Road Retaining Wall Repair Project",
            "topic": "retaining wall, FEMA, CalOES, emergency",
            "type": "disaster",
            "status": "design" # Awaiting approval, so still in design
        })
        
    # Outdoor Warning Signs (emergency warning)
    warning_match = re.search(r'Outdoor Warning Signs.*?Project to be discussed during a joint Public Works and Public Safety Commission meeting for project direction due to concerns regarding sirens height and feedback from residents and the community', text, re.DOTALL)
    if warning_match:
        projects.append({
            "Project_Name": "Outdoor Warning Signs",
            "topic": "emergency warning, public safety",
            "type": "capital", # Assuming this is a capital project for public safety infrastructure
            "status": "design" # To be discussed
        })


    # City Traffic Signals Backup Power
    traffic_signals_match = re.search(r'City Traffic Signals Backup Power.*?Project is in the preliminary design phase', text, re.DOTALL)
    if traffic_signals_match:
        projects.append({
            "Project_Name": "City Traffic Signals Backup Power",
            "topic": "traffic signals, backup power, emergency",
            "type": "capital",
            "status": "design"
        })

# Filter out duplicates
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
