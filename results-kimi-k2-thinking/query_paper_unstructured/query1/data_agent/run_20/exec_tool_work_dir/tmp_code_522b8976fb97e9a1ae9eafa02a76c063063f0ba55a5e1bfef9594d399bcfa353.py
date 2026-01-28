code = """import json
import re

# Load paper documents
paper_docs_path = locals().get('var_functions.query_db:16', None)
if paper_docs_path and isinstance(paper_docs_path, str) and paper_docs_path.endswith('.json'):
    with open(paper_docs_path, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = locals().get('var_functions.query_db:16', [])

# Load citations
citations_path = locals().get('var_functions.query_db:10', None)
if citations_path and isinstance(citations_path, str) and citations_path.endswith('.json'):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
else:
    citations = locals().get('var_functions.query_db:10', [])

print(f"Loaded {len(paper_docs)} papers")
print(f"Loaded {len(citations)} citation records")

# Define food-related terms for pattern matching
food_terms = ['food', 'eating', 'nutrition', 'diet', 'dietary', 'meal', 'restaurant', 'grocery', 'calorie', 'kitchen', 'recipe', 'hunger', 'weight loss', 'weight management']

# Find food domain papers
food_papers = []
unique_titles = set()

for paper in paper_docs:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    
    # Skip if already processed (avoid duplicates)
    if title.lower() in unique_titles:
        continue
    unique_titles.add(title.lower())
    
    search_text = f"{title.lower()} {text.lower()}"
    
    # Check for explicit domain indication
    explicit_food_domain = 'domain:' in search_text and 'food' in search_text
    has_explicit_domain = re.search(r'domain\s*[:\-\s]*food|food\s*[:\-\s]*domain', search_text, re.IGNORECASE)
    
    # Check if title clearly indicates food focus
    title_indicates_food = any(term in title.lower() for term in food_terms)
    
    # Count food term occurrences in abstract/intro
    abstract_section = ''
    intro_section = ''
    if 'ABSTRACT' in text:
        abstract_start = text.find('ABSTRACT')
        abstract_section = text[abstract_start:abstract_start+500]
    if 'INTRODUCTION' in text:
        intro_start = text.find('INTRODUCTION')
        intro_section = text[intro_start:intro_start+500]
    
    early_section_text = (abstract_section + ' ' + intro_section).lower()
    term_count = sum(early_section_text.count(term) for term in food_terms)
    
    # Apply criteria: explicit domain OR clear title OR significant food terms in abstract/intro
    if has_explicit_domain or title_indicates_food or (term_count >= 3):
        # Additional check: exclude general informatics model papers
        exclude_keywords = ['general model', 'framework', 'lived informatics model', 'stage-based model']
        if not any(exclude in title.lower() for exclude in exclude_keywords):
            food_papers.append({'title': title, 'has_explicit_domain': bool(has_explicit_domain), 'title_indicates': title_indicates_food})

print(f"Found {len(food_papers)} food domain papers")
for fp in food_papers[:5]:
    print(f"  - {fp['title']}")

# Build citation dictionary (case-insensitive, aggregate all years)
citation_dict = {}
for cite in citations:
    cite_title = cite.get('title', '').strip()
    cite_count = int(cite.get('citation_count', 0))
    if cite_title:
        key = cite_title.lower()
        citation_dict[key] = citation_dict.get(key, 0) + cite_count

print(f"Built citation dictionary with {len(citation_dict)} unique paper titles")

# Calculate total citations for food papers
total_citations = 0
matched_food_papers = []

for paper in food_papers:
    title = paper['title']
    title_key = title.lower()
    
    if title_key in citation_dict:
        count = citation_dict[title_key]
        total_citations += count
        matched_food_papers.append({'title': title, 'citations': count})

# Sort by citation count
matched_food_papers.sort(key=lambda x: x['citations'], reverse=True)

result = {
    'total_food_domain_papers_identified': len(food_papers),
    'papers_with_citation_data': len(matched_food_papers),
    'total_citation_count': total_citations,
    'papers': matched_food_papers[:10]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}}

exec(code, env_args)
