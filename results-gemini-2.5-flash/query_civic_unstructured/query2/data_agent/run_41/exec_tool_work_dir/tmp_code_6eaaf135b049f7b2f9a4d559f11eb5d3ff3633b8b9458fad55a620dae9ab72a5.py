code = """import re
import json

docs = json.load(open(locals()['var_function-call-12914571133745161145'], 'r'))

def extract_project_info(text):
    projects = []
    # Regex to find project blocks
    # It looks for a project name followed by updates/schedule/status.
    # It also handles variations of "completed" dates
    project_blocks = re.split(r'\n(?=[A-Z][a-zA-Z0-9\s&,-]+\n\(cid:190\) (Updates|Project Description|Estimated Schedule|Project Schedule|Complete Construction|Final Design|Begin Construction))', text)
    
    # The split might create an empty string at the beginning if the text starts with a project.
    # It also splits the project name and the rest of the block.
    # We need to re-group them.
    
    # The first element might be an intro before any project
    if len(project_blocks) > 0 and not project_blocks[0].strip().startswith("Public Works Commission"): # Basic check for non-project intro
         project_blocks = project_blocks[1:] # remove intro if present, assuming real projects start after it

    # Re-grouping: each project block starts with a name, followed by "Updates", "Project Description", etc.
    # So we'll iterate by two.
    
    # Handle the case where the entire document might be one big project description or general text.
    # For this specific case, the project info is generally structured as "Project Name 
 (cid:190) Updates: 
 (cid:131) ..."
    
    # A more robust regex to capture individual projects.
    # This pattern looks for a project name (likely capitalized) followed by details.
    # It tries to capture everything until the next similar project heading or end of document.
    
    project_pattern = re.compile(r'([A-Z][a-zA-Z0-9\s&,\-\/\(\)]+?)(?:\n\(cid:190\) Updates:|\n\(cid:190\) Project Description:|\n\(cid:190\) Project Schedule:|\n\(cid:190\) Estimated Schedule:)(.*?)(?=\n[A-Z][a-zA-Z0-9\s&,\-\/\(\)]+?(?:\n\(cid:190\) Updates:|\n\(cid:190\) Project Description:|\n\(cid:190\) Project Schedule:|\n\(cid:190\) Estimated Schedule:)|$)', re.DOTALL)
    
    matches = project_pattern.findall(text)

    for name_raw, details_raw in matches:
        project_name = name_raw.strip()
        details = details_raw.strip()
        
        status = None
        et = None
        topic = []
        
        # Determine status
        if "completed" in details.lower():
            status = "completed"
        elif "design" in details.lower() or "planning phase" in details.lower():
            status = "design"
        elif "not started" in details.lower() or "identified but not begun" in details.lower():
            status = "not started"
        elif "under construction" in details.lower():
            status = "under construction" # This is a new status found
        
        # Extract end time (et)
        et_match = re.search(r'(Complete Construction|Construction was completed|Complete Design|Final Design):\s*([A-Za-z]+\s+\d{4}|\d{4}-[A-Za-z]+|\d{4}-\d{2})', details, re.IGNORECASE)
        if et_match:
            et = et_match.group(2).strip()
        elif "Construction was completed, " in details:
            et_match = re.search(r'Construction was completed,\s*([A-Za-z]+\s+\d{4})', details)
            if et_match:
                et = et_match.group(1).strip()
        elif "Construction was completed " in details: # sometimes without comma
            et_match = re.search(r'Construction was completed\s*([A-Za-z]+\s+\d{4})', details)
            if et_match:
                et = et_match.group(1).strip()
        
        # Determine topic - simple keyword search
        if "park" in project_name.lower() or "playground" in project_name.lower():
            topic.append("park")
        if "road" in project_name.lower() or "highway" in project_name.lower() or "PCH" in project_name.lower():
            topic.append("road")
        if "FEMA" in details.lower():
            topic.append("FEMA")
        if "fire" in details.lower():
            topic.append("fire")
        if "emergency" in details.lower():
            topic.append("emergency")
        if "drainage" in details.lower() or "storm drain" in project_name.lower():
            topic.append("drainage")
        if "water treatment" in project_name.lower():
            topic.append("water treatment")
            
        # Add a more general check within details for "park" as it might not be in the name
        if not topic and "park" in details.lower():
            topic.append("park")


        projects.append({
            "Project_Name": project_name,
            "topic": ", ".join(topic) if topic else None,
            "status": status,
            "et": et
        })
    return projects

all_projects = []
for doc in docs:
    all_projects.extend(extract_project_info(doc['text']))

# Filter for park-related projects completed in 2022
filtered_projects = [
    p for p in all_projects
    if p["status"] == "completed" and p["topic"] and "park" in p["topic"].lower() and p["et"] and "2022" in p["et"]
]

# Get unique project names to avoid duplicates in funding query
unique_project_names = list(set([p["Project_Name"] for p in filtered_projects]))

__RESULT__:
print(json.dumps(unique_project_names))"""

env_args = {'var_function-call-7964308287440170398': ['civic_docs'], 'var_function-call-12914571133745161145': 'file_storage/function-call-12914571133745161145.json'}

exec(code, env_args)
