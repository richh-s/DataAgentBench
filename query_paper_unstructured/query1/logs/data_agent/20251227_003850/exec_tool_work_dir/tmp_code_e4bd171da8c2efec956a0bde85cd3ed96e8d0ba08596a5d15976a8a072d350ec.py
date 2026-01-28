code = """import json

with open(var_call_KOAb1xgHNfb3JOSVlpr2sxoD, 'r') as f:
    docs = json.load(f)
with open(var_call_XFFPJlFw3TBBuuRwIfyp1MXj, 'r') as f:
    cites = json.load(f)

keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie']

food_titles = set()
for doc in docs:
    filename = doc.get('filename')
    text = (doc.get('text') or '').lower()
    if not filename:
        continue
    title = filename.replace('.txt', '')
    if any(k in text for k in keywords):
        food_titles.add(title)

# Sum citation counts for matching titles
sum_citations = 0
for row in cites:
    t = row.get('title')
    cc = row.get('citation_count')
    if t in food_titles:
        try:
            sum_citations += int(cc)
        except Exception:
            pass

result = {
    "food_titles": sorted(list(food_titles)),
    "total_citations_food_domain": sum_citations
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KOAb1xgHNfb3JOSVlpr2sxoD': 'file_storage/call_KOAb1xgHNfb3JOSVlpr2sxoD.json', 'var_call_XFFPJlFw3TBBuuRwIfyp1MXj': 'file_storage/call_XFFPJlFw3TBBuuRwIfyp1MXj.json', 'var_call_7x4P0KBQEa1dlWFV6BOGAVaZ': {'total_citations_food_domain': 0}, 'var_call_VMUHIoAr4PWJyDnTWS33EepV': {'food_titles_count': 0, 'food_titles_sample': [], 'citation_titles_count': 259, 'intersection_count': 0, 'intersection_sample': []}, 'var_call_B2jOeqkE4OXpK3u7YTVxd2C1': {'count_docs': 5, 'food_docs_count': 5, 'food_docs_sample': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}}

exec(code, env_args)
