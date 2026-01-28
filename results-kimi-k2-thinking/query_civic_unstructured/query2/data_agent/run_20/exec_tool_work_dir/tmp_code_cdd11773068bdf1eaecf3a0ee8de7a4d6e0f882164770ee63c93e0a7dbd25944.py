code = """import json
import re

# Load data from files
civic_docs_file = open(locals()['var_functions.query_db:2'], 'r')
civic_docs = json.load(civic_docs_file)
civic_docs_file.close()

funding_file = open(locals()['var_functions.query_db:5'], 'r')
funding_records = json.load(funding_file)
funding_file.close()

# Create funding lookup dictionary
funding_dict = {}
for record in funding_records:
    project_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    funding_dict[project_name] = amount

# Find park projects completed in 2022
park_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check document contains relevant keywords
    if 'park' in lower_text and 'completed' in lower_text and '2022' in lower_text:
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            lower_line = line.lower()
            
            # Identify park project names
            if 'park' in lower_line and len(line) > 10:
                # Skip non-project lines
                skip_terms = ['status:', 'updates:', 'schedule:', 'project description:', 'page', 'completed']
                should_skip = False
                for term in skip_terms:
                    if term in lower_line:
                        should_skip = True
                        break
                if should_skip:
                    continue
                if line.startswith('(') or line.startswith('•'):
                    continue
                
                # Check surrounding context for completion in 2022
                context_start = max(0, i-2)
                context_end = min(len(lines), i+6)
                context_text = ' '.join(lines[context_start:context_end]).lower()
                
                if 'completed' in context_text and '2022' in context_text:
                    park_projects.append(line)

# Remove duplicates
unique_park_projects = []
seen = set()
for proj in park_projects:
    if proj not in seen:
        seen.add(proj)
        unique_park_projects.append(proj)

result_data = {
    'projects': unique_park_projects,
    'count': len(unique_park_projects)
}
print('__RESULT__:')
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
