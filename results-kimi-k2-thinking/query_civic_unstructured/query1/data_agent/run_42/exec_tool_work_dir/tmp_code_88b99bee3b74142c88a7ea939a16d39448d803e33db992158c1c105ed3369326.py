code = """import re
import json

# Read the MongoDB results from the file stored in the previous query result
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    civic_docs_data = json.load(f)

# Print a sample of the data to debug
print("Number of documents:", len(civic_docs_data))

# Extract projects from the documents
projects_info = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Find sections containing project information
    # Look for pattern: Capital Improvement Projects (Design)
    lines = text.split('\n')
    in_design_section = False
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for section headers
        if 'Capital Improvement Projects (Design)' in line:
            in_design_section = True
            continue
            
        if in_design_section:
            # Check if we hit another section like (Construction) or (Not Started)
            if 'Capital Improvement Projects (Construction)' in line or 'Capital Improvement Projects (Not Started)' in line:
                in_design_section = False
                current_project = None
                continue
            
            # Look for project names (they typically appear as standalone lines, often with project names)
            # Skip empty lines, continuation markers, and status/update lines
            if line and not line.startswith('(') and not line.startswith('•') and 'Updates:' not in line and 'Project Schedule:' not in line and 'Estimated Schedule:' not in line:
                # Check if it's a project name (not a status/update line)
                # Project names often don't start with these keywords
                skip_patterns = ['Updates:', 'Project Schedule:', 'Estimated Schedule:', 'Complete Design:', 'Advertise:', 'Begin Construction:', 'Project is', 'Staff is', 'City is', 'Consultant', 'Plans are', 'Awards', 'Bids', 'Construction', 'Notice', 'Scheduled', 'Project Description', 'To:', 'From:', 'Subject:', 'Prepared by:', 'Approved by:', 'Date prepared', 'Meeting date:', 'RECOMMENDED ACTION', 'DISCUSSION', 'Page', 'Agenda Item', 'Public Works', 'Commission Meeting']
                
                should_skip = False
                for pattern in skip_patterns:
                    if pattern in line:
                        should_skip = True
                        break
                
                if not should_skip and len(line) > 5 and not line.isupper():  # Skip all-caps headers
                    # This looks like a project name
                    current_project = line
                    # Clean up project name
                    project_name = line.strip('• ').strip()
                    projects_info.append({
                        'project_name': project_name,
                        'status': 'design',
                        'type': 'capital',
                        'source_file': filename
                    })

print("Extracted projects (sample):")
for proj in projects_info[:10]:
    print(f"  - {proj['project_name']}")

print(f"\nTotal extracted projects with status='design': {len(projects_info)}")

__RESULT__:
print(json.dumps(projects_info[:20]))  # Return first 20 as JSON"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
