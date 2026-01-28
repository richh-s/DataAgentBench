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
    
    # Look for year in text - more robust patterns
    year = None
    
    # Pattern: Look for year patterns
    year_match = re.search(r"(20[12][0-9])", text[:1000])  # 2010-2029 in first 1000 chars
    if year_match:
        year = int(year_match.group(1))
    else:
        # Try short form like '15
        year_match = re.search(r"'(\d{2})\\b", text[:1000])
        if year_match:
            year = 2000 + int(year_match.group(1))
    
    # Look for contribution type
    contribution = None
    text_lower = text.lower()
    
    if 'empirical' in text_lower or 'empirically' in text_lower:
        contribution = 'empirical'
    elif 'theoretical' in text_lower or 'theory' in text_lower:
        contribution = 'theoretical'
    elif 'survey' in text_lower or 'literature review' in text_lower:
        contribution = 'survey'
    elif 'system' in text_lower or 'prototype' in text_lower or 'tool' in text_lower:
        contribution = 'artifact'
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter for empirical papers after 2016
empirical_papers = [p for p in papers_info if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]

print(f"Total papers processed: {len(papers_info)}")
print(f"Empirical papers found: {len([p for p in papers_info if p['contribution'] == 'empirical'])}")
print(f"Empirical papers after 2016: {len(empirical_papers)}")
print("First 10 empirical papers after 2016:")
for p in empirical_papers[:10]:
    print(f"  - {p['title']} ({p['year']})")

# Save the filtered papers for later use
with open('empirical_papers_2017.json', 'w') as f:
    json.dump(empirical_papers, f, indent=2)

final_result = {
    "total_empirical_papers": len([p for p in papers_info if p['contribution'] == 'empirical']),
    "empirical_papers_after_2016": len(empirical_papers),
    "papers": empirical_papers
}

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
