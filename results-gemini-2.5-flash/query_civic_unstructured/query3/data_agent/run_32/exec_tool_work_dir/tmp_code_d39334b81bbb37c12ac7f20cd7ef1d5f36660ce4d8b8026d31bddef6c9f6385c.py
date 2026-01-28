code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_details = []

# Keywords to help identify project names more accurately
project_name_keywords = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power", "Treatment", "Signs", "Emergency", "FEMA", "Recovery", "Center", "Slopes"]
project_detail_markers = ["(cid:190) Updates:", "(cid:190) Project Schedule:", "(cid:190) Project Description:", "(cid:190) Estimated Schedule:"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower() # For document-wide keyword search as a fallback

    processed_project_names_in_doc = set() # To store unique project names processed within this document

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        is_potential_project_name = False
        # Heuristic: Line starts with a capital letter and is of reasonable length.
        # Simplified regex for project name to avoid syntax issues. Rely more on keywords and markers.
        if re.match(r'^[A-Z].{4,}', stripped_line) and len(stripped_line) > 5: 
            if any(keyword.lower() in line_lower for keyword in project_name_keywords):
                # Check next few lines for the (cid:190) markers to confirm it's a project detail block
                for j in range(1, min(5, len(lines) - i)):
                    next_line = lines[i+j]
                    if any(marker in next_line for marker in project_detail_markers): 
                        is_potential_project_name = True
                        break
        
        if is_potential_project_name:
            project_name = stripped_line.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
            project_name_lower = project_name.lower()

            # Skip if this project name has already been processed in this document
            if project_name in processed_project_names_in_doc:
                continue

            # Create a context window around the project name for more accurate keyword extraction
            context_start = max(0, i - 5) # 5 lines before
            context_end = min(len(lines), i + 15) # 15 lines after to capture details
            project_context_text = " ".join(lines[context_start:context_end]).lower()

            # Filter for projects related to 'emergency' or 'FEMA' (critical filter)
            if not ('emergency' in project_name_lower or 'fema' in project_name_lower or \
                    'emergency' in project_context_text or 'fema' in project_context_text):
                continue

            # Add the project name to the set of processed names for this document
            processed_project_names_in_doc.add(project_name)

            topics = []
            status = 'N/A'
            project_type = 'N/A'

            # Extract topic
            if 'emergency' in project_context_text: topics.append('emergency')
            if 'fema' in project_context_text: topics.append('FEMA')
            if 'emergency warning' in project_context_text: topics.append('emergency warning')
            if '(fema project)' in project_name_lower: topics.append('FEMA') # specific suffix
            if 'homeland security' in project_context_text: topics.append('homeland security')
            if 'disaster' in project_context_text: topics.append('disaster')
            
            # Fallback to document-wide topics if not found in context
            if not topics: 
                if 'emergency' in text_lower: topics.append('emergency')
                if 'fema' in text_lower: topics.append('FEMA')
            if not topics: topics.append('N/A') # Ensure at least one topic is assigned
            
            # Extract status
            if 'completed' in project_context_text or 'completion filed' in project_context_text: status = 'completed'
            elif 'construction' in project_context_text or 'under construction' in project_context_text: status = 'construction'
            elif 'design' in project_context_text or 'preliminary design' in project_context_text: status = 'design'
            elif 'not started' in project_context_text: status = 'not started'
            elif 'delayed' in project_context_text: status = 'delayed'
            # Fallback to document-level status if not found in context (e.g., from section headers in the full text)
            elif 'capital improvement projects (construction)' in text_lower: status = 'construction'
            elif 'capital improvement projects (design)' in text_lower: status = 'design'
            elif 'capital improvement projects (not started)' in text_lower: status = 'not started'

            # Extract type
            if 'capital improvement projects' in project_context_text: project_type = 'capital'
            elif 'disaster recovery projects' in project_context_text: project_type = 'disaster'
            # Fallback to document-level type if not found in context
            elif 'capital improvement projects' in text_lower: project_type = 'capital'
            elif 'disaster recovery projects' in text_lower: project_type = 'disaster'
            
            project_details.append({
                'Project_Name': project_name,
                'topic': topics,
                'type': project_type,
                'status': status,
            })

# Final deduplication across all documents based on Project_Name
unique_projects_final = []
seen_project_names_global = set()
for project in project_details:
    if project['Project_Name'] not in seen_project_names_global:
        unique_projects_final.append(project)
        seen_project_names_global.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects_final, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
