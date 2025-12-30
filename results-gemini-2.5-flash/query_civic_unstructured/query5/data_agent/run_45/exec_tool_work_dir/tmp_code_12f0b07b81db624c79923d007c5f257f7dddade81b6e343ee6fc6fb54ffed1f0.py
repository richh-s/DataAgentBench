code = """import json
import re

with open(locals()['var_function-call-9214184878544642466'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Split text into sections for easier parsing
    sections = re.split(r'\n\n(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects)', text)
    
    current_type = ""
    for i, section in enumerate(sections):
        if "Capital Improvement Projects" in section:
            current_type = "capital"
        elif "Disaster Recovery Projects" in section:
            current_type = "disaster"
        else:
            # Process the project details within the current section
            
            # Regex to find project names and their schedules within a section
            # It looks for lines that seem like project titles, followed by updates or schedules
            project_matches = re.findall(r'\n\n([A-Z][a-zA-Z0-9_ -]+.*?)(?:\n\(cid:190\) Updates:|\n\(cid:190\) Project Schedule:|\n\(cid:190\) Estimated Schedule:|\n\(cid:190\) Project Description:|\nPage \d+ of \d+|$)', section, re.DOTALL)
            
            for project_name in project_matches:
                project_name = project_name.strip()
                if not project_name or "Page" in project_name or "Agenda Item" in project_name: # Exclude common headers
                    continue
                
                # Now try to find the start date (Begin Construction) for this specific project in the section
                # We need to find the specific block for this project within the section to get its schedule
                
                # A more precise regex to capture the project block and its schedule
                project_block_match = re.search(re.escape(project_name) + r'(?:\n\(cid:190\) Updates:.*?|\n\(cid:190\) Project Schedule:.*?|\n\(cid:190\) Estimated Schedule:.*?|\n\(cid:190\) Project Description:.*?)(.*?)(?=(?:\n\n\n|\n\n(?!\(cid:190\)))|$)', section, re.DOTALL)

                start_date = None
                if project_block_match:
                    project_details_block = project_block_match.group(1)
                    start_date_match = re.search(r'Begin Construction: (.*?)\n', project_details_block)
                    if start_date_match:
                        start_date = start_date_match.group(1).strip()
                
                projects_data.append({
                    "Project_Name": project_name,
                    "type": current_type,
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
