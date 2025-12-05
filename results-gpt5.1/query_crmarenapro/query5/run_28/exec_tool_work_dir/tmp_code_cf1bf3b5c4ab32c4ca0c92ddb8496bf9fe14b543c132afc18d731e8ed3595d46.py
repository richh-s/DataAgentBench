code = """import json
from collections import Counter

rows = var_call_cX4EyuSA2u2XZFPy8NV1Dc5U
issues = [r['issueid__c'].strip() for r in rows if r.get('issueid__c')]

most_common_issue = None
if issues:
    most_common_issue = Counter(issues).most_common(1)[0][0]

result = json.dumps(most_common_issue)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_goQHFVJ5DNqifx1S5ZEVgIQV': [], 'var_call_3QeDPDPPEzWX3GGoAjIRcEjZ': [], 'var_call_cX4EyuSA2u2XZFPy8NV1Dc5U': [{'issueid__c': 'a03Wt00000JqnHwIAJ'}, {'issueid__c': 'a03Wt00000JqnHwIAJ'}]}

exec(code, env_args)
