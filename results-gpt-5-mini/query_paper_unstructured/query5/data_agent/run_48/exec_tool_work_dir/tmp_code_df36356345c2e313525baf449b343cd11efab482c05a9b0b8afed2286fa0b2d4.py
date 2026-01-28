code = """import json
# Load the previous query results from storage keys
path1 = var_call_KO4ayhrGGokljFRCYb1f6BtF
path2 = var_call_I6kAKxaKG6ZuzVMussUMDepE

# helper to load either direct list or json file
def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

docs = load_var(path1)
citations = load_var(path2)

# Build set of filenames from docs
filenames = set(d.get('filename') for d in docs if 'filename' in d)

matched = []
total = 0
for c in citations:
    title = c.get('title')
    # some titles may have trailing spaces
    filename = title + '.txt'
    try:
        count = int(c.get('citation_count'))
    except:
        # if missing or not int, skip
        continue
    if filename in filenames:
        matched.append({'title': title, 'citation_count': count})
        total += count

result = {'total_citations_for_CHI_papers_in_2020': total, 'matched_papers_count': len(matched), 'papers': matched}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_KO4ayhrGGokljFRCYb1f6BtF': 'file_storage/call_KO4ayhrGGokljFRCYb1f6BtF.json', 'var_call_I6kAKxaKG6ZuzVMussUMDepE': 'file_storage/call_I6kAKxaKG6ZuzVMussUMDepE.json'}

exec(code, env_args)
