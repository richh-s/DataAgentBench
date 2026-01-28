code = """import json
import re

# Read the full MongoDB data from file
mongo_data_path = locals()['var_functions.query_db:5']

with open(mongo_data_path, 'r') as f:
    papers_raw = json.load(f)

print(f"Total papers in MongoDB: {len(papers_raw)}")

# Function to extract paper metadata
def extract_paper_info(doc):
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit year patterns (2000-2025)
    year_match = re.search(r"(?:\'|\\"|\b)(20[0-2][0-5])(?:\'|\\"|\b)", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution type - look for empirical
    contribution = None
    if re.search(r"\bempirical\b", text, re.IGNORECASE):
        contribution = "empirical"
    elif re.search(r"\btheoretical\b", text, re.IGNORECASE):
        contribution = "theoretical"
    elif re.search(r"\bartifact\b", text, re.IGNORECASE):
        contribution = "artifact"
    elif re.search(r"\bsurvey\b", text, re.IGNORECASE):
        contribution = "survey"
    elif re.search(r"\bmethodological\b", text, re.IGNORECASE):
        contribution = "methodological"
    
    # Extract venue - look for common venue patterns
    venue = None
    venue_patterns = [
        (r"CHI\s*'?\d{2}", "CHI"),
        (r"Ubi(?:Comp|comp)\s*'?\d{2}", "Ubicomp"),
        (r"CSCW\s*'?\d{2}", "CSCW"),
        (r"DIS\s*'?\d{2}", "DIS"),
        (r"PervasiveHealth\s*'?\d{2}", "PervasiveHealth"),
        (r"WWW\s*'?\d{2}", "WWW"),
        (r"IUI\s*'?\d{2}", "IUI"),
        (r"OzCHI\s*'?\d{2}", "OzCHI"),
        (r"TEI\s*'?\d{2}", "TEI"),
        (r"AH\s*'?\d{2}", "AH")
    ]
    
    for pattern, venue_name in venue_patterns:
        if re.search(pattern, text):
            venue = venue_name
            break
    
    return {
        'title': title,
        'year': year,
        'contribution': contribution,
        'venue': venue,
        'filename': filename
    }

# Process all papers
papers_info = []
for doc in papers_raw:
    info = extract_paper_info(doc)
    papers_info.append(info)

# Filter empirical papers after 2016
empirical_papers_2017_plus = [
    p for p in papers_info 
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

print(f"Empirical papers after 2016: {len(empirical_papers_2017_plus)}")
if empirical_papers_2017_plus:
    print("Sample papers:")
    for p in empirical_papers_2017_plus[:5]:
        print(f"  - {p['title']} ({p['year']})")

# Save to file for later use
result = {
    'all_papers': papers_info,
    'empirical_papers_2017_plus': empirical_papers_2017_plus
}

result_json = json.dumps(result, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
