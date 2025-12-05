# Reference of tool calling: https://docs.vllm.ai/en/v0.6.0/getting_started/examples/openai_chat_completion_client_with_tools.html

import json
import sys
from pathlib import Path
import os
from datetime import datetime
import time
import logging
from common_scaffold.db_utils.loader import query_db
from common_scaffold.agent_tools import (
    list_dbs,
    transform_tool_args,
    generate_var_name,
    execute_python,
    build_messages,
    get_tools_spec,
    format_preview,
    format_stdout,
    auto_ensure_databases,
    validate_and_log,
    log_failed,
    upload_to_client,
    RepeatedCallTracker, 
    QueryDbFailureTracker
)

PREVIEW_MAX_LEN = 10000

def run_basic_agent(
    query_dir: Path,
    project_dir: Path,
    db_description: str,
    db_config: dict,
    client,
    deployment_name: str
) -> bool:
    """
    Run one query task in the agent pipeline.

    Args:
        query_dir (Path): Path to the queryX folder.
        project_dir (Path): Path to the project root folder.
        db_description (str): Database description text.
        db_config (dict): Database configuration dictionary.
        client: OpenAI/AzureOpenAI client instance.
        deployment_name (str): Model deployment name.

    Returns:
        bool: True if query succeeded and passed validation, False otherwise.
    """
    # Setup logging directories
    root_log_dir = os.path.join(query_dir, "logs", run_basic_agent.__name__, datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(root_log_dir, exist_ok=True)
    logging.info(f"Log directory created at: {root_log_dir}")
    # Setup disk storage
    uploaded_files_dir = os.path.join(root_log_dir, "uploaded_files")
    os.makedirs(uploaded_files_dir, exist_ok=True)
    logging.info(f"File storage created at: {uploaded_files_dir}")
    # Setup DB
    db_clients = db_config["db_clients"]
    auto_ensure_databases(db_clients)
    logging.info(f"DB connections ready: {db_clients.keys()}")
    # Load user query
    with open(query_dir / "query.json") as f:
        query_content = json.load(f)
    if isinstance(query_content, str):
        user_query = query_content
    elif isinstance(query_content, dict) and "query" in query_content:
        user_query = query_content["query"]
    else:
        raise ValueError("Invalid query format: query.json must contain either a string or a {'query': ...} dict")
    logging.info(f"User query: {user_query}")

    messages = build_messages(user_query, db_description)
    # Define tools
    def list_dbs_tool(**tool_args):
        return list_dbs(tool_args["db_name"], db_clients)

    def return_answer(answer: str):
        """
        Handle final answer from LLM and validate it.
        """
        is_valid, reason = validate_and_log(query_dir, answer, root_log_dir)

        return is_valid, reason

    tools_spec = get_tools_spec()

    TOOLS = {
        "query_db": query_db,
        "list_dbs": list_dbs_tool,
        "execute_python": lambda code: execute_python(code),
        "return_answer": lambda **kwargs: return_answer(**kwargs)
    }
    # Define LLM call
    def call_llm(messages)-> tuple:
        """
        Call the LLM to get the next step decision and tool arguments.
        """
        start = time.time()
        resp = client.chat.completions.create(
            model=deployment_name,
            messages=messages,
            tools=tools_spec
        )
        end = time.time()
        #### log
        log_entry = {
            "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "start_time": start,
            "end_time": end,
            "duration": end - start,
            "model": deployment_name,
            "response": resp.to_dict(),
            "messages": [m.model_dump() if not isinstance(m, dict) else m for m in messages],
        }
        log_path = os.path.join(root_log_dir, "llm_calls.jsonl")
        with open(log_path, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")
        ####
        assistant_msg = resp.choices[0].message
        print(f"\n{'-' * 10}\nLLM response:\n{assistant_msg}\n{'-' * 10}\n")
        # Parse tool call if present
        if assistant_msg.tool_calls:
            tool_calls = []
            for tc in assistant_msg.tool_calls:
                tool_name = tc.function.name
                tool_args = json.loads(tc.function.arguments)
                if isinstance(tool_args, dict) and "args" in tool_args:
                    tool_args = tool_args["args"]
                tool_calls.append({
                    "id": tc.id,
                    "name": tool_name,
                    "args": tool_args
                })
            return assistant_msg, tool_calls
        # Fallback: try parsing content as JSON (for return_answer-style messages)
        if assistant_msg.content:
            try:
                obj = json.loads(assistant_msg.content)
                if isinstance(obj, dict) and obj.get("tool") == "return_answer" and "args" in obj:
                    return assistant_msg, [{
                        "id": "fallback_return_answer",
                        "name": "return_answer",
                        "args": obj["args"]
                    }]
            except Exception as e:
                raise ValueError(f"Failed to parse fallback content: {str(e)}")
        raise ValueError("LLM did not return any tool_calls or valid return_answer.")

    # Define tool execution
    def exec_tool(tool_id, tool_name, tool_args):
        start = time.time()
        result = TOOLS[tool_name](**tool_args)
        end = time.time()
        #### log
        log_entry = {
            "timestamp": datetime.now().strftime("%Y%m%d_%H%M%S"),
            "tool_name": tool_name,
            "tool_args": tool_args,
            "tool_call_id": tool_id,
            "start_time": start,
            "end_time": end,
            "duration": end - start,
            "result": result,
        }
        log_path = os.path.join(root_log_dir, "tool_calls.jsonl")
        with open(log_path, "a") as log_file:
            log_file.write(json.dumps(log_entry) + "\n")
        ####
        return result

    # Main agent loop
    def run_agent_loop(messages, db_clients):
        step = 1
        repeat_tracker = RepeatedCallTracker(max_repeats=5)
        failure_tracker = QueryDbFailureTracker(max_failures=5)
        while True:
            print('=' * 30)
            print(f"\n{'=' * 10} Step {step} {'=' * 10}")
            # Add response to messages
            assistant_msg, tool_calls = call_llm(messages)
            messages.append({
                "role": "assistant",
                "tool_calls": assistant_msg.tool_calls,
            })
            # Handle tool calls
            for tc in tool_calls:
                tool_call_id = tc["id"]
                tool_name = tc["name"]
                tool_args = tc["args"]

                print(f"\n{'-' * 10}\n🔨 Tool Call ID: {tool_call_id}\ntool name: {tool_name}\ntool args: {tool_args}\n")

                if repeat_tracker.check_and_update(tool_name, tool_args):
                    error_log = f"Agent repeated the same call to `{tool_name}` >= {repeat_tracker.max_repeats} times. Terminating."
                    log_failed(query_dir, error_log)
                    print(f"tool_result: ❌ {error_log}\n{'-' * 10}\n")
                    return False

                if tool_name == "return_answer":
                    # success = TOOLS[tool_name](**tool_args)
                    is_valid, reason = exec_tool(tool_call_id, tool_name, tool_args)
                    if is_valid:
                        print(f"tool_result: ✅ Final answer returned.\n{'-' * 10}\n")
                    else:
                        print(f"tool_result: ❌ Final answer validation failed: {reason}\n{'-' * 10}\n")
                    return is_valid

                if tool_name not in TOOLS:
                    raise ValueError(f"Unknown tool name: {tool_name}")

                if tool_name == "query_db": # reformat tool args
                    tool_args = transform_tool_args(tool_args, db_clients)
                    if tool_args["success"] == False:
                        error_msg = tool_args["error"]
                        print(f"transform_tool_args failed: {error_msg}")
                        preview = f"[query_db ERROR] {error_msg}"
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call_id,
                            "name": tool_name,
                            "content": json.dumps({
                                "result": preview[:PREVIEW_MAX_LEN]
                            })
                        })

                        step += 1
                        continue

                try:
                    # result = TOOLS[tool_name](**tool_args)
                    result = exec_tool(tool_call_id, tool_name, tool_args)
                except Exception as e:
                    result = {"success": False, "error": str(e)}

                file_id = None

                if tool_name == "query_db":
                    if result["success"] == False:
                        error_msg = result.get("error", "Unknown query_db error")
                        print(f"tool_result: ❌ {result}")
                        if failure_tracker.record(success=False):
                            failure_log = f"Agent hit > {failure_tracker.max_failures} consecutive query_db failures. Terminating."
                            log_failed(query_dir, failure_log)
                            print(f"{failure_log}\n{'-' * 10}\n")
                            return False  
                        message = f"[query_db ERROR] {error_msg}"
                    else: # the tool succeeded
                        out = result["data"]
                        if len(out) > PREVIEW_MAX_LEN:
                            filename = f"query_result_{step}.json"
                            file_id = upload_to_client(client, out, filename, uploaded_files_dir)
                            message = f"The result of the query is in the file {file_id}."
                        else:
                            message = out

                elif tool_name == "execute_python":
                    if isinstance(result, dict) and not result.get("success", False):
                        error_msg = result.get("error", "Unknown Python error.")
                        print(f"❌ execute_python failed: {error_msg}")
                        message = f"[ERROR] execute_python failed: {error_msg}"
                    else:
                        out, ext = format_stdout(result["data"])
                        if len(out) > 10000:
                            filename = f"exec_result_{step}.{ext}"
                            file_id = upload_to_client(client, out, filename, uploaded_files_dir)
                            message = f"The result of the query is in the file {file_id}."
                        else:
                            message = out

                else:
                    if isinstance(result, dict) and not result.get("success", False):
                        error_msg = result.get("error", "Unknown tool error.")
                        print(f"❌ {tool_name} failed: {error_msg}")
                        message = f"[ERROR] {tool_name} failed: {error_msg}"
                    else:
                        output_data = result.get("data", result)  # fallback for legacy
                        out, ext = format_stdout(output_data)
                        if len(out) > 10000:
                            filename = f"result_{step}.{ext}"
                            file_id = upload_to_client(client, out, filename, uploaded_files_dir)
                            message = f"The result of the query is in the file {file_id}."
                        else:
                            message = out

                content = {"result": message}
                if file_id:
                    content["file_id"] = file_id

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call_id,
                    "name": tool_name,
                    "content": json.dumps(content)
                })

                if not message.strip():
                    print("📄 Preview sent to LLM: \n[empty string]\n")
                else:
                    print(f"📄 Preview sent to LLM:\n{message}\n")



                step += 1


    try:
        return run_agent_loop(messages, db_clients)
    except Exception as e:
        print(f"❌ Agent failed with error: {str(e)}")
        fail_reason = f"Agent crashed: {type(e).__name__}: {str(e)}"
        log_failed(query_dir, fail_reason)
        return False
    finally:
        print(f"\n🧹 Cleaning up temporary files from client...")
        file_ids = [f.id for f in list(client.files.list())]
        for fid in file_ids:
            try:
                client.files.delete(fid)
            except Exception as e:
                print(f"⚠️ Failed to delete temp file {fid}: {e}")

        print(f"\n🛑 Agent run completed")
