code = """import json
import re

# Load MongoDB data
storage_key = 'var_functions.query_db:12'
mongo_result = locals()[storage_key]

if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

print(f"Total papers loaded: {len(all_papers)}")

# Analyze years
year_counts = {}
post_2016_papers = []

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Try to find year
    year = None
    
    # Pattern 1: Venue format like CHI '17
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern 2: Full year
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year:
        year_counts[year] = year_counts.get(year, 0) + 1
        if year > 2016:
            post_2016_papers.append({
                'title': filename.replace('.txt', ''),
                'year': year,
                'text': text
            })

print("Year distribution:")
for year in sorted(year_counts.keys()):
    print(f"  {year}: {year_counts[year]}")

print(f"\nPapers after 2016: {len(post_2016_papers)}")

# Find empirical papers
empirical_keywords = ['empirical', 'empirically', 'user study', 'field study', 'experiment']
empirical_papers = []

for paper in post_2016_papers:
    text_lower = paper['text'].lower()
    
    if 'empirical' in text_lower:
        empirical_papers.append(paper)
    else:
        # Count indicators
        count = sum(1 for keyword in empirical_keywords if keyword in text_lower)
        if count >= 2:
            empirical_papers.append(paper)

print(f"Empirical papers after 2016: {len(empirical_papers)}")
result = [{'title': p['title'], 'year': p['year']} for p in empirical_papers[:20]]

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': []}

exec(code, env_args)
