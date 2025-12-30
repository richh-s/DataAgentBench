code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_details_extracted = []

# Keywords that often appear in project names or titles
project_name_indicators = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power", "Treatment", "Signs", "Emergency", "FEMA", "Recovery", "Center", "Slopes", "Mitigation", "Program", "Initiative"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower() # For document-wide keyword checks

    processed_project_names_in_doc = set() # To prevent duplicate projects within the same document

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        # Filter for lines that contain 'emergency' or 'FEMA' keywords
        if not ('emergency' in line_lower or 'fema' in line_lower):
            continue

        # Heuristic to identify a project name line:
        # 1. Starts with a capital letter.
        # 2. Is of reasonable length (more than 5 characters).
        # 3. Contains at least one of the defined project name indicators.
        is_potential_project_name = False
        if re.match(r'^[A-Z][a-zA-Z0-9\s&,-_.]+', stripped_line) and len(stripped_line) > 5: 
            if any(indicator.lower() in line_lower for indicator in project_name_indicators):
                # Check for a (cid:190) marker in the next few lines to confirm it's a structured project detail block
                for j in range(1, min(5, len(lines) - i)):
                    if "(cid:190)" in lines[i+j]:
                        is_potential_project_name = True
                        break
        
        if is_potential_project_name:
            project_name = stripped_line.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
            project_name_lower = project_name.lower()

            if project_name in processed_project_names_in_doc:
                continue
            processed_project_names_in_doc.add(project_name)

            # Create a larger context window around the project name for detailed keyword extraction
            context_start = max(0, i - 10) # 10 lines before
            context_end = min(len(lines), i + 20) # 20 lines after
            project_context_text = " ".join(lines[context_start:context_end]).lower()

            topics = []
            status = 'N/A'
            project_type = 'N/A'

            # Extract topic
            if 'emergency' in project_context_text: topics.append('emergency')
            if 'fema' in project_context_text: topics.append('FEMA')
            if 'emergency warning' in project_context_text: topics.append('emergency warning')
            if '(fema project)' in project_name_lower: topics.append('FEMA')
            if 'homeland security' in project_context_text: topics.append('homeland security')
            if 'disaster' in project_context_text: topics.append('disaster')
            if not topics: topics.append('N/A') # Ensure at least one topic is assigned
            
            # Extract status
            if 'completed' in project_context_text or 'completion filed' in project_context_text: status = 'completed'
            elif 'construction' in project_context_text or 'under construction' in project_context_text: status = 'construction'
            elif 'design' in project_context_text or 'preliminary design' in project_context_text: status = 'design'
            elif 'not started' in project_context_text: status = 'not started'
            elif 'delayed' in project_context_text: status = 'delayed'

            # Extract type
            if 'capital improvement projects' in project_context_text: project_type = 'capital'
            elif 'disaster recovery projects' in project_context_text: project_type = 'disaster'
            
            project_details_extracted.append({
                'Project_Name': project_name,
                'topic': topics,
                'type': project_type,
                'status': status,
            })

# Final deduplication across all documents based on Project_Name
unique_projects_final = []
seen_project_names_global = set()
for project in project_details_extracted:
    if project['Project_Name'] not in seen_project_names_global:
        unique_projects_final.append(project)
        seen_project_names_global.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects_final, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
