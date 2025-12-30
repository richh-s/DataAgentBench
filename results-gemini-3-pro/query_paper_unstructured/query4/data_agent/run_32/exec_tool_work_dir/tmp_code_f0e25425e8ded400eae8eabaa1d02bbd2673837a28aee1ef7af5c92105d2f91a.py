code = """import json
import os

# Load paper_docs
paper_docs_path = locals()['var_function-call-14925158578354177648']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load Citations
citations_path = locals()['var_function-call-15838681542065948214']
with open(citations_path, 'r') as f:
    citations = json.load(f)

matching_papers = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 2016 in the first 1000 chars. 
    # Also check for "Copyright 2016" or conference headers.
    # To be safe, let's look for "2016" in the first 1000 chars.
    header_text = text[:1000]
    is_2016 = '2016' in header_text
    
    # Extract Domain
    # Check for "physical activity" in the full text (case insensitive)
    is_physical_activity = 'physical activity' in text.lower()
    
    if is_2016 and is_physical_activity:
        matching_papers.append(title)

# Calculate total citations for matching papers
results = []
for title in matching_papers:
    total_citations = 0
    for citation in citations:
        if citation['title'].strip().lower() == title.strip().lower():
             total_citations += int(citation['citation_count'])
    results.append({'title': title, 'total_citation_count': total_citations})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1637384971147103697': ['paper_docs'], 'var_function-call-1637384971147100208': ['Citations', 'sqlite_sequence'], 'var_function-call-12832305372190774842': 'file_storage/function-call-12832305372190774842.json', 'var_function-call-8891803198092466496': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-15218699156222790202': 5, 'var_function-call-14925158578354177648': 'file_storage/function-call-14925158578354177648.json', 'var_function-call-15838681542065948214': 'file_storage/function-call-15838681542065948214.json'}

exec(code, env_args)
