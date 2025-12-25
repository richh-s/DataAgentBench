code = """import json

def parse_tool_output_json(raw_output_string):
    # The actual JSON list is embedded within a verbose string output by the tool.
    # We need to find the substring that is a valid JSON list.
    
    # The marker indicating the start of the result JSON
    start_marker = "The result is:\n"
    start_index = raw_output_string.find(start_marker)

    if start_index != -1:
        # Extract the part of the string that should contain the JSON list
        json_candidate = raw_output_string[start_index + len(start_marker):].strip()
        
        # Find the actual JSON list within the candidate string
        # It should start with '[' and end with ']'
        first_bracket_idx = json_candidate.find('[')
        last_bracket_idx = json_candidate.rfind(']')

        if first_bracket_idx != -1 and last_bracket_idx != -1 and first_bracket_idx < last_bracket_idx:
            pure_json_string = json_candidate[first_bracket_idx : last_bracket_idx + 1]
            try:
                return json.loads(pure_json_string)
            except json.JSONDecodeError:
                # If JSON parsing fails, return an empty list
                return []
    return [] # If marker not found or invalid JSON structure, return empty list

# Retrieve the raw outputs from previous tool calls
transfer_counts_raw = locals()['var_function-call-13417668301760133805']['query_db_response']['results'][0]
cases_handled_raw = locals()['var_function-call-6458495966495700760']['query_db_response']['results'][0]

# Parse the raw outputs into Python lists of dictionaries
transfer_counts = parse_tool_output_json(transfer_counts_raw)
cases_handled = parse_tool_output_json(cases_handled_raw)

final_agent_id = None

# Based on the initial query, 'transfer_counts' is an empty list, meaning no transfers occurred.
# Therefore, any agent who handled cases (filtered by >0 cases) has a transfer count of 0, which is the minimum.
if cases_handled:
    # Sort by 'agent_id' for consistent output if multiple agents qualify.
    cases_handled_sorted = sorted(cases_handled, key=lambda x: x['agent_id'])
    final_agent_id = cases_handled_sorted[0]['agent_id']
else:
    final_agent_id = "No agents handled cases in the last 4 quarters."

print("__RESULT__:")
print(json.dumps(final_agent_id))"""

env_args = {'var_function-call-13417668301760133805': [], 'var_function-call-6458495966495700760': [{'agent_id': '005Wt000003NJrRIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NBykIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIVZIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NEzqIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHpeIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NI2XIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJD9IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIc2IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NHsrIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJhlIAG', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJTFIA4', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJEjIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ0DIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFKoIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NJ8HIAW', 'cases_handled': '3'}, {'agent_id': '#005Wt000003NBcAIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NInLIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NGjuIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDJ1IAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDsUIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NINVIA4', 'cases_handled': '2'}, {'agent_id': '005Wt000003NJ6gIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIwzIAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NDqFIAW', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NJoDIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NISLIA4', 'cases_handled': '1'}, {'agent_id': '005Wt000003NFKoIAO', 'cases_handled': '2'}, {'agent_id': '005Wt000003NEGhIAO', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIvNIAW', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIliIAG', 'cases_handled': '1'}, {'agent_id': '#005Wt000003NFr4IAG', 'cases_handled': '1'}, {'agent_id': '005Wt000003NIaQIAW', 'cases_handled': '1'}]}

exec(code, env_args)
