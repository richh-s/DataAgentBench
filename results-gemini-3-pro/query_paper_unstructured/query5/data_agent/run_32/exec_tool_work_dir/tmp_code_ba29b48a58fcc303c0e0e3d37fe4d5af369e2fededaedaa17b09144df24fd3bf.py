code = """import json
import re

# Load citations
with open(locals()['var_function-call-13891558846941465066'], 'r') as f:
    citations_data = json.load(f)

# Load papers
with open(locals()['var_function-call-4279784200820574316'], 'r') as f:
    papers_data = json.load(f)

print(f"Loaded {len(citations_data)} citation records and {len(papers_data)} papers.")

# Create a map of title -> citation_count for 2020
citations_map = {}
for item in citations_data:
    citations_map[item['title']] = item['citation_count']

# Filter papers for CHI
chi_papers = []
chi_titles = []

# Regex for CHI
# Matches: "CHI '15", "CHI '20", "CHI 2020", "CHI 2015", "CHI  '15"
# Also full name: "Conference on Human Factors in Computing Systems"
regex_chi = re.compile(r"\bCHI\s*['’]?\d{2}|\bCHI\s+20\d{2}|Conference on Human Factors in Computing Systems", re.IGNORECASE)

for paper in papers_data:
    text = paper.get('text', '')
    # Check first 1000 chars
    header = text[:1000]
    if regex_chi.search(header):
        title = paper.get('filename', '').replace('.txt', '')
        chi_papers.append(paper)
        chi_titles.append(title)

print(f"Identified {len(chi_papers)} CHI papers.")
# print(f"Sample CHI titles: {chi_titles[:5]}")

total_citations = 0
found_count = 0
missing_count = 0

for title in chi_titles:
    if title in citations_map:
        total_citations += citations_map[title]
        found_count += 1
    else:
        # Check if title mismatch due to case or spacing?
        # The prompt says: "The paper title in the Citations SQLite table matches the filename (without .txt extension)"
        # So exact match should work.
        missing_count += 1

print(f"Matched {found_count} papers in citations db. Missing {missing_count}.")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-3161297584091160815': ['paper_docs'], 'var_function-call-3161297584091160886': ['Citations', 'sqlite_sequence'], 'var_function-call-16261242641906617785': 'file_storage/function-call-16261242641906617785.json', 'var_function-call-4279784200820574316': 'file_storage/function-call-4279784200820574316.json', 'var_function-call-13891558846941465066': 'file_storage/function-call-13891558846941465066.json'}

exec(code, env_args)
