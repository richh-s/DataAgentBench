code = """import json
order_items = var_call_a433CLEzt6I8m4RjuvJ70625
ids = [row['Id'].replace('#','') for row in order_items]
ids_list = "','".join(ids)
query = f"SELECT to_char(createddate::timestamp, 'Month') AS month_name, date_trunc('month', createddate::timestamp) AS month, COUNT(*) AS case_count FROM \"Case\" WHERE createddate >= '2020-06-10' AND createddate < '2021-04-11' AND REPLACE(orderitemid__c, '#', '') IN ('{ids_list}') GROUP BY month_name, month ORDER BY month;"
print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_call_a433CLEzt6I8m4RjuvJ70625': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
