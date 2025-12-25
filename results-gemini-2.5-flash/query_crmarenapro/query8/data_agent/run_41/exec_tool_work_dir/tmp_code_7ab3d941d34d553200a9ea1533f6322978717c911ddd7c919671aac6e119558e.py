code = """import json

def parse_json_from_tool_output(tool_output_string):
    lines = tool_output_string.split('\n')
    json_line = ''
    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith('[') and stripped_line.endswith(']'):
            json_line = stripped_line
            break
    
    if json_line:
        try:
            return json.loads(json_line)
        except json.JSONDecodeError:
            return []
    return []

# Retrieve the raw outputs from previous tool calls
transfer_counts_raw = locals()['var_function-call-13417668301760133805']['query_db_response']['results'][0]
cases_handled_raw = locals()['var_function-call-6458495966495700760']['query_db_response']['results'][0]

# Parse the raw outputs into Python lists of dictionaries
transfer_counts = parse_json_from_tool_output(transfer_counts_raw)
cases_handled = parse_json_from_tool_output(cases_handled_raw)

final_agent_id = None

# As 'transfer_counts' is an empty list, it means no transfers occurred in the last 4 quarters.
# Therefore, all agents who handled cases (filtered by >0 cases) have a transfer count of 0, which is the fewest.
if cases_handled:
    # Sort by 'agent_id' for consistent output if multiple agents qualify (all have 0 transfers).
    cases_handled_sorted = sorted(cases_handled, key=lambda x: x['agent_id'])
    final_agent_id = cases_handled_sorted[0]['agent_id']
else:
    final_agent_id = "No agents handled cases in the last 4 quarters."

print("__RESULT__:")
print(json.dumps(final_agent_id))"""

env_args = {'var_function-call-13417668301760133805': [], 'var_function-call-6458495966495700760': [{'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}]}

exec(code, env_args)
