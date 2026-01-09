code = """import json

# food titles from filename matches
food_docs = var_call_49aoLBWpMRSg6QfAn6jIkHIj
food_titles = set([(d['filename'][:-4] if d['filename'].lower().endswith('.txt') else d['filename']) for d in food_docs])

cit_var = var_call_Vqy4Fmxf4oirwPb1Gcp0fCbK
if isinstance(cit_var, str):
    with open(cit_var, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = cit_var

# sum
s=0
for r in citations:
    if r.get('title') in food_titles:
        s += int(r.get('citation_count') or 0)

print('__RESULT__:')
print(json.dumps({'total_citation_count_food_domain': s, 'food_paper_count': len(food_titles), 'food_titles': sorted(list(food_titles))}))"""

env_args = {'var_call_Vqy4Fmxf4oirwPb1Gcp0fCbK': 'file_storage/call_Vqy4Fmxf4oirwPb1Gcp0fCbK.json', 'var_call_fHG9HzygcJwNedr1XK4wg67i': 'file_storage/call_fHG9HzygcJwNedr1XK4wg67i.json', 'var_call_bdDFjy0diCigKQHTZYmNikO2': 'file_storage/call_bdDFjy0diCigKQHTZYmNikO2.json', 'var_call_E4zIZWG89gOqMntw95Exjp2B': {'total_citation_count_food_domain': 0, 'food_paper_count': 0}, 'var_call_CQCxZZHSlBIPcrkROlHhswqX': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt'}, {'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}, {'filename': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt'}, {'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}], 'var_call_49aoLBWpMRSg6QfAn6jIkHIj': [{'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness.txt'}, {'filename': 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers.txt'}, {'filename': 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance.txt'}, {'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt'}, {'filename': "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps.txt"}, {'filename': 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture.txt'}, {'filename': 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating.txt'}]}

exec(code, env_args)
