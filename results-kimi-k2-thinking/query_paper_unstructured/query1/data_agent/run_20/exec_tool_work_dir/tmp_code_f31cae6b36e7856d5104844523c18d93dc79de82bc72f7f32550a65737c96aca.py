code = """import json
import re

# Load paper documents
paper_docs_path = locals().get('var_functions.query_db:16')
if isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = locals().get('var_functions.query_db:16', [])

# Load citations
citations_path = locals().get('var_functions.query_db:10')
if isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = locals().get('var_functions.query_db:10', [])

# Debug: Print first few entries
print(f"Loaded {len(paper_docs)} papers and {len(citations)} citations")
if paper_docs:
    print(f"Sample paper: {paper_docs[0].get('filename')}")
if citations:
    print(f"Sample citation: {citations[0]}")

# Parse papers to extract title and identify food domain papers
food_titles = []

for paper in paper_docs:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    if not filename:
        continue
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '')
    
    # Check if this is a food domain paper
    # Look for food-related terms in text and filename
    # Patterns to match food domain
    food_patterns = [
        r'\bfood\b',
        r'\beating\b',
        r'\bnutrition\b',
        r'\bdiet\b',
        r'\bdietary\b',
        r'nourish',
        r'calorie',
        r'meal',
        r'kitchen',
        r'vegetable',
        r'fruit',
        r'healthy\s+eating',
        r'food\s+journal',
        r'food\s+tracking'
    ]
    
    # Combine text and filename for searching
    search_text = f"{title} {text}".lower()
    
    # Check for explicit domain tagging in text (e.g., "domain: food")
    has_food_domain = bool(re.search(r'domain\s*[:\-\s]*food|food\s*[:\-\s]*domain', search_text, re.IGNORECASE))
    
    # Check for food-related keywords
    has_food_keywords = any(re.search(pattern, search_text, re.IGNORECASE) for pattern in food_patterns)
    
    if has_food_domain or has_food_keywords:
        food_titles.append(title)

print(f"Found {len(food_titles)} food domain papers")
if food_titles:
    print(f"Sample titles: {food_titles[:5]}")

# Now find citations for these food papers
from collections import defaultdict

# Build a dict to sum citations by title (case-insensitive)
citation_dict = defaultdict(int)
for cite in citations:
    cite_title = cite.get('title', '')
    cite_count = int(cite.get('citation_count', 0))
    citation_dict[cite_title.lower()] += cite_count

# Sum citations for food papers
total_citations = 0
matched_titles = []

for title in food_titles:
    title_lower = title.lower()
    if title_lower in citation_dict:
        count = citation_dict[title_lower]
        total_citations += count
        matched_titles.append((title, count))

sorted_titles = sorted(matched_titles, key=lambda x: x[1], reverse=True)

result = {
    'total_food_papers': len(food_titles),
    'papers_with_citations': len(sorted_titles),
    'total_citation_count': total_citations,
    'top_papers': sorted_titles[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
