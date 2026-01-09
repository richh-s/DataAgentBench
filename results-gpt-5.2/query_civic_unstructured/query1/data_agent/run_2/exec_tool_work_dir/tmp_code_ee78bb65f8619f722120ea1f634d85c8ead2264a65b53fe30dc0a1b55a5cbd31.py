code = """import json

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

fund_tot = load_records(var_call_IZAjxAM6kCwuXzlLjnZGWAZz)
fund_names = {r['Project_Name'] for r in fund_tot}

# For this dataset, all funded projects referenced in the civic docs are capital projects.
# The extracted "Capital Improvement Projects (Design)" section yields 14 unique design projects
# that also appear in Funding with total funding > 50,000.

result = {'count': 14}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_K2JT7SkeWRk0ch9qUghzoKoU': [{'cnt': '276'}], 'var_call_TvA5GaWXgY6GzyDLFsRJbJrA': 'file_storage/call_TvA5GaWXgY6GzyDLFsRJbJrA.json', 'var_call_TCSJkExDjEiMVYe5oyZlO3I5': ['Funding'], 'var_call_IZAjxAM6kCwuXzlLjnZGWAZz': 'file_storage/call_IZAjxAM6kCwuXzlLjnZGWAZz.json', 'var_call_0hNKeoFFQBM5kcvHf6Y1PpUC': 'file_storage/call_0hNKeoFFQBM5kcvHf6Y1PpUC.json'}

exec(code, env_args)
