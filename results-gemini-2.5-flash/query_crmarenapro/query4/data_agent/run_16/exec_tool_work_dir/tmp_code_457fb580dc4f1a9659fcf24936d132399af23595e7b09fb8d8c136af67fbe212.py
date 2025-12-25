code = """order_item_ids = [item['Id'] for item in locals()['var_function-call-10613779557943060826']]
# Clean the IDs by removing '#' and trailing whitespace
cleaned_order_item_ids = [item.replace('#', '').strip() for item in order_item_ids]

# Construct the WHERE clause for the SQL query
# Use "IN" clause for multiple IDs
ids_str = ", ".join([f"'{item}'" for item in cleaned_order_item_ids])

# Construct the SQL query to get cases that match the order item IDs
# and are within the last 10 months from 2021-04-10
# PostgreSQL date functions: EXTRACT(MONTH FROM date_field) extracts the month as a number
# and AGE(DATE 'end_date', date_field) calculates the difference
# To filter for the last 10 months, we can filter for createddate >= '2020-06-10'
# Convert the result into a list of dictionaries with month and count
query = f"""
SELECT
    EXTRACT(MONTH FROM createddate) AS month,
    COUNT(id) AS case_count
FROM
    "Case"
WHERE
    orderitemid__c IN ({ids_str}) AND createddate >= '2020-06-10' AND createddate <= '2021-04-10'
GROUP BY
    month
ORDER BY
    month;
"""
print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-10613779557943060826': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
