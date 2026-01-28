code = """import json
# var_call_WZjjt622oljE9QsIQtAmDFDg contains the file path to the Mongo query result
p = var_call_WZjjt622oljE9QsIQtAmDFDg
with open(p, 'r') as f:
    articles = json.load(f)
# create a dict mapping article_id (int) to title+description
art_map = {int(a['article_id']): {'title': a.get('title',''), 'description': a.get('description','')} for a in articles}
# load the list of europe article ids from previous step
p2 = var_call_V0pf7rdm4uvo2Rl6H30qr7pA
with open(p2, 'r') as f:
    europe_ids = json.load(f)
# filter art_map to only include europe_ids
europe_articles = {aid: art_map[aid] for aid in europe_ids if aid in art_map}
# prepare list
result = [{'article_id': aid, 'title': europe_articles[aid]['title'], 'description': europe_articles[aid]['description']} for aid in sorted(europe_articles.keys())]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XMxWfkStcIg1BRmcW7WUxm9W': 'file_storage/call_XMxWfkStcIg1BRmcW7WUxm9W.json', 'var_call_V0pf7rdm4uvo2Rl6H30qr7pA': 'file_storage/call_V0pf7rdm4uvo2Rl6H30qr7pA.json', 'var_call_WZjjt622oljE9QsIQtAmDFDg': 'file_storage/call_WZjjt622oljE9QsIQtAmDFDg.json'}

exec(code, env_args)
