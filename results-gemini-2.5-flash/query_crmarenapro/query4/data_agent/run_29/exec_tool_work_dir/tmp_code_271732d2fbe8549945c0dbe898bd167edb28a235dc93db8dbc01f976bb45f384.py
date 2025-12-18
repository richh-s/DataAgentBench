code = """import json
from datetime import date, timedelta

# The raw string output from the previous tool call, which is the first element of the 'results' list
raw_output_string = locals()['var_function-call-10285647207720889935']['results'][0]

# Find the start and end of the actual JSON array within the string
json_start_index = raw_output_string.find('[')
json_end_index = raw_output_string.rfind(']') + 1

# Extract the JSON string
json_data_string = raw_output_string[json_start_index:json_end_index]

# Load the JSON string into a Python list of dictionaries
order_item_data = json.loads(json_data_string)

# Extract and clean the 'Id' values
order_item_ids = [item['Id'].replace('#', '') for item in order_item_data]

# Calculate the date range for the past 10 months from 2021-04-10
today = date(2021, 4, 10)
# Approximating 10 months as 304 days (10 * 30.4 days/month)
start_date = today - timedelta(days=304)

# Format the order item IDs for the SQL IN clause
order_item_ids_str = ', '.join(["'" + id_ + "'" for id_ in order_item_ids])

# Construct the SQL query using string concatenation
sql_query = "SELECT createddate FROM \"Case\" WHERE orderitemid__c IN (" + order_item_ids_str + ") AND createddate >= '" + start_date.strftime('%Y-%m-%d') + "' AND createddate <= '" + today.strftime('%Y-%m-%d') + "';"

print('__RESULT__:')
print(json.dumps({'sql_query': sql_query}))"""

env_args = {'var_function-call-10285647207720889935': [{'Id': '#802Wt0000078yuGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790mOIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000790zGIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000794F2IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt000007968eIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796bfIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000796qFIAQ', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079734IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797W5IAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000797z7IAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798YdIAI', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt00000798okIAA', 'Product2Id': '01tWt000006hVJdIAM'}, {'Id': '802Wt0000079B0EIAU', 'Product2Id': '01tWt000006hVJdIAM'}]}

exec(code, env_args)
