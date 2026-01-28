code = """import json
import re

# Read the full paper documents data from the file stored at var_functions.query_db:5
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Initialize results
empirical_papers = []

# Extract information from each paper
def extract_year(text):
    # Look for year patterns in the text (e.g., 2015, 2016, 2017)
    year_match = re.search(r'(20(1[7-9]|[2-9][0-9]))', text)
    if year_match:
        return int(year_match.group(1))
    return None

def extract_contribution(text):
    # Check if the text mentions empirical contribution
    # Look for variations of 'empirical'
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        return 'empirical'
    return None

for doc in paper_docs:
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    
    year = extract_year(text)
    contribution = extract_contribution(text)
    
    if year and year > 2016 and contribution == 'empirical':
        empirical_papers.append({
            'title': title,
            'year': year
        })

print('__RESULT__:')
print(json.dumps({
    "empirical_papers_count": len(empirical_papers),
    "sample_papers": empirical_papers[:5]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
