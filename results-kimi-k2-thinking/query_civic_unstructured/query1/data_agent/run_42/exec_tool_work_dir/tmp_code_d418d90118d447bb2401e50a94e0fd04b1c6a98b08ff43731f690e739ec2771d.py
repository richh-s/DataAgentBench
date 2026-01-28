code = """import json
import re

# Access the stored result from the MongoDB query
mongo_result = var_functions.query_db_2

# Check if it's a file path (string) or the actual data (list)
if isinstance(mongo_result, str):
    with open(mongo_result, 'r') as f:
        civic_docs_data = json.load(f)
else:
    civic_docs_data = mongo_result

print(f"Number of documents: {len(civic_docs_data)}")

# Extract projects with status='design' from the text
projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Improved extraction logic
    lines = text.split('\n')
    in_design_section = False
    
    for line in lines:
        clean_line = line.strip()
        
        # Look for design section header
        if 'Capital Improvement Projects (Design)' in clean_line:
            in_design_section = True
            continue
        
        # Look for end of design section
        if in_design_section and ('Capital Improvement Projects (Construction)' in clean_line or 
                                 'Capital Improvement Projects (Not Started)' in clean_line):
            in_design_section = False
            continue
        
        if in_design_section:
            # Check if this is a project name line (not empty, not bullet, doesn't contain common keywords)
            if (clean_line and not clean_line.startswith('(') and not clean_line.startswith('•') 
                and 'Updates:' not in clean_line and 'Project Schedule:' not in clean_line 
                and 'Estimated Schedule:' not in clean_line and 'Complete Design:' not in clean_line
                and 'Advertise:' not in clean_line and 'Begin Construction:' not in clean_line
                and not clean_line.startswith('To:') and not clean_line.startswith('Subject:')
                and len(clean_line) > 5 and clean_line != 'RECOMMENDED ACTION:'
                and 'DISCUSSION:' not in clean_line and 'Page' not in clean_line
                and 'Agenda Item' not in clean_line and 'Prepared by:' not in clean_line
                and 'Approved by:' not in clean_line and 'Date prepared:' not in clean_line
                and not all(word.isupper() for word in clean_line.split()[:3] if word)):
                
                # This appears to be a project name
                project_name = clean_line.strip('•- ')
                
                # Skip if it looks like a status or schedule update
                if not any(keyword in project_name for keyword in 
                          ['Consultant', 'Staff', 'City', 'Project is', 'Plans', 'Bids', 'Construction']):
                    
                    projects.append({
                        'project_name': project_name,
                        'status': 'design',
                        'type': 'capital',
                        'source_doc': filename
                    })
                    #print(f"Debug: Found project: {project_name}")

print(f"Total design projects extracted: {len(projects)}")
for i, proj in enumerate(projects[:15]):
    print(f"  {i+1}. {proj['project_name']}")

__RESULT__:
print(json.dumps(projects))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
