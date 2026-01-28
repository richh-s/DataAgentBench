code = """import json

# Get all papers from the query result
result_path = var_functions.query_db:30
with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers to process: {len(papers)}")

# Filter for papers from 2016 in physical activity domain
papers_2016_pa = []

for paper in papers:
    text = paper.get('text', '')
    text_lower = text.lower()
    
    # Check if published in 2016
    has_2016 = '2016' in text
    
    # Check if in physical activity domain
    has_physical_activity = 'physical activity' in text_lower
    
    if has_2016 and has_physical_activity:
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '') if filename else 'Unknown'
        papers_2016_pa.append({
            'title': title,
            'filename': filename
        })

print(f"Found {len(papers_2016_pa)} papers from 2016 in physical activity domain")
for paper in papers_2016_pa:
    print(f"  - {paper['title']}")

result = json.dumps(papers_2016_pa)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
