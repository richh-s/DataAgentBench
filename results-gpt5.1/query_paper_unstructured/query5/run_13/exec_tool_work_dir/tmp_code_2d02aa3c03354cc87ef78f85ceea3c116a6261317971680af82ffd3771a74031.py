code = """import json, re

# Load Mongo result from file
mongo_path = var_call_W2oJpWHkDBFZxqU7ZJOYjY18
with open(mongo_path, 'r') as f:
    mongo_docs = json.load(f)

# Extract titles and detect CHI venue heuristically from text
chi_titles = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    # Heuristic: look for "CHI" near ACM copyright/footer or as conference name
    if re.search(r"CHI '\d+" , text) or 'Conference on Human Factors in Computing Systems' in text or 'CHI Conference' in text:
        filename = doc.get('filename', '')
        if filename.endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load citations for 2020
citations_path = var_call_zNHwpztmHAvNXFNqsfakVhuM
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Sum citation_count for records where title in chi_titles
total_citations = 0
for row in citations:
    title = row.get('title')
    if title in chi_titles:
        try:
            c = int(row.get('citation_count', 0))
        except ValueError:
            c = 0
        total_citations += c

result = {"total_citations_for_CHI_papers_cited_in_2020": total_citations}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_W2oJpWHkDBFZxqU7ZJOYjY18': 'file_storage/call_W2oJpWHkDBFZxqU7ZJOYjY18.json', 'var_call_zNHwpztmHAvNXFNqsfakVhuM': 'file_storage/call_zNHwpztmHAvNXFNqsfakVhuM.json'}

exec(code, env_args)
