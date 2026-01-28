code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Keywords to help identify project names more accurately
project_name_keywords = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power", "Treatment", "Signs", "Emergency", "FEMA", "Recovery"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower() # For document-wide keyword search

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        # Heuristic to identify a project name: Starts with a capital letter, is not too short, and contains a project keyword.
        # Also, it should be followed by a line containing a (cid:190) marker and a detail descriptor.
        is_potential_project_name = False
        if re.match(r'^[A-Z][a-zA-Z0-9\s&,-]+', stripped_line) and len(stripped_line) > 5:
            if any(keyword.lower() in line_lower for keyword in project_name_keywords):
                # Check next few lines for the (cid:190) markers to confirm it's a project detail block
                for j in range(1, min(5, len(lines) - i)):
                    next_line = lines[i+j]
                    if "(cid:190)" in next_line and any(marker in next_line.lower() for marker in ["updates:", "project schedule:", "project description:", "estimated schedule:"]):
                        is_potential_project_name = True
                        break
        
        if is_potential_project_name:
            project_name = stripped_line.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
            project_name_lower = project_name.lower()

            # Create a context window around the project name for detailed keyword extraction
            context_start = max(0, i - 5) # 5 lines before
            context_end = min(len(lines), i + 15) # 15 lines after to capture more context
            project_context_text = " ".join(lines[context_start:context_end]).lower()

            # Filter for projects related to 'emergency' or 'FEMA' (redundant check, but safer)
            if not ('emergency' in project_name_lower or 'fema' in project_name_lower or \
                    'emergency' in text_lower or 'fema' in text_lower):
                continue

            topics = []
            status = 'N/A'
            project_type = 'N/A'

            # Extract topic
            if 'emergency' in project_context_text:
                topics.append('emergency')
            if 'fema' in project_context_text:
                topics.append('FEMA')
            if 'emergency warning' in project_context_text:
                topics.append('emergency warning')
            if '(fema project)' in project_name_lower:
                topics.append('FEMA')
            if 'homeland security' in project_context_text:
                topics.append('homeland security')
            if 'disaster' in project_context_text:
                topics.append('disaster')
            if not topics and ('emergency' in text_lower or 'fema' in text_lower): # Fallback to document level for topics
                if 'emergency' in text_lower and 'emergency' not in topics: topics.append('emergency')
                if 'fema' in text_lower and 'FEMA' not in topics: topics.append('FEMA')
            if not topics: topics.append('N/A') # Ensure at least one topic
            
            # Extract status
            if 'completed' in project_context_text or 'completion filed' in project_context_text:
                status = 'completed'
            elif 'construction' in project_context_text or 'under construction' in project_context_text:
                status = 'construction'
            elif 'design' in project_context_text or 'preliminary design' in project_context_text:
                status = 'design'
            elif 'not started' in project_context_text:
                status = 'not started'
            elif 'delayed' in project_context_text:
                status = 'delayed'
            # Fallback to document-level status if not found in context (from section headers)
            elif 'capital improvement projects (construction)' in text_lower and 'construction' in text_lower:
                 status = 'construction'
            elif 'capital improvement projects (design)' in text_lower and 'design' in text_lower:
                 status = 'design'
            elif 'capital improvement projects (not started)' in text_lower and 'not started' in text_lower:
                 status = 'not started'

            # Extract type
            if 'capital improvement projects' in project_context_text:
                project_type = 'capital'
            elif 'disaster recovery projects' in project_context_text:
                project_type = 'disaster'
            # Fallback to document-level type if not found in context
            elif 'capital improvement projects' in text_lower:
                project_type = 'capital'
            elif 'disaster recovery projects' in text_lower:
                project_type = 'disaster'
            
            project_data.append({
                'Project_Name': project_name,
                'topic': topics,
                'type': project_type,
                'status': status,
            })

# Remove duplicates based on Project_Name
unique_projects = []
seen_project_names = set()
for project in project_data:
    if project['Project_Name'] not in seen_project_names:
        unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
