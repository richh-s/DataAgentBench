code = """import json
# load the SQL query result from storage
var = var_call_JYMWUpPslGKbjesIWXIYEE0A
# ensure citation counts are ints
for r in var:
    r['total_citations'] = int(r['total_citations'])
# Sort by total_citations descending
var_sorted = sorted(var, key=lambda x: x['total_citations'], reverse=True)
print('__RESULT__:')
print(json.dumps(var_sorted))"""

env_args = {'var_call_ge3CyFMCqYeAaqjfssn5Y002': 'file_storage/call_ge3CyFMCqYeAaqjfssn5Y002.json', 'var_call_qsmoTKbjAMCZq5fJOKRkhlJH': {'titles': ['Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Technologies for Everyday Life Reflection: Illustrating a Design Space'], 'count': 3}, 'var_call_JYMWUpPslGKbjesIWXIYEE0A': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}]}

exec(code, env_args)
