code = """import json
from datetime import datetime
import pandas as pd

oli_cases = var_call_TcqMo52Gu1ed2CbXgDF7IIgm
cases = var_call_65EStR2PAIXiBDD8kF77GRsH
order_items = var_call_x7zFkSKGL5VTJnJaOOivtzBO

# normalize order item ids (strip leading #)
oids = {oi['Id'].lstrip('#') for oi in order_items}

# filter cases linked to those order items
filtered_cases = [
    {
        'id': c['id'],
        'createddate': c['createddate']
    }
    for c in cases
    if c.get('orderitemid__c') in oids
]

# convert to DataFrame
if not filtered_cases:
    result = json.dumps(None)
else:
    df = pd.DataFrame(filtered_cases)
    df['createddate'] = pd.to_datetime(df['createddate'])

    # limit to past 10 months from 2021-04-10
    today = datetime(2021, 4, 10)
    start_date = today - pd.DateOffset(months=10)
    df = df[(df['createddate'] >= start_date) & (df['createddate'] <= today)]

    if df.empty:
        result = json.dumps(None)
    else:
        # group by month name and year
        df['month'] = df['createddate'].dt.to_period('M')
        counts = df.groupby('month').size().reset_index(name='count')
        # identify if a month significantly exceeds others: strictly greater than all others
        max_count = counts['count'].max()
        top_months = counts[counts['count'] == max_count]
        if len(top_months) != 1:
            result = json.dumps(None)
        else:
            m = top_months.iloc[0]['month']
            month_name = m.to_timestamp().strftime('%B')
            result = json.dumps(month_name)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_TcqMo52Gu1ed2CbXgDF7IIgm': 'file_storage/call_TcqMo52Gu1ed2CbXgDF7IIgm.json', 'var_call_65EStR2PAIXiBDD8kF77GRsH': 'file_storage/call_65EStR2PAIXiBDD8kF77GRsH.json', 'var_call_x7zFkSKGL5VTJnJaOOivtzBO': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}]}

exec(code, env_args)
