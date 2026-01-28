code = """import json, re
# Load mongo query result and citations result
try:
    if isinstance(var_call_I9tf0clGC8oTadzuC6RDDAPU, str):
        with open(var_call_I9tf0clGC8oTadzuC6RDDAPU, 'r', encoding='utf-8') as f:
            docs = json.load(f)
    else:
        docs = var_call_I9tf0clGC8oTadzuC6RDDAPU
except Exception as e:
    docs = var_call_I9tf0clGC8oTadzuC6RDDAPU

try:
    if isinstance(var_call_jBPOkEPIh0ctKA8k0oKbj4v6, str):
        with open(var_call_jBPOkEPIh0ctKA8k0oKbj4v6, 'r', encoding='utf-8') as f:
            citations = json.load(f)
    else:
        citations = var_call_jBPOkEPIh0ctKA8k0oKbj4v6
except Exception as e:
    citations = var_call_jBPOkEPIh0ctKA8k0oKbj4v6

# build citation map
cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []
for doc in docs:
    fn = doc.get('filename','')
    title = fn[:-4] if fn.endswith('.txt') else fn
    text = doc.get('text','')
    # search for explicit publication year near top (first 800 chars), else first occurrence in whole text
    head = text[:2000]
    years = re.findall(r"\b(19|20)(\d{2})\b", head)
    pub_year = None
    if years:
        # pick first occurrence
        pub_year = int(years[0][0]+years[0][1])
    else:
        years2 = re.findall(r"\b(19|20)(\d{2})\b", text)
        if years2:
            pub_year = int(years2[0][0]+years2[0][1])
    # also check for patterns like "2016." or "'16" nearby title
    if pub_year is None:
        m = re.search(r"'(?P<yy>\d{2})", head)
        if m:
            yy = int(m.group('yy'))
            if yy <= 30:
                pub_year = 2000 + yy
            else:
                pub_year = 1900 + yy
    results.append({'title': title, 'filename': fn, 'inferred_year': pub_year, 'citations_total': cit_map.get(title)})

# filter for inferred_year == 2016
filtered = [r for r in results if r.get('inferred_year')==2016]
print("__RESULT__:")
print(json.dumps(filtered))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json', 'var_call_U44SEcLG6zWizxmxE0Aypv5k': [], 'var_call_CR3mHeGx2Vc5CLD705Vvdb00': [], 'var_call_MdHRAbGQSZUCx0toe578graa': ['Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'], 'var_call_jBPOkEPIh0ctKA8k0oKbj4v6': [{'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}], 'var_call_j4fG1UHF84Arl4vMCadNzJNk': []}

exec(code, env_args)
