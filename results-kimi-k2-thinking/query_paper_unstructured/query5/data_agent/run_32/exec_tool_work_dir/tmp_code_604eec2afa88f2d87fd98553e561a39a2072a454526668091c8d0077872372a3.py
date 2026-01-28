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
    title = filename.replace('.txt', '')
    
    import re
    lines = text.split('\n')[:50]  # Look in first 50 lines
    year = None
    venue = None
    
    for line in lines:
        line = line.strip()
        line_upper = line.upper()
        # Check for CHI
        if 'CHI' in line_upper:
            venue = 'CHI'
        # Check for Ubicomp
        elif 'UBICOMP' in line_upper or 'UBI COMP' in line_upper:
            venue = 'Ubicomp'
        # Check for CSCW
        elif 'CSCW' in line_upper:
            venue = 'CSCW'
        # Check for other venues
        elif 'DIS' in line and line.startswith('DIS'):
            venue = 'DIS'
        elif 'PERVASIVEHEALTH' in line_upper:
            venue = 'PervasiveHealth'
        elif 'WWW' in line and line.startswith('WWW'):
            venue = 'WWW'
        elif 'IUI' in line and line.startswith('IUI'):
            venue = 'IUI'
        elif 'OZCHI' in line_upper:
            venue = 'OzCHI'
        elif 'TEI' in line and line.startswith('TEI'):
            venue = 'TEI'
        elif 'AH' in line and line.startswith('AH'):
            venue = 'AH'
        else:
            continue
        
        # Extract year
        year_match = re.search(r'\b(20\d{2})\b|\b(\d{2})\b', line)
        if year_match:
            yr = year_match.group(1) or year_match.group(2)
            if len(yr) == 2:
                year = int('20' + yr)
            else:
                year = int(yr)
            if year < 2000 or year > 2030:
                year = None
                venue = None
            else:
                break
    
    return {
        'title': title,
        'year': year,
        'venue': venue,
    }

parsed_papers = [parse_paper(p) for p in papers if p]
# Filter those with venue and year
valid_papers = [p for p in parsed_papers if p['venue'] and p['year']]
# Keep only CHI papers
chi_papers = [p for p in valid_papers if p['venue'] == 'CHI']
print('__RESULT__:')
print(json.dumps(chi_papers[:20]))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
