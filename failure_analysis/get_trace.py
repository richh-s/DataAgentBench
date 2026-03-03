import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common_scaffold.validate.validate  import validate
from pathlib import Path
import json

def get_trace(model, task, query_id, run_id):
    query_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f"results-{model}", f"query_{task}", f"query{query_id}")
    if model != "gpt5.1":
        final_agent_file = os.path.join(query_folder, "data_agent", f"run_{run_id}", "final_agent.json")
    else:
        final_agent_file = os.path.join(query_folder, f"run_{run_id}", "final_agent.json")
    
    assert os.path.exists(os.path.dirname(final_agent_file)), f"Query folder {os.path.dirname(final_agent_file)} does not exist."
    is_failed = False
    failed_reason = None
    failed_trace = None
    if not os.path.exists(final_agent_file):
        is_failed = True
        failed_reason = "final_agent.json not found"
        return is_failed, failed_reason, failed_trace
    
    with open(final_agent_file, encoding="utf-8") as f:
        final_agent_json = json.load(f)

    llm_answer = final_agent_json['final_result']
    terminate_reason = final_agent_json['terminate_reason']

    validation_result = validate(Path(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f"query_{task}", f"query{query_id}")), llm_answer, terminate_reason)
    
    if validation_result["is_valid"]:
        return is_failed, failed_reason, failed_trace
    
    is_failed = True

    if terminate_reason != "return_answer":
        failed_reason = terminate_reason
        return is_failed, failed_reason, failed_trace
    
    try:
        messages = final_agent_json['messages']
    except KeyError:
        failed_reason = "messages not found in final_agent.json"
        return is_failed, failed_reason, failed_trace
    
    
    try:
        failed_trace = format_trace(messages)
        failed_reason = "return_answer"
    except Exception as e:
        failed_reason = f"Error formatting trace: {str(e)}"

    return is_failed, failed_reason, failed_trace.strip()


def convert_strings(obj):
    if isinstance(obj, dict):
        return {k: convert_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_strings(v) for v in obj]
    elif isinstance(obj, str):
        try:
            return json.loads(obj)
        except json.JSONDecodeError:
            return obj
    else:
        return obj


def format_trace(messages):
    clean_msg = convert_strings(messages)
    trace_str = ""

    for msg in clean_msg:
        role = msg['role']
        if role == "system":
            trace_str += f"==========[system message]==========\n{msg['content'].strip()}\n"
        elif role == "user":
            trace_str += f"==========[user message]==========\n{msg['content'].strip()}\n"
        elif role == "assistant":
            tool_calls = msg['tool_calls']
            trace_str += "==========[assistant message]==========\n"
            for tool_call in tool_calls:
                tool_id = tool_call['id']
                tool_name = tool_call['function']['name']
                tool_arg_dict = tool_call['function']['arguments']
                assert isinstance(tool_arg_dict, dict)
                trace_str += f'''--------[tool call]--------\nid: "{tool_id}"\nname: {tool_name}\narguments: {', '.join(list(tool_arg_dict.keys()))}\n'''
                for arg_key, arg_value in tool_arg_dict.items():
                    trace_str += f"--[{arg_key} argument]--\n"
                    trace_str += f"{arg_value}\n"
        elif role == "tool":
            tool_name = msg['name']
            if tool_name == "return_answer":
                break
            trace_str += f"==========[tool message]==========\n"
            tool_id = msg['tool_call_id']
            tool_result = msg['content'].strip()
            trace_str += f'''id: "{tool_id}"\nname: {tool_name}\n--[execution result]--\n{tool_result}\n'''

    return trace_str.strip()

if __name__ == "__main__":
    is_failed, failed_reason, failed_trace = get_trace(
        model="gpt-5-mini",
        task="bookreview",
        query_id=1,
        run_id=1
    )

    print(failed_trace)
    