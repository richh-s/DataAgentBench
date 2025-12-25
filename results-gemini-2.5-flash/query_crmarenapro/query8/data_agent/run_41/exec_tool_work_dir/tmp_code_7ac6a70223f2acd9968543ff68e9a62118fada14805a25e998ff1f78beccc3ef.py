code = """import json

transfer_counts_raw = locals()['var_function-call-13417668301760133805']['query_db_response']['results'][0]
cases_handled_raw = locals()['var_function-call-6458495966495700760']['query_db_response']['results'][0]

# --- Transfer Counts Extraction ---
transfer_counts_extracted = []
transfer_lines = transfer_counts_raw.split('\n')
for line in transfer_lines:
    stripped_line = line.strip()
    if stripped_line.startswith('[') and stripped_line.endswith(']'):
        try:
            transfer_counts_extracted = json.loads(stripped_line)
            break
        except json.JSONDecodeError:
            continue

# --- Cases Handled Extraction ---
cases_handled_extracted = []
cases_lines = cases_handled_raw.split('\n')
for line in cases_lines:
    stripped_line = line.strip()
    if stripped_line.startswith('[') and stripped_line.endswith(']'):
        try:
            cases_handled_extracted = json.loads(stripped_line)
            break
        except json.JSONDecodeError:
            continue

final_agent_id = None

if not transfer_counts_extracted:
    if cases_handled_extracted:
        cases_handled_sorted = sorted(cases_handled_extracted, key=lambda x: x['agent_id'])
        final_agent_id = cases_handled_sorted[0]['agent_id']
    else:
        final_agent_id = "No agents handled cases in the last 4 quarters."
else:
    # This branch is not expected given the current data.
    final_agent_id = "Unexpected scenario: Transfer counts were found."

print("__RESULT__:")
print(json.dumps(final_agent_id))"""

env_args = {'var_function-call-13417668301760133805': [], 'var_function-call-6458495966495700760': [{'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}]}

exec(code, env_args)
