code = """import json, re

# Access the stored result (likely a preview string)
preview_data = locals().get('var_functions.query_db:2', '')

# Try to extract JSON records from the preview
# The preview shows it starts with [{...}] format
if preview_data:
    print('Got preview data, type:', type(preview_data))
    if isinstance(preview_data, list):
        print('Already have list with', len(preview_data), 'documents')
        civic_docs = preview_data
    elif isinstance(preview_data, str):
        print('Preview is string length:', len(preview_data))
        # Try to parse if it's JSON
        try:
            civic_docs = json.loads(preview_data)
            print('Parsed JSON list with', len(civic_docs), 'documents')
        except:
            print('Could not parse as JSON directly')
            # The preview shows a Python-like list of dicts
            civic_docs = eval(preview_data)
            print('Evaluated to', len(civic_docs), 'documents')
else:
    print('No preview data available')

# Now process the documents to extract project info
if 'civic_docs' in locals() and civic_docs:
    all_projects = []
    
    for doc in civic_docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        # Look for project sections - projects are listed with bullet points or headers
        # Pattern to find project names and their details
        
        # Find sections that look like projects
        # Projects often appear after clear line breaks or headers
        lines = text.split('\n')
        
        current_project = None
        project_details = {}
        
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip empty lines
            if not line:
                continue
                
            # Look for project name patterns (often title case, no bullet)
            # Projects like "2022 Morning View Resurfacing & Storm Drain Improvements"
            if (len(line) > 10 and 
                not line.startswith('(') and 
                not line.startswith('cid:') and
                not line.startswith('Page') and
                not 'RECOMMENDED ACTION' in line and
                not 'DISCUSSION' in line and
                not 'Prepared by' in line and
                not 'Approved by' in line and
                not 'Subject' in line and
                not 'To:' in line and
                not 'Meeting date' in line):
                
                # This might be a project name
                if i > 0 and lines[i-1].strip() == '' or 'Project' in lines[i-1]:
                    # Found a new project
                    if current_project:
                        all_projects.append(project_details)
                    
                    current_project = line
                    project_details = {
                        'Project_Name': line,
                        'filename': filename
                    }
                    
                    # Look for dates in the project description
                    if '2022' in line:
                        project_details['st'] = '2022'
                    if '2023' in line:
                        project_details['et'] = '2023'
        
        # Add last project
        if current_project:
            all_projects.append(project_details)
    
    print('Extracted', len(all_projects), 'potential projects')
    
    # Filter for Spring 2022 projects
    spring_2022_projects = []
    for proj in all_projects:
        # Look for 2022 in project name or details
        project_name = proj.get('Project_Name', '').lower()
        if '2022' in project_name or proj.get('st') == '2022':
            # Check if it's spring (March-May)
            # Many projects use format like "2022 Morning View..."
            spring_2022_projects.append(proj)
    
    print('Found', len(spring_2022_projects), 'projects from 2022')
    
    result = {
        'status': 'success',
        'total_projects': len(all_projects),
        'spring_2022_projects': len(spring_2022_projects),
        'projects': spring_2022_projects[:10]  # First 10
    }
else:
    result = {'status': 'no_data'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}}

exec(code, env_args)
