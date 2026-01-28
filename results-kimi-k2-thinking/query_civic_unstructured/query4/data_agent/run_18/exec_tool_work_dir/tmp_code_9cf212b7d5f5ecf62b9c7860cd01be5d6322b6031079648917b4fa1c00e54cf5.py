code = """import json
import re

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:11']
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project names from civic documents containing 2022
project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        # Look for lines that contain project information
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and obvious non-project lines
            if not line or len(line) < 10:
                continue
            if any(skip in line.lower() for skip in ['chair', 'commission', 'prepared by', 'approved by', 'subject:', 'discussion:', 'page ']):
                continue
                
            # Look for capitalized phrases that might be project names
            # Pattern: Starts with capital letter, has multiple words, ends with common project terms
            project_patterns = [
                r'([A-Z][a-zA-Z\s]+?(?:Road|Street|Avenue|Drive|Park|Beach|Canyon|Highway|Project|Improvements|Repairs|Maintenance|Drainage|Storm|Water|Treatment|Facility|Structure|Signs|Sirens|Lights|Bridge|Culvert|Retaining Wall|Signal|System|Study|Program))',
            ]
            
            for pattern in project_patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    project_name = match.strip()
                    if (len(project_name) > 10 and 
                        not any(word in project_name.lower() for word in ['update', 'schedule', 'design', 'construction', 'council', 'commission']) and
                        project_name.count(' ') >= 1):
                        project_names.add(project_name)

# Clean up project names
clean_projects = []
for name in project_names:
    # Remove common suffixes and prefixes that aren't part of the actual name
    clean_name = name.split(' (')[0]  # Remove parenthetical content
    clean_name = clean_name.split('\n')[0]  # Remove newlines
    clean_name = clean_name.strip()
    if len(clean_name) > 10 and not clean_name.isupper():
        clean_projects.append(clean_name)

print('__RESULT__:')
print(json.dumps({
    'projects_found': len(clean_projects),
    'sample_projects': list(clean_projects)[:20]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
