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

# Analyze year patterns in the data
year_patterns_found = []
papers_by_year = {}

for paper in all_papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Look for year patterns
    # Pattern 1: Venue notation (e.g., CHI '17, UbiComp '15)
    venue_matches = re.findall(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    
    # Pattern 2: Full year (e.g., 2017, 2018)
    full_year_matches = re.findall(r"\b(20\d{2})\b", text)
    
    title = filename.replace('.txt', '')
    
    year = None
    if venue_matches:
        year = 2000 + int(venue_matches[0])
    elif full_year_matches:
        year = int(full_year_matches[0])
    
    if year:
        year_patterns_found.append({
            'title': title,
            'year': year,
            'venue_matches': venue_matches,
            'full_year_matches': full_year_matches
        })
        
        if year not in papers_by_year:
            papers_by_year[year] = 0
        papers_by_year[year] += 1

# Show year distribution
sorted_years = sorted(papers_by_year.items())
print("\nYear distribution:")
for year, count in sorted_years:
    print(f"{year}: {count} papers")

# Show post-2016 papers
post_2016 = [p for p in year_patterns_found if p['year'] > 2016]
print(f"\nPapers after 2016: {len(post_2016)}")

# Check empirical mentions for post-2016 papers
empirical_post_2016 = []
for paper in all_papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Extract year
    venue_matches = re.findall(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", paper.get('text', ''))
    full_year_matches = re.findall(r"\b(20\d{2})\b", paper.get('text', ''))
    
    year = None
    if venue_matches:
        year = 2000 + int(venue_matches[0])
    elif full_year_matches:
        year = int(full_year_matches[0])
    
    if year and year > 2016:
        has_empirical = 'empirical' in text
        if has_empirical:
            empirical_post_2016.append({
                'title': filename.replace('.txt', ''),
                'year': year
            })

print(f"\nPapers with 'empirical' keyword after 2016: {len(empirical_post_2016)}")
for paper in empirical_post_2016[:5]:
    print(f"  {paper['title']} ({paper['year']})")

# Broader empirical detection for post-2016
broader_empirical = []
empirical_keywords = ['empirical', 'empirically', 'user study', 'field study', 'experiment', 
                      'we conducted', 'we studied', 'participants', 'interview', 'survey']

for paper in all_papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Extract year
    venue_matches = re.findall(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", paper.get('text', ''))
    full_year_matches = re.findall(r"\b(20\d{2})\b", paper.get('text', ''))
    
    year = None
    if venue_matches:
        year = 2000 + int(venue_matches[0])
    elif full_year_matches:
        year = int(full_year_matches[0])
    
    if year and year > 2016:
        keyword_matches = [kw for kw in empirical_keywords if kw in text]
        if keyword_matches:
            broader_empirical.append({
                'title': filename.replace('.txt', ''),
                'year': year,
                'keywords': keyword_matches
            })

print(f"\nPapers with empirical indicators after 2016 (broader): {len(broader_empirical)}")
for paper in broader_empirical[:10]:
    print(f"  {paper['title']} ({paper['year']})")
    print(f"    Keywords: {paper['keywords']}")

print('__RESULT__:')
print(json.dumps(broader_empirical))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': []}

exec(code, env_args)
