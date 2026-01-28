code = """import json
from pathlib import Path

# Load the MongoDB documents
papers_path = "var_functions.query_db:2"
try:
    with open(papers_path, "r") as f:
        papers = json.load(f)
except Exception as e:
    print('Error loading papers', e)
    papers = []

# Parse each paper to extract title, year, venue
def parse_paper(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    # Extract title from filename (without .txt)
    title = filename.replace('.txt', '')
    
    import re
    lines = text.split('\n')[:50]  # Look in first 50 lines
    year = None
    venue = None
    
    # Patterns for venue and year
    for line in lines:
        line = line.strip()
        # Check for venue patterns
        # Pattern: VENUE 'YY or VENUE YYYY
        pattern = r'\b(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\b\s*[\'’]?\s*(20\d{2}|\d{2})\b'
        m = re.search(pattern, line, re.IGNORECASE)
        if m:
            venue_raw = m.group(1).upper()
            # Normalise venue names
            if 'UBICOMP' in venue_raw.upper():
                venue = 'Ubicomp'
            else:
                venue = venue_raw.upper()
            # year capture
            yr = m.group(2)
            if len(yr) == 2:
                year = int('20' + yr)
            else:
                year = int(yr)
            break
    
    return {
        'title': title,
        'year': year,
        'venue': venue,
    }

parsed_papers = [parse_paper(p) for p in papers if p]
# Filter those with venue and year
valid_papers = [p for p in parsed_papers if p['venue'] and p['year']]
print('__RESULT__:')
print(json.dumps(valid_papers[:10]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
