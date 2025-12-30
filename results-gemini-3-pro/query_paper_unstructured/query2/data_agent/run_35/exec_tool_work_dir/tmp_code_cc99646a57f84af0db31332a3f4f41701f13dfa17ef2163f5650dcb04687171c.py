code = """import json

# Load citations
with open(locals()['var_function-call-5092927225989285410'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-2239282102762620256'], 'r') as f:
    paper_docs = json.load(f)

# Identify ACM papers
acm_titles = set()
for doc in paper_docs:
    text = doc.get('text', '')
    if "ACM" in text: 
        title = doc['filename'].replace('.txt', '')
        acm_titles.add(title)

# Filter citations
acm_citations = []
for cit in citations_data:
    if cit['title'] in acm_titles:
        try:
            count = int(cit['citation_count'])
            acm_citations.append(count)
        except ValueError:
            continue # Handle cases where citation_count might not be a valid int

# Calculate average
if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
else:
    avg_citation = 0

print("__RESULT__:")
print(json.dumps(avg_citation))"""

env_args = {'var_function-call-5092927225989285410': 'file_storage/function-call-5092927225989285410.json', 'var_function-call-2239282102762620256': 'file_storage/function-call-2239282102762620256.json'}

exec(code, env_args)
