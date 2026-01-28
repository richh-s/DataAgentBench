code = """import json
import re
from datetime import datetime

# Read the MongoDB query results from the file
result_file = var_functions.query_db:2

# Load the full result
with open(result_file, 'r') as f:
    papers = json.load(f)

# Extract relevant information from each paper
paper_info = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Extract year from text
    # Look for patterns like: UBICOMP '15, ... 2015; CHI '16, ... 2016; etc.
    # Also look for 4-digit years in the text
    year = None
    
    # Pattern 1: Look for venue with year like "UBICOMP '15, ... 2015"
    venue_year_patterns = [
        r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s+'?(\d{2})\d{2}?[^\d]*(\d{4})",
        r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)[^\d]*(\d{4})"
    ]
    
    for pattern in venue_year_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            # If pattern has 3 groups, third group is the year
            # If pattern has 2 groups, second group is the year
            groups = match.groups()
            if len(groups) == 3 and groups[2]:
                year = int(groups[2])
                break
            elif len(groups) == 2 and groups[1]:
                year_str = groups[1]
                if len(year_str) == 4:
                    year = int(year_str)
                elif len(year_str) == 2:
                    # Assume 20xx for 2-digit years
                    year = int('20' + year_str)
                break
    
    # Pattern 2: If not found yet, look for any 4-digit year in the first 1000 characters
    if not year:
        year_match = re.search(r'\b(20\d{2})\b', text[:1000])
        if year_match:
            year = int(year_match.group(1))
    
    # Check for empirical contribution
    has_empirical = False
    contribution_patterns = [
        r'contribution[^\n]*empirical',
        r'empirical[^\n]*contribution',
        r'empirical study',
        r'empirical research',
        r'empirical investigation',
        r'empirical analysis'
    ]
    
    # Look for contribution-related keywords in the first part of the paper
    # Check abstract, introduction for contribution statements
    text_to_search = text[:3000].lower()
    
    for pattern in contribution_patterns:
        if re.search(pattern, text_to_search, re.IGNORECASE):
            has_empirical = True
            break
    
    # Also check if the word "empirical" appears in context of the paper
    if not has_empirical:
        # More specific check for empirical in methodology or abstract
        if re.search(r'\bempirical\b', text_to_search):
            # Check if it's not just a reference to other work
            # Look for patterns indicating this paper is empirical
            empirical_context = [
                r'we conducted[^\n]*empirical',
                r'our empirical',
                r'this empirical',
                r'an empirical study',
                r'empirical data',
                r'empirical results'
            ]
            for pattern in empirical_context:
                if re.search(pattern, text_to_search, re.IGNORECASE):
                    has_empirical = True
                    break
    
    if title and year and has_empirical:
        paper_info.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

# Filter for papers published after 2016
filtered_papers = [p for p in paper_info if p['year'] and p['year'] > 2016]

# Sort and prepare output
filtered_papers = sorted(filtered_papers, key=lambda x: x['year'])

# Save to file
output_file = '/tmp/empirical_papers_after_2016.json'
with open(output_file, 'w') as f:
    json.dump(filtered_papers, f, indent=2)

print('__RESULT__:')
print(json.dumps({
    'count': len(filtered_papers),
    'papers_file': output_file,
    'sample_papers': filtered_papers[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
