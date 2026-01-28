code = """import json
import re

# Read the MongoDB query results from file
result_path = var_functions.query_db:22
with open(result_path, 'r') as f:
    papers = json.load(f)

print('Total papers mentioning physical activity:', len(papers))

# Filter papers from 2016
papers_2016 = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '').upper()
    
    # Check if paper is from 2016 (simple check)
    has_2016 = '2016' in text
    
    if has_2016:
        # Count physical activity mentions
        physical_activity_count = len(re.findall(r'physical activity', paper.get('text', ''), re.IGNORECASE))
        
        papers_2016.append({
            'title': title,
            'filename': filename,
            'year': 2016,
            'physical_activity_mentions': physical_activity_count
        })

print('Found', len(papers_2016), 'papers from 2016 in physical activity domain')

# Print titles
for paper in sorted(papers_2016, key=lambda x: x['title']):
    print('  -', paper['title'])

# Return the filtered papers
result = json.dumps(papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
