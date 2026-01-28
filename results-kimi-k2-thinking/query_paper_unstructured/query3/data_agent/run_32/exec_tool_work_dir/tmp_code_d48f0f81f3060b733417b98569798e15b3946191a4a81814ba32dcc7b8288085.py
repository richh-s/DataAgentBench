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

print('Total papers loaded: ' + str(len(all_papers)))

# Track years and post-2016 papers
year_counts = {}
post_2016_papers = []

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract year from text
    year = None
    
    # Pattern: Venue notation like CHI '17
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern: Full year like 2017
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

# Show year distribution
sorted_years = sorted(year_counts.keys())
print('Year distribution:')
for year in sorted_years:
    print('  ' + str(year) + ': ' + str(year_counts[year]))

print('Papers after 2016: ' + str(len(post_2016_papers)))

# Find empirical papers among post-2016 papers
empirical_papers = []
keywords = ['empirical', 'empirically', 'user study', 'field study', 'experiment']

for paper in post_2016_papers:
    text_lower = paper['text'].lower()
    
    # Simple check for empirical keyword
    if 'empirical' in text_lower:
        empirical_papers.append(paper)
    else:
        # Count multiple research indicators
        count = 0
        for kw in keywords:
            if kw in text_lower:
                count += 1
        if count >= 2:
            empirical_papers.append(paper)

print('Empirical papers after 2016: ' + str(len(empirical_papers)))

# Prepare result with title and year
result = []
for p in empirical_papers[:50]:
    result.append({'title': p['title'], 'year': p['year']})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': []}

exec(code, env_args)
