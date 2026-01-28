code = """import json
# var_call_IgvP8VbGkFQXGvNQHbO8ipmQ is the storage key containing the file path
fp = var_call_IgvP8VbGkFQXGvNQHbO8ipmQ
with open(fp, 'r') as f:
    data = json.load(f)

biz_refs = []
biz_to_cats = {}
for rec in data:
    bid = rec.get('business_id')
    attrs = rec.get('attributes')
    cats = rec.get('categories')
    accepts = False
    if isinstance(attrs, dict):
        val = attrs.get('BusinessAcceptsCreditCards')
        if val is True or (isinstance(val, str) and val.lower() == 'true'):
            accepts = True
    # sometimes attributes stored as string 'None' or None
    if accepts:
        # convert businessid_ to businessref_
        bref = bid.replace('businessid_', 'businessref_')
        biz_refs.append(bref)
        # parse categories
        if cats is None:
            cat_list = []
        elif isinstance(cats, list):
            cat_list = [c.strip() for c in cats if c]
        else:
            # assume string of comma-separated categories
            cat_list = [c.strip() for c in str(cats).split(',') if c.strip()]
        biz_to_cats[bref] = cat_list

out = {'business_refs': biz_refs, 'biz_to_cats': biz_to_cats}
import json as _json
print("__RESULT__:")
print(_json.dumps(out))"""

env_args = {'var_call_LobF8jjX5IiHLMNao3tSLznC': ['business', 'checkin'], 'var_call_OrnNU9ZV8xUaiyij8J5RX1O1': ['review', 'tip', 'user'], 'var_call_8sPXPQmnDjxWuVFFLvf712sa': 'file_storage/call_8sPXPQmnDjxWuVFFLvf712sa.json', 'var_call_IgvP8VbGkFQXGvNQHbO8ipmQ': 'file_storage/call_IgvP8VbGkFQXGvNQHbO8ipmQ.json'}

exec(code, env_args)
