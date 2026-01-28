code = """import json
import re

# Get the file path from the storage variable
file_path = var_functions.query_db:2

# Load the data
with open(file_path, 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(papers)} papers from file")

# Function to extract paper information
def extract_paper_info(text, filename):
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for venue and year patterns
    year_match = re.search(r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(\d{4})', text)
    year = 0
    if year_match:
        year = int(year_match.group(2))
    
    # Check if it has empirical contribution
    # Look for "contribution" and "empirical" near each other
    text_lower = text.lower()
    has_contribution = 'contribution' in text_lower
    has_empirical = 'empirical' in text_lower
    
    # More specific check - find if empirical is mentioned in context of contribution
    sentences = text.split('.')
    empirical_contribution = False
    for sentence in sentences:
        sent_lower = sentence.lower()
        if 'empirical' in sent_lower and ('contribution' in sent_lower or 'study' in sent_lower or 'investigation' in sent_lower):
            empirical_contribution = True
            break
    
    return {
        'title': title,
        'year': year,
        'has_empirical': empirical_contribution or (has_empirical and has_contribution)
    }

# Filter papers
empirical_papers = []
for paper in papers:
    info = extract_paper_info(paper['text'], paper['filename'])
    if info['has_empirical'] and info['year'] > 2016:
        empirical_papers.append(info)

print(f"Found {len(empirical_papers)} empirical papers after 2016")

# Result to pass to next step
result = json.dumps(empirical_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
