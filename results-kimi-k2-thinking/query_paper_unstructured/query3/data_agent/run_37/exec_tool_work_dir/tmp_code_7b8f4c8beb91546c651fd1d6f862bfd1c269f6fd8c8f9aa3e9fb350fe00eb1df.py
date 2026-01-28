code = """import json
import re

# Read the MongoDB query results from the file
result_file = var_functions.query_db:2

# Load the full result
with open(result_file, 'r') as f:
    papers = json.load(f)

print('Total papers loaded:', len(papers))

# Extract relevant information from each paper
paper_info = []

for paper in papers:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    # Extract title from filename (remove .txt extension)
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    text = paper.get('text', '')
    
    # Extract year from text
    year = None
    # First, look for known venue patterns with years
    first_part = text[:3000]
    
    # Pattern: venue abbreviation with year like "CHI '17" or "Ubicomp 2017"
    patterns = [
        r'(CHI|UBICOMP|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[\s\'"]+(\d{2})(\d{2})?',
        r'(CHI|UBICOMP|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(20\d{2})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, first_part)
        if match:
            year_str = match.group(0)
            # Extract 4-digit year
            year_match = re.search(r'20\d{2}', year_str)
            if year_match:
                year = int(year_match.group())
                break
    
    if not year:
        # Try to find any 4-digit year starting with 20 or 19 (for 2010s)
        year_match = re.search(r'20\d{2}', first_part)
        if year_match:
            year = int(year_match.group())
    
    if not year:
        continue
    
    # Check for empirical contribution
    has_empirical = False
    search_text = text[:5000].lower()
    
    # Simple keyword matching for empirical
    if 'empirical' in search_text:
        has_empirical = True
    
    if title and year and has_empirical:
        paper_info.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

total_extracted = len(paper_info)
filtered_papers = [p for p in paper_info if p['year'] > 2016]

result = {
    'total_with_empirical': total_extracted,
    'after_2016': len(filtered_papers),
    'sample_papers': filtered_papers[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
