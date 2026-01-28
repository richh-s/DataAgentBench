code = """import json
# var_call_ULoT7Yja3x7BR5LtpdHMT3FN is a path to the JSON file with citation records
path = var_call_ULoT7Yja3x7BR5LtpdHMT3FN
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

filenames = [r['title'] + '.txt' for r in records]
# convert citation_count to int
citations = {r['title']: int(r['citation_count']) for r in records}

output = {'filenames': filenames, 'citations': citations}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_ULoT7Yja3x7BR5LtpdHMT3FN': 'file_storage/call_ULoT7Yja3x7BR5LtpdHMT3FN.json'}

exec(code, env_args)
