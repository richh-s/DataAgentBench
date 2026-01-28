code = """import json
p = var_call_COm8Aw8kN260BreJqf2C2xDz
with open(p, 'r') as f:
    records = json.load(f)
repo_names = sorted({r['repo_name'] for r in records if 'repo_name' in r})
# chunk
batch_size = 300
batches = [repo_names[i:i+batch_size] for i in range(0, len(repo_names), batch_size)]
queries = []
for batch in batches:
    def qquote(s):
        return "'" + s.replace("'","''") + "'"
    in_list = ','.join(qquote(r) for r in batch)
    q = (
        'SELECT COUNT(*) AS count FROM commits '
        f"WHERE repo_name IN ({in_list}) "
        "AND message IS NOT NULL "
        "AND message <> '' "
        "AND length(message) < 1000 "
        "AND ltrim(lower(message)) NOT LIKE 'merge%' "
        "AND ltrim(lower(message)) NOT LIKE 'update%' "
        "AND ltrim(lower(message)) NOT LIKE 'test%';"
    )
    queries.append(q)

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_call_COm8Aw8kN260BreJqf2C2xDz': 'file_storage/call_COm8Aw8kN260BreJqf2C2xDz.json', 'var_call_cmi9iKVzjejooAD4B3gfpXVU': "SELECT COUNT(*) AS count FROM commits WHERE repo_name IN () AND message IS NOT NULL AND message <> '' AND length(message) < 1000 AND lower(message) NOT LIKE 'merge%' AND lower(message) NOT LIKE 'update%' AND lower(message) NOT LIKE 'test%';", 'var_call_Hg5QnUaG1ogZUJOfkpKAvqZu': 'file_storage/call_Hg5QnUaG1ogZUJOfkpKAvqZu.json', 'var_call_mlcgYrrAALylwRu863N25x4l': [{'repo_name': 'facebook/react', 'cnt': '104'}, {'repo_name': 'tensorflow/tensorflow', 'cnt': '114'}, {'repo_name': 'twbs/bootstrap', 'cnt': '251'}, {'repo_name': 'apple/swift', 'cnt': '963'}, {'repo_name': 'torvalds/linux', 'cnt': '13413'}, {'repo_name': 'Microsoft/vscode', 'cnt': '171'}]}

exec(code, env_args)
