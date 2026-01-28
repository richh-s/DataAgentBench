code = """import json
import re

# Load the data from storage
citations_path = locals()['var_functions.query_db:0']
papers_path = locals()['var_functions.query_db:2']

with open(citations_path, 'r') as f:
    citations_2018 = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

print(f"Loaded {len(citations_2018)} citation records for 2018")
print(f"Loaded {len(papers)} paper documents")

# Extract paper information with a simpler approach
acm_paper_titles = set()

# Look for ACM in the text of each paper document
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Check if ACM appears in the text (case insensitive)
    if 'acm' in text.lower():
        acm_paper_titles.add(title.lower())

print(f"Found {len(acm_paper_titles)} ACM papers")

# Match citations with ACM papers
acm_citation_counts = []
for citation in citations_2018:
    citation_title = citation['title'].lower()
    if citation_title in acm_paper_titles:
        acm_citation_counts.append(int(citation['citation_count']))

print(f"Found {len(acm_citation_counts)} ACM papers with 2018 citations")

# Calculate average
if acm_citation_counts:
    average_citations = sum(acm_citation_counts) / len(acm_citation_counts)
    print(f"Average citation count: {average_citations:.2f}")
else:
    print("No ACM papers found with citations in 2018")

# Show some examples
print("\nSample ACM paper citations in 2018:")
count = 0
for citation in citations_2018:
    if count >= 5:
        break
    if citation['title'].lower() in acm_paper_titles:
        print(f"{citation['title']}: {citation['citation_count']} citations")
        count += 1"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
