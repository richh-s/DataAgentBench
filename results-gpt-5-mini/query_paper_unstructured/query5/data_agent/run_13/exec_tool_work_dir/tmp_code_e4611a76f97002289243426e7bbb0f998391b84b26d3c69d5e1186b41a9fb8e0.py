code = """import json
import re
# Load citations from SQLite query result file
citations_path = var_call_GFY4OJaYJwwlSMS6nFnauMDQ
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Load paper docs from Mongo query result file
papers_path = var_call_tLJRvHiVzDPuiKSyA6QDVHfw
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
# Build map from title to text
papers_map = {}
for p in papers:
    fn = p.get('filename', '')
    if fn.endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    papers_map[title] = p.get('text', '')
# Process citations and find those matching CHI venue
def is_chi(text):
    if not text:
        return False
    header = text[:2000]
    up = header.upper()
    # check for explicit SIGCHI/CHI proceedings phrases
    if 'PROCEEDINGS OF THE SIGCHI' in up or 'PROCEEDINGS OF THE CHI' in up or 'SIGCHI CONFERENCE' in up or 'ACM CHI' in up:
        return True
    # word-boundary CHI
    if re.search(r"\bCHI\b", header):
        return True
    return False

matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    count_raw = rec.get('citation_count', 0)
    try:
        count = int(count_raw)
    except:
        try:
            count = int(float(count_raw))
        except:
            count = 0
    # find paper text
    text = papers_map.get(title)
    if text and is_chi(text):
        matched.append({'title': title, 'citation_count': count})
        total += count
# Prepare result
result = {
    'total_citations_2020_for_CHI_papers': total,
    'num_matched_papers': len(matched),
    'matched_papers_sample': matched[:200]
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GFY4OJaYJwwlSMS6nFnauMDQ': 'file_storage/call_GFY4OJaYJwwlSMS6nFnauMDQ.json', 'var_call_Q0KHbpchSx4GRnFX7lhyIr79': 'file_storage/call_Q0KHbpchSx4GRnFX7lhyIr79.json', 'var_call_tLJRvHiVzDPuiKSyA6QDVHfw': 'file_storage/call_tLJRvHiVzDPuiKSyA6QDVHfw.json'}

exec(code, env_args)
