code = """import json
import re

# Get the MongoDB file path
mongo_var = locals()['var_functions.query_db:2']
print(f"MongoDB data file path: {mongo_var}")

# Read the MongoDB documents
with open(mongo_var, 'r') as f:
    paper_docs = json.load(f)

print(f"Total papers in MongoDB: {len(paper_docs)}")

# Let's examine the structure of the documents
if len(paper_docs) > 0:
    print("\nFirst document structure:")
    first_doc = paper_docs[0]
    print(f"Keys: {list(first_doc.keys())}")
    print(f"Filename: {first_doc.get('filename', 'N/A')}")
    
    # Print preview of text
    text_preview = first_doc.get('text', '')[:500]
    print(f"Text preview: {text_preview[:200]}...")

# Extract all papers with their years
papers_info = []
for i, doc in enumerate(paper_docs):
    try:
        filename = doc.get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        text = doc.get('text', '')
        
        # Extract year using multiple patterns
        year = None
        
        # Pattern 1: Look for four-digit year in parentheses or after comma
        year_match = re.search(r"\b(20[0-9]{2})\b", text)
        if year_match:
            year = int(year_match.group(1))
        
        # Pattern 2: Look for year in venue format like "UbiComp '15"
        if not year:
            venue_year_match = re.search(r"'([0-9]{2})\b", text)
            if venue_year_match:
                year_str = venue_year_match.group(1)
                # Assume 2000s for HCI papers
                year = 2000 + int(year_str)
        
        papers_info.append({
            'title': title,
            'year': year,
            'filename': filename
        })
    except Exception as e:
        print(f"Error processing document {i}: {e}")

# Check for 2016 papers
papers_2016 = [p for p in papers_info if p['year'] == 2016]
print(f"\nTotal papers from 2016: {len(papers_2016)}")

for p in papers_2016:
    print(f"  - {p['title']} (Year: {p['year']})")

# Now check domains for 2016 papers
detailed_papers_2016 = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year
    year = None
    year_match = re.search(r"\b(20[0-9]{2})\b", text)
    if year_match:
        year = int(year_match.group(1))
    
    if year == 2016:
        # Check for physical activity domain
        text_lower = text.lower()
        domain_mentions = []
        
        if 'physical activity' in text_lower:
            domain_mentions.append('physical activity')
        if 'sleep' in text_lower:
            domain_mentions.append('sleep')
        if 'food' in text_lower:
            domain_mentions.append('food')
        if 'mental' in text_lower:
            domain_mentions.append('mental')
        if 'finances' in text_lower:
            domain_mentions.append('finances')
        if 'fitness' in text_lower:
            domain_mentions.append('fitness')
        
        domain_str = ', '.join(domain_mentions) if domain_mentions else None
        
        detailed_papers_2016.append({
            'title': title,
            'year': year,
            'domain': domain_str,
            'has_physical_activity': 'physical activity' in text_lower
        })

print(f"\nPapers from 2016 with domain info:")
for p in detailed_papers_2016:
    print(f"  - {p['title']}")
    print(f"    Domain: {p['domain']}")
    print(f"    Has physical activity: {p['has_physical_activity']}")

# Count physical activity papers in 2016
physical_activity_2016 = [p for p in detailed_papers_2016 if p['has_physical_activity']]
print(f"\nPapers from 2016 in 'physical activity' domain: {len(physical_activity_2016)}")

result = {
    'total_papers': len(paper_docs),
    'papers_2016_count': len(papers_2016),
    'physical_activity_2016_count': len(physical_activity_2016),
    'physical_activity_papers': physical_activity_2016
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:10': {'all_papers_count': 5, 'filtered_papers': []}}

exec(code, env_args)
