code = """import json
import re

# Access the stored results
citations = locals()['var_functions.query_db:2']  # From SQLite Citations table
paper_docs = locals()['var_functions.query_db:3']  # From MongoDB paper_docs collection

# If they are file paths, load them
if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Extract information from paper documents
papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text (look for patterns like 2016, '16, etc.)
    year = None
    year_patterns = [
        r"'16", r"\b2016\b", r"2016\b",
        r"'15", r"\b2015\b", r"2015\b",
        r"'17", r"\b2017\b", r"2017\b",
        r"'14", r"\b2014\b", r"2014\b",
        r"'18", r"\b2018\b", r"2018\b",
        r"'19", r"\b2019\b", r"2019\b",
        r"'20", r"\b2020\b", r"2020\b",
        r"'21", r"\b2021\b", r"2021\b",
        r"'22", r"\b2022\b", r"2022\b",
        r"'23", r"\b2023\b", r"2023\b",
        r"'24", r"\b2024\b", r"2024\b",
        r"'25", r"\b2025\b", r"2025\b"
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            if "'" in pattern:
                year = int('20' + match.group().replace("'", ""))
            else:
                year = int(match.group())
            break
    
    # Extract domain (look for physical activity, etc.)
    domain = []
    domain_keywords = {
        'physical activity': ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable', 'steps', 'walking', 'running'],
        'food': ['food', 'diet', 'eating', 'nutrition', 'calorie'],
        'sleep': ['sleep', 'sleeping', 'bedtime', 'circadian'],
        'mental': ['mental', 'psychology', 'mood', 'stress', 'anxiety', 'depression'],
        'finances': ['finance', 'money', 'expense', 'budget', 'spending'],
        'location': ['location', 'place', 'gps', 'geo'],
        'productivity': ['productivity', 'work', 'task', 'time management']
    }
    
    text_lower = text.lower()
    for domain_name, keywords in domain_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            domain.append(domain_name)
    
    papers_info.append({
        'title': title,
        'year': year,
        'domain': domain,
        'filename': filename
    })

# Filter for 2016 papers in physical activity domain
papers_2016_physical_activity = []
for paper in papers_info:
    if paper['year'] == 2016 and 'physical activity' in paper['domain']:
        papers_2016_physical_activity.append(paper)

print(f"Total papers analyzed: {len(papers_info)}")
print(f"Papers from 2016 in physical activity domain: {len(papers_2016_physical_activity)}")

# Get citation counts for these papers
citation_dict = {}
for cit in citations:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    
    if title not in citation_dict:
        citation_dict[title] = 0
    citation_dict[title] += count

# Combine paper info with citations
result = []
for paper in papers_2016_physical_activity:
    title = paper['title']
    total_citations = citation_dict.get(title, 0)
    result.append({
        'title': title,
        'total_citations': total_citations
    })

# Sort by citations
result_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(result_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json'}

exec(code, env_args)
