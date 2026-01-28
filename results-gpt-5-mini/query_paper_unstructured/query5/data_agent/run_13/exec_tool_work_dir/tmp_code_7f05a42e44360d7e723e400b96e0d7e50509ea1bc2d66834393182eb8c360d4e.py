code = """import json
import re
citations_path = var_call_GFY4OJaYJwwlSMS6nFnauMDQ
papers_path = var_call_tLJRvHiVzDPuiKSyA6QDVHfw
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(papers_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)
# Build map title->text
papers_map = {}
for p in papers:
    fn = p.get('filename','')
    title = fn[:-4] if fn.endswith('.txt') else fn
    papers_map[title] = p.get('text','')

def is_chi(text):
    if not text:
        return False
    up = text.upper()
    # common explicit patterns
    if 'PROCEEDINGS OF THE SIGCHI' in up or 'PROCEEDINGS OF THE CHI' in up or 'ACM CHI' in up or 'SIGCHI' in up:
        return True
    # patterns like "CHI 2015", "CHI'15", "CHI 15"
    if re.search(r"\bCHI\b\s*(?:'\d{2}|\d{4}|\d{2})", up):
        return True
    # patterns like "CHI conference" or "CHI proceedings"
    if re.search(r"\bCHI\b.*(CONFERENCE|PROCEEDINGS|PRESIDING|EXTENDED|PAPER)", up):
        return True
    return False

matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    try:
        count = int(rec.get('citation_count',0))
    except:
        try:
            count = int(float(rec.get('citation_count',0)))
        except:
            count = 0
    text = papers_map.get(title)
    if text and is_chi(text):
        matched.append({'title': title, 'citation_count': count})
        total += count
# If no matches found, attempt looser matching: search title list for known CHI years in filename? But first return results
result = {'total_citations_2020_for_CHI_papers': total, 'num_matched_papers': len(matched), 'matched_papers_sample': matched[:200]}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GFY4OJaYJwwlSMS6nFnauMDQ': 'file_storage/call_GFY4OJaYJwwlSMS6nFnauMDQ.json', 'var_call_Q0KHbpchSx4GRnFX7lhyIr79': 'file_storage/call_Q0KHbpchSx4GRnFX7lhyIr79.json', 'var_call_tLJRvHiVzDPuiKSyA6QDVHfw': 'file_storage/call_tLJRvHiVzDPuiKSyA6QDVHfw.json', 'var_call_ixgsA85dsNHNgYxvDRYz2HY8': {'total_citations_2020_for_CHI_papers': 0, 'num_matched_papers': 0, 'matched_papers_sample': []}}

exec(code, env_args)
