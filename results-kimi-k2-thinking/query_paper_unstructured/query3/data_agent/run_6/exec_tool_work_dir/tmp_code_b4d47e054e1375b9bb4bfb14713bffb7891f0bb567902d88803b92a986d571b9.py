code = """import json
import re

# Load MongoDB data - empirical papers
with open('/tmp/tmpk3cghq9p.json', 'r') as f:
    mongo_data = json.load(f)

# Load SQLite data - total citations per paper
with open('/tmp/tmpk0z7xbrf.json', 'r') as f:
    citations_data = json.load(f)

print(f"Loaded {len(mongo_data)} papers from MongoDB")
print(f"Loaded {len(citations_data)} citation records from SQLite")

# Create mapping of title to total citations
title_to_citations = {}
for record in citations_data:
    title = record['title']
    citations = int(record['total_citations'])
    title_to_citations[title] = citations

# Process MongoDB papers to extract info
empirical_papers_after_2016 = []

for doc in mongo_data:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Extract year from text
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
            for group in match.groups():
                if group and group.isdigit() and len(group) == 4:
                    year = int(group)
                    break
            if year:
                break
    
    # Check if paper has empirical contribution (already filtered by MongoDB query)
    has_empirical = True  # Since we filtered on 'empirical' in the query
    
    # Check if published after 2016
    if has_empirical and year and year > 2016:
        # Check if we have citation data
        if title in title_to_citations:
            empirical_papers_after_2016.append({
                'title': title,
                'year': year,
                'total_citations': title_to_citations[title]
            })

# Sort by citations descending
empirical_papers_after_2016.sort(key=lambda x: x['total_citations'], reverse=True)

print(f"\nFound {len(empirical_papers_after_2016)} empirical papers after 2016 with citation data")

# Show top 15 results
print("\nTop 15 papers:")
for i, paper in enumerate(empirical_papers_after_2016[:15]):
    print(f"  {i+1}. {paper['title']}")
    print(f"     Year: {paper['year']}, Total Citations: {paper['total_citations']}")

# Create final result
result = {
    'count': len(empirical_papers_after_2016),
    'papers': empirical_papers_after_2016
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
