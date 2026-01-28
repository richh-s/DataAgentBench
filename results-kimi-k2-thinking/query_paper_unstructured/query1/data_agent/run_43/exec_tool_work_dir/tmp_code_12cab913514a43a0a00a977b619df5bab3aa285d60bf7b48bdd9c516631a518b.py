code = """import json
import re

# Read the paper documents from the file
papers_file = locals()['var_functions.query_db:5']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Read the citations from the file
citations_file = locals()['var_functions.query_db:6']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Process papers to extract title and domain
paper_domains = []
for paper in papers:
    filename = paper['filename']
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    text = paper['text'].lower()
    
    # Check if paper is in 'food' domain
    # Look for domain indicators in the text
    # Common patterns: "food", "eating", "diet", "nutrition", "meal", "cuisine"
    food_keywords = ['food', 'eating', 'diet', 'nutrition', 'meal', 'cuisine', 'dietary']
    is_food_domain = any(keyword in text for keyword in food_keywords)
    
    if is_food_domain:
        paper_domains.append(title)

# Count food domain papers
food_paper_count = len(paper_domains)

# Sum citations for food domain papers
total_citations = 0
food_citation_count = 0

# Create a set of food paper titles for faster lookup
food_titles_set = set(paper_domains)

for citation in citations:
    citation_title = citation['title']
    if citation_title in food_titles_set:
        total_citations += int(citation['citation_count'])
        food_citation_count += 1

# Print the result
print('__RESULT__:')
print(json.dumps({
    'total_citation_count': total_citations,
    'food_papers_found': food_paper_count,
    'citation_records_for_food_papers': food_citation_count
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
