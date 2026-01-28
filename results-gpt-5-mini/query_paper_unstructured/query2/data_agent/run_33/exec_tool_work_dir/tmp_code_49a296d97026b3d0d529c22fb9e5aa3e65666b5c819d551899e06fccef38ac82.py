code = """import json
with open(var_call_s2L9n5FvYwuoXzIUTTRBT7kd, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_mCuZg5iKPsfdwCKdDFRVhAXR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

def title_from_filename(fn):
    return fn[:-4] if fn.lower().endswith('.txt') else fn

title_to_text = { title_from_filename(d.get('filename','')): d.get('text','') for d in paper_docs }

import re
pattern = re.compile(r"\bACM\b", re.IGNORECASE)

matched = []
for rec in citations:
    title = rec.get('title')
    count_raw = rec.get('citation_count')
    try:
        count = int(count_raw)
    except:
        try:
            count = int(float(count_raw))
        except:
            count = None
    text = title_to_text.get(title)
    has_acm = False
    if text and pattern.search(text):
        has_acm = True
    matched.append({'title': title, 'citation_count': count, 'has_text': bool(text), 'has_acm_in_text': has_acm})

# Summary
total_citations = len(citations)
has_text_count = sum(1 for m in matched if m['has_text'])
has_acm_count = sum(1 for m in matched if m['has_acm_in_text'])

result = {
    'total_citations_2018': total_citations,
    'papers_with_text_in_mongo': has_text_count,
    'papers_with_ACM_in_text': has_acm_count,
    'sample_matches': matched[:20]
}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_4TLSbqKdwtqhq1Vnnxhqk1BW': ['paper_docs'], 'var_call_s2L9n5FvYwuoXzIUTTRBT7kd': 'file_storage/call_s2L9n5FvYwuoXzIUTTRBT7kd.json', 'var_call_ooNYWIIpdQsyKmBg6iMSVvXp': ['Citations', 'sqlite_sequence'], 'var_call_mCuZg5iKPsfdwCKdDFRVhAXR': 'file_storage/call_mCuZg5iKPsfdwCKdDFRVhAXR.json', 'var_call_oyuZVcUutsJqKKX0IJCFGREN': {'average_citation_count': None, 'paper_count': 0}}

exec(code, env_args)
