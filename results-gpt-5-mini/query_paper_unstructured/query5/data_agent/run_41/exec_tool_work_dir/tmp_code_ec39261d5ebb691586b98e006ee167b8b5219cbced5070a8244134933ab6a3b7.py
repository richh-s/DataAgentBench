code = """import json
# Load the large citations result from file path stored in var_call_p81JDtxnp8mBvbbHGH9DbqQY
with open(var_call_p81JDtxnp8mBvbbHGH9DbqQY, 'r', encoding='utf-8') as f:
    citations = json.load(f)
# Load CHI filenames from the Mongo query result stored in var_call_arEDsBqA2AxPGQIaUGJXMHJu
chi_files = var_call_arEDsBqA2AxPGQIaUGJXMHJu
# Extract titles by stripping .txt
chi_titles = set()
for d in chi_files:
    fn = d.get('filename', '')
    if fn.endswith('.txt'):
        chi_titles.add(fn[:-4])
    else:
        chi_titles.add(fn)

matched = []
total = 0
for rec in citations:
    title = rec.get('title')
    # citation_count may be string, convert to int safely
    try:
        count = int(rec.get('citation_count', 0))
    except:
        try:
            count = int(float(rec.get('citation_count', 0)))
        except:
            count = 0
    if title in chi_titles:
        matched.append({'title': title, 'citation_count': count})
        total += count

output = {'per_paper': matched, 'total': total}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_p81JDtxnp8mBvbbHGH9DbqQY': 'file_storage/call_p81JDtxnp8mBvbbHGH9DbqQY.json', 'var_call_arEDsBqA2AxPGQIaUGJXMHJu': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
