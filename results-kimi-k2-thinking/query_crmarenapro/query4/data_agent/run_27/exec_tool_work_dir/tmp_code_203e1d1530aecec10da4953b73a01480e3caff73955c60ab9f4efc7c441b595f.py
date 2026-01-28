code = """import json
import datetime

# Get the file path from storage
file_path = locals()['var_functions.query_db:12']

# Load the case data
with open(file_path, 'r') as f:
    cases = json.load(f)

# Find all cases with matching orderitemid__c that contain "802Wt00000797" 
# (this appears to be in SecureAnalytics Pro based on the product detail)
secure_cases = []
for case in cases:
    order_item_id = case.get('orderitemid__c', '')
    if order_item_id and '802Wt00000797' in order_item_id:
        secure_cases.append(case)

# Group by month and year
case_months = {}
for case in secure_cases:
    created_date = case.get('createddate', '')
    if created_date:
        try:
            date_obj = datetime.datetime.fromisoformat(created_date.replace('Z', '+00:00'))
            month_key = date_obj.strftime('%Y-%m')
            month_name = date_obj.strftime('%B %Y')
            
            if month_key not in case_months:
                case_months[month_key] = {'name': month_name, 'count': 0, 'cases': []}
            
            case_months[month_key]['count'] += 1
            case_months[month_key]['cases'].append({
                'date': created_date,
                'orderitemid': case.get('orderitemid__c')
            })
        except:
            continue

# Sort by date
sorted_months = sorted(case_months.items(), key=lambda x: x[0])

# Count all cases from 2020-06 to 2021-04
cutoff_date = datetime.datetime(2021, 4, 10)
start_date = datetime.datetime(2020, 6, 1)

filtered_by_date = {}
for key, data in case_months.items():
    month_date = datetime.datetime.strptime(key, '%Y-%m')
    if start_date <= month_date <= cutoff_date:
        filtered_by_date[key] = data

# Sort by count to find the month with most cases
sorted_by_count = sorted(filtered_by_date.items(), key=lambda x: x[1]['count'], reverse=True)

print("__RESULT__:")
print(json.dumps({
    'all_secure_analytics_cases': case_months,
    'filtered_by_date': filtered_by_date,
    'sorted_by_count': sorted_by_count,
    'total_cases_in_range': sum(data['count'] for data in filtered_by_date.values())
}))"""

env_args = {'var_functions.query_db:0': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro', 'Description': 'Data analytics platform with enhanced focus on security and compliance.', 'IsActive': '1', 'External_ID__c': 'Data Analytics Platforms,Security and Compliance Modules_13'}], 'var_functions.query_db:4': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.list_db:6': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:8': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:16': {'month_counts': {}, 'sorted_months': [], 'total_cases': 0}}

exec(code, env_args)
