code = """import json
import re

# Load data
mongo_path = 'var_functions.query_db:70'
citation_path = 'var_functions.query_db:71'

with open(locals()[mongo_path], 'r') as f:
    mongo_data = json.load(f)

with open(locals()[citation_path], 'r') as f:
    citations = json.load(f)

print('=== DATA OVERVIEW ===')
print('Papers:', len(mongo_data))
print('Citations:', len(citations))

# Build citation title map for exact matching
citation_titles = [cit['title'] for cit in citations]
citation_map = {cit['title']: int(cit['total_citations']) for cit in citations}

print('\n=== SAMPLING PAPERS ===')
# Check random papers to see their structure
for i in range(0, min(10, len(mongo_data)), 2):
    filename = mongo_data[i].get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = mongo_data[i].get('text', '')
        
        # Check for year
        year_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
        year = None
        if year_match:
            year = 2000 + int(year_match.group(1))
        else:
            year_match = re.search(r"\b(20\d{2})\b", text)
            if year_match:
                year = int(year_match.group(1))
        
        # Check for empirical
        has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
        
        # Check citation match
        has_citation = title in citation_map
        citation_count = citation_map.get(title, 0)
        
        print(f"{i+1}. {title}")
        print(f"   Year: {year}, Empirical: {has_empirical}, Has citation: {has_citation}, Citations: {citation_count}")
        
        # Show year pattern if found
        if year_match:
            print(f"   Found year pattern in text: {year_match.group(0)}")

# Now search thoroughly for any post-2015 papers
print('\n=== SEARCHING FOR POST-2015 PAPERS ===')
post_2015_count = 0
post_2015_empirical = 0

all_post_2015 = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Try multiple year patterns
    year = None
    
    # Pattern 1: Conference venue format (CHI '17, UbiComp '15)
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern 2: Any year in 2010s or 2020s
        match = re.search(r"\b(201[5-9]|202[0-9])\b", text)
        if match:
            year = int(match.group(1))
            
    # Pattern 3: Search for "20xx" pattern
    if not year:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year and year >= 2015:  # Use 2015 to see border cases
        post_2015_count += 1
        
        has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
        
        if has_empirical:
            post_2015_empirical += 1
            all_post_2015.append({
                'title': title,
                'year': year,
                'empirical': has_empirical
            })

print(f'Papers in 2015+ date range: {post_2015_count}')
print(f'Empirical papers in 2015+ range: {post_2015_empirical}')

# Show what we found
if all_post_2015:
    print('\nPapers in 2015+ range with empirical keyword:')
    for i, paper in enumerate(all_post_2015[:10]):
        print(f"{i+1}. {paper['title']} ({paper['year']})")

# Try to match these with citations
results = []
for paper in all_post_2015:
    if paper['year'] > 2016:  # Now filter for post-2016
        if paper['title'] in citation_map:
            results.append({
                'title': paper['title'],
                'total_citations': citation_map[paper['title']]
            })

print(f'\nPapers after 2016 with empirical & citations: {len(results)}')

# Sort by citations
def cit_sort_func(x):
    return x['total_citations']
results.sort(key=cit_sort_func, reverse=True)

# Show results
if results:
    print('\nTop results:')
    for i, result in enumerate(results):
        print(f"{i+1}. {result['title']} - {result['total_citations']} citations")
else:
    print('No papers found matching all criteria')
    print('\nCheck if any papers have exact title matches:')
    
    # Check for exact matches between any paper and citations
    exact_matches = []
    for doc in mongo_data:
        filename = doc.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            if title in citation_map:
                exact_matches.append(title)
    
    print(f'Exact title matches (any year): {len(exact_matches)}')
    for i, title in enumerate(exact_matches[:10]):
        print(f"{i+1}. {title} - {citation_map[title]} citations")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': [], 'var_functions.execute_python:116': []}

exec(code, env_args)
