code = """import json, re

# Load full citations result
with open(var_call_w2WtTDPNwBTXjmi1YYx2x0y6, 'r') as f:
    citations = json.load(f)

# Build a set of titles cited in 2020
titles_2020 = {c['title'] for c in citations}

# Load paper docs
with open(var_call_qN0xpZYO5YtcKqz2AJxpxtGk, 'r') as f:
    docs = json.load(f)

chi_titles = set()
for doc in docs:
    filename = doc.get('filename', '')
    title = re.sub(r'\.txt$', '', filename)
    text = doc.get('text', '').upper()
    if ' CHI ' in text or "CHI '" in text or '\nCHI ' in text:
        chi_titles.add(title)

chi_cited_2020 = {t for t in titles_2020 if t in chi_titles}

total_citations = 0
for c in citations:
    if c['title'] in chi_cited_2020:
        try:
            total_citations += int(c['citation_count'])
        except Exception:
            pass

out = json.dumps(total_citations)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_w2WtTDPNwBTXjmi1YYx2x0y6': 'file_storage/call_w2WtTDPNwBTXjmi1YYx2x0y6.json', 'var_call_19IsZbyNimik3aHfkGZI9BT7': ['paper_docs'], 'var_call_qN0xpZYO5YtcKqz2AJxpxtGk': 'file_storage/call_qN0xpZYO5YtcKqz2AJxpxtGk.json'}

exec(code, env_args)
