code = """import json
import pandas as pd
from datetime import datetime

# Load Case data
with open(locals()['var_function-call-5866975110549239295'], 'r') as f:
    cases = json.load(f)

# Load OrderItem data
order_items = locals()['var_function-call-5866975110549240888']

# Create set of target OrderItem Ids (cleaned)
target_ids = set()
for item in order_items:
    oid = item['Id']
    if oid:
        cleaned = oid.strip().lstrip('#')
        target_ids.add(cleaned)

# Process Cases
relevant_cases = []
for case in cases:
    # Check if case is in target product list
    raw_oid = case.get('orderitemid__c')
    if not raw_oid:
        continue
    cleaned_oid = raw_oid.strip().lstrip('#')
    
    if cleaned_oid in target_ids:
        # Parse date
        cdate_str = case['createddate']
        # Format example: "2023-07-02T11:00:00.000+0000"
        # We only need month and year, and to filter by range.
        # Date filtering: past 10 months from 2021-04-10.
        # Range: [2020-06-10, 2021-04-10] approximately.
        # Let's use strict date comparison.
        
        try:
            # simple string slice might work for YYYY-MM
            cdate_dt = datetime.strptime(cdate_str, "%Y-%m-%dT%H:%M:%S.%f%z")
            
            # Check range
            # 2021-04-10
            ref_date = datetime(2021, 4, 10).date()
            case_date = cdate_dt.date()
            
            # 10 months ago approx.
            # Let's check logic: "past 10 months". Usually means [2020-06-10, 2021-04-10].
            # Or just strictly the months within that window.
            # Let's collect all cases first, then filter.
            
            # Calculate months difference
            # (2021 * 12 + 4) - (y * 12 + m) <= 10 and >= 0
            
            # Actually just comparing dates is easier.
            start_date = datetime(2020, 6, 10).date() # Approximate start of "past 10 months"
            # It says "in the past 10 months".
            
            if start_date <= case_date <= ref_date:
                relevant_cases.append({
                    'month': case_date.strftime('%B'),
                    'year_month': case_date.strftime('%Y-%m')
                })
                
        except ValueError:
            pass

# Count by month
df = pd.DataFrame(relevant_cases)
if not df.empty:
    counts = df['year_month'].value_counts().sort_index()
    # Also get month name for the answer
    counts_named = df['month'].value_counts()
    
    print("__RESULT__:")
    print(json.dumps({
        "counts_by_ym": counts.to_dict(),
        "counts_by_name": counts_named.to_dict()
    }))
else:
    print("__RESULT__:")
    print(json.dumps({"counts": {}}))"""

env_args = {'var_function-call-2761220900479506085': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_function-call-2761220900479505406': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_function-call-5866975110549239295': 'file_storage/function-call-5866975110549239295.json', 'var_function-call-5866975110549240888': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
