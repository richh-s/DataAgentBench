code = """import json, re

def load_records(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_records(var_call_wflmjMBsRVXEHklUWMBHxqGH)
texts = [r.get('Project_Information') or '' for r in pi[:2000]]

repo_re = re.compile(r'\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b')
stars_re = re.compile(r'\b([0-9,]+)\s+stars\b')

count_repo = sum(1 for t in texts if repo_re.search(t))
count_stars = sum(1 for t in texts if stars_re.search(t))
count_both = sum(1 for t in texts if repo_re.search(t) and stars_re.search(t))

examples=[]
for t in texts:
    if repo_re.search(t) and stars_re.search(t):
        examples.append({'text': t[:250], 'repo': repo_re.search(t).group(1), 'stars': stars_re.search(t).group(1)})
        if len(examples)>=5:
            break

print('__RESULT__:')
print(json.dumps({'count_repo': count_repo, 'count_stars': count_stars, 'count_both': count_both, 'examples': examples}))"""

env_args = {'var_call_g1fm6eUvyVnnJpURKPCqQdKj': 'file_storage/call_g1fm6eUvyVnnJpURKPCqQdKj.json', 'var_call_ARjOrtyN7tkr12WKKpms1n3O': 'file_storage/call_ARjOrtyN7tkr12WKKpms1n3O.json', 'var_call_wflmjMBsRVXEHklUWMBHxqGH': 'file_storage/call_wflmjMBsRVXEHklUWMBHxqGH.json', 'var_call_IBrNSDvMfnv3jfKQamNJ8heQ': {'columns': ['System', 'Name', 'Version', 'ProjectName'], 'ncols': 4, 'sample': [{'System': 'NPM', 'Name': '@dms/io', 'Version': '0.9.0', 'ProjectName': 'dataminingsupply/dms-io'}, {'System': 'NPM', 'Name': '@dvo/fc', 'Version': '0.0.4', 'ProjectName': 'isacvale/fc'}, {'System': 'NPM', 'Name': '@djie/ui', 'Version': '1.0.17', 'ProjectName': 'laihaojie/jie'}]}, 'var_call_0xhBUaBnto81g7HSpNr1oQWV': {'merged_cols': ['System', 'Name', 'Version', 'ProjectName'], 'head': [{'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/music', 'Version': '6.0.2', 'ProjectName': 'discordx-ts/discordx'}, {'System': 'NPM', 'Name': '@discordx/pagination', 'Version': '3.4.1', 'ProjectName': 'discordx-ts/discordx'}]}, 'var_call_g8YLSokAr1uGRucKV2PWspX9': {'stars_cols': [], 'stars_head': []}}

exec(code, env_args)
