code = """import re
import json

data_path = locals()['var_function-call-2718406926601295619']

with open(data_path, 'r') as f:
    data = json.load(f)

projects = []
for doc in data:
    text = doc['text']
    lines = text.split('\n')
    current_project_name = None
    project_details_buffer = []

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic to identify a potential project name
        # It should be a non-empty line, not starting with a bullet point,
        # and not looking like a simple date or a short status update.
        if stripped_line and not stripped_line.startswith('(cid:') and not re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:)', stripped_line) and len(stripped_line) > 5 and len(stripped_line) < 100:
            # Check if this line is followed by project update/schedule indicators
            potential_project_name = stripped_line
            # Look ahead a few lines for common project detail indicators
            next_lines_sample = "\n".join(lines[i+1:i+6]) if i+6 <= len(lines) else ""
            if '(cid:190) Updates:' in next_lines_sample or '(cid:190) Project Schedule:' in next_lines_sample or '(cid:190) Estimated Schedule:' in next_lines_sample:
                # If we found a new project, process the previous one if it exists
                if current_project_name:
                    # Process the buffered details for the previous project
                    full_details = "\n".join(project_details_buffer).lower()
                    project_type = "capital"
                    if "disaster" in full_details or "fema" in full_details or "fire" in full_details or "emergency" in full_details or "(fema project)" in current_project_name.lower():
                        project_type = "disaster"
                    
                    start_date = None
                    start_date_match = re.search(r"(?:begin construction|advertise|complete design|project schedule|estimated schedule):\s*(.*?2022.*?)(?=\n|\s*\(cid:131)|\s*\(cid:190))", full_details, re.IGNORECASE)
                    if start_date_match:
                        date_str = start_date_match.group(1).strip()
                        if "2022" in date_str:
                            start_date = date_str
                    
                    if project_type == "disaster" and start_date:
                        projects.append({'Project_Name': current_project_name, 'type': project_type, 'st': start_date})
                
                # Start buffering for the new project
                current_project_name = potential_project_name
                project_details_buffer = []
            elif current_project_name: # If we are in a project block, add lines to buffer
                project_details_buffer.append(stripped_line)
        elif stripped_line.startswith('(cid:') and current_project_name: # Bullet points under a project
            project_details_buffer.append(stripped_line)
        elif not stripped_line and current_project_name: # Empty line, might be end of project block
            # If we are in a project block and encounter an empty line,
            # it might signify the end of the project's details,
            # or just a paragraph break. We'll keep buffering until a new project is clearly identified.
            project_details_buffer.append(stripped_line)
        elif not current_project_name: # Not in a project block yet, or a non-project related line
            pass # Skip and look for next potential project

    # Process the last project after the loop finishes
    if current_project_name:
        full_details = "\n".join(project_details_buffer).lower()
        project_type = "capital"
        if "disaster" in full_details or "fema" in full_details or "fire" in full_details or "emergency" in full_details or "(fema project)" in current_project_name.lower():
            project_type = "disaster"
        
        start_date = None
        start_date_match = re.search(r"(?:begin construction|advertise|complete design|project schedule|estimated schedule):\s*(.*?2022.*?)(?=\n|\s*\(cid:131)|\s*\(cid:190))", full_details, re.IGNORECASE)
        if start_date_match:
            date_str = start_date_match.group(1).strip()
            if "2022" in date_str:
                start_date = date_str
        
        if project_type == "disaster" and start_date:
            projects.append({'Project_Name': current_project_name, 'type': project_type, 'st': start_date})

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for p in projects:
    normalized_name = re.sub(r'\s+', ' ', p['Project_Name']).strip()
    if normalized_name not in seen_project_names:
        unique_projects.append({'Project_Name': normalized_name, 'type': p['type'], 'st': p['st']})
        seen_project_names.add(normalized_name)

print("__RESULT__:")
print(json.dumps(unique_projects))"""

env_args = {'var_function-call-18410950440773738686': ['civic_docs'], 'var_function-call-2718406926601295619': 'file_storage/function-call-2718406926601295619.json'}

exec(code, env_args)
