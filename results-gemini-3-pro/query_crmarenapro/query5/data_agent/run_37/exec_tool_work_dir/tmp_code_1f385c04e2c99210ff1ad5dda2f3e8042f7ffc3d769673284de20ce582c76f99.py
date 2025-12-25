code = """import json

# Get the list of OrderItem IDs
order_items = locals()['var_function-call-14234415989743051165']
order_item_ids = [item['Id'] for item in order_items]

# Create a normalized list (removing '#')
normalized_ids = [oid.lstrip('#') for oid in order_item_ids]

# Create a set of all possible variations (original + normalized + maybe with added #)
# To be safe, let's just use the normalized ones and handle the comparison in SQL or python
# PostgreSQL has string functions.

# Let's try to pass the list of IDs to the query.
# Since the list is not too long (around 76 items), we can put them in an IN clause.
# But we should handle the potential '#' in the database column too.
# Query: SELECT issueid__c, createddate FROM Case WHERE orderitemid__c IN (...) 
# But wait, if the DB has "#ABC" and I query "ABC", it won't match.
# If I query "ABC" and DB has "#ABC", it won't match.
# So I should include both "ABC" and "#ABC" in my IN list for every ID.

search_ids = set()
for oid in normalized_ids:
    search_ids.add(oid)
    search_ids.add('#' + oid)

search_ids_list = list(search_ids)

# Quote the IDs for SQL
sql_ids = ", ".join([f"'{oid}'" for oid in search_ids_list])

print("__RESULT__:")
print(json.dumps(sql_ids))"""

env_args = {'var_function-call-11052246743373366289': [], 'var_function-call-10982358805991146901': [], 'var_function-call-17189253336373642667': [{'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}], 'var_function-call-14234415989743051165': [{'Id': '802Wt0000078wz5IAA'}, {'Id': '802Wt0000078xAAIAY'}, {'Id': '802Wt0000078yXiIAI'}, {'Id': '#802Wt00000790WEIAY'}, {'Id': '802Wt00000792gDIAQ'}, {'Id': '802Wt00000792zTIAQ'}, {'Id': '#802Wt0000079315IAA'}, {'Id': '802Wt00000793sTIAQ'}, {'Id': '802Wt00000794F3IAI'}, {'Id': '802Wt00000794F4IAI'}, {'Id': '#802Wt00000794JmIAI'}, {'Id': '#802Wt00000794YFIAY'}, {'Id': '802Wt00000794YJIAY'}, {'Id': '802Wt000007959OIAQ'}, {'Id': '802Wt00000795akIAA'}, {'Id': '802Wt00000795ywIAA'}, {'Id': '802Wt000007962JIAQ'}, {'Id': '802Wt000007968hIAA'}, {'Id': '802Wt000007968iIAA'}, {'Id': '802Wt00000796F5IAI'}, {'Id': '#802Wt00000796N7IAI'}, {'Id': '802Wt00000796NAIAY'}, {'Id': '802Wt00000796RzIAI'}, {'Id': '802Wt00000796S0IAI'}, {'Id': '802Wt00000796S1IAI'}, {'Id': '802Wt00000796VDIAY'}, {'Id': '802Wt00000796YPIAY'}, {'Id': '802Wt00000796YQIAY'}, {'Id': '802Wt00000796a1IAA'}, {'Id': '802Wt00000796dFIAQ'}, {'Id': '#802Wt00000796dIIAQ'}, {'Id': '#802Wt00000796jiIAA'}, {'Id': '802Wt00000796myIAA'}, {'Id': '802Wt00000796oaIAA'}, {'Id': '802Wt00000796rlIAA'}, {'Id': '802Wt00000796tTIAQ'}, {'Id': '802Wt00000796v0IAA'}, {'Id': '802Wt00000796wbIAA'}, {'Id': '802Wt00000796wcIAA'}, {'Id': '802Wt00000797FxIAI'}, {'Id': '802Wt00000797MQIAY'}, {'Id': '#802Wt00000797O5IAI'}, {'Id': '#802Wt00000797axIAA'}, {'Id': '802Wt00000797e9IAA'}, {'Id': '802Wt00000797hNIAQ'}, {'Id': '802Wt00000797j0IAA'}, {'Id': '#802Wt00000797mDIAQ'}, {'Id': '802Wt00000797nsIAA'}, {'Id': '#802Wt00000797pSIAQ'}, {'Id': '802Wt00000797sfIAA'}, {'Id': '802Wt00000797z8IAA'}, {'Id': '802Wt000007982LIAQ'}, {'Id': '802Wt00000798IUIAY'}, {'Id': '802Wt00000798IVIAY'}, {'Id': '802Wt00000798NKIAY'}, {'Id': '#802Wt00000798S9IAI'}, {'Id': '#802Wt00000798nBIAQ'}, {'Id': '802Wt00000798rxIAA'}, {'Id': '802Wt00000798wpIAA'}, {'Id': '802Wt000007991dIAA'}, {'Id': '802Wt0000079987IAA'}, {'Id': '802Wt00000799EZIAY'}, {'Id': '802Wt00000799HoIAI'}, {'Id': '#802Wt00000799JPIAY'}, {'Id': '802Wt00000799T3IAI'}, {'Id': '802Wt00000799ckIAA'}, {'Id': '#802Wt00000799fxIAA'}, {'Id': '802Wt00000799srIAA'}, {'Id': '802Wt00000799w5IAA'}, {'Id': '#802Wt0000079A0wIAE'}, {'Id': '802Wt0000079A2aIAE'}, {'Id': '802Wt0000079A49IAE'}, {'Id': '802Wt0000079AU1IAM'}, {'Id': '802Wt0000079AgrIAE'}, {'Id': '802Wt0000079AqXIAU'}, {'Id': '802Wt0000079As9IAE'}]}

exec(code, env_args)
