code = """import json
from pathlib import Path

# Read the MongoDB query result stored in storage variable
p = Path(var_call_AMs1LTGeLtTG44p5m35fTNCl)
records = json.loads(p.read_text())

out = []
for r in records:
    attrs = r.get('attributes') or {}
    accepts = attrs.get('BusinessAcceptsCreditCards')
    # normalize boolean-like values
    if accepts in (True, 'True', 'true', 'TRUE', "u'True'"):
        biz_id = r.get('business_id')
        # convert to business_ref prefix
        if biz_id and biz_id.startswith('businessid_'):
            biz_ref = 'businessref_' + biz_id.split('_', 1)[1]
        else:
            biz_ref = biz_id
        # parse categories: might be absent, None, or a string
        cats = r.get('categories')
        if cats is None:
            cats_list = None
        elif isinstance(cats, list):
            cats_list = [str(c).strip() for c in cats if c]
        else:
            # string, split by comma
            cats_list = [c.strip() for c in str(cats).split(',') if c.strip()]
        out.append({'business_id': biz_id, 'business_ref': biz_ref, 'name': r.get('name'), 'categories': cats_list})

# Produce JSON string
result_json = json.dumps(out)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_call_pmHQOWf5XZpZBfTwoeAsLrn5': ['business', 'checkin'], 'var_call_AyQe6THSNrZu3vGFHFiFVdxz': ['review', 'tip', 'user'], 'var_call_AMs1LTGeLtTG44p5m35fTNCl': 'file_storage/call_AMs1LTGeLtTG44p5m35fTNCl.json'}

exec(code, env_args)
