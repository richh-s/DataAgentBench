code = """# Read the order item results
order_items = locals()['var_function-call-5856619715739053562']

# Extract IDs and handle potential '#' corruption
ids = []
for item in order_items:
    raw_id = item['Id']
    clean_id = raw_id.lstrip('#')
    ids.append(clean_id)
    ids.append('#' + clean_id)

# Remove duplicates
ids = list(set(ids))

# Prepare SQL IN clause string
# Postgres uses single quotes for strings
in_clause = ", ".join([f"'{x}'" for x in ids])

print("__RESULT__:")
print(in_clause)"""

env_args = {'var_function-call-6912517263467216327': [{'Id': '#01tWt000006hVJdIAM', 'Name': 'SecureAnalytics Pro'}], 'var_function-call-5856619715739053562': [{'Id': '#802Wt0000078yuGIAQ'}, {'Id': '802Wt00000790mOIAQ'}, {'Id': '802Wt00000790zGIAQ'}, {'Id': '802Wt00000794F2IAI'}, {'Id': '802Wt000007968eIAA'}, {'Id': '802Wt00000796bfIAA'}, {'Id': '802Wt00000796qFIAQ'}, {'Id': '802Wt0000079734IAA'}, {'Id': '802Wt00000797W5IAI'}, {'Id': '802Wt00000797awIAA'}, {'Id': '802Wt00000797z7IAA'}, {'Id': '#802Wt00000798VPIAY'}, {'Id': '802Wt00000798YdIAI'}, {'Id': '802Wt00000798okIAA'}, {'Id': '#802Wt00000799o1IAA'}, {'Id': '802Wt0000079A2bIAE'}, {'Id': '802Wt0000079ACGIA2'}, {'Id': '802Wt0000079B0EIAU'}, {'Id': '802Wt0000079B6gIAE'}]}

exec(code, env_args)
