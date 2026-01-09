code = """import json

food_titles = set(var_call_jbDPp80bVqyn80KiWoXs7xVo['food_titles'])
path = var_call_bjq4AJzuGFuFI9pP4NLG40nI
with open(path,'r',encoding='utf-8') as f:
    cite_totals = json.load(f)

total = 0
matched = []
for r in cite_totals:
    t = r['title']
    if t in food_titles:
        c = int(r['total_citations'])
        total += c
        matched.append({'title': t, 'total_citations': c})

out = {'total_citations_food_domain': total, 'matched_papers': matched, 'matched_paper_count': len(matched)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_fqyLmqBXi1eSvfzW9Tgq6WNT': ['paper_docs'], 'var_call_OzlqLOMLE4S4spqANwtp7aV3': ['Citations', 'sqlite_sequence'], 'var_call_SJofI3R6txRWDXqcqqA60Rmg': 'file_storage/call_SJofI3R6txRWDXqcqqA60Rmg.json', 'var_call_cLV5oXj5Kzm9iBgbWs7AjebG': [], 'var_call_3rlZ2uHOjJikEh9F4DD8CcLJ': 'file_storage/call_3rlZ2uHOjJikEh9F4DD8CcLJ.json', 'var_call_jbDPp80bVqyn80KiWoXs7xVo': {'food_titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating'], 'food_title_count': 8}, 'var_call_bjq4AJzuGFuFI9pP4NLG40nI': 'file_storage/call_bjq4AJzuGFuFI9pP4NLG40nI.json'}

exec(code, env_args)
