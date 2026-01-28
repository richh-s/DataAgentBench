code = """import json
import re

# Load the civic docs data
civic_docs_path = locals()['var_functions.query_db:2']
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project patterns in the text
    # Projects are often listed with names and details
    lines = text.split('\n')
    
    current_project = None
    
    for line in lines:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
            
        # Look for project names (often bolded or standalone)
        # Patterns that suggest project names:
        # - Lines ending without punctuation
        # - Lines that are followed by status indicators
        # - Lines with project-like names
        
        # Check if this line looks like a project name
        if (len(line) < 200 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and
            not line.startswith('Page') and
            'Updates:' not in line and
            'Schedule:' not in line and
            'Project Description:' not in line):
            
            # Look for common project name patterns
            project_patterns = [
                r'^[A-Z][A-Za-z\s&/-]+(Project|Improvements|Repairs|Replacement|Program|Study|System)$',
                r'^[A-Z][A-Za-z\s&/-]+Drain(age)?',
                r'^[A-Z][A-Za-z\s&/-]+Road',
                r'^[A-Z][A-Za-z\s&/-]+Park',
                r'^[A-Z][A-Za-z\s&/-]+Bridge',
                r'^[A-Z][A-Za-z\s&/-]+Warning'
            ]
            
            for pattern in project_patterns:
                if re.match(pattern, line):
                    current_project = line
                    projects.append({
                        'Project_Name': line,
                        'doc_filename': doc.get('filename', ''),
                        'text_excerpt': text[max(0, text.find(line)-100):text.find(line)+200]
                    })
                    break

print("__RESULT__:")
print(json.dumps({
    "extracted_projects_count": len(projects),
    "sample_projects": projects[:10]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:4': 'file_storage/functions.execute_python:4.json'}

exec(code, env_args)
