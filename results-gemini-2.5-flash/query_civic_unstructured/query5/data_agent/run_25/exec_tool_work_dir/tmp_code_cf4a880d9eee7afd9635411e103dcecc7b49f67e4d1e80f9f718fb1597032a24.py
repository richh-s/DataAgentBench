code = """import json
import re

file_path = locals()['var_function-call-4723927449613075700']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022_start_names = set()

for doc in civic_docs:
    text = doc['text']
    
    lines = text.split('\n')
    
    current_context_type = "unknown"
    current_project_name = None
    project_details_buffer = []

    for i, line in enumerate(lines):
        line = line.strip()

        if "Disaster Recovery Projects" in line:
            current_context_type = "disaster"
            if current_project_name:
                project_detail_text = '\n'.join(project_details_buffer)
                
                is_disaster_project = False
                if current_context_type == "disaster":
                    is_disaster_project = True
                elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
                    is_disaster_project = True
                    
                if is_disaster_project:
                    start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):\s*.*?(2022(?:-|\s*(?:Spring|Summer|Fall|January|February|March|April|May|June|July|August|September|October|November|December))?)", project_detail_text, re.IGNORECASE)
                    if start_date_match:
                        disaster_projects_2022_start_names.add(current_project_name)

            current_project_name = None
            project_details_buffer = []
            continue
        elif "Capital Improvement Projects" in line:
            current_context_type = "capital"
            if current_project_name:
                project_detail_text = '\n'.join(project_details_buffer)
                
                is_disaster_project = False
                if current_context_type == "disaster":
                    is_disaster_project = True
                elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
                    is_disaster_project = True
                    
                if is_disaster_project:
                    start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):\s*.*?(2022(?:-|\s*(?:Spring|Summer|Fall|January|February|March|April|May|June|July|August|September|October|November|December))?)", project_detail_text, re.IGNORECASE)
                    if start_date_match:
                        disaster_projects_2022_start_names.add(current_project_name)

            current_project_name = None
            project_details_buffer = []
            continue
        
        if any(keyword in line for keyword in ["Page", "Item", "Agenda Report", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:"]) or not line:
            continue
        
        is_potential_project_name_header = (
            not line.startswith('(cid:') and 
            len(line) > 5 and 
            line[0].isupper() and 
            (i + 1 < len(lines) and lines[i+1].strip().startswith('(cid:')) 
        )

        if is_potential_project_name_header:
            if current_project_name:
                project_detail_text = '\n'.join(project_details_buffer)
                
                is_disaster_project = False
                if current_context_type == "disaster":
                    is_disaster_project = True
                elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
                    is_disaster_project = True
                    
                if is_disaster_project:
                    start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):\s*.*?(2022(?:-|\s*(?:Spring|Summer|Fall|January|February|March|April|May|June|July|August|September|October|November|December))?)", project_detail_text, re.IGNORECASE)
                    if start_date_match:
                        disaster_projects_2022_start_names.add(current_project_name)
            
            current_project_name = line
            project_details_buffer = []
        elif current_project_name:
            project_details_buffer.append(line)
    
    if current_project_name:
        project_detail_text = '\n'.join(project_details_buffer)
        
        is_disaster_project = False
        if current_context_type == "disaster":
            is_disaster_project = True
        elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
            is_disaster_project = True
            
        if is_disaster_project:
            start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):\s*.*?(2022(?:-|\s*(?:Spring|Summer|Fall|January|February|March|April|May|June|July|August|September|October|November|December))?)", project_detail_text, re.IGNORECASE)
            if start_date_match:
                disaster_projects_2022_start_names.add(current_project_name)

project_names_list = list(disaster_projects_2022_start_names)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-7673823113563948285': ['civic_docs'], 'var_function-call-4723927449613075700': 'file_storage/function-call-4723927449613075700.json', 'var_function-call-6314443807874731014': ['Funding']}

exec(code, env_args)
