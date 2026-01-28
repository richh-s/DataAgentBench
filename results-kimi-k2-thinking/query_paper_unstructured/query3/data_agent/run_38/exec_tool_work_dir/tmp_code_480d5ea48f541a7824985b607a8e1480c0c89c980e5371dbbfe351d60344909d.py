code = """import json
import re

# Load the paper documents from the file
with open('var_functions.query_db:0.json', 'r') as f:
    paper_docs = json.load(f)

# Load the citations data from the file
with open('var_functions.query_db:2.json', 'r') as f:
    citations = json.load(f)

print(f"Total papers: {len(paper_docs)}")
print(f"Total citation records: {len(citations)}")

# Extract paper information
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit years in text, especially near conference info
    year_match = re.search(r"(20\d{2})", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract contribution - look for empirical in text (case insensitive)
    has_empirical = 'empirical' in text.lower()
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'text_preview': text[:500]  # For debugging
    })

# Filter papers: has empirical and published after 2016
filtered_papers = [p for p in papers if p['has_empirical'] and p['year'] and p['year'] > 2016]

print(f"Papers with empirical and year > 2016: {len(filtered_papers)}")

# Show first few filtered papers
for p in filtered_papers[:5]:
    print(f"\nTitle: {p['title']}")
    print(f"Year: {p['year']}")
    print(f"Has empirical: {p['has_empirical']}")

# For citations, group by title and sum counts
citation_dict = {}
for cit in citations:
    title = cit['title']
    count = int(cit['citation_count'])
    citation_dict[title] = citation_dict.get(title, 0) + count

print(f"\nTotal unique papers with citations: {len(citation_dict)}")

# Match papers with citations
result = []
for paper in filtered_papers:
    title = paper['title']
    if title in citation_dict:
        result.append({
            'title': title,
            'total_citations': citation_dict[title],
            'year': paper['year']
        })

print(f"\nMatching papers: {len(result)}")

# Sort by citations descending
result_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

# Format output
output = []
for item in result_sorted:
    output.append(f"{item['title']}: {item['total_citations']} citations")

__RESULT__ = json.dumps(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
