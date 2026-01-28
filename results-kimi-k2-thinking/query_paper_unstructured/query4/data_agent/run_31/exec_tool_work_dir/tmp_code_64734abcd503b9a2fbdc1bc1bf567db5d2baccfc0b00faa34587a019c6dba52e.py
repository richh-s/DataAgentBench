code = """import json

# Access the variable using locals()
result_key = 'var_functions.query_db:2'
result_path = locals().get(result_key, '')

if result_path:
    with open(result_path, 'r') as f:
        papers = json.load(f)
else:
    papers = []

print(f"Number of papers found: {len(papers)}")

# Process papers to extract title and check for year/domain
paper_info = []
for paper in papers[:50]:  # Limit to first 50 for now
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '')
    
    # Check if it's from 2016 and about physical activity
    is_2016 = '2016' in text
    has_physical_activity = 'physical activity' in text.lower()
    
    paper_info.append({
        'title': title,
        'is_2016': is_2016,
        'has_physical_activity': has_physical_activity
    })

# Filter papers
matching_papers = [p for p in paper_info if p['is_2016'] and p['has_physical_activity']]
print(f"Papers with 2016 and physical activity (first 50): {len(matching_papers)}")

for p in matching_papers:
    print(f"- {p['title']}")

print('__RESULT__:')
print(json.dumps(paper_info[:10]))  # Return first 10 as sample"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
