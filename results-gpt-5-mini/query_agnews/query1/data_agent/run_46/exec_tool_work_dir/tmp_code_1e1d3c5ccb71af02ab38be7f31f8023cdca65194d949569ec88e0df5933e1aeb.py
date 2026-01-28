code = """import json, re
# Load the previous query results file
path = var_call_7ukuTkElSgRzK53NkENJVjkn
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# More precise sports tokens
sports_tokens = ['\bfootball\b','\bmadden\b','\bnfl\b','\bespn\b','\bsoccer\b',
                 '\bskate\b','\bskateboard\b','\btennis\b','\bbaseball\b','\bbasketball\b',
                 '\bhockey\b','\bolympic\b','\bolympics\b','\bgolf\b','\brugby\b', '\bcricket\b']
pattern = re.compile('|'.join(sports_tokens), flags=re.I)

sports_articles = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    combined = f"{title} {desc}"
    if pattern.search(combined):
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

if not sports_articles:
    result = None
else:
    maxlen = max(a['desc_len'] for a in sports_articles)
    max_articles = [a for a in sports_articles if a['desc_len']==maxlen]
    # If multiple, return all titles
    titles = [a['title'] for a in max_articles]
    result = titles[0] if len(titles)==1 else titles

print("__RESULT__:")
import json
print(json.dumps(result))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json', 'var_call_16BOmpLOc47MkkRohoNMEvIz': None, 'var_call_YQfUbJnpTqIYRi81JJ49dHBo': [], 'var_call_SfNLTHncCUA7WEyfazX4c5s2': 'file_storage/call_SfNLTHncCUA7WEyfazX4c5s2.json', 'var_call_GM4QgztfJXfopi75nFvuVEiC': None}

exec(code, env_args)
