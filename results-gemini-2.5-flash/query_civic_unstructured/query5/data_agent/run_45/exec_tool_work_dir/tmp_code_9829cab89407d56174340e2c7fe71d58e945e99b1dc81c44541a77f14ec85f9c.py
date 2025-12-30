code = """import json
import re

with open(locals()['var_function-call-9214184878544642466'], 'r') as f:
    civic_docs = json.load(f)

projects_data = []

for doc in civic_docs:
    text = doc['text']
    
    # Use a more robust pattern to split the document into major project type sections
    # This pattern captures the section header and the content until the next similar header or end of text
    sections = re.split(r'\n\n(Capital Improvement Projects \(.*?\)|Disaster Recovery Projects.*?)\n\n', text, flags=re.DOTALL)
    
    current_type = ""
    # The split function might return empty strings or headers in alternating fashion
    for i in range(len(sections)):
        section_content = sections[i]
        if "Capital Improvement Projects" in section_content:
            current_type = "capital"
            continue # Move to the next part which contains actual project details
        elif "Disaster Recovery Projects" in section_content:
            current_type = "disaster"
            continue # Move to the next part which contains actual project details
        
        # Process the content of the section for projects if a type has been established
        if current_type:
            # Pattern to capture project name and its subsequent details (including schedule)
            # This pattern looks for a line starting with an uppercase letter as a potential project name,
            # followed by indented lines (cid:190) which contain project details.
            # It stops at the next line that looks like a new project name or a major section break.
            project_blocks = re.findall(r'^([A-Z][a-zA-Z0-9_ -]+.*?)\n((?:\(cid:190\).*?\n)*)', section_content, re.MULTILINE)
            
            for project_name_raw, project_details_block in project_blocks:
                project_name = project_name_raw.strip()
                
                # Filter out lines that are not actual project names (e.g., small fragments, page numbers)
                if not project_name or len(project_name) < 5 or "Page" in project_name or "Agenda Item" in project_name or project_name.lower().endswith("project")):
                    continue

                start_date = None
                # Search for 'Begin Construction' within the details block of the current project
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
