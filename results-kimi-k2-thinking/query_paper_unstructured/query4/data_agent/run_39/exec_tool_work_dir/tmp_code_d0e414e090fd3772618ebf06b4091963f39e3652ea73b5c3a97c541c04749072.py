code = """import json
import re

# Get the file path from the stored variable
paper_docs_file = locals()['var_functions.query_db:2']

print(f"Loading paper documents from: {paper_docs_file}")

with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print(f"Total number of paper documents loaded: {len(paper_docs)}")

# Initialize list to store extracted paper metadata
papers_metadata = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (without .txt extension)
    import os
    title = os.path.splitext(filename)[0]
    
    # Extract year - look for 4-digit years in reasonable range
    year = None
    year_matches = re.findall(r'\b(20\d{2})\b', text)
    for match in year_matches:
        yr = int(match)
        if 2010 <= yr <= 2025:  # Reasonable range for HCI papers
            year = yr
            break
    
    # Extract domain - check if physical activity related
    domain = []
    text_lower = text.lower()
    
    # Check for physical activity domain
    physical_activity_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 
                                  'steps', 'walking', 'running', 'workout', 'active']
    if any(keyword in text_lower for keyword in physical_activity_keywords):
        domain.append('physical activity')
    
    # Check for other domains too for completeness
    if 'food' in text_lower or 'diet' in text_lower or 'nutrition' in text_lower:
        domain.append('food')
    if 'sleep' in text_lower:
        domain.append('sleep')
    if 'mental' in text_lower or 'mood' in text_lower or 'stress' in text_lower:
        domain.append('mental')
    
    # Only process papers with physical activity domain
    if 'physical activity' in domain and year == 2016:
        papers_metadata.append({
            'title': title,
            'year': year,
            'domain': domain,
            'filename': filename
        })

print(f"Number of 2016 papers in physical activity domain: {len(papers_metadata)}")

# Get citation data
citations_file = locals()['var_functions.query_db:10']

print(f"Loading citation data from: {citations_file}")

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print(f"Total papers in citation database: {len(citations_data)}")

# Create dictionary for easy lookup
citation_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Match papers with their citation counts
result_data = []
for paper in papers_metadata:
    title = paper['title']
    if title in citation_dict:
        result_data.append({
            'title': title,
            'total_citation_count': citation_dict[title]
        })
        print(f"Found: {title} - {citation_dict[title]} citations")
    else:
        print(f"No citation data found for: {title}")

print('__RESULT__:') 
print(json.dumps(result_data))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
