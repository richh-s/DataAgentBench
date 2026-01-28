code = """import pandas as pd
import json

df_items = pd.DataFrame(var_call_PfPxAZZFZBFLgz1wmxFVPd4B)
df_cases = pd.DataFrame(var_call_MoeRG59lUbH5eukc8O1IMDHo)

# Helper to clean IDs (strip leading # and whitespace)
def clean_id(x):
    if pd.isna(x):
        return x
    s = str(x).strip()
    if s.startswith('#'):
        s = s[1:]
    return s

# Clean OrderItem Ids
if not df_items.empty:
    df_items['clean_Id'] = df_items['Id'].apply(clean_id)
    order_item_ids = set(df_items['clean_Id'].astype(str).tolist())
else:
    order_item_ids = set()

# Clean case orderitemid__c
if not df_cases.empty:
    df_cases['clean_orderitemid'] = df_cases['orderitemid__c'].apply(clean_id)
else:
    df_cases['clean_orderitemid'] = []

# Filter cases linked to our product's order items
linked_cases = df_cases[df_cases['clean_orderitemid'].isin(order_item_ids)].copy()

result_month = "No month"

if not linked_cases.empty:
    # parse createddate
    linked_cases['createddate_parsed'] = pd.to_datetime(linked_cases['createddate'], errors='coerce')
    # keep only within the past 10 months window already queried, but ensure non-null dates
    linked_cases = linked_cases[linked_cases['createddate_parsed'].notnull()].copy()
    if not linked_cases.empty:
        # create month-year label and month name
        linked_cases['month_year'] = linked_cases['createddate_parsed'].dt.strftime('%B %Y')
        linked_cases['month_name'] = linked_cases['createddate_parsed'].dt.strftime('%B')
        counts = linked_cases.groupby(['month_year', 'month_name']).size().reset_index(name='count')
        # compute statistics
        mean_count = counts['count'].mean()
        std_count = counts['count'].std(ddof=0)  # population std
        # find max
        max_row = counts.loc[counts['count'].idxmax()]
        max_count = int(max_row['count'])
        max_month_name = str(max_row['month_name'])
        # significance: max > mean + 2*std
        if std_count == 0:
            # if std is zero (all equal), then no significant month
            significant = False
        else:
            significant = (max_count > (mean_count + 2 * std_count))
        if significant:
            result_month = max_month_name

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result_month))"""

