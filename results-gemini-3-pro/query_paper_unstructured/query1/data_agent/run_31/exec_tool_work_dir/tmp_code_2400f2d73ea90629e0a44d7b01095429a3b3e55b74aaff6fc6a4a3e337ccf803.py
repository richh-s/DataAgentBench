code = """import json
import re

citations_path = locals()['var_function-call-99245770254800995']
papers_path = locals()['var_function-call-5874155478376628757']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

food_papers = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # regex to find keywords
    # Look for 'Author Keywords' and capture text until 'ACM Classification' or double newline followed by uppercase
    # We use a simple approach: extract 500 chars after 'Author Keywords' and split
    
    match = re.search(r'Author Keywords(.*?)(?=ACM Classification|INTRODUCTION|\n[A-Z]+[A-Z\s]{5,})', text, re.DOTALL | re.IGNORECASE)
    
    keywords = ""
    if match:
        keywords = match.group(1)
    
    # Check if 'food' in keywords
    # Normalize
    keywords_lower = keywords.lower()
    
    if 'food' in keywords_lower:
        food_papers.append(title)

total_citations = 0
for cit in citations:
    if cit['title'] in food_papers:
        c = cit['citation_count']
        if isinstance(c, str):
            c = int(c) if c.strip() else 0
        total_citations += c

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "food_papers": food_papers}))"""

env_args = {'var_function-call-853909438841445340': 'file_storage/function-call-853909438841445340.json', 'var_function-call-1978902813264061650': 'file_storage/function-call-1978902813264061650.json', 'var_function-call-99245770254800995': 'file_storage/function-call-99245770254800995.json', 'var_function-call-5874155478376628757': 'file_storage/function-call-5874155478376628757.json'}

exec(code, env_args)
