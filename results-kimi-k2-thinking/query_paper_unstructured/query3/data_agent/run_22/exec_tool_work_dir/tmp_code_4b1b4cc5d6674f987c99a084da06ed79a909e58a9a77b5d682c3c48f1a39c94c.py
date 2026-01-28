code = """import json
import re

# Load MongoDB data
mongo_path = locals()['var_functions.query_db:18']
with open(mongo_path, 'r') as f:
    papers = json.load(f)

# Function to extract paper information
def extract_paper_info(paper):
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else 'Unknown'
    
    # Extract year - look for patterns like '2015', '2016', etc.
    # Common patterns: YEAR, YEAR., YEAR), YEAR], YEAR-
    year_match = re.search(r'(?:19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    # Extract venue - look for common conference/journal names
    venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH', 'UIST', 'MobileHCI']
    venue = None
    text_upper = text.upper()
    for v in venues:
        if v.upper() in text_upper:
            venue = v
            break
    
    # Extract source (publisher) - look for ACM, IEEE, PubMed
    sources = ['ACM', 'IEEE', 'PubMed']
    source = None
    text_upper = text.upper()
    for s in sources:
        if s.upper() in text_upper:
            source = s
            break
    
    # Extract contribution type - look for empirical, artifact, theoretical, survey, methodological
    contributions = ['empirical', 'artifact', 'theoretical', 'survey', 'methodological']
    contribution = []
    text_lower = text.lower()
    for c in contributions:
        if c in text_lower:
            contribution.append(c)
    
    # Extract domain - look for common domains
    domains = ['food', 'physical activity', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 
               'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    domain = []
    text_lower = text.lower()
    for d in domains:
        if d in text_lower:
            domain.append(d)
    
    return {
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'contribution': contribution,
        'domain': domain
    }

# Extract info from all papers
paper_info = [extract_paper_info(paper) for paper in papers]

# Print first paper's info to test
print("__RESULT__:")
print(json.dumps(paper_info[0]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:24': {'message': 'Loaded 5 papers'}}

exec(code, env_args)
