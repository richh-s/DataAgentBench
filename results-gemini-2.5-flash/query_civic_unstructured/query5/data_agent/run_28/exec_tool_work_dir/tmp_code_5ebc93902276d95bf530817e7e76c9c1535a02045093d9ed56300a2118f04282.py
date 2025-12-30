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
    project_details = []

    for i, line in enumerate(lines):
        stripped_line = line.strip()

        # Heuristic for identifying a project name
        # A line that is not too short, not too long, not a bullet point, and doesn't look like a general header.
        is_potential_project_name = (
            len(stripped_line) > 5 and 
            len(stripped_line) < 100 and 
            not stripped_line.startswith('(cid:') and
            not re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:)', stripped_line, re.IGNORECASE)
        )

        # Look for typical project schedule/update indicators in the next few lines
        next_lines_sample = "\n".join(lines[i+1:min(i+6, len(lines))]) # Look up to 5 lines ahead
        has_project_indicators = (
            '(cid:190) Updates:' in next_lines_sample or
            '(cid:190) Project Schedule:' in next_lines_sample or
            '(cid:190) Estimated Schedule:' in next_lines_sample
        )

        if is_potential_project_name and has_project_indicators:
            # If we were processing a previous project, save it first
            if current_project_name and project_details:
                full_details_text = "\n".join(project_details).lower()
                project_type = "capital" # Default

                if re.search(r"disaster|fema|fire|emergency", full_details_text) or re.search(r"disaster|fema|fire|emergency", current_project_name.lower()):
                    project_type = "disaster"

                start_date = None
                start_date_match = re.search(r"(?:begin construction|advertise|complete design|project schedule|estimated schedule):\s*(.*?2022.*?)(?=\n|\s*\(cid:131)|\s*\(cid:190))", full_details_text, re.IGNORECASE)
                if start_date_match:
                    date_str = start_date_match.group(1).strip()
                    if "2022" in date_str:
                        start_date = date_str
                
                if project_type == "disaster" and start_date:
                    projects.append({'Project_Name': current_project_name, 'type': project_type, 'st': start_date})

            # Start a new project
            current_project_name = stripped_line
            project_details = []
            # Add the current line as a detail if it contains relevant info, though it's primarily the name.
            # We'll rely more on the subsequent lines for details.
            project_details.append(stripped_line)
        elif current_project_name: # If we are in a project block, add lines to its details buffer
            project_details.append(stripped_line)

    # After the loop, process the very last project if it exists
    if current_project_name and project_details:
        full_details_text = "\n".join(project_details).lower()
        project_type = "capital"

        if re.search(r"disaster|fema|fire|emergency", full_details_text) or re.search(r"disaster|fema|fire|emergency", current_project_name.lower()):
            project_type = "disaster"

        start_date = None
        start_date_match = re.search(r"(?:begin construction|advertise|complete design|project schedule|estimated schedule):\s*(.*?2022.*?)(?=\n|\s*\(cid:131)|\s*\(cid:190))", full_details_text, re.IGNORECASE)
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
