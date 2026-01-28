code = """import json
import re

# Read the full data
citation_path = locals()['var_functions.query_db:0']
with open(citation_path, 'r') as f:
    citations_2020 = json.load(f)

paper_path = locals()['var_functions.query_db:2']
with open(paper_path, 'r') as f:
    paper_docs = json.load(f)

# Extract paper information from documents
papers_info = []

for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract venue - look for CHI, Ubicomp, CSCW, etc.
    venue = None
    year = None
    source = None
    
    # Common venue patterns
    venue_patterns = [
        r'CHI\s*\'\d{2}|CHI\s*\d{4}',  # CHI '15, CHI 2015
        r'UBICOMP\s*\'\d{2}|UbiComp\s*\'\d{2}|UbiComp\s*\d{4}',  # UbiComp
        r'CSCW\s*\'\d{2}|CSCW\s*\d{4}',  # CSCW
        r'DIS\s*\'\d{2}|DIS\s*\d{4}',  # DIS
        r'PervasiveHealth\s*\'\d{2}|PervasiveHealth\s*\d{4}',  # PervasiveHealth
        r'WWW\s*\'\d{2}|WWW\s*\d{4}',  # WWW
        r'IUI\s*\'\d{2}|IUI\s*\d{4}',  # IUI
        r'Proceedings of the .*? Conference on Human Factors in Computing Systems' # CHI full
    ]
    
    # Look for venue in text
    text_upper = text.upper()
    
    if 'CHI' in text_upper:
        # Check if it's CHI conference
        if 'PROCEEDINGS OF THE' in text_upper and 'HUMAN FACTORS IN COMPUTING SYSTEMS' in text_upper:
            venue = "CHI"
            # Extract year
            year_match = re.search(r'CHI\s*\'?(\d{2})|\b(\d{4})\b', text)
            if year_match:
                year_str = year_match.group(1) or year_match.group(2)
                if len(year_str) == 2:
                    year = int('20' + year_str if int(year_str) < 50 else '19' + year_str)
                else:
                    year = int(year_str)
    elif 'UBICOMP' in text_upper or 'UBI COMP' in text_upper:
        venue = "Ubicomp"
    elif 'CSCW' in text_upper:
        venue = "CSCW"
    
    # Look for source/publisher
    if 'ACM' in text_upper:
        source = "ACM"
    elif 'IEEE' in text_upper:
        source = "IEEE"
    
    if venue == "CHI":
        papers_info.append({
            'title': title,
            'venue': venue,
            'year': year,
            'source': source,
            'filename': filename
        })

print('__RESULT__:')
print(json.dumps({
    'chi_papers_found': len(papers_info),
    'chi_papers': papers_info
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:5': {'citation_records_2020': 100, 'paper_documents': 5}}

exec(code, env_args)
