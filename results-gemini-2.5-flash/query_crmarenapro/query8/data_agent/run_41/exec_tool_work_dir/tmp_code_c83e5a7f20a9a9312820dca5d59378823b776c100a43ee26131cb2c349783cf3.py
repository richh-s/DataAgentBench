code = """import json

def parse_json_from_tool_output(tool_output_string):
    # Find the start of the actual JSON data after 'The result is:\n'
    start_marker = "The result is:\n"
    start_index = tool_output_string.find(start_marker)

    if start_index != -1:
        json_candidate = tool_output_string[start_index + len(start_marker):].strip()
        
        # Ensure we only try to parse the JSON array part
        first_bracket = json_candidate.find('[')
        last_bracket = json_candidate.rfind(']')

        if first_bracket != -1 and last_bracket != -1 and first_bracket < last_bracket:
            json_pure_string = json_candidate[first_bracket : last_bracket + 1]
            try:
                return json.loads(json_pure_string)
            except json.JSONDecodeError:
                # If JSON parsing fails, return an empty list
                return []
    return []

# Retrieve raw outputs from previous tool calls
transfer_counts_raw_output = locals()['var_function-call-13417668301760133805']['query_db_response']['results'][0]
cases_handled_raw_output = locals()['var_function-call-6458495966495700760']['query_db_response']['results'][0]

# Parse the raw outputs into Python lists of dictionaries
transfer_counts = parse_json_from_tool_output(transfer_counts_raw_output)
cases_handled = parse_json_from_tool_output(cases_handled_raw_output)

final_agent_id = None

# If no transfer counts are recorded, it means all agents who handled cases had 0 transfers.
if not transfer_counts:
    if cases_handled:
        # All agents in 'cases_handled' (who handled > 0 cases) have the minimum (0) transfers.
        # Sort by agent_id to ensure a consistent output if multiple agents qualify.
        cases_handled_sorted = sorted(cases_handled, key=lambda x: x['agent_id'])
        final_agent_id = cases_handled_sorted[0]['agent_id']
    else:
        final_agent_id = "No agents handled cases in the last 4 quarters."
else:
    # This block would execute if transfer counts were found. However, based on the prior query,
    # 'transfer_counts' is empty for the last 4 quarters, so this path is not taken in this execution.
    # If it were, we would perform a merge and find the agent with the minimum transfer_count.
    final_agent_id = "Unexpected state: Transfers were found, but the problem description implies none should be present given the 'transfer_counts' query result."

print("__RESULT__:")
print(json.dumps(final_agent_id))"""

env_args = {'var_function-call-13417668301760133805': [], 'var_function-call-6458495966495700760': [{'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}]}

exec(code, env_args)
