code = """import json
import re

# Read the MongoDB query results from the file
result_file = var_functions.query_db:2

# Load the full result
with open(result_file, 'r') as f:
    papers = json.load(f)

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
    
    # Extract year - look for year patterns in first 2000 chars
    year = None
    # Common patterns: venue name followed by year
    patterns = [
        r'(CHI|UBICOMP|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+[\'"](\d{2})',
        r'(CHI|UBICOMP|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(20\d{2})',
        r'20\d{2}'
    ]
    
    first_part = text[:2000]
    for pattern in patterns:
        match = re.search(pattern, first_part)
        if match:
            # Extract 4-digit year
            year_str = match.group(0)
            year_match = re.search(r'20\d{2}', year_str)
            if year_match:
                year = int(year_match.group())
                break
    
    if not year:
        # Last resort: find any 4-digit year starting with 20
        year_match = re.search(r'20\d{2}', first_part)
        if year_match:
            year = int(year_match.group())
    
    # Check for empirical contribution
    has_empirical = False
    search_text = text[:3000].lower()
    
    # Look for combination of contribution and empirical
    if 'empirical' in search_text and 'contribution' in search_text:
        has_empirical = True
    
    # Look for specific phrases
    if not has_empirical:
        phrases = [
            'empirical study',
            'empirical research', 
            'empirical investigation',
            'we conducted',
            'our empirical',
            'this empirical',
            'empirical data',
            'empirical results'
        ]
        for phrase in phrases:
            if phrase in search_text:
                has_empirical = True
                break
    
    # Only include papers that meet criteria
    if title and year and has_empirical:
        paper_info.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

# Filter for papers after 2016
filtered_papers = [p for p in paper_info if p['year'] > 2016]

output = {
    'total_extracted': len(paper_info),
    'total_filtered': len(filtered_papers),
    'sample_filtered': filtered_papers[:3]
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
