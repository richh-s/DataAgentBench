code = """import json

citations_path = locals()['var_function-call-14649324199470214251']
with open(citations_path, 'r') as f:
    citations = json.load(f)

counts = [int(c['citation_count']) for c in citations]
avg = sum(counts) / len(counts)
print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-14649324199470214251': 'file_storage/function-call-14649324199470214251.json', 'var_function-call-1435401735284119985': 'file_storage/function-call-1435401735284119985.json', 'var_function-call-14005966684331283554': 'file_storage/function-call-14005966684331283554.json', 'var_function-call-5323787067724034665': 'file_storage/function-call-5323787067724034665.json', 'var_function-call-14065168965893616449': 68.5, 'var_function-call-14204041391851595483': 68.5}

exec(code, env_args)
