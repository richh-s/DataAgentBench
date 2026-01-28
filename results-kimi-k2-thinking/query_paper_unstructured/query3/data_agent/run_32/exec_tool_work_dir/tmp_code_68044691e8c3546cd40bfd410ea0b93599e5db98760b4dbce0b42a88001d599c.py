code = """import json
import re

# Load data from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)

if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Simple debug: just list some papers and check their years
print('=== EXPLORING DATA ===')
print(f'Papers loaded: {len(mongo_data)}')
print(f'Citations loaded: {len(citations)}')

# Build citation map for exact matching
citation_titles_exact = [cit['title'] for cit in citations]
citation_map_exact = {cit['title']: int(cit['total_citations']) for cit in citations}

# Check first 20 papers
print('\n=== FIRST 20 PAPERS ===')
for i in range(min(20, len(mongo_data))):
    filename = mongo_data[i].get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = mongo_data[i].get('text', '')[:200]  # First 200 chars
        
        # Extract year
        year = None
        match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
        if match:
            year = 2000 + int(match.group(1))
        else:
            match = re.search(r"\b(20\d{2})\b", text)
            if match:
                year = int(match.group(1))
        
        # Check empirical
        has_empirical = 'empirical' in mongo_data[i].get('text', '').lower()
        
        # Check if has citation
        has_citation = title in citation_map_exact
        citation_count = citation_map_exact.get(title, 0)
        
        print(f"{i+1}. {title}")
        print(f"   Year: {year}, Empirical: {has_empirical}, Has citation: {has_citation}")
        if has_citation:
            print(f"   Citations: {citation_count}")

# Check last 10 papers to see if we see any post-2016
print('\n=== LAST 5 PAPERS ===')
for i in range(max(0, len(mongo_data)-5), len(mongo_data)):
    filename = mongo_data[i].get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = mongo_data[i].get('text', '')[:200]
        
        # Extract year
        year = None
        match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
        if match:
            year = 2000 + int(match.group(1))
        else:
            match = re.search(r"\b(20\d{2})\b", text)
            if match:
                year = int(match.group(1))
        
        has_empirical = 'empirical' in mongo_data[i].get('text', '').lower()
        
        print(f"{title}")
        print(f"   Year: {year}, Empirical: {has_empirical}")

# Check if there are ANY post-2015 papers with empirical keyword
print('\n=== SEARCHING FOR POST-2016 EMPIRICAL PAPERS ===')
foundsomething = 0
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Extract year
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check
    has_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and has_empirical:
        foundsomething += 1
        if foundsomething <= 5:  # Show first 5
            print(f"{foundsomething}. {title} (Year: {year})")

print(f'Total post-2016 empirical papers: {foundsomething}')

# Check citation match count
print('\n=== CITATION MATCH COUNT ===')
match_count = 0
matched_titles = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    title = filename.replace('.txt', '')
    if title in citation_map_exact:
        match_count += 1
        matched_titles.append(title)

print(f'Total papers with citation records: {match_count}')

# Check if any matched papers are empirical and post-2016
final_matches = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    if title not in citation_map_exact:
        continue
    
    text = doc.get('text', '')
    
    # Extract year
    year = None
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check empirical and filter
    has_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and has_empirical:
        final_matches.append({
            'title': title,
            'total_citations': citation_map_exact[title]
        })

print(f'Final qualifying papers: {len(final_matches)}')

# Sort by citations
final_matches.sort(key=lambda x: x['total_citations'], reverse=True)

print('\n__RESULT__:')
print(json.dumps(final_matches))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': [], 'var_functions.execute_python:84': [], 'var_functions.execute_python:88': [], 'var_functions.execute_python:96': [], 'var_functions.execute_python:100': [], 'var_functions.execute_python:110': []}

exec(code, env_args)
