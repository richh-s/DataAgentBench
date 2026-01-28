code = """import json
import re

with open(locals()['var_function-call-9214184878544642466'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Split the document into sections based on major project type headers
    sections = re.split(r'\n\n(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects)', text)
    
    current_type = ""
    for i in range(len(sections)):
        section_content = sections[i]
        
        if "Capital Improvement Projects" in section_content:
            current_type = "capital"
            continue
        elif "Disaster Recovery Projects" in section_content:
            current_type = "disaster"
            continue

        # Process project details within the current section if a type is set
        if current_type:
            # A regex to find individual project blocks. 
            # It looks for a line starting with an uppercase letter (likely a project name) 
            # followed by lines starting with (cid:190) for project details.
            project_blocks = re.findall(r'\n\n([A-Z][a-zA-Z0-9_ -]+.*?)(?:\n\(cid:190\).*?)*', section_content, re.DOTALL)
            
            for project_name_raw in project_blocks:
                project_name = project_name_raw.strip()
                
                # Further filter out non-project names or headers
                if not project_name or len(project_name) < 5 or "Page" in project_name or "Agenda Item" in project_name or project_name.startswith("(") or project_name.endswith("project"):
                    continue

                # Now search for 'Begin Construction' within the same section_content, 
                # but specifically linked to this project name. This is tricky due to loose structure.
                # A safer approach is to get the block of text *after* the project name and *before* the next project name/section.
                
                # Find the start and end of this specific project's detailed block
                project_start_index = section_content.find(project_name_raw)
                if project_start_index == -1: # Should not happen if project_name_raw was found by re.findall
                    continue
                
                # Try to find the next project name or section header to define the end of the current project's block
                next_project_match = re.search(r'\n\n([A-Z][a-zA-Z0-9_ -]+.*?)(?:\n\(cid:190\).*?)*', section_content[project_start_index + len(project_name_raw):], re.DOTALL)
                
                project_detail_block = ""
                if next_project_match:
                    project_detail_block = section_content[project_start_index : project_start_index + len(project_name_raw) + next_project_match.start()]
                else:
                    project_detail_block = section_content[project_start_index:]
                    
                start_date = None
                start_date_match = re.search(r'Begin Construction: (.*?)\n', project_detail_block)
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