env_args = {'var_call_PfPxAZZFZBFLgz1wmxFVPd4B': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796bfIAA', 'OrderId': '801Wt00000PGRh3IAH', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '3.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000796qFIAQ', 'OrderId': '801Wt00000PHRdKIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '7.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079734IAA', 'OrderId': '#801Wt00000PGu6KIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '802Wt00000797W5IAI', 'OrderId': '801Wt00000PHWZlIAP', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000797awIAA', 'OrderId': '801Wt00000PGdVGIA1', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0', 'UnitPrice': '584.991'}, {'Id': '802Wt00000797z7IAA', 'OrderId': '801Wt00000PGos9IAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '#802Wt00000798VPIAY', 'OrderId': '#801Wt00000PGdjoIAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '10.0', 'UnitPrice': '584.991'}, {'Id': '802Wt00000798YdIAI', 'OrderId': '801Wt00000PH8yvIAD', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt00000798okIAA', 'OrderId': '#801Wt00000PGVJJIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '1.0', 'UnitPrice': '649.99'}, {'Id': '#802Wt00000799o1IAA', 'OrderId': '#801Wt00000PGoc0IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '19.0', 'UnitPrice': '584.991'}, {'Id': '802Wt0000079A2bIAE', 'OrderId': '801Wt00000PGe00IAD', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '12.0', 'UnitPrice': '584.991'}, {'Id': '802Wt0000079ACGIA2', 'OrderId': '#801Wt00000PGSYIIA5', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '20.0', 'UnitPrice': '552.4915'}, {'Id': '802Wt0000079B0EIAU', 'OrderId': '801Wt00000PHHMIIA5', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905'}, {'Id': '802Wt0000079B6gIAE', 'OrderId': '#801Wt00000PHQz1IAH', 'Product2Id': '#01tWt000006hVJdIAM', 'Quantity': '4.0', 'UnitPrice': '649.99'}], 'var_call_MoeRG59lUbH5eukc8O1IMDHo': [{'id': '500Wt00000DDDtTIAX', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2020-12-29T08:36:00.000+0000'}, {'id': '500Wt00000DDPM6IAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-01T10:30:00.000+0000'}, {'id': '500Wt00000DDRB2IAP', 'orderitemid__c': '802Wt00000797axIAA', 'createddate': '2021-01-10T09:30:00.000+0000'}, {'id': '500Wt00000DDRVzIAP', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-05T09:15:00.000+0000'}, {'id': '500Wt00000DDYpGIAX', 'orderitemid__c': '802Wt00000798OvIAI', 'createddate': '2021-03-31T11:41:00.000+0000'}, {'id': '#500Wt00000DDZmsIAH', 'orderitemid__c': '802Wt00000795XwIAI', 'createddate': '2020-07-05T09:45:00.000+0000'}, {'id': '500Wt00000DDeoCIAT', 'orderitemid__c': '802Wt00000794bTIAQ', 'createddate': '2020-07-01T15:30:00.000+0000'}, {'id': '#500Wt00000DDfvXIAT', 'orderitemid__c': '802Wt00000796dGIAQ', 'createddate': '2021-03-24T18:04:00.000+0000'}, {'id': '#500Wt00000DDg8QIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-03-05T09:45:00.000+0000'}, {'id': '500Wt00000DDsG4IAL', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-11-05T11:00:00.000+0000'}, {'id': '500Wt00000DDt7HIAT', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-02-01T10:30:00.000+0000'}, {'id': '#500Wt00000DDxnbIAD', 'orderitemid__c': '802Wt00000799o1IAA', 'createddate': '2021-01-25T09:30:00.000+0000'}, {'id': '500Wt00000DDy8bIAD', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-05T08:19:00.000+0000'}, {'id': '500Wt00000DDymuIAD', 'orderitemid__c': '802Wt0000079A2ZIAU', 'createddate': '2020-10-01T14:30:00.000+0000'}, {'id': '500Wt00000DDz6GIAT', 'orderitemid__c': '802Wt00000797r5IAA', 'createddate': '2020-09-03T14:45:00.000+0000'}, {'id': '#500Wt00000DDzKjIAL', 'orderitemid__c': '802Wt00000796JtIAI', 'createddate': '2020-10-22T03:55:00.000+0000'}, {'id': '500Wt00000DDzmAIAT', 'orderitemid__c': '802Wt00000798aDIAQ', 'createddate': '2021-02-20T14:30:00.000+0000'}, {'id': '500Wt00000DE00gIAD', 'orderitemid__c': '802Wt00000796bfIAA', 'createddate': '2020-09-29T01:59:00.000+0000'}, {'id': '500Wt00000DE05VIAT', 'orderitemid__c': '802Wt00000799b7IAA', 'createddate': '2021-01-03T15:30:00.000+0000'}, {'id': '500Wt00000DE0AMIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2021-03-07T11:25:00.000+0000'}, {'id': '500Wt00000DE0DZIA1', 'orderitemid__c': '802Wt00000799uTIAQ', 'createddate': '2020-11-10T22:14:00.000+0000'}, {'id': '500Wt00000DE0NFIA1', 'orderitemid__c': '802Wt00000796qFIAQ', 'createddate': '2020-11-09T19:02:00.000+0000'}, {'id': '500Wt00000DE0WwIAL', 'orderitemid__c': '802Wt00000797foIAA', 'createddate': '2021-03-10T15:45:00.000+0000'}]}

exec(code, env_args)
