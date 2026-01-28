code = """import json

# Load the data files
funding_json_path = var_functions.query_db:68
civic_json_path = var_functions.query_db:5

with open(funding_json_path) as f:
    funding_records = json.load(f)

with open(civic_json_path) as f:
    civic_documents = json.load(f)

# Extract project names from civic docs that are capital design projects
candidate_names = []

for document in civic_documents:
    if 'text' in document:
        text_content = document['text']
        
        # Look for capital design projects section
        if 'Capital Improvement Projects' in text_content and 'Design' in text_content:
            lines = text_content.split('\n')
            for line in lines:
                line = line.strip()
                # Basic filtering for project name lines
                if line and 8 < len(line) < 60:
                    lower_line = line.lower()
                    # Skip metadata lines
                    if 'updates' not in lower_line and 'schedule' not in lower_line:
                        # Look for infrastructure keywords
                        if 'road' in lower_line or 'park' in lower_line or 'canyon' in lower_line or 'storm' in lower_line:
                            candidate_names.append(line)

# Remove duplicate project names
unique_candidates = []
seen = set()
for name in candidate_names:
    if name not in seen:
        seen.add(name)
        unique_candidates.append(name)

# Count matching projects with funding > 50000
matched_count = 0

for project_name in unique_candidates:
    # Normalize project name for comparison
    proj_normalized = ''.join(c for c in project_name.lower() if c.isalnum())
    
    for funding_rec in funding_records:
        amount = int(funding_rec['Amount'])
        if amount > 50000:
            fund_name = funding_rec['Project_Name']
            # Normalize funding project name
            fund_normalized = ''.join(c for c in fund_name.lower() if c.isalnum())
            
            # Check if project names match (one contains the other)
            if proj_normalized in fund_normalized or fund_normalized in proj_normalized:
                if len(proj_normalized) > 8:  # Avoid trivial matches
                    matched_count += 1
                    break

print('__RESULT__:')
print(json.dumps({'count': matched_count}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:48': ['civic_docs'], 'var_functions.query_db:68': 'file_storage/functions.query_db:68.json'}

exec(code, env_args)
