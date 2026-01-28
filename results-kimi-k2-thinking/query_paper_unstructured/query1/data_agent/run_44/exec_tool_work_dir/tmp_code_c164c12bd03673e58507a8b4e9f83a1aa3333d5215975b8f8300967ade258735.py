code = """import json
import re

# Access the file paths from storage
citations_file_path = locals()['var_functions.query_db:12']
papers_file_path = locals()['var_functions.query_db:5']

# Load the full data
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Process papers to extract domains - with better matching logic
paper_domains = {}  # title -> domains list

# Read paper_docs collection from MongoDB
for paper in papers_data:
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    
    # Extract domain information from text (case insensitive)
    text = paper['text'].lower()
    
    domains = []
    
    # Check for food domain using various patterns
    if re.search(r'\bfood\b', text):
        domains.append('food')
    if 'nutrition' in text:
        domains.append('food')
    if 'eating' in text:
        domains.append('food')
    if 'diet' in text:
        domains.append('food')
    
    # Also check other domains for completeness
    if re.search(r'\bphysical activity\b', text):
        domains.append('physical activity')
    if re.search(r'\bexercise\b', text):
        domains.append('physical activity')
    if 'fitness' in text:
        domains.append('physical activity')
    if re.search(r'\bsleep\b', text):
        domains.append('sleep')
    if re.search(r'\bmental\b', text):
        domains.append('mental')
    if re.search(r'\bfinancial\b', text) or re.search(r'\bfinances\b', text):
        domains.append('finances')
    
    # Store the domains for this paper
    paper_domains[title] = domains

# Match citations with papers and filter for food domain
total_citations = 0
food_papers_citations = {}
food_papers_titles = []

for citation in citations_data:
    title = citation['title']
    
    # Check if this paper is in the food domain
    if title in paper_domains and 'food' in paper_domains[title]:
        citation_count = int(citation['citation_count'])
        total_citations += citation_count
        food_papers_titles.append(title)
        
        # Track per paper
        if title not in food_papers_citations:
            food_papers_citations[title] = 0
        food_papers_citations[title] += citation_count

# Remove duplicates from list
food_papers_titles = list(set(food_papers_titles))

# Prepare result
result = {
    'total_citation_count': total_citations,
    'food_papers_count': len(food_papers_titles),
    'food_papers_titles': food_papers_titles,
    'detailed_breakdown': food_papers_citations
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'citations_records': 100, 'paper_documents': 5}, 'var_functions.execute_python:10': {'total_citation_count': 266, 'food_papers_count': 1, 'food_papers_details': {'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App': 266}}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
