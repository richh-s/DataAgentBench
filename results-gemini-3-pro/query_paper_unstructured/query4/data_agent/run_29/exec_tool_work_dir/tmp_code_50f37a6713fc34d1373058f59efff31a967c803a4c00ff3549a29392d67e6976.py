code = """import json
import re

# Load data
with open(locals()['var_function-call-9551284447428775563'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-4736821834278124027'], 'r') as f:
    citations = json.load(f)

# Aggregate citations by title
citation_map = {}
for cit in citations:
    title = cit['title']
    count = int(cit['citation_count'])
    if title not in citation_map:
        citation_map[title] = 0
    citation_map[title] += count

# Process papers
results = []
for p in papers:
    # Title
    filename = p['filename']
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    text = p.get('text', '')
    if not text:
        continue
        
    # Domain check
    if 'physical activity' not in text.lower():
        continue
        
    # Year check
    # Check first 2000 chars for 2016
    header = text[:2000]
    
    # Heuristics for Year 2016:
    # 1. "2016" appears in the text
    # 2. But we must be careful not to pick up references.
    # Usually the publication year is in the conference info at the top.
    # e.g. "CHI '16", "UbiComp '16", "September ... 2016", "Copyright 2016"
    
    # Regex for 2016
    if '2016' in header:
        # Check if it looks like a date/year context
        # Just simple check might be enough given the dataset nature
        is_2016 = True
    else:
        is_2016 = False
        
    if is_2016:
        # Get citation count
        total_citations = citation_map.get(title, 0)
        results.append({'title': title, 'total_citation_count': total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-524279506149407119': ['paper_docs'], 'var_function-call-524279506149405588': 'file_storage/function-call-524279506149405588.json', 'var_function-call-524279506149408153': ['Citations', 'sqlite_sequence'], 'var_function-call-524279506149406622': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-9551284447428774224': [{'count(*)': '1405'}], 'var_function-call-9551284447428775563': 'file_storage/function-call-9551284447428775563.json', 'var_function-call-4736821834278124027': 'file_storage/function-call-4736821834278124027.json'}

exec(code, env_args)
