code = """import json
import re
# Access the file path directly 
file_path = 'civic_docs_query_result.json'

# Initialize an empty list for the documents
all_documents = []

# Try multiple approaches to load the data
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Try to parse as JSON
        if content.strip().startswith('['):
            all_documents = json.loads(content)
        else:
            print("Content is not a JSON array")
except Exception as e:
    print(f"Error loading file: {e}")

print(f"Total documents retrieved: {len(all_documents)}")

# Initialize list to store extracted project information  
park_projects = []

for doc in all_documents:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Split text into blocks
    project_blocks = re.split(r'\n\s*\n', text)
    
    for block in project_blocks:
        # Check if block mentions park
        if re.search(r'park', block, re.IGNORECASE):
            # Check if block mentions completion or dates
            if re.search(r'completed|2022|construction', block, re.IGNORECASE):
                # Extract project name
                lines = block.strip().split('\n')
                if lines:
                    project_name = lines[0].strip()
                    
                    # Filter out heading lines
                    skip_patterns = ['Public Works', 'Commission', 'Agenda', 'Meeting', 'Item', 'To:', 'Prepared by', 'Approved by', 'Date', 'Subject', 'RECOMMENDED', 'DISCUSSION']
                    should_skip = any(pattern in project_name for pattern in skip_patterns)
                    
                    if (project_name and not should_skip and len(project_name) < 200):
                        # Check for 2022 completion
                        completion_patterns = [
                            r'completed.*?(2022|Nov|Nov\.|Novemb|Dec|Dec\.|Decemb)',
                            r'construction was completed[^.]*2022',
                            r'notice of completion[^.]*2022'
                        ]
                        
                        is_completed_2022 = False
                        for pattern in completion_patterns:
                            if re.search(pattern, block, re.IGNORECASE | re.DOTALL):
                                is_completed_2022 = True
                                break
                        
                        if is_completed_2022:
                            status = "completed"
                            
                            # Extract date info
                            date_match = re.search(r'(2022|Nov\w*|Dec\w*)[^\n]*', block, re.IGNORECASE)
                            date_str = date_match.group() if date_match else ""
                            
                            project_info = {
                                'project_name': project_name,
                                'status': status,
                                'completion_date': date_str,
                                'topic': 'park'
                            }
                            park_projects.append(project_info)

result_data = park_projects
print('__RESULT__:') 
print(json.dumps(result_data))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
