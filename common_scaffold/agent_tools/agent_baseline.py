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
    VariableStore,
    format_preview,
    auto_ensure_databases,
    validate_and_log,
    log_failed
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
        "execute_python": lambda code: execute_python(code, _vars),
        "return_answer": lambda **kwargs: return_answer(**kwargs)
    }

    def call_llm(messages):
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
            tool_call = assistant_msg.tool_calls[0]
            tool_call_id = tool_call.id
            tool_name = tool_call.function.name
            tool_args = json.loads(tool_call.function.arguments)
            if isinstance(tool_args, dict) and "args" in tool_args:
                tool_args = tool_args["args"]
            return assistant_msg, tool_call_id, tool_name, tool_args

        # Fallback: try parsing content as JSON
        if assistant_msg.content:
            try:
                obj = json.loads(assistant_msg.content)
                if isinstance(obj, dict) and obj.get("tool") == "return_answer" and "args" in obj:
                    return assistant_msg, None, "return_answer", obj["args"]
            except Exception as e:
                print(f"⚠️ Failed to parse fallback content: {e}")

        raise ValueError("❌ LLM did not return any tool_calls or valid return_answer.")

    def run_agent_loop(messages, db_clients, _vars):
        """
        Main agent loop.
        """
        step = 1
        while True:
            assistant_msg, tool_call_id, tool_name, tool_args = call_llm(messages)

            print(f"🤖 Agent chose tool: {tool_name}")
            print(f"🔷 Args: {tool_args}")

            if tool_name == "return_answer":
                success = TOOLS[tool_name](**tool_args)
                return success

            if tool_name not in TOOLS:
                raise ValueError(f"❌ Unknown tool: {tool_name}")

            if tool_name == "query_db":
                tool_args = transform_tool_args(tool_args, db_clients)

            result = TOOLS[tool_name](**tool_args)
            print(f"[DEBUG] Raw result from tool {tool_name}:\n{result}")

            var_name = generate_var_name(tool_name, tool_args, step)

            if tool_name == "query_db":
                if isinstance(result, dict) and not result.get("success", False):
                    error_msg = result.get("error", "Unknown query_db error.")
                    print(f"❌ query_db failed: {error_msg}")
                    _vars[var_name] = error_msg  
                    preview = f"[ERROR] query_db failed: {error_msg}"
                else:
                    df = result["data"]
                    _vars[var_name] = df
                    preview = format_preview(df)

            elif tool_name == "execute_python":
                if isinstance(result, dict) and not result.get("success", False):
                    error_msg = result.get("error", "Unknown Python error.")
                    print(f"❌ execute_python failed: {error_msg}")
                    _vars[var_name] = error_msg
                    preview = f"[ERROR] execute_python failed: {error_msg}"
                else:
                    _vars[var_name] = result["data"]
                    preview = format_preview(result["data"])

            else:
                if isinstance(result, dict) and not result.get("success", False):
                    error_msg = result.get("error", "Unknown tool error.")
                    print(f"❌ {tool_name} failed: {error_msg}")
                    _vars[var_name] = error_msg
                    preview = f"[ERROR] {tool_name} failed: {error_msg}"
                else:
                    output_data = result.get("data", result)  # fallback for legacy
                    _vars[var_name] = output_data
                    print(f"📄 Tool result stored in `{var_name}`")
                    preview = format_preview(output_data)
                        

            messages.append(assistant_msg)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": tool_name,
                "content": json.dumps({
                    "available_variables": list(_vars.keys()),
                    "result_variable": var_name,
                    "result_preview": preview[:10000]
                })
            })

            print(f"📄 Preview sent to LLM:\n{preview[:10000]}...\n")

            step += 1

    _vars = VariableStore()

    try:
        return run_agent_loop(messages, db_clients, _vars)
    except Exception as e:
        print(f"❌ Agent failed with error: {e}")
        fail_reason = f"❌ Agent crashed: {type(e).__name__}: {e}"
        log_failed(query_dir, fail_reason)
        return False
