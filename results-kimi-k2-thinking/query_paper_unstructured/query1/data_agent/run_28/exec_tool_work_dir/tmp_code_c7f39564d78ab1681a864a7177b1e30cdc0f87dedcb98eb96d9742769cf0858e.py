code = """import json
import pandas as pd
from difflib import get_close_matches

# Load all the data first
citations_path = locals()['var_functions.query_db:2']
papers_path = locals()['var_functions.query_db:22']

# Load citations - check file or direct
if isinstance(citations_path, str) and citations_path.endswith('.json'):
    ci_file = open(citations_path, 'r')
    citations_list = json.load(ci_file)
else:
    citations_list = citations_path

# Load paper documents
if isinstance(papers_path, str) and papers_path.endswith('.json'):
    pd_file = open(papers_path, 'r')
    papers_list = json.load(pd_file)
else:
    papers_list = papers_path

# Process citations into dictionary for fast lookup
citation_counts = {}
for cit in citations_list:
    title = cit.get('title', '')
    count = int(cit.get('citation_count', 0))
    citation_counts[title] = citation_counts.get(title, 0) + count

# Process papers and find food domain papers
total_food_citations = 0
food_papers_matched = 0
food_paper_titles = []

for doc in papers_list:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    text_content = doc.get('text', '').lower()
    
    # Check if paper is in food domain based on text content
    if 'food' in text_content or 'eating' in text_content or 'diet' in text_content:
        food_paper_titles.append(title)
        
        # Try to find this paper in citations (exact match first)
        if title in citation_counts:
            total_food_citations += citation_counts[title]
            food_papers_matched += 1
        else:
            # Try fuzzy matching
            citation_titles = list(citation_counts.keys())
            matches = get_close_matches(title, citation_titles, n=1, cutoff=0.85)
            if matches:
                total_food_citations += citation_counts[matches[0]]
                food_papers_matched += 1

# Also check if there are any citations that directly mention food in their title
for title, count in citation_counts.items():
    if 'food' in title.lower() or 'diet' in title.lower() or 'eating' in title.lower():
        # Only add if we haven't already counted it
        if title not in food_paper_titles:
            # Check if we have this paper in our documents
            paper_titles = [doc.get('filename', '').replace('.txt', '') for doc in papers_list]
            if title in paper_titles:
                total_food_citations += count
                food_papers_matched += 1
                food_paper_titles.append(title)

result = {
    "total_citation_count": total_food_citations,
    "food_papers_matched": food_papers_matched,
    "total_food_papers_found": len(food_paper_titles)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:28': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:38': {'total_citation_count': 0}, 'var_functions.execute_python:42': {'total_citation_count': 0, 'matched_papers': 0}, 'var_functions.execute_python:48': {'total_citation_count': 0}}

exec(code, env_args)
