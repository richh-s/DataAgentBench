code = """import json

with open(locals()['var_function-call-996362830735493393'], 'r') as f:
    order_items = json.load(f)

target_product_id = '01tWt000006hVJdIAM'
matching_order_item_ids = []

for item in order_items:
    p_id = item.get('Product2Id')
    o_id = item.get('Id')
    if p_id and p_id.strip().lstrip('#') == target_product_id:
        if o_id:
            matching_order_item_ids.append(o_id.strip().lstrip('#'))

print("__RESULT__:")
print(json.dumps(list(set(matching_order_item_ids))))"""

env_args = {'var_function-call-996362830735493393': 'file_storage/function-call-996362830735493393.json'}

exec(code, env_args)
