import json
import sys
from pathlib import Path

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


def run_baseline_agent(
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

    db_clients = db_config["db_clients"]
    auto_ensure_databases(db_clients)
    print(f"\n✅ DB connections ready: {db_clients.keys()}")

    with open(query_dir / "query.json") as f:
        query_content = json.load(f)

    if isinstance(query_content, str):
        user_query = query_content
    elif isinstance(query_content, dict) and "query" in query_content:
        user_query = query_content["query"]
    else:
        raise ValueError("Invalid format: query.json must contain either a string or a {'query': ...} dict")

    messages = build_messages(user_query, db_description)

    def list_dbs_tool(**tool_args):
        return list_dbs(tool_args["db_name"], db_clients)

    def return_answer(answer: str):
        """
        Handle final answer from LLM and validate it.
        """
        print(f"\n✅ Final Answer: {answer}")
        is_valid, reason = validate_and_log(query_dir, answer)

        if is_valid:
            print("✅ Validation passed!")
        else:
            print(f"❌ Validation failed: {reason}")
        return is_valid

    tools_spec = get_tools_spec()

    TOOLS = {
        "query_db": query_db,
        "list_dbs": list_dbs_tool,
        "execute_python": lambda code: execute_python(code),
        "return_answer": lambda **kwargs: return_answer(**kwargs)
    }

    def call_llm(messages)-> tuple:
        """
        Call the LLM to get the next step decision and tool arguments.
        """
        resp = client.chat.completions.create(
            model=deployment_name,
            messages=messages,
            tools=tools_spec
        )
        assistant_msg = resp.choices[0].message
        print(f"\n💬 LLM response:\n{assistant_msg}\n")

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


        # Fallback: try parsing content as JSON
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
                print(f"⚠️ Failed to parse fallback content: {e}")


        raise ValueError("❌ LLM did not return any tool_calls or valid return_answer.")

    def run_agent_loop(messages, db_clients):
        """
        Main agent loop.
        """
        step = 1
        repeat_tracker = RepeatedCallTracker(max_repeats=5)
        failure_tracker = QueryDbFailureTracker(max_failures=5)
        while True:
            assistant_msg, tool_calls = call_llm(messages)
            messages.append(assistant_msg)

            for tc in tool_calls:
                tool_call_id = tc["id"]
                tool_name = tc["name"]
                tool_args = tc["args"]

                print(f"🤖 Agent chose tool: {tool_name}")
                print(f"🔷 Args: {tool_args}")

                if repeat_tracker.check_and_update(tool_name, tool_args):
                    log_failed(query_dir, f"❌ Agent repeated the same call to `{tool_name}` >=5 times. Terminating.")
                    return False

                if tool_name == "return_answer":
                    success = TOOLS[tool_name](**tool_args)
                    return success

                if tool_name not in TOOLS:
                    raise ValueError(f"❌ Unknown tool: {tool_name}")

                if tool_name == "query_db":
                    tool_args = transform_tool_args(tool_args, db_clients)

                    if tool_args.get("success") is False:
                        error_msg = tool_args.get("error", "Unknown transform_tool_args error.")
                        print(f"❌ transform_tool_args failed: {error_msg}")
                        preview = f"[ERROR] transform_tool_args failed: {error_msg}"

                        #messages.append(assistant_msg)
                        #print(f"🛠 Sending tool response for tool_call_id={tool_call_id}, tool={tool_name}")

                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call_id,
                            "name": tool_name,
                            "content": json.dumps({
                                "result": preview[:10000]
                            })
                        })

                        if not preview.strip():
                            print("📄 Preview sent to LLM: \n[empty string]\n")
                        elif len(preview) > 10000:
                            print(f"📄 Preview sent to LLM:\n{preview[:10000]}\n... (truncated)\n")
                        else:
                            print(f"📄 Preview sent to LLM:\n{preview}\n")

                        step += 1
                        continue

                try:
                    result = TOOLS[tool_name](**tool_args)
                except Exception as e:
                    result = {"success": False, "error": str(e)}
                # print(f"[DEBUG] Raw result from tool {tool_name}:\n{result}")

                file_id = None

                if tool_name == "query_db":
                    if isinstance(result, dict) and not result.get("success", False):
                        error_msg = result.get("error", "Unknown query_db error.")
                        print(f"❌ query_db failed: {error_msg}")
                        if failure_tracker.record(success=False):
                            log_failed(query_dir, f"❌ Agent hit >5 consecutive query_db failures. Terminating.")
                            return False  
                        message = f"[ERROR] query_db failed: {error_msg}"
                    else:
                        out = result["data"]
                        if len(out) > 10000:
                            filename = f"query_result_{step}.json"
                            file_id = upload_to_client(client, out, filename)
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
                            file_id = upload_to_client(client, out, filename)
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
                            file_id = upload_to_client(client, out, filename)
                            message = f"The result of the query is in the file {file_id}."
                        else:
                            message = out

                #messages.append(assistant_msg)
                #print(f"🛠 Sending tool response for tool_call_id={tool_call_id}, tool={tool_name}")

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
        print(f"❌ Agent failed with error: {e}")
        fail_reason = f"❌ Agent crashed: {type(e).__name__}: {e}"
        log_failed(query_dir, fail_reason)
        return False
