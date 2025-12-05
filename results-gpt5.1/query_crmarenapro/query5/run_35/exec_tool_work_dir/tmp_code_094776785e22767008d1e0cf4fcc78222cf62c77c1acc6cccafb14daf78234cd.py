code = """import json
from collections import Counter

rows = var_call_LOBOoVm6TZdkli2GGAMr0E6S
counts = Counter(r['issueid__c'] for r in rows if r['issueid__c'])
most_common_issue = counts.most_common(1)[0][0] if counts else None

result = json.dumps(most_common_issue)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_YVrsPkIL24sgqZHzT5dyHVZI': [], 'var_call_LOBOoVm6TZdkli2GGAMr0E6S': [{'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ'}]}

exec(code, env_args)
