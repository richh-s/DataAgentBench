code = """import json
import re

# Load paper docs
with open(locals()['var_function-call-14323313354234643834'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-7764328309385985012'], 'r') as f:
    citations = json.load(f)

# Aggregate citations by title
citation_map = {}
for c in citations:
    t = c['title']
    count = c['citation_count']
    citation_map[t] = citation_map.get(t, 0) + count

results = []

for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 2016 in the first 1000 characters
    header = text[:1000]
    # Simple regex for year
    # We specifically look for 2016 to filter
    # But let's extract the year generally to be safe
    years = re.findall(r'\b(20\d{2})\b', header)
    
    published_in_2016 = False
    if '2016' in years:
        published_in_2016 = True
    
    # Extract Domain
    # Check if 'physical activity' is in the text (case insensitive)
    # The prompt suggests looking at keywords, but searching the whole text is safer for recall 
    # as long as we don't get too many false positives.
    # Given the specificity, let's search in the first 5000 chars (header + abstract + intro)
    content_sample = text[:5000].lower()
    is_physical_activity = 'physical activity' in content_sample
    
    if published_in_2016 and is_physical_activity:
        # Get citation count
        total_citations = citation_map.get(title, 0)
        results.append({"title": title, "citation_count": total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8814252410451424238': ['paper_docs'], 'var_function-call-5259206578733669392': 'file_storage/function-call-5259206578733669392.json', 'var_function-call-14323313354234643834': 'file_storage/function-call-14323313354234643834.json', 'var_function-call-12161874527337870347': ['Citations', 'sqlite_sequence'], 'var_function-call-7764328309385985012': 'file_storage/function-call-7764328309385985012.json'}

exec(code, env_args)
