code = """import json
import re

file_path = locals()['var_function-call-4723927449613075700']

with open(file_path, 'r') as f:
    civic_docs = json.load(f)

disaster_projects_2022_start_names = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_context_type = "unknown" # "capital", "disaster", or "unknown"
    current_project_name = None
    project_details_buffer = []

    for i, line in enumerate(lines):
        line = line.strip()

        # Update section context based on headers
        if "Disaster Recovery Projects" in line:
            # Process the previous project if any, before changing context
            if current_project_name:
                project_detail_text = '\n'.join(project_details_buffer)
                
                is_disaster_project = False
                if current_context_type == "disaster": # This project was in a disaster section
                    is_disaster_project = True
                elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
                    is_disaster_project = True
                        
                if is_disaster_project:
                    start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):.*?2022", project_detail_text, re.IGNORECASE)
                    if start_date_match:
                        disaster_projects_2022_start_names.add(current_project_name)

            current_context_type = "disaster"
            current_project_name = None # Reset project name
            project_details_buffer = [] # Clear details for new section
            continue
        elif "Capital Improvement Projects" in line:
            # Process the previous project if any
            if current_project_name:
                project_detail_text = '\n'.join(project_details_buffer)
                
                is_disaster_project = False
                if current_context_type == "disaster":
                    is_disaster_project = True
                elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
                    is_disaster_project = True
                        
                if is_disaster_project:
                    start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):.*?2022", project_detail_text, re.IGNORECASE)
                    if start_date_match:
                        disaster_projects_2022_start_names.add(current_project_name)

            current_context_type = "capital"
            current_project_name = None
            project_details_buffer = []
            continue
        
        # Skip purely informational lines that are not part of project details or names
        if any(keyword in line for keyword in ["Page", "Item", "Agenda Report", "To:", "Prepared by:", "Approved by:", "Date prepared:", "Meeting date:", "Subject:", "RECOMMENDED ACTION:", "DISCUSSION:"]) or not line:
            continue
        
        # Heuristic for a new project name: starts with uppercase, not a bullet,
        # and is followed by a line starting with a bullet indicating project details.
        is_potential_project_name_header = (
            not line.startswith('(cid:') and 
            len(line) > 5 and # Project names are typically longer than short phrases
            line[0].isupper() and # Most project names start with a capital letter
            (i + 1 < len(lines) and lines[i+1].strip().startswith('(cid:')) # Expecting bulleted details next
        )

        if is_potential_project_name_header:
            # If we were tracking a previous project, evaluate it before starting a new one
            if current_project_name:
                project_detail_text = '\n'.join(project_details_buffer)
                
                is_disaster_project = False
                if current_context_type == "disaster":
                    is_disaster_project = True
                elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
                    is_disaster_project = True
                    
                if is_disaster_project:
                    start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):.*?2022", project_detail_text, re.IGNORECASE)
                    if start_date_match:
                        disaster_projects_2022_start_names.add(current_project_name)
            
            # Start tracking the new project
            current_project_name = line
            project_details_buffer = [] # Reset buffer for details of the new project
        elif current_project_name: # If we're inside a project block, accumulate its details
            project_details_buffer.append(line)
    
    # After the loop, process the last project block if one was being tracked
    if current_project_name:
        project_detail_text = '\n'.join(project_details_buffer)
        
        is_disaster_project = False
        if current_context_type == "disaster":
            is_disaster_project = True
        elif re.search(r"(FEMA Project|CalOES Project|CalJPIA Project|disaster|emergency|fire)", current_project_name, re.IGNORECASE):
            is_disaster_project = True
            
        if is_disaster_project:
            start_date_match = re.search(r"(?:Begin Construction|Project Schedule|Estimated Schedule):.*?2022", project_detail_text, re.IGNORECASE)
            if start_date_match:
                disaster_projects_2022_start_names.add(current_project_name)

project_names_list = list(disaster_projects_2022_start_names)

print("__RESULT__:")
print(json.dumps(project_names_list))"""

env_args = {'var_function-call-7673823113563948285': ['civic_docs'], 'var_function-call-4723927449613075700': 'file_storage/function-call-4723927449613075700.json', 'var_function-call-6314443807874731014': ['Funding']}

exec(code, env_args)
