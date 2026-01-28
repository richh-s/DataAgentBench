code = """import json
import re

# Load the paper data
paper_data_path = locals()['var_functions.query_db:14']

with open(paper_data_path, 'r') as f:
    all_papers = json.load(f)

print('Total papers loaded:', len(all_papers))

# Find papers from 2016 in physical activity domain
papers_2016_pa = []

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if contains physical activity and year 2016
    has_physical_activity = 'physical activity' in text.lower()
    year_match = re.search(r'2016', text)
    
    if has_physical_activity and year_match:
        title = filename.replace('.txt', '')
        papers_2016_pa.append({'title': title, 'filename': filename})

print('Found papers:', len(papers_2016_pa))

# Convert to JSON serializable format
result = json.dumps(papers_2016_pa)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
