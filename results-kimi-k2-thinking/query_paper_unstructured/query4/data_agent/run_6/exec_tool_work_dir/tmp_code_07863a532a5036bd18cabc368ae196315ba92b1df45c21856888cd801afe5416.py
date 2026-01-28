code = """import json

# Read the full MongoDB result
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    papers = json.load(f)

# Extract titles and other info from the papers
paper_info = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Try to extract year - look for 2016 in the text
    # Also look for common publication patterns
    year = None
    if '2016' in text:
        year = 2016
    
    paper_info.append({
        'title': title,
        'year': year,
        'filename': filename
    })

print('__RESULT__:')
print(json.dumps(paper_info, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
