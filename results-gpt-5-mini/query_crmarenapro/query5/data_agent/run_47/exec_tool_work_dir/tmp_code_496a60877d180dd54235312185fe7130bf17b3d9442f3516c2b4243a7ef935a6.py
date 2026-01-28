code = """import json
# Load the large OrderItem result file
path = var_call_GwD7geH1LW9bQUli1wd5d5pM
with open(path, 'r') as f:
    records = json.load(f)
ids = [r.get('Id') for r in records if r.get('Id')]
# Unique
uniq_ids = sorted(list(dict.fromkeys(ids)))
import json
print("__RESULT__:")
print(json.dumps(uniq_ids))"""

env_args = {'var_call_VrL9J6J1ZkUp2Ddps0l13pWS': [], 'var_call_xKPQIIpQM8CMKRr2R8YkQEAB': [], 'var_call_0jixH7usbE2pPs3Fk8S93l9M': [{'id': 'a03Wt00000JqhItIAJ', 'name': 'Software Installation Error'}, {'id': '#a03Wt00000JqmLvIAJ', 'name': 'Billing Discrepancy'}, {'id': 'a03Wt00000JqmX6IAJ', 'name': 'Customizability Limitation   '}, {'id': 'a03Wt00000JqnHwIAJ', 'name': 'User Interface Bug'}, {'id': '#a03Wt00000JqtOtIAJ', 'name': 'Support Response Delay'}, {'id': 'a03Wt00000JqvLsIAJ', 'name': 'License Renewal Confusion'}, {'id': '#a03Wt00000JqvNUIAZ', 'name': 'Training Module Access   '}, {'id': 'a03Wt00000JqvvOIAR', 'name': 'Data Loss Incident'}, {'id': '#a03Wt00000JqxVjIAJ', 'name': 'AI Feature Malfunction'}, {'id': '#a03Wt00000JqxtvIAB', 'name': 'Scalability Issue'}, {'id': 'a03Wt00000JqzKcIAJ', 'name': 'Data Integration Error'}, {'id': 'a03Wt00000JqzPSIAZ', 'name': 'Security Compliance Query'}, {'id': 'a03Wt00000JqzR3IAJ', 'name': 'Workflow Integration Lag'}, {'id': 'a03Wt00000JqzSfIAJ', 'name': 'Feature Update Notification'}, {'id': '#a03Wt00000JqzUHIAZ', 'name': 'ROI Assessment Discrepancy'}], 'var_call_m2ZKEuSeEOq1ywr528HuNQ9y': [], 'var_call_GwD7geH1LW9bQUli1wd5d5pM': 'file_storage/call_GwD7geH1LW9bQUli1wd5d5pM.json'}

exec(code, env_args)
