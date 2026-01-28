code = """import json
import re

# Get file path
file_path = locals()['var_functions.query_db:10']

# Read all papers
with open(file_path, 'r') as f:
    papers_data = json.load(f)

print("Total papers loaded:", len(papers_data))

# Extract paper metadata
papers_metadata = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '')
    
    # Try to find year in text (look for patterns like YEAR=XXXX, or common conference formats)
    year_match = None
    
    # Look for patterns like CHI 2018, UbiComp 2017, etc.
    venue_patterns = [
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})',
        r'\d{4}\s+(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)',
        r'\b(20(1[7-9]|[2-9][0-9]))\b',  # Years 2017-2099
    ]
    
    year = None
    for pattern in venue_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # Extract year from match
            for group in match.groups():
                if group and len(group) == 4 and group.isdigit() and int(group) >= 1900:
                    year = int(group)
                    break
            if year:
                break
    
    # Check if 'empirical' appears in contribution context (case-insensitive)
    has_empirical = bool(re.search(r'empirical', text, re.IGNORECASE))
    
    papers_metadata.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'filename': filename
    })

# Filter papers
empirical_after_2016 = [p for p in papers_metadata if p['year'] and p['year'] > 2016 and p['has_empirical']]

print("Total empirical papers after 2016:", len(empirical_after_2016))
print("\nFirst 10 papers:")
for p in empirical_after_2016[:10]:
    print(f"  {p['title']} ({p['year']})")

result = {
    'count': len(empirical_after_2016),
    'papers': empirical_after_2016
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'count': 1, 'papers': [{'title': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System", 'year': 2018, 'filename': "Time for Break: Understanding Information Workers' Sedentary Behavior Through a Break Prompting System.txt"}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
