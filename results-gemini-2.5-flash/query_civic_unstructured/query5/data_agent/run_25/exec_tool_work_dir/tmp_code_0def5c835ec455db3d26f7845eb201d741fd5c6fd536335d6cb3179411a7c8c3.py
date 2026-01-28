code = """import json
import re

file_path = locals()['var_function-call-4723927449613075700']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022_start_names = set()

disaster_keywords_pattern = re.compile(r'(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)', re.IGNORECASE)
start_date_2022_pattern = re.compile(r'(?:Begin Construction|Project Schedule|Estimated Schedule):.*?2022', re.IGNORECASE)

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_context_type = "unknown"
    current_project_name = None
    project_details_buffer = []

    def process_current_project():
        nonlocal current_project_name, project_details_buffer, current_context_type, disaster_projects_2022_start_names
        if current_project_name:
            project_detail_text = '\n'.join(project_details_buffer)
            
            is_disaster_project = False
            if current_context_type == "disaster":
                is_disaster_project = True
            elif disaster_keywords_pattern.search(current_project_name):
                is_disaster_project = True
                    
            if is_disaster_project:
                if start_date_2022_pattern.search(project_detail_text):
                    disaster_projects_2022_start_names.add(current_project_name)

    for i, line in enumerate(lines):
        line = line.strip()

        if "Disaster Recovery Projects" in line:
            process_current_project()
            current_context_type = "disaster"
            current_project_name = None
            project_details_buffer = []
            continue
        elif "Capital Improvement Projects" in line:
            process_current_project()
            current_context_type = "capital"
            current_project_name = None
            project_details_buffer = []
            continue
        
        # Skip purely informational lines that are not part of project details or names
        if any(keyword in line for keyword in ["Page", "Item", "Agenda Report", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:"]) or not line:
            if current_project_name:
                project_details_buffer.append(line)
            continue
        
        # Heuristic for a new project name: starts with uppercase, not a bullet ((cid:)),
        # and is followed by a line starting with a bullet indicating project details.
        is_potential_project_name_header = (
            not line.startswith('(cid:') and 
            len(line) > 5 and 
            line[0].isupper() and 
            (i + 1 < len(lines) and lines[i+1].strip().startswith('(cid:')) 
        )

        if is_potential_project_name_header:
            process_current_project()
            current_project_name = line
            project_details_buffer = []
        elif current_project_name:
            project_details_buffer.append(line)
    
    process_current_project()

project_names_list = list(disaster_projects_2022_start_names)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-7673823113563948285': ['civic_docs'], 'var_function-call-4723927449613075700': 'file_storage/function-call-4723927449613075700.json', 'var_function-call-6314443807874731014': ['Funding']}

exec(code, env_args)
