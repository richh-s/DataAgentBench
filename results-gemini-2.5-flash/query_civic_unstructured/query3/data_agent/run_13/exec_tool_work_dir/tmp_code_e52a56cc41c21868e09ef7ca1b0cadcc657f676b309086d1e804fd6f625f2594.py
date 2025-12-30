code = """import json
import re

with open(locals()['var_function-call-13297758767889787610'], 'r') as f:
    docs = json.load(f)

projects_data = []

for doc in docs:
    text = doc['text']

    # Regex to find project blocks. Assuming projects are listed with names followed by updates/schedules.
    # This regex looks for lines that start with capital letters (potentially project names) followed by (cid:190) Updates/Schedule or similar patterns.
    project_blocks = re.split(r'\\n([A-Z][a-zA-Z0-9\\s,\\-&()\/]+(?: Project)?)(?:\\n\\(cid:190) Updates:|\\n\\(cid:190) Project Description:|\\n\\(cid:190) Estimated Schedule:|\\nCapital Improvement Projects \\(Construction\\)|\\nCapital Improvement Projects \\(Not Started\\)|\\nDisaster Recovery Projects)', text)

    # The split might create an empty string at the beginning if the text starts with a project name.
    # Also, the first element might be introductory text.
    # We are interested in pairs of (Project Name, Project Details)
    # The first element is usually generic text before any project.
    # The split might also include "Capital Improvement Projects (Design)", "Capital Improvement Projects (Construction)" etc as project names, these need to be handled.
    
    # Let's refine the parsing based on the observed document structure
    # Projects are usually listed under headers like "Capital Improvement Projects (Design)"
    
    current_type = None
    current_status = None
    
    lines = text.split('\\n')
    project_name = None
    project_status_from_header = None # Status from the header like 'Capital Improvement Projects (Design)'

    for i, line in enumerate(lines):
        line = line.strip()

        # Update project type and general status from headers
        if "Capital Improvement Projects (Design)" in line:
            current_type = "capital"
            project_status_from_header = "design"
            continue
        elif "Capital Improvement Projects (Construction)" in line:
            current_type = "capital"
            project_status_from_header = "construction" # This can be translated to 'in progress' or similar, for now let's keep it as construction
            continue
        elif "Capital Improvement Projects (Not Started)" in line:
            current_type = "capital"
            project_status_from_header = "not started"
            continue
        elif "Disaster Recovery Projects" in line:
            current_type = "disaster"
            project_status_from_header = None # Disaster projects can have various statuses within their description
            continue

        # Look for project names
        # A project name is often a capitalized phrase that might be followed by "(cid:190) Updates:", "(cid:190) Project Schedule:", etc.
        # It should not be a general header like "Agenda Item #"
        
        # Regex to capture project names, being careful about false positives
        # Project names are usually followed by an update, description, or schedule section.
        project_name_match = re.match(r'^([A-Z][a-zA-Z0-9\\s,\\-&()\\/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Plan)?(?: Phase \\d)?)$', line)
        if project_name_match and not line.startswith("Page ") and not line.startswith("Agenda Item #"):
            project_name = project_name_match.group(1).strip()
            
            # Now, extract details for this project_name from subsequent lines
            project_text_block = []
            j = i + 1
            while j < len(lines) and not re.match(r'^([A-Z][a-zA-Z0-9\\s,\\-&()\\/]+(?: Project)?(?: Repair)?(?: Improvements)?(?: Study)?(?: Plan)?(?: Phase \\d)?)$', lines[j].strip()) and not ("Capital Improvement Projects" in lines[j] or "Disaster Recovery Projects" in lines[j]):
                project_text_block.append(lines[j].strip())
                j += 1
            
            project_details = " ".join(project_text_block)

            status = project_status_from_header # Default status from the section header
            if "Updates: Project is currently under construction" in project_details or "Updates: Construction was completed" in project_details:
                status = "completed" if "Construction was completed" in project_details else "in progress" # More granular status
            elif "Updates: Project is in the preliminary design phase" in project_details or "Complete Design:" in project_details:
                status = "design"
            
            # Infer topics
            topic = []
            if "emergency" in project_details.lower() or "emergency" in project_name.lower():
                topic.append("emergency")
            if "FEMA" in project_details or "FEMA" in project_name:
                topic.append("FEMA")
            if "fire" in project_details.lower():
                topic.append("fire")
            if "disaster" in current_type:
                topic.append("disaster")
            if "storm drain" in project_details.lower() or "storm drain" in project_name.lower():
                topic.append("storm drain")
            if "road" in project_details.lower() or "road" in project_name.lower():
                topic.append("road")
            if "park" in project_details.lower() or "park" in project_name.lower():
                topic.append("park")
            if "water treatment" in project_details.lower() or "water treatment" in project_name.lower():
                topic.append("water treatment")
            if "traffic" in project_details.lower() or "traffic" in project_name.lower():
                topic.append("traffic")
            if "drainage" in project_details.lower() or "drainage" in project_name.lower():
                topic.append("drainage")
            
            if project_name and (any(t in ['emergency', 'FEMA'] for t in topic) or "emergency" in project_name.lower() or "FEMA" in project_name.lower()):
                projects_data.append({
                    "Project_Name": project_name,
                    "topic": ", ".join(topic),
                    "type": current_type,
                    "status": status if status else "unknown"
                })
            
            project_name = None # Reset for the next project

# Filter out duplicates based on project name and ensure at least one of the topics is 'emergency' or 'FEMA'
unique_projects = {}
for project in projects_data:
    if project['Project_Name'] not in unique_projects:
        unique_projects[project['Project_Name']] = project
    else:
        # Merge topics if a project appears multiple times
        existing_topics = set(unique_projects[project['Project_Name']]['topic'].split(', '))
        new_topics = set(project['topic'].split(', '))
        unique_projects[project['Project_Name']]['topic'] = ", ".join(sorted(list(existing_topics.union(new_topics))))

final_projects = [proj for proj in unique_projects.values() if 'emergency' in proj['topic'] or 'FEMA' in proj['topic']]

print('__RESULT__:')
print(json.dumps(final_projects))"""

env_args = {'var_function-call-13297758767889787610': 'file_storage/function-call-13297758767889787610.json'}

exec(code, env_args)
