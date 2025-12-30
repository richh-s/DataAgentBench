code = """import json, re
import pandas as pd

# Load citations for 2020 from storage file
with open(var_call_XfVY2LtnN68c9JyztuuX7Ozl, 'r') as f:
    citations_2020 = json.load(f)

# Load paper docs
with open(var_call_hUeYhHMnczfmuvq1REld6Ovl, 'r') as f:
    paper_docs = json.load(f)

# Build map from title to venue by parsing text
venue_map = {}
for doc in paper_docs:
    filename = doc.get('filename','')
    title = re.sub(r"\.txt$","", filename)
    text = doc.get('text','')
    # Simple venue detection: look for known venues near top of paper
    header = text[:1000].upper()
    venue = None
    for v in ["CHI", "UBICOMP", "CSCW", "DIS", "PERVASIVEHEALTH", "WWW", "IUI", "OZCHI", "TEI", "AH"]:
        if v in header:
            venue = v
            break
    venue_map[title] = venue

# Sum citation counts for papers that are CHI venue and cited in 2020
chi_citations_total = 0
for rec in citations_2020:
    title = rec['title']
    count = int(rec['citation_count']) if rec['citation_count'] is not None else 0
    venue = venue_map.get(title)
    if venue == 'CHI':
        chi_citations_total += count

result = chi_citations_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XfVY2LtnN68c9JyztuuX7Ozl': 'file_storage/call_XfVY2LtnN68c9JyztuuX7Ozl.json', 'var_call_iKybNZf9zMsurKcVooYY2Z9I': ['paper_docs'], 'var_call_hUeYhHMnczfmuvq1REld6Ovl': 'file_storage/call_hUeYhHMnczfmuvq1REld6Ovl.json'}

exec(code, env_args)
