code = """import re
import json

data_path = locals()['var_function-call-2718406926601295619']

with open(data_path, 'r') as f:
    data = json.load(f)

projects = []

for doc in data:
    text = doc['text']
    
    # Split text into sections that might contain project descriptions
    # We are looking for lines that indicate the start of a project description,
    # which often begins with a project name, followed by bullet points like (cid:190) Updates:
    # We need to escape the literal parentheses in (cid:190)
    project_blocks = re.split(r'\n\n\(cid:190\) (?:Updates|Project Schedule|Estimated Schedule):', text)
    
    # The first element might be preamble, so we iterate from the second block
    for i in range(1, len(project_blocks)):
        block = project_blocks[i]
        
        # The project name should be what came just before the split point, or the first meaningful line in the block
        # Given the split, the project name is likely the last non-empty line of the *previous* block segment that led to this split.
        # This makes extraction from `project_blocks[i]` tricky for the name itself. 
        # Instead, let's try to find project names and their details within each original `doc['text']` using a different strategy.
        
        # Alternative strategy: Iterate through lines and identify project names and their details sequentially.
        
        lines = block.split('\n')
        current_project_name = None
        project_details_buffer = []

        for j, line in enumerate(lines):
            stripped_line = line.strip()

            # Heuristic for identifying a potential project name
            # A line that is not too short, not too long, not a bullet point, and doesn't look like a general header.
            is_potential_project_name = (
                len(stripped_line) > 5 and 
                len(stripped_line) < 100 and 
                not stripped_line.startswith("(cid:") and # Avoid lines that are just bullet points
                not re.match(r"^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:)", stripped_line, re.IGNORECASE)
            )

            # If we detect a potential project name, and it's followed by project detail indicators
            # (like updates or schedule), then it's likely a new project.
            next_lines_sample = "\n".join(lines[j+1:min(j+6, len(lines))]) # Look up to 5 lines ahead
            has_project_indicators = (
                "(cid:190) Updates:" in next_lines_sample or
                "(cid:190) Project Schedule:" in next_lines_sample or
                "(cid:190) Estimated Schedule:" in next_lines_sample
            )

            if is_potential_project_name and has_project_indicators:
                # If we were processing a previous project, save it first
                if current_project_name and project_details_buffer:
                    full_details_text = "\n".join(project_details_buffer).lower()
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
                project_details_buffer = []
                project_details_buffer.append(stripped_line) # Add the name itself to details for broader search
            elif current_project_name: # If we are in a project block, add lines to its details buffer
                project_details_buffer.append(stripped_line)

        # After the inner loop, process the very last project in this document if it exists
        if current_project_name and project_details_buffer:
            full_details_text = "\n".join(project_details_buffer).lower()
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
