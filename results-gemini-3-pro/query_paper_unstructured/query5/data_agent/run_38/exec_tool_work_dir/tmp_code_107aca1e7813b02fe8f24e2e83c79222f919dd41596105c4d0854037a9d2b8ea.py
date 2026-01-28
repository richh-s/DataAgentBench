code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-937877723818181910']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Filter citations for 2020 and create a lookup
citations_2020 = {}
for entry in citations_data:
    if str(entry['citation_year']) == '2020':
        # Ensure count is int
        count = int(entry['citation_count'])
        citations_2020[entry['title']] = count

print(f"Loaded {len(citations_2020)} citations for 2020.")

# Load papers
papers_file = locals()['var_function-call-4834077622578291638']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print(f"Loaded {len(papers_data)} papers.")

chi_papers_count = 0
total_citations = 0

# Regex for CHI venue
# Patterns:
# CHI '16
# CHI 2016
# CHI Conference
# Conference on Human Factors in Computing Systems
chi_patterns = [
    r"CHI\s+'\d{2}",
    r"CHI\s+20\d{2}",
    r"CHI\s+Conference",
    r"Conference on Human Factors in Computing Systems"
]
compiled_patterns = [re.compile(p, re.IGNORECASE) for p in chi_patterns]

matched_titles = []

for paper in papers_data:
    text = paper.get('text', '')
    # Check first 2000 chars
    header = text[:2000]
    
    is_chi = False
    for p in compiled_patterns:
        if p.search(header):
            is_chi = True
            break
            
    if is_chi:
        chi_papers_count += 1
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '')
        
        if title in citations_2020:
            total_citations += citations_2020[title]
            matched_titles.append(title)

print(f"Identified {chi_papers_count} CHI papers.")
print(f"Matched {len(matched_titles)} CHI papers with citations in 2020.")
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-937877723818181910': 'file_storage/function-call-937877723818181910.json', 'var_function-call-937877723818184371': 'file_storage/function-call-937877723818184371.json', 'var_function-call-5956507868376137751': 'file_storage/function-call-5956507868376137751.json', 'var_function-call-4834077622578291638': 'file_storage/function-call-4834077622578291638.json'}

exec(code, env_args)
