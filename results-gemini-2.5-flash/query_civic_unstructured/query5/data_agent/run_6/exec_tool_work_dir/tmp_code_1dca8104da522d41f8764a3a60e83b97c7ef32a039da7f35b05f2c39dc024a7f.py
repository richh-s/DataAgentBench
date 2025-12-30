code = """import json
import re

def extract_project_details_simple(text):
    projects = []
    lines = text.split('\n')
    current_project = None
    
    # Flag to indicate if the document generally discusses disaster recovery
    is_global_disaster_context = "Disaster Recovery Projects" in text or "FEMA" in text or "CalOES" in text

    for i, line in enumerate(lines):
        line = line.strip()

        # Heuristic to identify a project name line: contains "Project" but not a schedule or update indicator
        # and is not too short or all uppercase (which might indicate a header).
        # Also, check if it's not a known non-project phrase.
        if "Project" in line and \
           "(cid:190)" not in line and \
           "Schedule:" not in line and \
           "Updates:" not in line and \
           len(line) > 10 and \
           not line.isupper() and \
           "Agenda Item" not in line and \
           not re.match(r'^\d+\.\s*\w+\s*Project$', line): # Exclude numbered project headers
            
            if current_project:
                projects.append(current_project)
            
            project_name = line.replace("(Design)", "").replace("(Construction)", "").replace("(Not Started)", "").strip()
            current_project = {
                "Project_Name": project_name,
                "type": "capital",
                "st": None
            }
            # Check for disaster keywords in the project name itself
            if "FEMA" in project_name or "CalOES" in project_name or "Disaster" in project_name or \
               "(FEMA Project)" in project_name or "(CalJPIA Project)" in project_name or "(CalOES Project)" in project_name:
                current_project["type"] = "disaster"
            continue

        if current_project:
            # Refine project type if disaster keywords are found in surrounding lines
            if current_project["type"] == "capital" and \
               ("FEMA" in line or "CalOES" in line or "Disaster Recovery" in line):
                current_project["type"] = "disaster"

            # Extract start time
            if "(cid:190) Project Schedule:" in line:
                for j in range(i + 1, min(i + 6, len(lines))): # Look up to 5 lines ahead
                    schedule_detail_line = lines[j].strip()
                    
                    # Look for explicit 'Begin Construction:' or 'Advertise:'
                    begin_construction_match = re.search(r'Begin Construction:\s*([^\n]+)', schedule_detail_line)
                    if begin_construction_match:
                        current_project["st"] = begin_construction_match.group(1).strip()
                        break
                    
                    advertise_match = re.search(r'Advertise:\s*([^\n]+)', schedule_detail_line)
                    if advertise_match:
                        current_project["st"] = advertise_match.group(1).strip()
                        break
                    
                    # Fallback: look for year/season/month if specific phrases aren't found
                    date_match = re.search(r'\b(202\d|Spring|Summer|Fall|Winter|January|February|March|April|May|June|July|August|September|October|November|December)\b', schedule_detail_line)
                    if date_match:
                        current_project["st"] = date_match.group(0).strip()
                        break
    
    if current_project: # Add the last project if any
        projects.append(current_project)

    # Final pass to apply global disaster context if individual project didn't catch it
    for project in projects:
        if project["type"] == "capital" and is_global_disaster_context:
            project["type"] = "disaster"

    return projects

file_path = locals()['var_function-call-6524522302801542169']
with open(file_path, 'r') as f:
    data = json.load(f)

all_projects_extracted = []
for doc in data:
    all_projects_extracted.extend(extract_project_details_simple(doc['text']))


disaster_projects_2022_names = set()
for project in all_projects_extracted:
    if project['type'] == 'disaster' and project['st'] and '2022' in str(project['st']):
        disaster_projects_2022_names.add(project['Project_Name'])

# Convert set to list for printing
print("__RESULT__:")
print(json.dumps(list(disaster_projects_2022_names)))"""

env_args = {'var_function-call-6524522302801542169': 'file_storage/function-call-6524522302801542169.json', 'var_function-call-17434838567716078401': ['Funding'], 'var_function-call-7943208518371631309': 'file_storage/function-call-7943208518371631309.json'}

exec(code, env_args)
