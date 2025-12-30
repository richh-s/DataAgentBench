code = """import json
import os

# Load paper_docs
with open(locals()['var_function-call-13906461946553771185'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-3552239526712038918'], 'r') as f:
    citations = json.load(f)

matching_titles = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Check Year: Look for 2016 in first 1000 chars
    # Heuristic: often in header "Conference 2016" or "Copyright 2016"
    # To be safer, just check if "2016" is present in the beginning.
    header = text[:1000]
    if "2016" in header:
        # Check Domain: "physical activity" (case insensitive)
        # Search in a larger chunk, e.g., first 5000 chars or full text?
        # Hint says "For each paper, you may need to extract: ... domain"
        # and "Common domains include: ... physical activity".
        # It's likely in the abstract or keywords.
        content_to_search = text[:5000].lower()
        if "physical activity" in content_to_search:
            matching_titles.append(title)

# Filter citations
results = {}
for citation in citations:
    c_title = citation.get('title')
    c_count = int(citation.get('citation_count', 0))
    
    if c_title in matching_titles:
        if c_title not in results:
            results[c_title] = 0
        results[c_title] += c_count

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5218844926592326471': ['paper_docs'], 'var_function-call-5218844926592327304': ['Citations', 'sqlite_sequence'], 'var_function-call-3045611188522186041': 'file_storage/function-call-3045611188522186041.json', 'var_function-call-13906461946553771185': 'file_storage/function-call-13906461946553771185.json', 'var_function-call-3552239526712038918': 'file_storage/function-call-3552239526712038918.json'}

exec(code, env_args)
