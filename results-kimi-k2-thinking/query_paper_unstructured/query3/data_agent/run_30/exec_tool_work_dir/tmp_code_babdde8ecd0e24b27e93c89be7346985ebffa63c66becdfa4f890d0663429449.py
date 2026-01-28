code = """import json
import re

# Load paper documents data
paper_docs_path = var_functions.query_db:22
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load total citations data
citations_path = var_functions.query_db:24
with open(citations_path, 'r') as f:
    citations = json.load(f)

print(f"Paper documents: {len(paper_docs)}")
print(f"Citation totals: {len(citations)}")

# Extract paper information
papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = None
    # Look for patterns like "UbiComp '15" or "2015" or "CHI 2017"
    year_matches = re.findall(r"(?:UbiComp|CHI|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b", text)
    if not year_matches:
        year_matches = re.findall(r"'?(\d{2}),\s+(20\d{2})\b", text)
        if year_matches:
            year = int(year_matches[0][1])
    
    if year_matches and not year:
        for match in year_matches:
            if isinstance(match, tuple):
                year_val = int(match[1])
            else:
                year_val = int(match)
            if year_val < 50:
                year_candidate = 2000 + year_val
            else:
                year_candidate = 1900 + year_val
            if year is None or (year_candidate > 2000 and year_candidate < 2100):
                year = year_candidate
    
    # Check if empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Also check for research methods that indicate empirical work
    empirical_indicators = ['survey', 'interview', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study']
    if not has_empirical:
        for indicator in empirical_indicators:
            if indicator in text.lower() and ('we conducted' in text.lower() or 'we collected' in text.lower()):
                has_empirical = True
                break
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    })

# Create citations dictionary for easy lookup
citations_dict = {c['title']: int(c['total_citations']) for c in citations}

print(f"Processed {len(papers)} papers")

# Filter papers with empirical contribution published after 2016
results = []
for paper in papers:
    if paper['has_empirical'] and paper['year'] and paper['year'] > 2016:
        total_citations = citations_dict.get(paper['title'], 0)
        if total_citations > 0:  # Only include papers with citation data
            results.append({
                'title': paper['title'],
                'total_citations': total_citations
            })

print(f"Empirical papers after 2016 with citations: {len(results)}")
print("Sample results:")
for r in results[:10]:
    print(f"  {r['title'][:60]}... - {r['total_citations']} citations")

# Sort by citation count descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Export results to JSON format
json_result = json.dumps(results_sorted, indent=2)
print("__RESULT__:")
print(json_result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
