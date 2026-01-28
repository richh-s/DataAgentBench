code = """import json
import re

# Load MongoDB data
storage_key = 'var_functions.query_db:12'
mongo_result = locals()[storage_key]

if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r', encoding='utf-8') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

print(f"Total papers loaded: {len(all_papers)}")

# First, let's understand the year distribution
years_count = {}
post_2016_papers = []

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    year = None
    # Pattern 1: Venue notation like CHI '17
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        # Pattern 2: Full year like 2017
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    if year:
        years_count[year] = years_count.get(year, 0) + 1
        paper_info = {
            'title': filename.replace('.txt', ''),
            'year': year,
            'text': text
        }
        if year > 2016:
            post_2016_papers.append(paper_info)

print("Year distribution (sorted):")
for year in sorted(years_count.keys()):
    print(f"  {year}: {years_count[year]} papers")

print(f"\nTotal papers after 2016: {len(post_2016_papers)}")

# Now find empirical papers among post-2016 papers
empirical_keywords = ['empirical', 'empirically', 'user study', 'field study', 'experiment', 'we conducted', 'we studied', 'participants', 'interview', 'survey', 'case study', 'evaluation']

empirical_papers = []
for paper in post_2016_papers:
    text_lower = paper['text'].lower()
    
    # Check for empirical contribution
    has_empirical = False
    if 'empirical' in text_lower:
        has_empirical = True
    else:
        # Count how many empirical indicators are present
        indicator_count = sum(1 for keyword in empirical_keywords if keyword in text_lower)
        if indicator_count >= 2:  # At least 2 indicators
            has_empirical = True
    
    if has_empirical:
        empirical_papers.append({
            'title': paper['title'],
            'year': paper['year']
        })

print(f"\nEmpirical papers after 2016: {len(empirical_papers)}")
for i, paper in enumerate(empirical_papers[:10]):
    print(f"  {i+1}. {paper['title']} ({paper['year']})")

print('__RESULT__:')
print(json.dumps(empirical_papers))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': []}

exec(code, env_args)
