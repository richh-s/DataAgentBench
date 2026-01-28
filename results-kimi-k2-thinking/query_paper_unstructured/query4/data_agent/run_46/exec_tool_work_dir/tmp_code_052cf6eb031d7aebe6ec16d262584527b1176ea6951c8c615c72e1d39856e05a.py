code = """import json

# Get the file path from the variable
file_path = locals()['var_functions.query_db:0']

# Read the MongoDB query result from the file
with open(file_path, 'r') as f:
    papers = json.load(f)

# Filter papers for those published in 2016 and in 'physical activity' domain
papers_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper mentions 2016 publication year
    has_2016 = '2016' in text
    
    if has_2016:
        papers_2016.append({
            '_id': paper['_id'],
            'title': title,
            'filename': filename,
            'has_2016': has_2016
        })

print('__RESULT__:')
print(json.dumps(papers_2016, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
