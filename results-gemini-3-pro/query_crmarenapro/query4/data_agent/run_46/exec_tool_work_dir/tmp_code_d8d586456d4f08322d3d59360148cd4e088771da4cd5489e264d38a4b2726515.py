code = """import pandas as pd
import json

order_items_raw = locals()['var_function-call-17975000750771845418']
cases_file = locals()['var_function-call-12209838126625057797']

with open(cases_file, 'r') as f:
    cases_raw = json.load(f)

# Clean Order Item IDs
target_ids = set()
for item in order_items_raw:
    oid = item['Id']
    if oid:
        # remove leading # and whitespace
        clean_id = oid.strip().lstrip('#')
        target_ids.add(clean_id)

# Process Cases
relevant_cases = []
for c in cases_raw:
    oid = c.get('orderitemid__c')
    if oid:
        clean_oid = oid.strip().lstrip('#')
        if clean_oid in target_ids:
            relevant_cases.append(c)

df = pd.DataFrame(relevant_cases)
if not df.empty:
    # Handle mixed format if any, but preview looked consistent iso8601
    # Preview: "2023-07-02T11:00:00.000+0000"
    df['createddate'] = pd.to_datetime(df['createddate'])

    # Filter date range
    # Target date: 2021-04-10
    # Past 10 months -> 2020-06-10 to 2021-04-10
    end_date = pd.Timestamp('2021-04-10').tz_localize('UTC')
    start_date = end_date - pd.DateOffset(months=10)

    # Normalize df timezone to UTC
    if df['createddate'].dt.tz is None:
        df['createddate'] = df['createddate'].dt.tz_localize('UTC')
    else:
        df['createddate'] = df['createddate'].dt.tz_convert('UTC')

    mask = (df['createddate'] >= start_date) & (df['createddate'] <= end_date)
    df_filtered = df[mask].copy()

    if not df_filtered.empty:
        df_filtered['month_name'] = df_filtered['createddate'].dt.month_name()
        df_filtered['year_month'] = df_filtered['createddate'].dt.to_period('M')

        counts = df_filtered.groupby('month_name').size()
        counts_detailed = df_filtered.groupby(['year_month', 'month_name']).size().sort_values(ascending=False)
        
        result = {
            "counts_by_month_name": counts.to_dict(),
            "counts_detailed": {str(k): v for k, v in counts_detailed.to_dict().items()},
            "start_date": str(start_date),
            "end_date": str(end_date)
        }
    else:
        result = {"error": "No cases in date range"}
else:
    result = {"error": "No relevant cases found"}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17975000750771845418': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_function-call-12209838126625057797': 'file_storage/function-call-12209838126625057797.json'}

exec(code, env_args)
