code = """import json
import re

# Load the paper documents
with open('var_functions.query_db:2.json', 'r') as f:
    paper_docs = json.load(f)

# Function to extract paper information from text
papers_info = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Look for year in text (common patterns)
    year_match = re.search(r"('\d{2}|\d{4})\s*,\s*(Ubicomp|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[",'\s]", text)
    if not year_match:
        year_match = re.search(r"(201\d|202\d)", text)
    
    year = int(year_match.group(1)) if year_match else None
    if year and year < 100:  # Handle '15 as 2015
        year = 2000 + year
    
    # Look for contribution type
    contribution = None
    if re.search(r'empiric(al|al study|al work|al research|al investigation)', text, re.IGNORECASE):
        contribution = 'empirical'
    elif re.search(r'theoretic(al|al work|al model|al framework|al contribution)', text, re.IGNORECASE):
        contribution = 'theoretical'
    elif re.search(r'artifact|system|prototype|tool|application', text, re.IGNORECASE):
        if re.search(r'design|develop|implement|create|build', text, re.IGNORECASE):
            contribution = 'artifact'
    elif re.search(r'survey|review|literature', text, re.IGNORECASE):
        contribution = 'survey'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter for empirical papers after 2016
empirical_papers = [p for p in papers_info if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]

print(f"Found {len(empirical_papers)} empirical papers after 2016")
if empirical_papers:
    print("Sample:", empirical_papers[:3])"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
