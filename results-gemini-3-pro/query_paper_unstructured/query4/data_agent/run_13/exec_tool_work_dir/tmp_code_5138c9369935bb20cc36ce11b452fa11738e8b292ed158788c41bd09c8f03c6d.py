code = """import json

file_path = locals()['var_function-call-5063725347681925527']
candidates = ["Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers", "Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace", "Technologies for Everyday Life Reflection: Illustrating a Design Space"]

try:
    with open(file_path, 'r') as f:
        docs = json.load(f)
except Exception as e:
    docs = []

results = {}

for d in docs:
    title = d.get('filename', '').replace('.txt', '')
    if title in candidates:
        results[title] = d.get('text', '')[:1000]

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1380107038733155732': 'file_storage/function-call-1380107038733155732.json', 'var_function-call-1380107038733154663': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-10254966279675134776': 'file_storage/function-call-10254966279675134776.json', 'var_function-call-5480804102424637066': [], 'var_function-call-5063725347681925527': 'file_storage/function-call-5063725347681925527.json', 'var_function-call-14207739170194732954': ['Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'Technologies for Everyday Life Reflection: Illustrating a Design Space'], 'var_function-call-5883576434040758970': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'total_citations': '349'}, {'title': 'Steps, Choices and Moral Accounting: Observations from a Step-Counting Campaign in the Workplace', 'total_citations': '434'}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'total_citations': '358'}]}

exec(code, env_args)
