code = """import json, pandas as pd

# Load full results
with open(var_call_ARrxfa8uS6zaS6hLufyBQSKz) as f:
    chi_files = json.load(f)
with open(var_call_gnOoDoW5FtsgRn6Gq9Z3s5mf) as f:
    citations_2020 = json.load(f)

chi_titles = {d['filename'].rsplit('.txt', 1)[0] for d in chi_files}

cit_df = pd.DataFrame(citations_2020)

mask = cit_df['title'].isin(chi_titles)

result_total = int(cit_df[mask]['total_citations'].astype(int).sum())

result = result_total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ARrxfa8uS6zaS6hLufyBQSKz': 'file_storage/call_ARrxfa8uS6zaS6hLufyBQSKz.json', 'var_call_gnOoDoW5FtsgRn6Gq9Z3s5mf': 'file_storage/call_gnOoDoW5FtsgRn6Gq9Z3s5mf.json'}

exec(code, env_args)
