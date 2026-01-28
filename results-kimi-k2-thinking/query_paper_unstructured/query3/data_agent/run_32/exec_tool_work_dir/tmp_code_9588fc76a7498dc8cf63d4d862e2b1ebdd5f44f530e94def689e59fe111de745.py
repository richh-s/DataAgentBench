code = """import json
import re

# Load the full datasets from storage
mongo_data = locals()['var_functions.query_db:70']
citations = locals()['var_functions.query_db:71']

# Convert from file paths if needed
if isinstance(mongo_data, str) and mongo_data.endswith('.json'):
    with open(mongo_data, 'r') as f:
        mongo_data = json.load(f)
if isinstance(citations, str) and citations.endswith('.json'):
    with open(citations, 'r') as f:
        citations = json.load(f)

# Debug: Check what papers actually exist
print('Total papers in MongoDB:', len(mongo_data))
print('Total citation records:', len(citations))

# Sample some papers to see their structure
print('\nSample papers:')
for i in range(min(5, len(mongo_data))):
    filename = mongo_data[i].get('filename', 'No filename')
    title = filename.replace('.txt', '') if filename else 'No title'
    print(f"{i+1}. {title}")

# Sample some citations
print('\nSample citations:')
for i in range(min(5, len(citations))):
    print(f"{i+1}. {citations[i]['title']}")

# Check year extraction for a few papers
print('\nYear extraction test:')
for i in range(min(5, len(mongo_data))):
    text = mongo_data[i].get('text', '')
    filename = mongo_data[i].get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    print(f"{title[:50]}... - Year: {year}")

# Check for empirical keyword in a few papers
print('\nEmpirical keyword check:')
for i in range(min(10, len(mongo_data))):
    text = mongo_data[i].get('text', '')
    filename = mongo_data[i].get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    print(f"{title[:50]}... - Has 'empirical': {has_empirical}")

# Check if any papers have both empirical and post-2016
empirical_post_2016 = []
for doc in mongo_data:
    filename = doc.get('filename', '')
    if not filename:
        continue
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    year = None
    venue_match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if venue_match:
        year = 2000 + int(venue_match.group(1))
    else:
        year_match = re.search(r"\b(20\d{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    has_empirical = 'empirical' in text.lower() or 'empirically' in text.lower()
    
    if year and year > 2016 and has_empirical:
        empirical_post_2016.append(title)

print(f'\nTotal empirical papers after 2016: {len(empirical_post_2016)}')

# Check title matching
print(f'\nChecking title matching:')
if empirical_post_2016:
    citation_titles = [c['title'].lower() for c in citations]
    
    matches = []
    for paper_title in empirical_post_2016:
        if paper_title.lower() in citation_titles:
            matches.append(paper_title)
    
    print(f'Found {len(matches)} matching titles')
    if matches:
        print('Matching papers:')
        for title in matches[:5]:
            print(f'  - {title}')
    else:
        print('No exact title matches found')
        
        # Check for partial matches
        print('\nChecking for partial matches:')
        for paper_title in empirical_post_2016[:5]:
            paper_lower = paper_title.lower()
            for cit_title in citations[:10]:
                cit_lower = cit_title['title'].lower()
                if paper_lower in cit_lower or cit_lower in paper_lower:
                    print(f'  Possible match: "{paper_title}" vs "{cit_title["title"]}"')
                    break
else:
    print('No empirical papers after 2016 found')

print('__RESULT__:')
print(json.dumps([]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json', 'var_functions.execute_python:38': {'papers': [], 'count': 0}, 'var_functions.execute_python:52': [], 'var_functions.execute_python:66': [], 'var_functions.query_db:70': 'file_storage/functions.query_db:70.json', 'var_functions.query_db:71': 'file_storage/functions.query_db:71.json', 'var_functions.execute_python:76': [], 'var_functions.execute_python:80': []}

exec(code, env_args)
