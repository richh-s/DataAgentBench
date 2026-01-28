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

print(f"Loaded {len(paper_docs)} papers and {len(citations)} citations")

# Define more specific patterns for food domain
# These should identify papers where food/nutrition/eating is a primary topic
food_patterns = [
    # Explicit domain indicators
    r'domain\s*[:\-\s]*food',
    r'food.*domain',
    r'research domain.*food',
    
    # Title patterns that clearly indicate food focus
    r'^[^\n]*food (journal|logging|track|tracking|intake|choice|choice|photo|photo|journal)[^\n]*$',
    r'^[^\n]*healthy (eating|food|diet)[^\n]*$',
    r'^[^\n]*nutrition[^\n]*$',
    r'^[^\n]*dietary[^\n]*$',
    r'^[^\n]*meal[^\n]*$',
    r'^[^\n]*grocery[^\n]*$',
    r'^[^\n]*restaurant[^\n]*$',
    r'^[^\n]*cooking[^\n]*$',
    r'^[^\n]*eating (behavior|habit|pattern)[^\n]*$',
    
    # Strong indicators in abstract/key sections
    r'ABSTRACT[^\n]{0,200}\\bfood\\b',
    r'ABSTRACT[^\n]{0,200}\\beating\\b(?! (disorder|habit|pattern|behavior))',
    r'ABSTRACT[^\n]{0,200}\\bnutrition\\b',
    r'INTRODUCTION[^\n]{0,200}\\bfood\\b[^\n]{0,200}(journal|tracking|logging)',
    
    # Food-specific research terms
    r'food (desert|deserts|environment|environments)',
    r'calorie (count|counter|counting)',
    r'diet (track|tracking|logger|journal)',
    r'nutritional? (information|data|intake|content)',
    r'food (photo|photograph)',
    r'meal (planning|choice|decision)',
    r'portion size',
    r'weight loss',  # Often food-related
    r'weight management',  # Often food-related
]

# Papers to exclude (false positives from general informatics papers)
exclusion_terms = [
    'Lived Informatics Model',
    'Stage-based Model',
    'Personal Informatics Systems',
    'Overactive Bladder',
    'Stroke Rehabilitation'
]

food_titles = []
food_papers_info = []

for paper in paper_docs:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    if not filename:
        continue
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Check if this should be excluded
    should_exclude = any(exclude.lower() in title.lower() for exclude in exclusion_terms)
    if should_exclude:
        continue
    
    search_text = f"{title} {text}".lower()
    
    # Check for explicit domain indicator
    explicit_food = bool(re.search(r'domain\s*[:\-\s]*food|food\s*[:\-\s]*domain', search_text, re.IGNORECASE))
    
    # Check for food patterns
    has_food_focus = False
    for pattern in food_patterns:
        if re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
            has_food_focus = True
            break
    
    # Also check title for very clear food indicators
    title_lower = title.lower()
    clear_title_indicator = any([
        'food' in title_lower and any(word in title_lower for word in ['journal', 'logging', 'track', 'photo', 'intake']),
        'healthy eating' in title_lower,
        'nutrition' in title_lower and 'personal' not in title_lower,
        'meal' in title_lower and 'track' in title_lower,
        'dietary' in title_lower,
        'weight loss' in title_lower,
        'weight management' in title_lower
    ])
    
    if explicit_food or has_food_focus or clear_title_indicator:
        food_titles.append(title)
        food_papers_info.append({
            'title': title,
            'explicit_domain': explicit_food,
            'title_indicator': clear_title_indicator
        })

# Debug: print found papers
print(f"Found {len(food_titles)} food domain papers:")
for info in food_papers_info:
    print(f"  - {info['title']}")
    print(f"    Explicit domain: {info['explicit_domain']}, Title indicator: {info['title_indicator']}")

# Sum citations for food papers
# Build a lowercase dict for case-insensitive matching
citation_dict = {}
for cite in citations:
    cite_title = cite.get('title', '').strip()
    cite_count = int(cite.get('citation_count', 0))
    if cite_title:
        citation_dict[cite_title.lower()] = citation_dict.get(cite_title.lower(), 0) + cite_count

# Match and sum
total_citations = 0
matched_papers = []

for title in food_titles:
    title_lower = title.lower()
    if title_lower in citation_dict:
        count = citation_dict[title_lower]
        total_citations += count
        matched_papers.append((title, count))

# Sort by citation count
matched_papers.sort(key=lambda x: x[1], reverse=True)

result = {
    'total_food_papers': len(food_titles),
    'papers_with_citation_data': len(matched_papers),
    'total_citation_count': total_citations,
    'food_papers': [{'title': t, 'citations': c} for t, c in matched_papers]
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}], 'var_functions.list_db:14': ['paper_docs'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_food_papers': 4, 'papers_with_citations': 4, 'total_citation_count': 1328, 'top_papers': [['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 452], ['A Lived Informatics Model of Personal Informatics', 390], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 266], ['A Stage-based Model of Personal Informatics Systems', 220]]}}

exec(code, env_args)
