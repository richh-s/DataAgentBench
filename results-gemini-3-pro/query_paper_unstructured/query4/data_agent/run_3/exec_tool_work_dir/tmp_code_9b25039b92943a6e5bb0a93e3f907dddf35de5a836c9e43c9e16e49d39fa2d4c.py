code = """import json

# Load Citations
# The previous query result for citations is a list of dicts: [{'title': '...', 'total_citations': '53'}, ...]
# Access via var_function-call-1669477486731597489
with open(locals()['var_function-call-1669477486731597489'], 'r') as f:
    citations_data = json.load(f)

# Convert to dict for easy lookup
citation_map = {}
for entry in citations_data:
    try:
        count = int(entry['total_citations'])
    except:
        count = 0
    citation_map[entry['title']] = count

# Load Paper Docs
# Access via var_function-call-1669477486731597534
with open(locals()['var_function-call-1669477486731597534'], 'r') as f:
    paper_docs = json.load(f)

results = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract Title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    # Extract Year
    # Check first 2000 chars for "2016"
    # To be more robust, we might look for specific patterns, but "2016" in header/copyright is a good heuristic.
    header_text = text[:2000]
    
    # Check for 2016
    is_2016 = '2016' in header_text
    
    # Extract Domain
    # Check for "physical activity" in text (case insensitive)
    # Hint says substring matching
    is_physical_activity = 'physical activity' in text.lower()
    
    if is_2016 and is_physical_activity:
        # Get citation count
        count = citation_map.get(title, 0)
        results.append({
            "title": title,
            "citation_count": count
        })

# Sort results by citation count descending (optional but nice) or just print
# The prompt doesn't specify sort order.
# I'll output the list.

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json'}

exec(code, env_args)
