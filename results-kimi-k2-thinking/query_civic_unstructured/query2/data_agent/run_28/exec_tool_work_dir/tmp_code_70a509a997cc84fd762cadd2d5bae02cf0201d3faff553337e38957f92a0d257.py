code = """import json
import re
from pathlib import Path

# Read the full result from the file
file_path = var_functions.query_db:2
with open(file_path, 'r', encoding='utf-8') as f:
    all_documents = json.load(f)

print(f"Total documents retrieved: {len(all_documents)}")

# Initialize list to store extracted project information
park_projects = []

for doc in all_documents:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Look for project patterns in the text
    # Projects typically follow patterns like:
    # "Project Name" followed by status info
    # Extract sections that mention "park" and have dates
    
    # Find all potential project blocks
    project_blocks = re.split(r'\n\s*\n', text)
    
    for block in project_blocks:
        # Check if block mentions park
        if re.search(r'park', block, re.IGNORECASE):
            # Check if block mentions completion or dates
            if re.search(r'completed|2022|construction', block, re.IGNORECASE):
                # Extract project name (usually first line or bolded text)
                lines = block.strip().split('\n')
                if lines:
                    project_name = lines[0].strip()
                    
                    # Filter out heading lines and meeting info
                    if (project_name and 
                        not re.match(r'(Public Works|Commission|Agenda|Meeting|Item|To:|Prepared by|Approved by|Date|Subject|RECOMMENDED|DISCUSSION)', project_name, re.IGNORECASE) and
                        len(project_name) < 200):  # Reasonable length for project name
                        
                        # Check if this is about a completed project in 2022
                        # Look for completion indicators
                        completion_match = re.search(r'(completed.*?(2022|Nov|Nov\.|November|Dec|Dec\.|December)|construction was completed[^.]*2022|notice of completion[^.]*2022|completed[^.]*November[^.]*2022|completed[^.]*December[^.]*2022)', 
                                                   block, re.IGNORECASE | re.DOTALL)
                        
                        if completion_match:
                            status = "completed"
                            # Extract date info
                            date_info = re.search(r'(2022|Nov\w*|Dec\w*)[^\n]*', block, re.IGNORECASE)
                            date_str = date_info.group() if date_info else ""
                            
                            project_info = {
                                'project_name': project_name,
                                'status': status,
                                'completion_date': date_str,
                                'text_snippet': block[:300],  # First 300 chars for context
                                'topic': 'park'
                            }
                            park_projects.append(project_info)

print(f"Found {len(park_projects)} park-related projects that might be completed in 2022")

# Print the projects found
for i, proj in enumerate(park_projects[:10]):  # Show first 10
    print(f"\n{i+1}. {proj['project_name']}")
    print(f"   Status: {proj['status']}")
    print(f"   Date: {proj['completion_date']}")
    print(f"   Topic: {proj['topic']}")

# Save results for next step
result_data = park_projects
print('__RESULT__:')
print(json.dumps(result_data, default=str))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
