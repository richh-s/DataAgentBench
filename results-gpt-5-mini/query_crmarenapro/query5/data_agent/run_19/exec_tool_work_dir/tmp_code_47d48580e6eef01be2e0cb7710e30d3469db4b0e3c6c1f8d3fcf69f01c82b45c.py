code = """import json,sys
# Read the OrderItem query result stored in var_call_LUZeqEYyYEBbmZLwf7NtARmc (file path)
path = var_call_LUZeqEYyYEBbmZLwf7NtARmc
with open(path,'r') as f:
    data = json.load(f)
# Extract unique OrderItem Ids, normalize by stripping leading/trailing whitespace and leading '#'
ids = []
for r in data:
    oid = r.get('Id') or r.get('id')
    if oid is None:
        continue
    oid = oid.strip()
    if oid.startswith('#'):
        oid = oid[1:]
    ids.append(oid)
ids = sorted(list(dict.fromkeys(ids)))
print("__RESULT__:")
print(json.dumps(ids))"""

env_args = {'var_call_NUIqU9twUGRd2ALoFbpUctTT': [], 'var_call_SoQuvSZyru7zlSdHk34yjETy': [], 'var_call_LUZeqEYyYEBbmZLwf7NtARmc': 'file_storage/call_LUZeqEYyYEBbmZLwf7NtARmc.json', 'var_call_yI5fIBUDLEi0zOD6h9zyAMX7': [{'Id': '001Wt00000PHVx3IAH', 'Name': 'Altai Innovations'}], 'var_call_DRMxEGt2msTMvDqQT1l0GXXF': [], 'var_call_CVs9zhl6eEJPKnbUCY5bThat': [{'Id': '01tWt000006hV8LIAU', 'External_ID__c': 'AI-Powered Circuit Design Tools,Customizable Workflow Automation_5', 'Name': 'AI Cirku-Tech'}]}

exec(code, env_args)
