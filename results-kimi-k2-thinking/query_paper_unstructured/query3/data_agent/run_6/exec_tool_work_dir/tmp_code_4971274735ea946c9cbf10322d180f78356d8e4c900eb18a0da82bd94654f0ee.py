code = """import json
import re

# Load MongoDB papers data from file
with open('/tmp/tmp_zsct1v0.json', 'r') as f:
    papers_data = json.load(f)

# Load SQLite citations data from file  
with open('/tmp/tmpk0z7xbrf.json', 'r') as f:
    citations_data = json.load(f)

print(f"Total papers in MongoDB: {len(papers_data)}")
print(f"Total citation records in SQLite: {len(citations_data)}")

# Extract paper information from MongoDB documents
title_to_paper = {}

for doc in papers_data:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from the text
    year = None
    year_patterns = [
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})',
        r'(\d{4})\s+(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'Copyright\s+.*\s+(\d{4})',
        r'Published\s+.*\s+(\d{4})',
        r'(\d{4})\s+Paper'
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            # Find the numeric year in the match
            for group in match.groups():
                if group and group.isdigit() and len(group) == 4:
                    year = int(group)
                    break
            if year:
                break
    
    # Check if paper has empirical contribution
    has_empirical = False
    if re.search(r'empirical', text, re.IGNORECASE):
        has_empirical = True
    else:
        # Also check for empirical study indicators
        empirical_terms = [
            r'field study', r'user study', r'interview', r'survey', 
            r'experiment', r'participants', r'data collection',
            r'qualitative', r'quantitative', r'mixed.method',
            r'case study', r'observation', r'ethnography',
            r'field work', r'lived informatics', r'in the wild'
        ]
        
        for term in empirical_terms:
            if re.search(term, text, re.IGNORECASE):
                has_empirical = True
                break
    
    # Extract venue
    venue_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+\d{4}', text)
    venue = venue_match.group(1) if venue_match else None
    
    # Store paper info
    title_to_paper[title] = {
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'venue': venue
    }

# Create dictionary for total citations per paper from SQLite data
title_to_citations = {}
for record in citations_data:
    title = record['title']
    citations = int(record['total_citations'])
    title_to_citations[title] = citations

# Find papers that are empirical, published after 2016, and have citation data
result = []
for title, paper_info in title_to_paper.items():
    if paper_info['has_empirical'] and paper_info['year'] and paper_info['year'] > 2016:
        if title in title_to_citations:
            result.append({
                'title': title,
                'year': paper_info['year'],
                'total_citations': title_to_citations[title]
            })

# Sort by total citations descending
result.sort(key=lambda x: x['total_citations'], reverse=True)

print(f"Found {len(result)} empirical papers published after 2016 with citation data")

# Display the top 10
print("Top 10 empirical papers after 2016 by total citations:")
for i, paper in enumerate(result[:10]):
    print(f"  {i+1}. {paper['title']} ({paper['year']}) - {paper['total_citations']} citations")

if len(result) == 0:
    print("No matching papers found. Let's debug:")
    # Debug: Check a few empirical papers and their years
    debug_count = 0
    for title, paper_info in title_to_paper.items():
        if paper_info['has_empirical']:
            debug_count += 1
            print(f"  Empirical: {title} - Year: {paper_info['year']}")
            if debug_count >= 10:
                break
    print(f"  Total empirical papers: {debug_count}")

# Save result
output = {
    'count': len(result),
    'papers': result
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
