code = """import json
import re

# Load the large results from the stored JSON files
with open(var_call_s2L9n5FvYwuoXzIUTTRBT7kd, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_mCuZg5iKPsfdwCKdDFRVhAXR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build mapping from title (filename without .txt) to text
def title_from_filename(fn):
    return fn[:-4] if fn.lower().endswith('.txt') else fn

title_to_text = { title_from_filename(d.get('filename','')): d.get('text','') for d in paper_docs }

# Iterate over citations from 2018 (query already filtered) and find those whose paper text contains 'ACM'
acm_counts = []
pattern = re.compile(r"\bACM\b", re.IGNORECASE)
for rec in citations:
    title = rec.get('title')
    # Some citation_count fields are strings; convert safely
    try:
        count = int(rec.get('citation_count'))
    except Exception:
        try:
            count = int(float(rec.get('citation_count')))
        except Exception:
            continue
    # Find matching paper doc
    text = title_to_text.get(title)
    if text and pattern.search(text):
        acm_counts.append(count)

# Compute average
if len(acm_counts) > 0:
    avg = sum(acm_counts) / len(acm_counts)
    # Round to 4 decimal places for clarity
    avg_rounded = round(avg, 4)
else:
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'paper_count': len(acm_counts)
}

import json as _json
print('__RESULT__:')
print(_json.dumps(result))"""

env_args = {'var_call_4TLSbqKdwtqhq1Vnnxhqk1BW': ['paper_docs'], 'var_call_s2L9n5FvYwuoXzIUTTRBT7kd': 'file_storage/call_s2L9n5FvYwuoXzIUTTRBT7kd.json', 'var_call_ooNYWIIpdQsyKmBg6iMSVvXp': ['Citations', 'sqlite_sequence'], 'var_call_mCuZg5iKPsfdwCKdDFRVhAXR': 'file_storage/call_mCuZg5iKPsfdwCKdDFRVhAXR.json'}

exec(code, env_args)
