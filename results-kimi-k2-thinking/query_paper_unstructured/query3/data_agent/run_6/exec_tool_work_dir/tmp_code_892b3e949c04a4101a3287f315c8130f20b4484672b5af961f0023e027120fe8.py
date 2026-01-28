code = """import json
import re

# First, let's read the MongoDB query result file
with open('/tmp/tmphc4q8y_5.json', 'r') as f:
    papers_data = json.load(f)

print(f"Total papers in MongoDB: {len(papers_data)}")
print("First few papers:")
for i, p in enumerate(papers_data[:3]):
    print(f"  {i+1}. {p['filename']}")

# Extract information from each paper
title_to_paper = {}
empirical_papers = []

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
            r'experiment(al)?', r'participants', r'data collection',
            r'qualitative', r'quantitative', r'mixed.method',
            r'case study', r'observation(al)?', r'ethnograph(y|ic)',
            r'field.work', r'lived.informatics', r'in.the.wild'
        ]
        
        for term in empirical_terms:
            if re.search(term, text, re.IGNORECASE):
                # Make sure it's not just mentioned in references
                if text.lower().count(term.replace(r'\', '').replace('?', '')) < 10:
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
    
    if has_empirical and year and year > 2016:
        empirical_papers.append(title)

print(f"\nPapers with empirical contribution after 2016: {len(empirical_papers)}")
print("First 10 empirical papers after 2016:")
for i, title in enumerate(empirical_papers[:10]):
    paper = title_to_paper[title]
    print(f"  {i+1}. {title} ({paper['year']}) - {paper['venue']}")

result = {
    'empirical_paper_titles': empirical_papers,
    'paper_details': title_to_paper
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
