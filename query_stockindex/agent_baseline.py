import json
import os
import sys
import yaml
from pathlib import Path
from dotenv import load_dotenv
from openai import AzureOpenAI
from datetime import datetime
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

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
    auto_ensure_databases
)

query_dir = Path(__file__).parent / "query1"
deployment_name = "o3"

load_dotenv()

with open(query_dir / "query.json") as f:
    query_content = json.load(f)

if isinstance(query_content, str):
    user_query = query_content
elif isinstance(query_content, dict) and "query" in query_content:
    user_query = query_content["query"]
else:
    raise ValueError("query.json wrong format")

with open("db_description.txt") as f:
    db_description = f.read()

project_dir = Path(__file__).parent
with open(project_dir / "db_config.yaml") as f:
    db_config = yaml.safe_load(f)
db_clients = db_config["db_clients"]

auto_ensure_databases(db_clients)
print(f"\n✅ DB connections ready: {db_clients.keys()}")

def list_dbs_tool(**tool_args):
    return list_dbs(tool_args["db_name"], db_clients)


def return_answer(answer: str):
    print(f"\n✅ Final Answer: {answer}")
    # 这里可以调用 validate_answer(answer) 或其他逻辑
    validate_answer(answer)
    sys.exit(0)

def validate_answer(answer: str):
    """
    Call query1/validate.py:validate() to validate answer and log the result.
    """
    import importlib.util
    gt_path = query_dir / "validate.py"
    spec = importlib.util.spec_from_file_location("validate", str(gt_path))
    validate_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validate_mod)

    is_valid, reason = validate_mod.validate(answer)

    if is_valid:
        print("✅ Validation passed!")
    else:
        print("❌ Validation failed!")

    write_validation_log(
        query_name=query_dir.name,
        llm_answer=answer,
        match_result=is_valid,
        reason=reason
    )


def write_validation_log(query_name: str, llm_answer: str, match_result: bool, reason: str):
    """
    Write validation log:
    - query name
    - LLM answer
    - ground truth (from ground_truth.csv)
    - result ✅ or ❌
    - reason if any
    """
    log_path = Path.cwd() / "validation_log.txt"

    gt_path = Path.cwd() / query_name / "ground_truth.csv"
    df_gt = pd.read_csv(gt_path, header=None)

    # build ground truth string cleanly
    gt_lines = [
        ",".join(map(str, row)) for row in df_gt.values.tolist()
    ]
    gt_str = "\n".join(gt_lines)

    timestamp = datetime.now().isoformat(timespec="seconds")
    result_str = "✅ MATCH" if match_result else f"❌ MISMATCH: {reason}"

    log_lines = [
        f"=== Validation Log ({timestamp}) ===",
        f"Query: {query_name}",
        "",
        "LLM Answer:",
        llm_answer.strip(),
        "",
        "Ground Truth:",
        gt_str,
        "",
        f"Result: {result_str}",
        "="*80,
        ""
    ]
    log_entry = "\n".join(log_lines)

    if log_path.exists():
        old_content = log_path.read_text(encoding="utf-8")
    else:
        old_content = ""

    with open(log_path, "w", encoding="utf-8") as f:
        f.write(log_entry + "\n" + old_content)

    print(f"\n📄 Validation log updated at: {log_path}")


client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY_o3"),
    api_version=os.getenv("AZURE_API_VERSION_o3", "2023-05-15"),
    azure_endpoint=os.getenv("AZURE_API_BASE_o3")
)

messages = build_messages(user_query, db_description)

TOOLS = {
    "query_db": query_db,
    "list_dbs": list_dbs_tool,
    "execute_python": lambda code: execute_python(code, _vars),
    "return_answer": lambda **kwargs: return_answer(**kwargs)
}


tools_spec = get_tools_spec()


def call_llm(messages):
    resp = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
        tools=tools_spec
    )
    assistant_msg = resp.choices[0].message
    print(f"\n💬 LLM response:\n{assistant_msg}\n")

    if assistant_msg.tool_calls:
        tool_call = assistant_msg.tool_calls[0]
        tool_call_id = tool_call.id
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments)
        if isinstance(tool_args, dict) and "args" in tool_args:
            tool_args = tool_args["args"]
        return assistant_msg, tool_call_id, tool_name, tool_args

    if assistant_msg.content:
        try:
            obj = json.loads(assistant_msg.content)
            if isinstance(obj, dict) and obj.get("tool") == "return_answer" and "args" in obj:
                return assistant_msg, None, "return_answer", obj["args"]
        except Exception as e:
            print(f"⚠️ Failed to parse fallback content: {e}")

    raise ValueError("❌ LLM did not return any tool_calls or valid return_answer.")



def run_agent_loop(messages, db_clients, _vars):
    step = 1
    while True:
        assistant_msg, tool_call_id, tool_name, tool_args = call_llm(messages)

        print(f"🤖 Agent chose tool: {tool_name}")
        print(f"🔷 Args: {tool_args}")

        if tool_name == "return_answer":
            #print(f"\n✅ Final Answer: {tool_args['answer']}")
            #break
            TOOLS[tool_name](**tool_args)
            break

        if tool_name not in TOOLS:
            raise ValueError(f"❌ Unknown tool: {tool_name}")
        
        if tool_name == "query_db":
            tool_args = transform_tool_args(tool_args, db_clients)

        result = TOOLS[tool_name](**tool_args)

        var_name = generate_var_name(tool_name, tool_args, step)
        _vars[var_name] = result

        print(f"📄 Tool result stored in `{var_name}`")

        preview = format_preview(result)

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

if __name__ == "__main__":
    _vars = VariableStore()
    run_agent_loop(messages, db_clients, _vars)
