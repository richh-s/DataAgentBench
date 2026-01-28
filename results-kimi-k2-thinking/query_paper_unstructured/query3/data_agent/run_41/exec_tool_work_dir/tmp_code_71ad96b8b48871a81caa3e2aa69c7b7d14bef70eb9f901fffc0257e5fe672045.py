code = """import json
import re

# Get the papers data from storage
papers = locals()['var_functions.query_db:17']

# Load from file if it's a file path
if isinstance(papers, str):
    with open(papers, 'r') as f:
        papers = json.load(f)

# Extract paper metadata
paper_list = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    
    # Try 4-digit year patterns first
    year_match = re.search(r'\b(20(1[7-9]|[2-9]\d))\b', text)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Try venue + 2-digit year
        venue_patterns = [
            r"CHI\s+'?(\d{2})",
            r"UbiComp\s+'?(\d{2})",
            r"CSCW\s+'?(\d{2})",
            r"DIS\s+'?(\d{2})",
            r"PervasiveHealth\s+'?(\d{2})",
            r"WWW\s+'?(\d{2})",
            r"IUI\s+'?(\d{2})",
            r"OzCHI\s+'?(\d{2})",
            r"TEI\s+'?(\d{2})",
            r"AH\s+'?(\d{2})"
        ]
        for pattern in venue_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                year_str = match.group(1)
                year = int('20' + year_str)
                break
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    if title and has_empirical and year:
        paper_list.append({
            'title': title,
            'year': year
        })

# Filter for papers after 2016
empirical_papers_after_2016 = [p for p in paper_list if p['year'] > 2016]

# Prepare result
result = {
    'empirical_papers': empirical_papers_after_2016,
    'count': len(empirical_papers_after_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
