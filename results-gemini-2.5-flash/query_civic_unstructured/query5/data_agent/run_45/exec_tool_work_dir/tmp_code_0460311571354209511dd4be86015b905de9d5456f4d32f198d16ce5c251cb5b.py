code = """import json
import re

with open(locals()['var_function-call-9214184878544642466'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Regex to find project names, types, and start dates
    # Looking for lines like "Project Name (type)" or "Project Name" followed by "Project Schedule: (cid:131) Begin Construction: Date"
    # And "Disaster Recovery Projects"
    
    # Pattern to capture project names and their associated details, especially start dates
    # This pattern tries to be comprehensive but also specific to project sections.
    project_pattern = re.compile(r'\n\n(.*?)(?:\n\(cid:190\) Project Description:.*?|\n\(cid:190\) Updates:.*?|\n\(cid:190\) Estimated Schedule:.*?|\n\(cid:190\) Project Schedule:.*?|\nPage \d+ of \d+.*?)(?=(?:\n\n\n|\n\n(?!\(cid:190\)))|$)


    # Find all potential project blocks
    for match in re.finditer(r'\n\n([A-Z][a-zA-Z0-9_ -]+.*?)(?:\n\(cid:190\) Updates:|\n\(cid:190\) Project Schedule:|\n\(cid:190\) Estimated Schedule:|\n\(cid:190\) Project Description:|\nPage \d+ of \d+|$)', text, re.DOTALL):
        block = match.group(0) # Get the full matched block including the potential project name
        
        project_name_line = block.split('\n')[2] if len(block.split('\n')) > 2 and "Page" not in block.split('\n')[2] else block.split('\n')[0]

        project_name = project_name_line.strip()

        # Heuristic to filter out non-project names (e.g., section headers, page numbers)
        if not project_name or "Page" in project_name or "Agenda Item" in project_name or project_name.startswith("Capital Improvement Projects") or project_name.startswith("Disaster Recovery Projects"): # Exclude common headers
            continue


        # Determine project type (disaster or capital)
        project_type = "capital"  # Default type
        if "Disaster Recovery Projects" in block or "FEMA" in block or "CalOES" in block or "fire" in block:
            project_type = "disaster"
            
        # Extract start date (begin construction)
        start_date_match = re.search(r'Begin Construction: (.*?)\n', block)
        start_date = start_date_match.group(1).strip() if start_date_match else None
        
        projects_data.append({
            "Project_Name": project_name,
            "type": project_type,
            "st": start_date
        })

# Filter for disaster projects that started in 2022
disaster_projects_2022 = [
    p for p in projects_data 
    if p["type"] == "disaster" and p["st"] and "2022" in p["st"]
]

# Extract project names for the next step
project_names_2022_disaster = [p["Project_Name"] for p in disaster_projects_2022]


print("__RESULT__:")
print(json.dumps(project_names_2022_disaster))"""

env_args = {'var_function-call-9214184878544642466': 'file_storage/function-call-9214184878544642466.json'}

exec(code, env_args)
