code = """import json
import pandas as pd
from datetime import datetime

# Load OrderItem IDs
order_items = locals()['var_function-call-15960168675309596331']
# Normalize OrderItem IDs (remove leading #)
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_ids.add(oid)

# Load Case data
file_path = locals()['var_function-call-5822691755495783972']
with open(file_path, 'r') as f:
    cases = json.load(f)

# Date limits
end_date = datetime(2021, 4, 10)
start_date = datetime(2020, 6, 10) # 10 months prior

counts = {}

for case in cases:
    oid = case.get('orderitemid__c')
    if not oid:
        continue
    # Normalize case order item id
    if oid.startswith('#'):
        oid = oid[1:]
    
    if oid in target_ids:
        c_date_str = case.get('createddate')
        # Parse date. Format: 2023-07-02T11:00:00.000+0000
        # We only care about date part usually, but let's parse fully
        try:
            # Simple substring parsing to avoid timezone lib issues if possible, or use strptime
            # 2020-09-01
            dt_str = c_date_str[:10]
            dt = datetime.strptime(dt_str, '%Y-%m-%d')
            
            if start_date <= dt <= end_date:
                month_key = dt.strftime('%B') # Full month name
                month_year_key = dt.strftime('%Y-%m')
                
                # Check if we need to distinguish years. 
                # The question asks for "a particular month".
                # Let's count by Month Name first.
                counts[month_key] = counts.get(month_key, 0) + 1
        except Exception as e:
            pass

print("__RESULT__:")
print(json.dumps(counts))"""

env_args = {'var_function-call-1114849343674935655': [], 'var_function-call-1114849343674935754': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}], 'var_function-call-10923393815479506923': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-15960168675309596331': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-5822691755495783972': 'file_storage/function-call-5822691755495783972.json'}

exec(code, env_args)
