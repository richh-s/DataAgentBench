code = """import json
import pandas as pd

# Load cases from storage
cases = var_call_3xA8RY38ByZPxMfTSKv3I7vz

# Create DataFrame
df = pd.DataFrame(cases)
# Parse createddate safely
if not df.empty:
    df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')
    # Create year-month key and month name
    df['year_month'] = df['createddate'].dt.strftime('%Y-%m')
    df['month_name'] = df['createddate'].dt.strftime('%B')
    # Count by year-month to avoid merging different years' months
    counts = df.groupby('year_month').size().reset_index(name='count')
    # Add month_name for each year_month
    counts['month_name'] = counts['year_month'].apply(lambda ym: pd.to_datetime(ym + '-01').strftime('%B'))
    # Sort by count desc
    counts_sorted = counts.sort_values('count', ascending=False).reset_index(drop=True)
    if counts_sorted.shape[0] == 0:
        result = None
    else:
        max_count = int(counts_sorted.loc[0,'count'])
        max_month = counts_sorted.loc[0,'month_name']
        second_count = int(counts_sorted.loc[1,'count']) if counts_sorted.shape[0] > 1 else 0
        # Define significant: max_count >= 2 and max_count >= 2 * second_count
        if max_count >= 2 and max_count >= 2 * second_count:
            result = max_month
        else:
            result = None
else:
    result = None

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_adGh85MUO8pihNQD181azUC5': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGdVHIA1'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PHQuGIAX'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGc9QIAT'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHLzOIAX'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PH4FLIA1'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGRh3IAH'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHRdKIAX'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGu6KIAT'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHWZlIAP'}, {'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGdVGIA1'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGos9IAD'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGdjoIAD'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PH8yvIAD'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGVJJIA5'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGoc0IAD'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM', 'OrderId': '801Wt00000PGe00IAD'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PGSYIIA5'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM', 'OrderId': '801Wt00000PHHMIIA5'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM', 'OrderId': '#801Wt00000PHQz1IAH'}], 'var_call_3xA8RY38ByZPxMfTSKv3I7vz': [{'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}]}

exec(code, env_args)
