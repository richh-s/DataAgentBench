code = """import json, re
# load the specific docs file
try:
    if isinstance(var_call_Fg1KBal7XjXiQo84W1y8oWkp, str):
        with open(var_call_Fg1KBal7XjXiQo84W1y8oWkp, 'r', encoding='utf-8') as f:
            docs = json.load(f)
    else:
        docs = var_call_Fg1KBal7XjXiQo84W1y8oWkp
except Exception as e:
    docs = var_call_Fg1KBal7XjXiQo84W1y8oWkp

out = []
for doc in docs:
    fn = doc.get('filename','')
    text = doc.get('text','')[:1000]
    # try to find publication year in first 500 chars
    m = re.search(r"\b(19|20)\d{2}\b", doc.get('text','')[:800])
    year = int(m.group(0)) if m else None
    out.append({'filename': fn, 'year_found': year, 'snippet': text})

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json', 'var_call_U44SEcLG6zWizxmxE0Aypv5k': [], 'var_call_CR3mHeGx2Vc5CLD705Vvdb00': [], 'var_call_MdHRAbGQSZUCx0toe578graa': ['Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'], 'var_call_jBPOkEPIh0ctKA8k0oKbj4v6': [{'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}], 'var_call_j4fG1UHF84Arl4vMCadNzJNk': [], 'var_call_j43hDSFtHKWATdMpBWV7gMcu': [], 'var_call_Fg1KBal7XjXiQo84W1y8oWkp': 'file_storage/call_Fg1KBal7XjXiQo84W1y8oWkp.json'}

exec(code, env_args)
