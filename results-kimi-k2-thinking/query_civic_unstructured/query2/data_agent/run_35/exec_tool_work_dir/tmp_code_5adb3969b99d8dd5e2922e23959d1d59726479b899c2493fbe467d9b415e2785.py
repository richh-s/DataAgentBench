code = """import json

# Read civic documents and extract park projects completed in 2022
civic_docs_file = locals()['var_functions.query_db:2']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Find projects with 'park' in name and completion in 2022
park_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # First check if the document mentions both park projects and 2022 completion
    if 'park' in text_lower and 'construction was completed' in text_lower and '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line_clean = line.strip()
            # Find park-related project names
            if 'park' in line_clean.lower() and len(line_clean) > 5 and len(line_clean) < 100:
                # Skip headers and status lines
                if 'Project Schedule' in line_clean or 'Updates' in line_clean:
                    continue
                
                # Check following lines for 2022 completion
                for j in range(i, min(i + 10, len(lines))):
                    next_line = lines[j]
                    if 'Construction was completed' in next_line and '2022' in next_line:
                        # Avoid duplicates
                        if line_clean not in [p['name'] for p in park_projects_2022]:
                            park_projects_2022.append({'name': line_clean})
                        break

print('__RESULT__:')
print(json.dumps({
    'projects': park_projects_2022,
    'count': len(park_projects_2022)
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'num_docs': 5, 'first_doc': {'filename': 'malibucity_agenda_03222023-2060.txt', 'text_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E'}}}

exec(code, env_args)
