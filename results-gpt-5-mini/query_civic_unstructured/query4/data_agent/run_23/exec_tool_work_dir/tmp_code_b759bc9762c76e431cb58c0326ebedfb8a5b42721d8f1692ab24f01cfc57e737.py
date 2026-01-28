code = """import json
import re

with open(var_call_4HdUiHnSFJBjIwK87YHCGUTC, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_wwbgDMXQ67DvK4hs4ybAOibf, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# build funding map by normalized name
import string

def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    # remove parenthetical parts
    s = re.sub(r"\([^)]*\)", "", s)
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = re.sub(r"\s+", " ", s).strip()
    return s

funding_map = {}
for r in funding_rows:
    name = r.get('Project_Name')
    amt_raw = r.get('Amount')
    try:
        amt = int(float(amt_raw))
    except:
        amt = 0
    norm = normalize(name)
    funding_map.setdefault(norm, 0)
    funding_map[norm] += amt

# list of funding project names (original)
funding_names = [r.get('Project_Name') for r in funding_rows if r.get('Project_Name')]

# compile spring indicators
spring_indicators = [r"spring", r"march 2022", r"april 2022", r"may 2022", r"2022-03", r"2022-04", r"2022-05", r"03/2022", r"04/2022", r"05/2022", r"2022/03", r"2022/04", r"2022/05", r"mar 2022", r"apr 2022", r"may 2022"]
spring_re = re.compile("(" + "|".join([re.escape(s) for s in spring_indicators]) + ")", re.IGNORECASE)

matched_projects = {}

for orig_name in funding_names:
    if not orig_name:
        continue
    norm = normalize(orig_name)
    # search for occurrences of the project name in civic docs
    name_re = re.compile(re.escape(orig_name), re.IGNORECASE)
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        for m in name_re.finditer(text):
            start, end = m.start(), m.end()
            window_start = max(0, start-500)
            window_end = min(len(text), end+500)
            window = text[window_start:window_end]
            if spring_re.search(window):
                found = True
                break
        if found:
            break
    if found:
        matched_projects[norm] = funding_map.get(norm, 0)

# dedupe by normalized name
unique_count = len(matched_projects)
total_funding = sum(matched_projects.values())

result = {"projects_count": unique_count, "total_funding": total_funding, "matched_projects": matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_S3MK3XxRWpjcrpcZo6SEYkoA': ['civic_docs'], 'var_call_124Wlw9LcWtohjHmorwIF8ck': ['Funding'], 'var_call_4HdUiHnSFJBjIwK87YHCGUTC': 'file_storage/call_4HdUiHnSFJBjIwK87YHCGUTC.json', 'var_call_wwbgDMXQ67DvK4hs4ybAOibf': 'file_storage/call_wwbgDMXQ67DvK4hs4ybAOibf.json', 'var_call_Er04skSPeO40hF9ntHhKeCnq': {'projects_count': 22, 'total_funding': 0, 'projects_detail': {'anticipated to have a final design by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Complete Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Begin Construction': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'project will have final approval by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'approval by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Complete Final Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'Commission will then review the project in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'consultant. It is anticipated that this agreement will go to Council in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Begin Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Completion Date': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'beginning in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) The project design will commence during the': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) This project will be presented to the Planning Commission in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'final approval. It is anticipated that the project will have final approval': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'go to Council in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Begin Design: Late': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Advertise': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'anticipated that the final design will be complete by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'completed by': {'matched_funding_sum': 0, 'matched_funding_projects': []}, 'draft plans are expected to be completed in': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Began Design': {'matched_funding_sum': 0, 'matched_funding_projects': []}, '(cid:131) Award Contract and Begin Construction': {'matched_funding_sum': 0, 'matched_funding_projects': []}}}}

exec(code, env_args)
