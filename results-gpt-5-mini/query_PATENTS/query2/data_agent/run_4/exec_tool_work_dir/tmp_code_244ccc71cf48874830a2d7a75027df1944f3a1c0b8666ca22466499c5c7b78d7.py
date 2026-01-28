code = """import json, re

path = var_call_T6EVN0wa6vXygggLELsEzSqf
with open(path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

patterns = ['DE', '/DE', 'Germany', 'country_code', 'DE-']
found_examples = {p: [] for p in patterns}

for rec in pubs[:500]:
    info = rec.get('Patents_info','')
    for p in patterns:
        if p in info:
            if len(found_examples[p]) < 5:
                found_examples[p].append(info)

# Also compute overall counts for tokens as whole words
word_counts = {}
for rec in pubs:
    info = rec.get('Patents_info','')
    words = re.findall(r"\b\w+\b", info)
    for w in words:
        if w == 'DE' or w == 'Germany' or w == 'Germany.' or w.startswith('DE-'):
            word_counts[w] = word_counts.get(w,0)+1

res = {'total_records_sampled': min(500,len(pubs)), 'found_examples': found_examples, 'word_counts_sample': word_counts}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_T6EVN0wa6vXygggLELsEzSqf': 'file_storage/call_T6EVN0wa6vXygggLELsEzSqf.json', 'var_call_m1Hpssfn6VXXHXhXmjgyXmHg': 'file_storage/call_m1Hpssfn6VXXHXhXmjgyXmHg.json', 'var_call_iCbx0nyULprDUxHZEIFTb9kJ': [], 'var_call_ABeRRIOm5CmvsmZQcYRzkK9j': {'num_records_sampled': 74, 'parsed_with_year_and_cpc': 0, 'years_found_sample': [], 'num_level4_symbols': 137, 'top_groups_sample': []}}

exec(code, env_args)
