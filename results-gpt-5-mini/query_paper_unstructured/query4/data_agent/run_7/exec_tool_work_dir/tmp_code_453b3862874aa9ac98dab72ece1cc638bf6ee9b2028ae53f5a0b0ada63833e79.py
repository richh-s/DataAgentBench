code = """import json
# read titles from previous python call result
titles = json.loads(var_call_KrmV8Nk6Np5uQKUMbesZbDfJ)
# read citation query result
citations = var_call_HUbkHLh2eH2MmNfDODKwxFCb

# Build final list for papers published in 2016 in 'physical activity' domain
# We assume the titles list are the papers; now join with citations
results = []
for t in titles:
    # find citation record
    rec = next((r for r in citations if r['title']==t), None)
    total = int(rec['total_citations']) if rec and rec.get('total_citations') is not None else None
    results.append({'title': t, 'total_citations': total})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_q1A0x1ef4aui3tx6vTkmVFcN': ['paper_docs'], 'var_call_BO6vopfLPkVKZx6CZsEf1NUO': ['Citations', 'sqlite_sequence'], 'var_call_aYiyKGOoBYD1V7En6jbcyyfz': 'file_storage/call_aYiyKGOoBYD1V7En6jbcyyfz.json', 'var_call_KrmV8Nk6Np5uQKUMbesZbDfJ': ['Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Technologies for Everyday Life Reflection: Illustrating a Design Space'], 'var_call_HUbkHLh2eH2MmNfDODKwxFCb': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}]}

exec(code, env_args)
