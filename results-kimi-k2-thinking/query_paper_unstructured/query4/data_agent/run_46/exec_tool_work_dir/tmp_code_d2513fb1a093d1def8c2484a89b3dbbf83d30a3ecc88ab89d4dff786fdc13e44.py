code = """import re
import json

# Read the MongoDB query result from the file
result_file = var_functions.query_db:0
with open(result_file, 'r') as f:
    papers = json.load(f)

# Filter papers for those published in 2016 and in 'physical activity' domain
papers_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper mentions 2016 publication year
    has_2016 = bool(re.search(r'\b2016\b', text)) or \
               bool(re.search(r"\b'16\b", text)) or \
               bool(re.search(r'UBICOMP\s*\'16', text)) or \
               bool(re.search(r'CHI\s*\'16', text)) or \
               bool(re.search(r'CHI\s*2016', text)) or \
               bool(re.search(r'CSCW\s*\'16', text)) or \
               bool(re.search(r'CSCW\s*2016', text))
    
    if has_2016:
        papers_2016.append({
            '_id': paper['_id'],
            'title': title,
            'filename': filename,
            'text': text
        })

print('__RESULT__:')
print(json.dumps(papers_2016, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
