code = """import json

# Read the full result from the path stored in the variable
result_path = var_functions.query_db:2

with open(result_path, 'r') as f:
    papers = json.load(f)

print(f"Number of papers found: {len(papers)}")
print("\nFirst paper example:")
if papers:
    print(json.dumps(papers[0], indent=2)[:2000])  # Print first 2000 chars of first paper

# Let's also extract basic info from the papers
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'Unknown'
    text = paper.get('text', '')
    
    # Try to extract year from text (look for patterns like "2016")
    import re
    year_match = re.search(r'(?:\b|[^0-9])(2016)(?:\b|[^0-9])', text)
    year = year_match.group(1) if year_match else None
    
    paper_info.append({
        'title': title,
        'year': year,
        'has_physical_activity': 'physical activity' in text.lower()
    })

# Count papers with 2016 and physical activity
matching_papers = [p for p in paper_info if p['year'] == '2016' and p['has_physical_activity']]
print(f"\nPapers with year 2016 and 'physical activity': {len(matching_papers)}")

# Show titles
for p in matching_papers[:10]:
    print(f"- {p['title']}")

print('__RESULT__:')
print(json.dumps(matching_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
