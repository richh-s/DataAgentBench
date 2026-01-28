code = """import json
import re

# Load the full JSON result from the file
file_path = locals()['var_function-call-12540492671589378295']
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

project_data = []

project_name_indicators = ["Project", "Improvements", "Plan", "Study", "Repairs", "System", "Road", "Drain", "Wall"]

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    text_lower = text.lower() # For document-wide keyword search

    for i, line in enumerate(lines):
        stripped_line = line.strip()
        # Look for lines that could be project names: start with uppercase, contain an indicator word, not too short
        # Also checking for specific project related phrases from the document analysis.
        if re.match(r'^[A-Z].{4,}', stripped_line) and any(ind.lower() in stripped_line.lower() for ind in project_name_indicators):
            project_name = stripped_line.replace('\ufffd', '').replace('\u2019', "'").replace('\u201c', '\"').replace('\u201d', '\"').replace('\u2013', '-')
            
            # Check for unique project names to avoid duplicates from multiple document mentions
            if project_name not in [p['Project_Name'] for p in project_data]:
                # Extract topic (checking against the entire document text and project name)
                topics = []
                if 'emergency' in text_lower or 'emergency' in project_name.lower():
                    topics.append('emergency')
                if 'fema' in text_lower or 'fema' in project_name.lower():
                    topics.append('FEMA')
                if 'emergency warning' in text_lower:
                    topics.append('emergency warning')
                if '(fema project)' in project_name.lower():
                    topics.append('FEMA')
                if 'homeland security' in text_lower:
                    topics.append('homeland security')
                if 'disaster' in text_lower or 'disaster' in project_name.lower():
                    topics.append('disaster')
                if not topics:
                    topics.append('N/A')
                    
                # Extract status (checking against the entire document text)
                status = 'N/A'
                if 'completed' in text_lower or 'completion filed' in text_lower:
                    status = 'completed'
                elif 'construction' in text_lower or 'under construction' in text_lower:
                    status = 'construction'
                elif 'design' in text_lower or 'preliminary design' in text_lower:
                    status = 'design'
                elif 'not started' in text_lower:
                    status = 'not started'
                elif 'delayed' in text_lower:
                    status = 'delayed'
                    
                # Extract type (checking against the entire document text)
                project_type = 'N/A'
                if 'capital improvement projects' in text_lower:
                    project_type = 'capital'
                elif 'disaster recovery projects' in text_lower:
                    project_type = 'disaster'
                
                # Filter for projects related to 'emergency' or 'FEMA'
                # This filter is already applied by the initial MongoDB query.
                # However, we re-check for robustness and to align with the prompt's request.
                if any(keyword in project_name.lower() or keyword in text_lower for keyword in ['emergency', 'fema']):
                    project_data.append({
                        'Project_Name': project_name,
                        'topic': topics,
                        'type': project_type,
                        'status': status,
                    })

# Remove duplicates (already handled by checking before appending, but good for final sanity)
final_unique_projects = []
seen_project_names = set()
for project in project_data:
    if project['Project_Name'] not in seen_project_names:
        final_unique_projects.append(project)
        seen_project_names.add(project['Project_Name'])

print("__RESULT__:")
print(json.dumps(final_unique_projects))"""

env_args = {'var_function-call-12540492671589378295': 'file_storage/function-call-12540492671589378295.json'}

exec(code, env_args)
