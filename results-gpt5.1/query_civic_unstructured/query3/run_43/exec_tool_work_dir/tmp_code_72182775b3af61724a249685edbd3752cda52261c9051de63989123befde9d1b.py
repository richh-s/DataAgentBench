code = """import json, re
from pathlib import Path

# Load full funding data
path_funding = Path(var_call_PkUkOgxk1KSQCsvshToIVIwR)
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Filter funding projects whose names suggest FEMA/emergency
emergency_keywords = ['fema', 'emergency', 'warning', 'sirens', 'backup power']
re_emerg = re.compile('|'.join(re.escape(k) for k in emergency_keywords), re.I)
fund_emerg = [r for r in funding if re_emerg.search(r['Project_Name'])]

result = fund_emerg

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_PkUkOgxk1KSQCsvshToIVIwR': 'file_storage/call_PkUkOgxk1KSQCsvshToIVIwR.json', 'var_call_jAQES1Qc29xMJYpmZJ8cqUAZ': 'file_storage/call_jAQES1Qc29xMJYpmZJ8cqUAZ.json'}

exec(code, env_args)
