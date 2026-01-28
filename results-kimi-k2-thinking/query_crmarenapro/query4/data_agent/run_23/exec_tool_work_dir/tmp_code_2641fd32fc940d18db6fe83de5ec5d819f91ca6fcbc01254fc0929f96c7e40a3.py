code = """import json
from datetime import datetime

# Access stored results
cases_data = locals()['var_functions.query_db:32']
order_items_data = locals()['var_functions.query_db:14']

# Extract product-related order item IDs
product_order_item_ids = set(item['Id'].lstrip('#') for item in order_items_data)

print("Product Order Item IDs:", product_order_item_ids)
print("\n" + "="*50)

# Analyze the cases
monthly_counts = {}
secureanalytics_cases = []

for case in cases_data:
    orderitem_id = case.get('orderitemid__c', '').lstrip('#')
    created_date_str = case.get('createddate')
    subject = case.get('subject', '')
    description = case.get('description', '')
    
    # Check if this case is actually for SecureAnalytics Pro
    if (('secureanalytics' in subject.lower() or 'secureanalytics' in description.lower()) and 
        orderitem_id and 
        created_date_str):
        
        # Convert date
        created_date = datetime.fromisoformat(created_date_str.replace('Z', '+00:00'))
        month_key = created_date.strftime('%Y-%m')
        month_name = created_date.strftime('%B %Y')
        
        secureanalytics_cases.append({
            'date': created_date,
            'orderitem_id': orderitem_id,
            'subject': subject,
            'in_product_list': orderitem_id in product_order_item_ids
        })
        
        if month_key not in monthly_counts:
            monthly_counts[month_key] = {'count': 0, 'name': month_name, 'month': created_date.strftime('%B')}
        monthly_counts[month_key]['count'] += 1

# Sort and display results
sorted_months = sorted(monthly_counts.items(), key=lambda x: x[0])

print("Monthly case counts for SecureAnalytics Pro:")
for month_key, data in sorted_months:
    print(f"  {data['name']}: {data['count']} cases")

print(f"\nTotal cases: {len(secureanalytics_cases)}")
print(f"Valid cases (with matching orderitem): {sum(1 for c in secureanalytics_cases if c['in_product_list'])}")

# Find month with most cases
if sorted_months:
    max_month = max(sorted_months, key=lambda x: x[1]['count'])
    counts = [data['count'] for month_key, data in sorted_months]
    
    if len(counts) > 1:
        max_count = max(counts)
        other_counts = [c for c in counts if c != max_count]
        
        if other_counts:
            avg_other = sum(other_counts) / len(other_counts)
            print(f"\nMax month: {max_month[1]['month']} with {max_count} cases")
            print(f"Average of other months: {avg_other:.1f}")
            
            if max_count > avg_other * 2:
                result = max_month[1]['month']
                print(f"SIGNIFICANT: Yes, {result}")
            else:
                result = "No significant month"
                print(f"SIGNIFICANT: No")
        else:
            result = max_month[1]['month']
    else:
        result = max_month[1]['month']
else:
    result = "No cases found"

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_functions.query_db:2': [], 'var_functions.query_db:5': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_functions.query_db:10': [{'id': '#500Wt00000DDDfwIAH', 'priority': 'Medium', 'subject': 'Feature Update Notifications Lack', 'description': "Without regular update notifications, we are unable to fully utilize CollabCircuit Hub's latest features.", 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqxKSIAZ', 'createddate': '2023-07-02T11:00:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000797r4IAA', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PFttwIAD', 'ownerid': '005Wt000003NJ0DIAW'}, {'id': '500Wt00000DDDtTIAX', 'priority': 'Medium', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.', 'status': 'Waiting on Customer   ', 'contactid': '003Wt00000Jqp3WIAR', 'createddate': '2020-12-29T08:36:00.000+0000', 'closeddate': 'None', 'orderitemid__c': '802Wt00000798aDIAQ', 'issueid__c': 'a03Wt00000JqzSfIAJ', 'accountid': '001Wt00000PHVkAIAX', 'ownerid': '#005Wt000003NJWTIA4'}, {'id': '500Wt00000DDNYoIAP', 'priority': 'Medium', 'subject': 'Delayed Support Response ', 'description': 'I am experiencing delays in getting timely responses from TechPulse support during busy periods, which is affecting our project timelines.', 'status': 'Closed', 'contactid': '#003Wt00000JqqVtIAJ', 'createddate': '2023-09-30T11:30:00.000+0000', 'closeddate': '2023-09-30T16:03:45.000+0000', 'orderitemid__c': '802Wt00000792tiIAA', 'issueid__c': 'a03Wt00000JqtOtIAJ', 'accountid': '001Wt00000PGZZoIAP', 'ownerid': '005Wt000003NIc3IAG'}, {'id': '500Wt00000DDPIsIAP', 'priority': 'Medium', 'subject': 'AI Feature Malfunction', 'description': 'Some of the AI-powered features in CloudLink Designer are intermittently failing to operate, leading to reduced efficiency and user frustration.', 'status': 'Closed ', 'contactid': '003Wt00000JqlkjIAB', 'createddate': '2022-08-05T14:30:00.000+0000', 'closeddate': '2022-08-05T14:39:32.000+0000', 'orderitemid__c': '802Wt00000797r3IAA', 'issueid__c': 'a03Wt00000JqxVjIAJ', 'accountid': '#001Wt00000PGRnYIAX', 'ownerid': '#005Wt000003NEzqIAG'}, {'id': '500Wt00000DDPM6IAP', 'priority': 'High', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite.", 'status': 'Closed', 'contactid': '#003Wt00000Jqv14IAB', 'createddate': '2020-09-01T10:30:00.000+0000', 'closeddate': '2020-09-01T14:08:55.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'issueid__c': 'a03Wt00000JqvNUIAZ', 'accountid': '001Wt00000PGzSaIAL', 'ownerid': '005Wt000003NISLIA4'}], 'var_functions.query_db:12': [{'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ', 'subject': 'Integration Lag Issue', 'description': 'I have been experiencing latency issues when deploying the AI Cirku-Tech platform within our complex workflows, and it is hindering our productivity.'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI', 'subject': 'Lack of Feature Updates', 'description': 'We are not consistently notified about new feature updates in the DesignWave Automation tool, causing us to miss out on utilizing its full capabilities.'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'subject': 'Access Issues with Training Module', 'description': "I am experiencing difficulty accessing the online training modules which are crucial for my team's smooth adoption of the SecureFlow Suite."}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'subject': 'Intermittent Training Module Access', 'description': 'My team is facing intermittent access issues with the training modules, hindering our ability to efficiently integrate the SecureFlow Suite into our operations.'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA', 'subject': 'Training Portal Login Problem', 'description': 'The login process for the training modules included with the SecureFlow Suite is causing disruption due to technical glitches, affecting our learning path.'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards."}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU', 'subject': 'Training Module Login Trouble   ', 'description': 'There are technical problems preventing me from logging into the training modules which are important for learning to use PulseSim Pro.'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI', 'subject': 'CloudLink Performance Issue', 'description': 'The deployment of CloudLink Designer into our existing systems is causing noticeable latency, affecting our project timelines significantly.'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them."}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU', 'subject': 'Cannot Access Training Resources', 'description': 'I am facing occasional difficulties accessing the training resources necessary for gaining proficiency with PulseSim Pro.'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ', 'subject': 'DesignWave Integration Delay', 'description': "There's a delay when implementing DesignWave Automation into our processes, which impacts efficiency."}, {'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'subject': 'Missing Feature Update Alerts', 'description': 'I have noticed that I am not consistently receiving notifications about new feature updates for the SecureFlow Suite, which affects my ability to use the software to its full potential.'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA', 'subject': 'Integration Lag Issue', 'description': 'I am experiencing latency issues when deploying AI Cirku-Tech within our existing workflows, which affects overall performance.'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA', 'subject': 'AI Cirku-Tech Workflow Lag', 'description': "I'm experiencing latency issues with AI Cirku-Tech when integrating it into our current workflow systems."}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA', 'subject': 'Security Compliance Standards', 'description': 'I am having difficulty comprehending the latest security compliance standards provided by TechPulse Solutions and require clarification.'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'subject': 'Uninformed on Updates', 'description': 'The lack of consistent update notifications for SecureFlow Suite is causing me to miss out on new features that are important for our compliance requirements.'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ', 'subject': 'Feature Updates Not Communicated', 'description': "I'm finding it difficult to keep up with the latest improvements in SecureFlow Suite as update alerts are not always received."}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA', 'subject': 'Compliance Guidelines Help', 'description': 'Navigating the security compliance guidelines established by TechPulse Solutions is proving challenging and I need assistance to better follow them.'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ', 'subject': 'Data Integration Error', 'description': 'I am experiencing challenges when integrating TechPulse solutions with specific third-party software, leading to workflow disruptions.'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI', 'subject': 'Workflow Integration Lag  ', 'description': 'I am experiencing latency issues when deploying TechPulse solutions within complex existing workflows, causing delays in operations.'}], 'var_functions.query_db:14': [{'Id': '802Wt00000797awIAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '#802Wt00000798VPIAY', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '#802Wt00000799o1IAA', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079A2bIAE', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079ACGIA2', 'Product2Id': '#01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B6gIAE', 'Product2Id': '#01tWt000006hVJdIAM'}], 'var_functions.execute_python:28': 'No significant month', 'var_functions.query_db:32': [{'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA', 'subject': 'ROI Metrics Clarification  ', 'description': 'I am experiencing difficulty aligning the performance metrics provided by SecureAnalytics Pro with our expected ROI, and need assistance to reconcile these discrepancies.'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'Update Alerts Absent', 'description': "The system does not alert me to the new features added to SecureAnalytics Pro, leading to underutilization of its updates as I'm unaware of them."}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA', 'subject': 'SecureAnalytics Compliance Concern', 'description': "I need clarification on SecureAnalytics Pro's adherence to security compliance standards."}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'No Feature Update Notices', 'description': 'I am consistently not getting notified about feature updates for SecureAnalytics Pro, which means I am unable to take advantage of improvements and enhancements.'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ', 'subject': 'Missing Feature Notifications', 'description': 'I have not been receiving notifications about new features in SecureAnalytics Pro, causing me to miss out on utilizing the full capabilities of the platform.'}]}

exec(code, env_args)
