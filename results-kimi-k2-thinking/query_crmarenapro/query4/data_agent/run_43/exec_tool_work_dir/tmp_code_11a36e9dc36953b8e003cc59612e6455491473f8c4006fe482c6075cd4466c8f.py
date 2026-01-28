code = """import json
from collections import defaultdict

# Get the data from previous queries
cases_result = locals()['var_functions.query_db:0']
order_items_result = locals()['var_functions.query_db:2']

# Extract order item IDs for SecureAnalytics Pro and clean them
secure_order_item_ids = set()
for item in order_items_result:
    order_item_id = item['Id']
    # Handle leading # corruption by removing it
    clean_id = order_item_id[1:] if order_item_id.startswith('#') else order_item_id
    secure_order_item_ids.add(clean_id)

print("Number of SecureAnalytics Pro order items:", len(secure_order_item_ids))

# Filter cases to only include those with SecureAnalytics Pro order items
secure_cases = []
for case in cases_result:
    case_order_item_id = case['orderitemid__c']
    if not case_order_item_id:
        continue
    # Clean case order item ID
    clean_case_id = case_order_item_id[1:] if case_order_item_id.startswith('#') else case_order_item_id
    
    if clean_case_id in secure_order_item_ids:
        secure_cases.append(case)

print("Number of SecureAnalytics Pro cases:", len(secure_cases))

# Group cases by month
monthly_counts = defaultdict(int)
month_names = {
    '06': 'June', '07': 'July', '08': 'August', '09': 'September',
    '10': 'October', '11': 'November', '12': 'December',
    '01': 'January', '02': 'February', '03': 'March', '04': 'April'
}

for case in secure_cases:
    created_date = case['createddate']
    # Extract month from date format
    date_part = created_date.split('T')[0]
    month_num = date_part.split('-')[1]  # MM format
    
    # Only include past 10 months from April 2021 (June 2020 to April 2021)
    if date_part >= '2020-06-01' and date_part <= '2021-04-10':
        if month_num in month_names:
            monthly_counts[month_num] += 1

# Prepare output with month names
output = []
for month_num in sorted(monthly_counts.keys()):
    output.append({
        'month': month_names[month_num],
        'case_count': monthly_counts[month_num],
        'month_number': month_num
    })

print("Monthly case counts for SecureAnalytics Pro:")
for item in output:
    print("  " + item['month'] + ": " + str(item['case_count']) + " cases")

# Check if there is a month with significantly more cases
result = None
if len(output) > 0:
    case_counts = [item['case_count'] for item in output]
    max_count = max(case_counts)
    
    if len(case_counts) > 1:
        avg_without_max = (sum(case_counts) - max_count) / (len(case_counts) - 1)
        
        print("\nMaximum cases: " + str(max_count))
        print("Average without max: " + str(round(avg_without_max, 2)))
        print("Ratio: " + str(round(max_count / avg_without_max, 2)) + "x")
        
        if max_count > avg_without_max * 1.5:  # 1.5x threshold
            for item in output:
                if item['case_count'] == max_count:
                    result = item['month']
                    break
    else:
        result = output[0]['month']

# Format final result
final_result = {
    'monthly_summary': output,
    'significant_month': result
}

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_functions.query_db:0': [{'id': '500Wt00000DDDtTIAX', 'createddate': '2020-12-29T08:36:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDPM6IAP', 'createddate': '2020-09-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDRB2IAP', 'createddate': '2021-01-10T09:30:00.000+0000', 'orderitemid__c': '802Wt00000797axIAA'}, {'id': '500Wt00000DDRVzIAP', 'createddate': '2020-09-05T09:15:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '500Wt00000DDYpGIAX', 'createddate': '2021-03-31T11:41:00.000+0000', 'orderitemid__c': '802Wt00000798OvIAI'}, {'id': '#500Wt00000DDZmsIAH', 'createddate': '2020-07-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000795XwIAI'}, {'id': '500Wt00000DDeoCIAT', 'createddate': '2020-07-01T15:30:00.000+0000', 'orderitemid__c': '802Wt00000794bTIAQ'}, {'id': '#500Wt00000DDfvXIAT', 'createddate': '2021-03-24T18:04:00.000+0000', 'orderitemid__c': '802Wt00000796dGIAQ'}, {'id': '#500Wt00000DDg8QIAT', 'createddate': '2021-03-05T09:45:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DDsG4IAL', 'createddate': '2020-11-05T11:00:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDt7HIAT', 'createddate': '2021-02-01T10:30:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}, {'id': '#500Wt00000DDxnbIAD', 'createddate': '2021-01-25T09:30:00.000+0000', 'orderitemid__c': '802Wt00000799o1IAA'}, {'id': '500Wt00000DDy8bIAD', 'createddate': '2020-11-05T08:19:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DDymuIAD', 'createddate': '2020-10-01T14:30:00.000+0000', 'orderitemid__c': '802Wt0000079A2ZIAU'}, {'id': '500Wt00000DDz6GIAT', 'createddate': '2020-09-03T14:45:00.000+0000', 'orderitemid__c': '802Wt00000797r5IAA'}, {'id': '#500Wt00000DDzKjIAL', 'createddate': '2020-10-22T03:55:00.000+0000', 'orderitemid__c': '802Wt00000796JtIAI'}, {'id': '500Wt00000DDzmAIAT', 'createddate': '2021-02-20T14:30:00.000+0000', 'orderitemid__c': '802Wt00000798aDIAQ'}, {'id': '500Wt00000DE00gIAD', 'createddate': '2020-09-29T01:59:00.000+0000', 'orderitemid__c': '802Wt00000796bfIAA'}, {'id': '500Wt00000DE05VIAT', 'createddate': '2021-01-03T15:30:00.000+0000', 'orderitemid__c': '802Wt00000799b7IAA'}, {'id': '500Wt00000DE0AMIA1', 'createddate': '2021-03-07T11:25:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0DZIA1', 'createddate': '2020-11-10T22:14:00.000+0000', 'orderitemid__c': '802Wt00000799uTIAQ'}, {'id': '500Wt00000DE0NFIA1', 'createddate': '2020-11-09T19:02:00.000+0000', 'orderitemid__c': '802Wt00000796qFIAQ'}, {'id': '500Wt00000DE0WwIAL', 'createddate': '2021-03-10T15:45:00.000+0000', 'orderitemid__c': '802Wt00000797foIAA'}], 'var_functions.query_db:2': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
