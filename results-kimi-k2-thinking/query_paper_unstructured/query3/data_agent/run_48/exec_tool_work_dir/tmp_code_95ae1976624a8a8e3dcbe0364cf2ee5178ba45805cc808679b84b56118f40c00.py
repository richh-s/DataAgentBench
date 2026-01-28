code = """import json
import re

# Load the paper documents
papers_json_path = 'var_functions.query_db:2.json'
with open(papers_json_path, 'r') as f:
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
    year = None
    # Look for year patterns like "2017" or "'17"
    year_match = re.search(r"('\d{2}|\d{4})", text)
    if year_match:
        year_str = year_match.group(1)
        if year_str.startswith("'") and len(year_str) == 3:  # Handle '15 as 2015
            year = 2000 + int(year_str[1:])
        elif len(year_str) == 4:  # Full year
            year = int(year_str)
    
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
for p in empirical_papers[:10]:
    print(f"Title: {p['title']}, Year: {p['year']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
