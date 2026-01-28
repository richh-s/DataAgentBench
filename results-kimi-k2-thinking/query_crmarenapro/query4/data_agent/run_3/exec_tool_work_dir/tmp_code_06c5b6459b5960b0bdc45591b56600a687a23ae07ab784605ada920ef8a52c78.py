code = """import json

# Read the cases from the file
cases_file = var_functions.query_db:8
with open(cases_file, 'r') as f:
    all_cases = json.load(f)

# Get the order item IDs for SecureAnalytics Pro
orderitem_ids = var_functions.query_db:12
orderitem_id_values = [item['Id'] for item in orderitem_ids]

# Normalize the order item IDs (remove leading # if present)
normalized_orderitem_ids = set()
for oid in orderitem_id_values:
    if oid.startswith('#'):
        normalized_orderitem_ids.add(oid[1:])
    else:
        normalized_orderitem_ids.add(oid)

# Filter cases that are related to SecureAnalytics Pro
secure_analytics_cases = []
for case in all_cases:
    case_orderitem_id = case.get('orderitemid__c', '')
    if not case_orderitem_id:
        continue
    
    # Normalize case orderitem ID
    if case_orderitem_id.startswith('#'):
        case_orderitem_id = case_orderitem_id[1:]
    
    # Check if this case belongs to SecureAnalytics Pro
    if case_orderitem_id in normalized_orderitem_ids:
        # Extract month from createddate
        created_date = case.get('createddate', '')
        if created_date:
            # Parse date and extract month name
            try:
                date_part = created_date.split('T')[0]
                year_month = date_part[:7]  # YYYY-MM format
                case['year_month'] = year_month
                secure_analytics_cases.append(case)
            except:
                continue

result = {
    'total_secure_analytics_cases': len(secure_analytics_cases),
    'cases': secure_analytics_cases
}

result_str = json.dumps(result)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:2': [{'column_name': 'id', 'data_type': 'text'}, {'column_name': 'priority', 'data_type': 'text'}, {'column_name': 'subject', 'data_type': 'text'}, {'column_name': 'description', 'data_type': 'text'}, {'column_name': 'status', 'data_type': 'text'}, {'column_name': 'contactid', 'data_type': 'text'}, {'column_name': 'createddate', 'data_type': 'text'}, {'column_name': 'closeddate', 'data_type': 'text'}, {'column_name': 'orderitemid__c', 'data_type': 'text'}, {'column_name': 'issueid__c', 'data_type': 'text'}, {'column_name': 'accountid', 'data_type': 'text'}, {'column_name': 'ownerid', 'data_type': 'text'}], 'var_functions.query_db:5': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'Id': '#802Wt0000078yuGIAQ', 'OrderId': '801Wt00000PGdVHIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '8.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790mOIAQ', 'OrderId': '#801Wt00000PHQuGIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '30.0', 'UnitPrice': '552.4915', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000790zGIAQ', 'OrderId': '#801Wt00000PGc9QIAT', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '6.0', 'UnitPrice': '617.4905', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt00000794F2IAI', 'OrderId': '801Wt00000PHLzOIAX', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}, {'Id': '802Wt000007968eIAA', 'OrderId': '801Wt00000PH4FLIA1', 'Product2Id': '01tWt000006hVJdIAM', 'Quantity': '2.0', 'UnitPrice': '649.99', 'PriceBookEntryId': '01uWt0000027PJtIAM'}], 'var_functions.query_db:12': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
