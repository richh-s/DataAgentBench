code = """import json, re
import pandas as pd

# load mongo docs
src = var_call_PXiqPkivBLVhRAWPZ3YcSN5A
if isinstance(src, str):
    with open(src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = src

chi_titles = []
for d in docs:
    fn = d.get('filename','')
    if not fn.endswith('.txt'):
        continue
    title = fn[:-4]
    text = (d.get('text') or '')
    # venue heuristic: look for CHI in top header/citation lines
    top = text[:2000]
    if re.search(r"\bCHI\b", top) and re.search(r"\bACM\b", top):
        # but exclude obvious non-CHI like UBICOMP, CSCW, DIS etc if present prominently
        if re.search(r"\b(UBICOMP|UbiComp|CSCW|DIS|IUI|WWW|TEI|OzCHI|PervasiveHealth)\b", top):
            # allow OzCHI? but question wants CHI only
            continue
        chi_titles.append(title)

# get citations in 2020 for these titles
# query citations db for all 2020 citations and merge in python
# (cannot access db here; only have prior SQL sum, so return titles count and note inability)
result = {
    "chi_papers_detected": len(chi_titles),
    "note": "Need citation join query; only overall 2020 sum already fetched.",
    "overall_total_citations_2020_all_titles": int(var_call_7iNfHZtOPqgKiIE2K6G3FtoQ[0]['total_citations_2020']) if var_call_7iNfHZtOPqgKiIE2K6G3FtoQ and var_call_7iNfHZtOPqgKiIE2K6G3FtoQ[0]['total_citations_2020'] is not None else None
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_7iNfHZtOPqgKiIE2K6G3FtoQ': [{'total_citations_2020': '9576'}], 'var_call_PXiqPkivBLVhRAWPZ3YcSN5A': 'file_storage/call_PXiqPkivBLVhRAWPZ3YcSN5A.json'}

exec(code, env_args)
