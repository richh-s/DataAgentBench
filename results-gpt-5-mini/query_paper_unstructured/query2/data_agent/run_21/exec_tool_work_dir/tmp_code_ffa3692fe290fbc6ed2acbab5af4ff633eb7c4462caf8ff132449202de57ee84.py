code = """import json, re
# Load tool results from storage files
with open(var_call_0IhcTd0dtQfLFy75CHzl4H5f, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_KPR0QfG3IgVsiP9AnZrxJYky, 'r', encoding='utf-8') as f:
    papers = json.load(f)

# Build title -> source mapping by inspecting paper text
title_to_source = {}
for p in papers:
    filename = p.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = p.get('text', '') or ''
    src = 'Unknown'
    if re.search(r'\bACM\b', text, re.IGNORECASE):
        src = 'ACM'
    elif re.search(r'\bIEEE\b', text, re.IGNORECASE):
        src = 'IEEE'
    elif re.search(r'PubMed', text, re.IGNORECASE) or re.search(r'Pub Med', text, re.IGNORECASE):
        src = 'PubMed'
    title_to_source[title] = src

# Collect citation counts for citation_year=2018 (already filtered in query) for ACM papers
counts = []
for c in citations:
    title = c.get('title')
    if title in title_to_source and title_to_source[title] == 'ACM':
        try:
            counts.append(int(c.get('citation_count', 0)))
        except:
            try:
                counts.append(int(float(c.get('citation_count')))
            except:
                pass

if len(counts) > 0:
    avg = sum(counts) / len(counts)
else:
    avg = None

result = {
    'average_citation_count': (avg if avg is None else round(avg, 4)),
    'paper_count': len(counts)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ACVHbXhs6Dqf6k8Z8Zu1aBoy': ['paper_docs'], 'var_call_0IhcTd0dtQfLFy75CHzl4H5f': 'file_storage/call_0IhcTd0dtQfLFy75CHzl4H5f.json', 'var_call_KPR0QfG3IgVsiP9AnZrxJYky': 'file_storage/call_KPR0QfG3IgVsiP9AnZrxJYky.json'}

exec(code, env_args)
