code = """import json
import re

# Load data from previous tool calls stored in variables
# var_call_rsTGBzAeF8wapUyg7hdHa7DT and var_call_XV7Lnb57Epzr6zYWSxiVmjVB

# Helper to load either from a file path string or use as-is
def load_var(v):
    if isinstance(v, str):
        # assume it's a file path to a .json
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            # maybe it's a direct JSON string
            try:
                return json.loads(v)
            except Exception:
                return None
    else:
        return v

paper_docs = load_var(var_call_rsTGBzAeF8wapUyg7hdHa7DT)
citations_agg = load_var(var_call_XV7Lnb57Epzr6zYWSxiVmjVB)

# Build citation dict: title -> total_citations (int)
cit_dict = {}
if isinstance(citations_agg, list):
    for rec in citations_agg:
        t = rec.get('title')
        tc = rec.get('total_citations')
        try:
            tc_int = int(tc)
        except Exception:
            try:
                tc_int = int(float(tc))
            except Exception:
                tc_int = 0
        cit_dict[t] = tc_int

results = []

if isinstance(paper_docs, list):
    for doc in paper_docs:
        filename = doc.get('filename', '')
        text = doc.get('text', '') or ''
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        # find first year-like token in the text
        year_match = re.search(r'\b(19|20)\d{2}\b', text)
        year = None
        if year_match:
            try:
                year = int(year_match.group(0))
            except:
                year = None
        # check contribution contains 'empirical' (case-insensitive)
        is_empirical = 'empirical' in text.lower()
        if year is not None and year > 2016 and is_empirical:
            total_citations = cit_dict.get(title, 0)
            results.append({'title': title, 'total_citations': total_citations, 'year': year})

# Prepare JSON-serializable output: list of dicts with title and total_citations
out = [{'title': r['title'], 'total_citations': r['total_citations']} for r in results]

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_rsTGBzAeF8wapUyg7hdHa7DT': 'file_storage/call_rsTGBzAeF8wapUyg7hdHa7DT.json', 'var_call_XV7Lnb57Epzr6zYWSxiVmjVB': 'file_storage/call_XV7Lnb57Epzr6zYWSxiVmjVB.json'}

exec(code, env_args)
