code = """import json
import re

# Load paper_docs
with open(var_function_call_15160889356619040949, 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(var_function_call_14370993471195573993, 'r') as f:
    citations_data = json.load(f)

# Process citations: Group by title and sum counts
citation_counts = {}
for record in citations_data:
    title = record['title']
    count = int(record['citation_count'])
    citation_counts[title] = citation_counts.get(title, 0) + count

# Process papers
results = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    text = doc.get('text', '')
    
    # Extract Year
    # Look for years 2017-2029 in the first 2000 characters
    # We want papers published AFTER 2016, so 2017+
    header_text = text[:2000]
    match = re.search(r'\b(201[7-9]|202[0-9])\b', header_text)
    
    year = None
    if match:
        year = int(match.group(1))
    
    # Check contribution
    # "empirical" in text
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        count = citation_counts.get(title, 0)
        results.append({
            "title": title,
            "citation_count": count
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15160889356619040949': 'file_storage/function-call-15160889356619040949.json', 'var_function-call-14370993471195573993': 'file_storage/function-call-14370993471195573993.json'}

exec(code, env_args)
