code = """import json
import re

# Get the paper documents data from storage
file_path = locals()['var_functions.query_db:8']

# Read and process the data
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

print(f"Total paper documents: {len(paper_docs)}")

# Process papers to extract information more carefully
papers_2016_pa = []

for doc in paper_docs[:]:  # Process all documents
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text - handle as string first
    year_str = None
    # Look for copyright year first
    copyright_match = re.search(r'Copyright\s*[@©]?\s*(20\d{2})', text)
    if copyright_match:
        year_str = copyright_match.group(1)
    else:
        # Look for 4-digit year patterns
        year_match = re.search(r'\b(20\d{2})\b', text)
        if year_match:
            year_str = year_match.group(1)
    
    # Check if domain includes physical activity
    text_lower = text.lower()
    pa_keywords = ['physical activity', 'physical activities', 'fitness', 'exercise', 'workout']
    
    has_physical_activity = any(keyword in text_lower for keyword in pa_keywords)
    
    if year_str == '2016' and has_physical_activity:
        papers_2016_pa.append({
            'title': title,
            'year': year_str,
            'filename': filename
        })

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")

if papers_2016_pa:
    print("Paper titles:")
    for p in papers_2016_pa:
        print("  - " + p['title'])
else:
    print("No papers found from 2016 in physical activity domain")

# Also try a broader search for papers with publication year 2016
papers_with_year = []
for doc in paper_docs[:]:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year_str = None
    copyright_match = re.search(r'Copyright\s*[@©]?\s*(20\d{2})', text)
    if copyright_match:
        year_str = copyright_match.group(1)
    else:
        year_match = re.search(r'\b(20\d{2})\b', text)
        if year_match:
            year_str = year_match.group(1)
    
    if year_str == '2016':
        papers_with_year.append({
            'title': title,
            'year': year_str,
            'filename': filename
        })

print("\nTotal papers from 2016 (all domains): " + str(len(papers_with_year)))
if papers_with_year:
    print("Sample titles:")
    for p in papers_with_year[:5]:
        print("  - " + p['title'])

# Prepare results
result = {
    'papers_2016_pa': papers_2016_pa,
    'papers_with_year': papers_with_year,
    'paper_titles_pa': [p['title'] for p in papers_2016_pa],
    'paper_titles_all_2016': [p['title'] for p in papers_with_year]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'paper_titles': [], 'papers': []}, 'var_functions.query_db:12': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}]}

exec(code, env_args)
