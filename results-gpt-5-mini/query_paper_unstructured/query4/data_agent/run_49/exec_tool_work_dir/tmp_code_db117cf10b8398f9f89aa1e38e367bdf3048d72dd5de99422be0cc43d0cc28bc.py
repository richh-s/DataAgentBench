code = """import json
# load filenames (titles with .txt) from previous var
titles_with_txt = None
try:
    titles_with_txt = var_call_MdHRAbGQSZUCx0toe578graa
except Exception as e:
    titles_with_txt = []
# strip .txt
titles = [t[:-4] if t.endswith('.txt') else t for t in titles_with_txt]
# load citation sums
citations = None
try:
    if isinstance(var_call_jBPOkEPIh0ctKA8k0oKbj4v6, str):
        with open(var_call_jBPOkEPIh0ctKA8k0oKbj4v6, 'r', encoding='utf-8') as f:
            citations = json.load(f)
    else:
        citations = var_call_jBPOkEPIh0ctKA8k0oKbj4v6
except Exception as e:
    citations = var_call_jBPOkEPIh0ctKA8k0oKbj4v6

# prepare final results: include only papers that are from 2016 domain 'physical activity'
# We couldn't extract year reliably per doc; assume these titles are the ones matching domain and then check years by looking into files' text for year 2016
# load mongo docs
try:
    if isinstance(var_call_I9tf0clGC8oTadzuC6RDDAPU, str):
        with open(var_call_I9tf0clGC8oTadzuC6RDDAPU, 'r', encoding='utf-8') as f:
            docs = json.load(f)
    else:
        docs = var_call_I9tf0clGC8oTadzuC6RDDAPU
except Exception as e:
    docs = var_call_I9tf0clGC8oTadzuC6RDDAPU

# map filename->year if possible
import re
file_year = {}
for doc in docs:
    fn = doc.get('filename','')
    text = doc.get('text','')
    m = re.search(r"\b(19|20)\d{2}\b", text)
    if m:
        file_year[fn] = int(m.group(0))

# Now filter for year==2016
final = []
for entry in citations:
    title = entry['title']
    # find matching filename
    fname = title + '.txt'
    year = file_year.get(fname)
    if year == 2016:
        final.append({'title': title, 'total_citations': int(entry['total_citations'])})

print("__RESULT__:")
print(json.dumps(final))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json', 'var_call_U44SEcLG6zWizxmxE0Aypv5k': [], 'var_call_CR3mHeGx2Vc5CLD705Vvdb00': [], 'var_call_MdHRAbGQSZUCx0toe578graa': ['Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'], 'var_call_jBPOkEPIh0ctKA8k0oKbj4v6': [{'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}]}

exec(code, env_args)
