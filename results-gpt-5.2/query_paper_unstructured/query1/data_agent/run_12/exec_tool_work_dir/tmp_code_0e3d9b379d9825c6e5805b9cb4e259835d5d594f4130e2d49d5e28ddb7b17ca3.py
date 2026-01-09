code = """import json, pandas as pd

# citations totals per title
cit_path = var_call_7CSMavulR5EYTbE2xp0EXyDs
if isinstance(cit_path, str) and cit_path.endswith('.json'):
    with open(cit_path, 'r', encoding='utf-8') as f:
        cit = json.load(f)
else:
    cit = cit_path

df_cit = pd.DataFrame(cit)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

food_info = var_call_EFA6fSYRhnQ9pUhCPf4WdHVj
food_titles = set(food_info['sample']) if isinstance(food_info, dict) else set()

matched = df_cit[df_cit['title'].isin(food_titles)].copy()

total = int(matched['total_citations'].sum())
print('__RESULT__:')
print(json.dumps({"total_citation_count_food_domain": total, "matched_titles": matched[['title','total_citations']].to_dict('records')}))"""

env_args = {'var_call_7CSMavulR5EYTbE2xp0EXyDs': 'file_storage/call_7CSMavulR5EYTbE2xp0EXyDs.json', 'var_call_aWFXXbvt8ZG9DZdeo3pg48h1': 'file_storage/call_aWFXXbvt8ZG9DZdeo3pg48h1.json', 'var_call_rnGisujxXWUhOsQF0cUgpe0v': {'total_citation_count_food_domain': 0, 'num_food_papers_matched': 0, 'num_food_papers_in_docs': 0}, 'var_call_EFA6fSYRhnQ9pUhCPf4WdHVj': {'num_food_titles': 8, 'sample': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', 'Does Journaling Encourage Healthier Choices?: Analyzing Healthy Eating Behaviors of Food Journalers', 'Eat & Tell: A Randomized Trial of Random-Loss Incentive to Increase Dietary Self-Tracking Compliance', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}}

exec(code, env_args)
