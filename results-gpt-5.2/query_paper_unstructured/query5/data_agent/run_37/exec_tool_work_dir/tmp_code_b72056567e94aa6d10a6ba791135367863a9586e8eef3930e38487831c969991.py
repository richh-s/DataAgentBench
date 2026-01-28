code = """import json, re

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

docs = load_records(var_call_0xzxrpc7YvsO6yzcV7d1dOG8)

# sample first 20 texts header lines
samples = []
for d in docs[:20]:
    text = (d.get('text','') or '')
    head = text[:400]
    samples.append({"filename": d.get('filename'), "head": head})

print('__RESULT__:')
print(json.dumps(samples))"""

env_args = {'var_call_TRpLmu1z1yAwlBlNZUz41qpT': 'file_storage/call_TRpLmu1z1yAwlBlNZUz41qpT.json', 'var_call_0xzxrpc7YvsO6yzcV7d1dOG8': 'file_storage/call_0xzxrpc7YvsO6yzcV7d1dOG8.json', 'var_call_fir9ov4PUWbvrSB6gVQLqz5q': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0}, 'var_call_Iux4gB9TPS5C9eUH6HBrhbT4': {'total_citations_2020_for_CHI_papers': 0, 'num_CHI_papers_cited_in_2020': 0, 'num_docs_detected_as_CHI': 0}}

exec(code, env_args)
