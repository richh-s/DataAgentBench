code = """import json

# Load full citations data from file
with open(var_call_41vyzEOvQmesQKDpUrzUvfbV, 'r') as f:
    citations = json.load(f)

# Build a map title -> total citations in 2020
cit_map = {c['title']: int(c['citation_count']) for c in citations}

# Load CHI-related papers from paper docs
with open(var_call_IA7MqvnB8uzFGVLmM7S7rk63, 'r') as f:
    papers = json.load(f)

# Identify CHI venue papers using simple heuristic: look for "CHI" patterns in the text
chi_titles = set()
for doc in papers:
    text = doc.get('text', '')
    lower = text.lower()
    if ' chi ' in lower or " chi'" in lower or "\nchi" in lower:
        filename = doc.get('filename', '')
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        chi_titles.add(title)

# Sum citation counts for CHI papers cited in 2020
total_citations_2020_chi = sum(cit_map.get(title, 0) for title in chi_titles)

result = json.dumps({"total_citations_2020_chi": total_citations_2020_chi})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_41vyzEOvQmesQKDpUrzUvfbV': 'file_storage/call_41vyzEOvQmesQKDpUrzUvfbV.json', 'var_call_jIY4Q0yv7KgsG0GlhNTWM8Wk': ['paper_docs'], 'var_call_IA7MqvnB8uzFGVLmM7S7rk63': 'file_storage/call_IA7MqvnB8uzFGVLmM7S7rk63.json'}

exec(code, env_args)
