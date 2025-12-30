code = """import json
import os
import re

# Load citations
citations_path = locals()['var_function-call-10316639782376099170']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for citations: title -> count
citation_map = {}
for item in citations_data:
    citation_map[item['title']] = int(item['citation_count'])

# Load papers
papers_path = locals()['var_function-call-3655541512535358306']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

chi_papers = []
total_citations = 0

# Regex for CHI
# Matches: "CHI '15", "CHI 2015", "CHI Conference", etc.
simple_pattern = re.compile(r"CHI\s*['\u2019]\d\d|CHI\s*20\d\d|Conference on Human Factors in Computing Systems", re.IGNORECASE)

count = 0
found_titles = []

for paper in papers_data:
    text_start = paper.get('text', '')[:1000] # Check first 1000 chars
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for CHI
    if simple_pattern.search(text_start):
        chi_papers.append(title)
        # Add citations if present
        if title in citation_map:
            total_citations += citation_map[title]
            count += 1
            found_titles.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_papers), "papers_with_citations": count, "sample_titles": found_titles[:5]}))"""

env_args = {'var_function-call-10316639782376097408': ['Citations', 'sqlite_sequence'], 'var_function-call-10316639782376098289': ['paper_docs'], 'var_function-call-10316639782376099170': 'file_storage/function-call-10316639782376099170.json', 'var_function-call-10316639782376095955': 'file_storage/function-call-10316639782376095955.json', 'var_function-call-3655541512535358306': 'file_storage/function-call-3655541512535358306.json'}

exec(code, env_args)
