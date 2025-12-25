code = """import json
import pandas as pd
from datetime import datetime, timedelta

# Load OrderItem IDs
# It is already a list of dicts
order_items = locals()['var_function-call-10023800480704351753']
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid.startswith('#'):
        oid = oid[1:]
    target_ids.add(oid)

# Load Cases
# This comes from a file path
with open(locals()['var_function-call-708752942025156642'], 'r') as f:
    cases = json.load(f)

# Filter Cases
relevant_cases = []
today = datetime(2021, 4, 10)
# Exact 10 months logic: 
# Let's consider 10 months back from April 2021 is June 2020.
cutoff_date = datetime(2020, 6, 1) 

for case in cases:
    # Check ID match
    oid = case.get('orderitemid__c')
    if not oid:
        continue
    if oid.startswith('#'):
        oid = oid[1:]
    
    if oid in target_ids:
        # Check Date
        cdate_str = case.get('createddate')
        if cdate_str:
            # Parse date. Format examples: "2023-07-02T11:00:00.000+0000"
            try:
                cdate = datetime.strptime(cdate_str[:10], "%Y-%m-%d")
                if cdate <= today and cdate >= cutoff_date:
                    relevant_cases.append(cdate)
            except ValueError:
                pass

# Group by Month
counts = {}
for d in relevant_cases:
    month_key = d.strftime("%B") # Just month name as requested? "Return only the month name."
    # Wait, if I aggregate across years, I might mix up e.g. March 2020 and March 2021.
    # The question asks "in the past 10 months". This implies a specific time window.
    # The result should be "only the month name".
    # But I should calculate based on Year-Month first to separate them.
    month_year_key = d.strftime("%Y-%m")
    counts[month_year_key] = counts.get(month_year_key, 0) + 1

# Find max
print("__RESULT__:")
print(json.dumps(counts))"""

env_args = {'var_function-call-10023800480704351753': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-13331700831189368373': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-708752942025156642': 'file_storage/function-call-708752942025156642.json'}

exec(code, env_args)
