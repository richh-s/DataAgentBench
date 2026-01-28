code = """import json, os

with open(var_call_2Hbz95VIWvJQczjZECJzyMYV, 'r', encoding='utf-8') as f:
    clinical_list = json.load(f)
with open(var_call_NbI2VMmvh0BNBWFTgNEKYiPB, 'r', encoding='utf-8') as f:
    mut_list = json.load(f)

# Analyze clinical_list
clin_types = [type(x).__name__ for x in clinical_list]
clin_type_counts = {}
for t in clin_types:
    clin_type_counts[t] = clin_type_counts.get(t,0)+1

# Keys distribution for dict items
keylen_counts = {}
sample_keys = []
for i,x in enumerate(clinical_list[:20]):
    if isinstance(x, dict):
        k = len(x.keys())
        keylen_counts[k] = keylen_counts.get(k,0)+1
        sample_keys.append(list(x.keys()))
    else:
        keylen_counts['non-dict'] = keylen_counts.get('non-dict',0)+1

# Mutation list analysis
mut_types = [type(x).__name__ for x in mut_list]
mut_type_counts = {}
for t in mut_types:
    mut_type_counts[t] = mut_type_counts.get(t,0)+1

mut_keylen_counts = {}
mut_sample_keys = []
for i,x in enumerate(mut_list[:20]):
    if isinstance(x, dict):
        k = len(x.keys())
        mut_keylen_counts[k] = mut_keylen_counts.get(k,0)+1
        mut_sample_keys.append(list(x.keys()))
    else:
        mut_keylen_counts['non-dict'] = mut_keylen_counts.get('non-dict',0)+1

res = {
    'clinical_count': len(clinical_list),
    'clinical_type_counts': clin_type_counts,
    'clinical_keylen_counts_sample': keylen_counts,
    'clinical_sample_keys_first20': sample_keys,
    'mutation_count': len(mut_list),
    'mutation_type_counts': mut_type_counts,
    'mutation_keylen_counts_sample': mut_keylen_counts,
    'mutation_sample_keys_first20': mut_sample_keys
}

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_euNu3hqX7o5pimk0JDlcvUZn': ['clinical_info'], 'var_call_TT4YmDFu1feeK1YWDQiVcdcZ': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_c48JMfZf7ddnSH9YptwaPZd0': 'file_storage/call_c48JMfZf7ddnSH9YptwaPZd0.json', 'var_call_2Hbz95VIWvJQczjZECJzyMYV': 'file_storage/call_2Hbz95VIWvJQczjZECJzyMYV.json', 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': 'file_storage/call_NbI2VMmvh0BNBWFTgNEKYiPB.json', 'var_call_DxXrBq1MATFsl2XFarMAL9Xr': {'var_call_2Hbz95VIWvJQczjZECJzyMYV': {'type': 'str', 'is_file': True, 'list_length': 1076, 'first_keys': ['Patient_description', 'histological_type', 'patient_id']}, 'var_call_NbI2VMmvh0BNBWFTgNEKYiPB': {'type': 'str', 'is_file': True, 'list_length': 261, 'first_keys': ['ParticipantBarcode', 'Hugo_Symbol', 'HGVSp_Short', 'Variant_Classification', 'FILTER']}}}

exec(code, env_args)
