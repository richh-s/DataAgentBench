code = """import json
# Load the clinical sample result stored in var_call_cvLxnMZPwIiMPdWajwObQTUM
path = var_call_cvLxnMZPwIiMPdWajwObQTUM
with open(path, 'r') as f:
    data = json.load(f)
# get the keys of the first record
keys = list(data[0].keys())
# find any columns that mention disease or dataset
candidates = [k for k in keys if 'disease' in k.lower() or 'tumor' in k.lower() or 'cancer' in k.lower() or 'dataset' in k.lower() or 'site' in k.lower() or 'diagnosis' in k.lower() or 'histology' in k.lower() or 'project' in k.lower()]
output = {'first_record_keys': keys, 'candidates': candidates, 'sample_patient_description': data[0].get('Patient_description')}
import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_l9BxyW69nXvgBIVU8MpUiO8K': ['clinical_info'], 'var_call_N6Qbzpu3ynJhE5mwzyHMaRsU': ['Mutation_Data', 'RNASeq_Expression'], 'var_call_cvLxnMZPwIiMPdWajwObQTUM': 'file_storage/call_cvLxnMZPwIiMPdWajwObQTUM.json'}

exec(code, env_args)
