code = """import json
import re

# Load civic documents
civic_docs_file = locals()['var_functions.query_db:11']
civic_docs = []
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load funding data  
funding_file = locals()['var_functions.query_db:12']
funding_data = []
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Extract project information from civic documents
projects_info = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern to match project sections - looking for lines that contain project names and dates
    # Spring 2022 pattern - looking for projects starting in Spring 2022
    spring_patterns = [
        r'(\d{4}.*?Spring\s+2022)',
        r'(Spring\s+2022.*)',
        r'(\d{4}.*?\b2022\b.*?(?:Spring|Mar|Apr|May))',
        r'(?:Mar|Apr|May)\s+2022'
    ]
    
    if '2022' in text:
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for patterns that suggest project names and Spring 2022
            if any(keyword in line for keyword in ['2022', 'Spring']):
                # Try to extract project names from the line
                # Look for capitalized phrases that look like project names
                project_patterns = [
                    r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+(?:Road|Street|Avenue|Drive|Park|Beach|Canyon|Highway)).*?)(?=\s+\(|\s+[\u2022\u00b7\-]|$)',
                    r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+(?:Project|Improvements|Repairs|Maintenance))',
                    r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*(?:\s+(?: drainage| storm| treatment| water| quality| safety| signal)).*?)(?=\s+\(|\s+[\u2022\u00b7\-]|$)'
                ]
                
                for pattern in project_patterns:
                    matches = re.findall(pattern, line)
                    for match in matches:
                        project_name = match.strip()
                        if (len(project_name) > 5 and 
                            not any(word in project_name.lower() for word in ['update', 'schedule', 'design', 'construction', 'council']) and
                            '2022' in line):
                            projects_info.append({
                                'project_name': project_name,
                                'source_line': line,
                                'filename': doc['filename']
                            })

print('__RESULT__:')
print(json.dumps({
    'projects_extracted': len(projects_info),
    'sample_projects': projects_info[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
