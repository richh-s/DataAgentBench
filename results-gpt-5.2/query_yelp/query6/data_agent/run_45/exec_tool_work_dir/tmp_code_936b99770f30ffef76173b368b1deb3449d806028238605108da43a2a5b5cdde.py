code = """import re, json
biz = var_call_B9tn5GKSVfeelkxDBwtGWNUJ[0]
desc = biz.get('description') or ''
# extract categories after 'services in'
m = re.search(r"services in (.+?)\.?$", desc)
cats = None
if m:
    cats = m.group(1).strip()
result = {
    'business_name': biz.get('name'),
    'business_id': biz.get('business_id'),
    'category': cats,
    'avg_rating': float(var_call_kUpbfBZb0ENWPno8ZSCTfV6I[0]['avg_rating']),
    'review_count_in_period': int(var_call_kUpbfBZb0ENWPno8ZSCTfV6I[0]['review_cnt'])
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_kUpbfBZb0ENWPno8ZSCTfV6I': [{'business_ref': 'businessref_37', 'avg_rating': '4.4', 'review_cnt': '5'}], 'var_call_B9tn5GKSVfeelkxDBwtGWNUJ': [{'business_id': 'businessid_37', 'name': 'Orangetheory Fitness Carrollwood', 'description': 'Located at 13122 N Dale Mabry Hwy in Tampa, FL, this facility offers a comprehensive range of services in Fitness & Instruction, Gyms, Boot Camps, Trainers, Active Life, and Interval Training Gyms.'}]}

exec(code, env_args)
