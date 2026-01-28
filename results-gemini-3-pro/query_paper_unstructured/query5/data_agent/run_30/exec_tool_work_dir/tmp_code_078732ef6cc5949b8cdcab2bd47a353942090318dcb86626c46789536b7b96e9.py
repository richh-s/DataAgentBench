code = """import json
import re

# Load citations
with open(locals()['var_function-call-7711183651007727056'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-4121090962908109712'], 'r') as f:
    paper_docs_data = json.load(f)

# Create a lookup for paper text by title
# filename is "Title.txt"
paper_map = {}
for doc in paper_docs_data:
    if 'filename' in doc and 'text' in doc:
        title = doc['filename'].replace('.txt', '')
        paper_map[title] = doc['text']

total_citations = 0
cited_papers = []

# Filter citations for 2020 and check venue
for record in citations_data:
    # citation_year is int in DB schema but might be string in JSON if not cast? 
    # Preview showed "citation_count": "65", but "citation_year" was not in preview.
    # The query was "SELECT title, citation_count FROM Citations WHERE citation_year = 2020".
    # So all records here are for 2020.
    
    title = record['title']
    count = int(record['citation_count'])
    
    if title in paper_map:
        text = paper_map[title]
        # Check for CHI in the first 2000 chars
        # Look for whole word CHI
        header_text = text[:2000]
        if re.search(r'\bCHI\b', header_text):
            total_citations += count
            cited_papers.append(title)
        elif "Conference on Human Factors in Computing Systems" in header_text:
            total_citations += count
            cited_papers.append(title)

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-7711183651007727056': 'file_storage/function-call-7711183651007727056.json', 'var_function-call-4121090962908109712': 'file_storage/function-call-4121090962908109712.json'}

exec(code, env_args)
