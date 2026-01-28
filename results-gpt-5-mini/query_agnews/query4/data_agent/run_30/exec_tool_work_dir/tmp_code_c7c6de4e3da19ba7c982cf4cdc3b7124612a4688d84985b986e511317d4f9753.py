code = """import json
# var_call_dQoiCxChR4oghhJO7R8ycSOr is the file path to the metadata query result
with open(var_call_dQoiCxChR4oghhJO7R8ycSOr, 'r') as f:
    data = json.load(f)
article_ids = [int(item['article_id']) for item in data]
import json
print("__RESULT__:")
print(json.dumps(article_ids))"""

env_args = {'var_call_8B3NDebFVOdGEGWGO8nU1Ntj': ['articles'], 'var_call_dQoiCxChR4oghhJO7R8ycSOr': 'file_storage/call_dQoiCxChR4oghhJO7R8ycSOr.json'}

exec(code, env_args)
