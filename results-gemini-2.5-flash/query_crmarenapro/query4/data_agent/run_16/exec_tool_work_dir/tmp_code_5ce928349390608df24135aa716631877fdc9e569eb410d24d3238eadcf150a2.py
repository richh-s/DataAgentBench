code = """order_item_ids = [item['Id'] for item in locals()['var_function-call-10613779557943060826']]
cleaned_order_item_ids = [item.replace('#', '').strip() for item in order_item_ids]
ids_str = ", ".join([f"'{item}'" for item in cleaned_order_item_ids])
query = f"""SELECT EXTRACT(MONTH FROM createddate) AS month, COUNT(id) AS case_count FROM "Case" WHERE orderitemid__c IN ({ids_str}) AND createddate >= '2020-06-10' AND createddate <= '2021-04-10' GROUP BY month ORDER BY month;"""
print("__RESULT__:")
print(query)"""

env_args = {'var_function-call-10613779557943060826': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '802Wt0000079B0EIAU'}]}

exec(code, env_args)
