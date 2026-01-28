code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

# Keywords to help identify project names more accurately
project_name_keywords = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall", "Park", "Facility", "Lane", "Signals", "Power", "Treatment", "Signs", "Emergency", "FEMA", "Recovery", "Center", "Slopes"]
project_detail_markers = ["(cid:190) Updates:", "(cid:190) Project Schedule:", "(cid:190) Project Description:", "(cid:190) Estimated Schedule:"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower() # For document-wide keyword search as a fallback

    processed_project_names_in_doc = set() # To store unique project names processed within this document

    # Iterate through lines to identify project names and their associated details
    current_project_name = None
    current_project_context = []

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        line_lower = stripped_line.lower()

        # Check if the line is a potential project name
        # Conditions: starts with a capital, reasonable length, contains a keyword, and followed by a detail marker
        is_potential_project_name_line = False
        if re.match(r'^[A-Z][a-zA-Z0-9\s&,-]+', stripped_line) and len(stripped_line) > 5:
            if any(keyword.lower() in line_lower for keyword in project_name_keywords):
                for j in range(1, min(5, len(lines) - i)):
                    next_line = lines[i+j]
                    if any(marker in next_line for marker in project_detail_markers):
                        is_potential_project_name_line = True
                        break
        
        if is_potential_project_name_line:
            # If we found a new project, process the previous one if it exists
            if current_project_name and current_project_name not in processed_project_names_in_doc:
                full_project_context_text = " ".join(current_project_context).lower()
                project_name_for_processing = current_project_name.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
                project_name_for_processing_lower = project_name_for_processing.lower()

                # Filter for projects related to 'emergency' or 'FEMA'
                if 'emergency' in project_name_for_processing_lower or 'fema' in project_name_for_processing_lower or \
                   'emergency' in full_project_context_text or 'fema' in full_project_context_text:
                    
                    topics = []
                    status = 'N/A'
                    project_type = 'N/A'

                    if 'emergency' in full_project_context_text: topics.append('emergency')
                    if 'fema' in full_project_context_text: topics.append('FEMA')
                    if 'emergency warning' in full_project_context_text: topics.append('emergency warning')
                    if '(fema project)' in project_name_for_processing_lower: topics.append('FEMA')
                    if 'homeland security' in full_project_context_text: topics.append('homeland security')
                    if 'disaster' in full_project_context_text: topics.append('disaster')
                    if not topics: 
                        if 'emergency' in text_lower: topics.append('emergency')
                        if 'fema' in text_lower: topics.append('FEMA')
                    if not topics: topics.append('N/A')
                    
                    if 'completed' in full_project_context_text or 'completion filed' in full_project_context_text: status = 'completed'
                    elif 'construction' in full_project_context_text or 'under construction' in full_project_context_text: status = 'construction'
                    elif 'design' in full_project_context_text or 'preliminary design' in full_project_context_text: status = 'design'
                    elif 'not started' in full_project_context_text: status = 'not started'
                    elif 'delayed' in full_project_context_text: status = 'delayed'
                    elif 'capital improvement projects (construction)' in text_lower: status = 'construction'
                    elif 'capital improvement projects (design)' in text_lower: status = 'design'
                    elif 'capital improvement projects (not started)' in text_lower: status = 'not started'

                    if 'capital improvement projects' in full_project_context_text: project_type = 'capital'
                    elif 'disaster recovery projects' in full_project_context_text: project_type = 'disaster'
                    elif 'capital improvement projects' in text_lower: project_type = 'capital'
                    elif 'disaster recovery projects' in text_lower: project_type = 'disaster'
                    
                    project_data.append({
                        'Project_Name': project_name_for_processing,
                        'topic': topics,
                        'type': project_type,
                        'status': status,
                    })
                    processed_project_names_in_doc.add(current_project_name)

            # Start a new project
            current_project_name = stripped_line
            current_project_context = [stripped_line]
        elif current_project_name: # If we are inside a project block, add lines to its context
            current_project_context.append(stripped_line)

    # After the loop, process the last project if any
    if current_project_name and current_project_name not in processed_project_names_in_doc:
        full_project_context_text = " ".join(current_project_context).lower()
        project_name_for_processing = current_project_name.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
        project_name_for_processing_lower = project_name_for_processing.lower()

        if 'emergency' in project_name_for_processing_lower or 'fema' in project_name_for_processing_lower or \
           'emergency' in full_project_context_text or 'fema' in full_project_context_text:
            
            topics = []
            status = 'N/A'
            project_type = 'N/A'

            if 'emergency' in full_project_context_text: topics.append('emergency')
            if 'fema' in full_project_context_text: topics.append('FEMA')
            if 'emergency warning' in full_project_context_text: topics.append('emergency warning')
            if '(fema project)' in project_name_for_processing_lower: topics.append('FEMA')
            if 'homeland security' in full_project_context_text: topics.append('homeland security')
            if 'disaster' in full_project_context_text: topics.append('disaster')
            if not topics: 
                if 'emergency' in text_lower: topics.append('emergency')
                if 'fema' in text_lower: topics.append('FEMA')
            if not topics: topics.append('N/A')
            
            if 'completed' in full_project_context_text or 'completion filed' in full_project_context_text: status = 'completed'
            elif 'construction' in full_project_context_text or 'under construction' in full_project_context_text: status = 'construction'
            elif 'design' in full_project_context_text or 'preliminary design' in full_project_context_text: status = 'design'
            elif 'not started' in full_project_context_text: status = 'not started'
            elif 'delayed' in full_project_context_text: status = 'delayed'
            elif 'capital improvement projects (construction)' in text_lower: status = 'construction'
            elif 'capital improvement projects (design)' in text_lower: status = 'design'
            elif 'capital improvement projects (not started)' in text_lower: status = 'not started'

            if 'capital improvement projects' in full_project_context_text: project_type = 'capital'
            elif 'disaster recovery projects' in full_project_context_text: project_type = 'disaster'
            elif 'capital improvement projects' in text_lower: project_type = 'capital'
            elif 'disaster recovery projects' in text_lower: project_type = 'disaster'
            
            project_data.append({
                'Project_Name': project_name_for_processing,
                'topic': topics,
                'type': project_type,
                'status': status,
            })

# Final deduplication across all documents based on Project_Name
unique_projects_final = []
seen_project_names_global = set()
for project in project_data:
    if project['Project_Name'] not in seen_project_names_global:
        unique_projects_final.append(project)
        seen_project_names_global.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(unique_projects_final, ensure_ascii=False))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
