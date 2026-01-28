code = """import json
import re

# Read the full result from the file
file_path = '/tmp/pwsxceql.json'

with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Total papers retrieved: {len(papers)}")

# Function to extract paper metadata from text
def extract_paper_info(paper):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for year in the text - common patterns in academic papers
    year_patterns = [
        r'CHI\s+\'?(\d{2})',  # CHI '18
        r'UbiComp\s+\'?(\d{2})',  # UbiComp '17
        r'CSCW\s+\'?(\d{2})',  # CSCW '16
        r'(\d{4})\s+(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(\d{4})',
        r'\b(20(?:1[7-9]|[2-9]\d))\b',  # Years 2017-2099
        r'Copyright\s+(?:\u00a9\s*)?\d+.*(\d{4})',  # Copyright year
    ]
    
    year = None
    for pattern in year_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            # Take the first match
            match = matches[0]
            if isinstance(match, tuple):
                match = match[0] if match[0] else match[1]
            
            if match:
                if len(match) == 2:  # 2-digit year
                    year = int('20' + match)
                elif len(match) == 4:  # 4-digit year
                    year = int(match)
                break
    
    # Look for contribution type in text
    contribution = None
    if 'empirical' in text.lower():
        contribution = 'empirical'
    elif 'artifact' in text.lower():
        contribution = 'artifact'
    elif 'theoretical' in text.lower():
        contribution = 'theoretical'
    elif 'survey' in text.lower():
        contribution = 'survey'
    elif 'methodological' in text.lower():
        contribution = 'methodological'
    
    return {
        'title': title,
        'year': year,
        'contribution': contribution
    }

# Extract info from all papers
paper_info_list = []
for paper in papers:
    info = extract_paper_info(paper)
    paper_info_list.append(info)

# Filter papers with empirical contribution and published after 2016
empirical_papers_after_2016 = []
for info in paper_info_list:
    if info['contribution'] == 'empirical' and info['year'] and info['year'] > 2016:
        empirical_papers_after_2016.append(info)

print(f"Empirical papers after 2016: {len(empirical_papers_after_2016)}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
