import json
import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import AzureOpenAI

sys.path.append(str(Path(__file__).resolve().parents[1]))

from common_scaffold.db_utils.loader import ensure_db, query_db, list_entities
#from execute_python import execute_python

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

db_name_mysql = "googlelocal_db"
sql_file_mysql = "query_dataset/business_description.sql"

print("\n=== 🔗 MySQL: Ensuring database is initialized ===")
ensure_db(
    db_type="mysql",
    db_name=db_name_mysql,
    sql_file=sql_file_mysql
)

db_clients = {
    "mysql": {
        "db_name": db_name_mysql
    },
    "sqlite": {
        "db_path": "query_dataset/review_query.db"
    }
}

print(f"\n✅ DB connections ready: {db_clients.keys()}")

client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY_o3"),
    api_version=os.getenv("AZURE_API_VERSION_o3", "2023-05-15"),
    azure_endpoint=os.getenv("AZURE_API_BASE_o3")
)

messages = [
    {
        "role": "system",
        "content": """
You are a data analysis agent.

You have access to the following tools, which I (the system) will execute for you:
- query_db: execute a SQL or Mongo query on the specified database and return a dataframe.
- list_dbs: list all available databases and their tables/collections.
- execute_python: execute a snippet of Python code.
- return_answer: return the final answer to the user and stop.

Whenever you want to use a tool, you MUST output ONLY a valid JSON object, on a single line, with exactly these two keys: `tool` and `args`.

You MUST always include all required arguments for the tool you call.
For example, `list_dbs` requires at least the `db_type` (e.g., mysql, sqlite) and if needed also `db_name` or `db_path`.

You MUST NOT output any explanation, reasoning, comments, or natural language outside of the JSON.
You MUST NOT assume the system will fill in missing arguments — if arguments are incomplete, the task will fail.

For example:
{"tool": "query_db", "args": {"db_type": "mysql", "db_name": "googlelocal_db", "sql": "SELECT * FROM businesses LIMIT 5;"}}

When you have determined the final answer and wish to end the task, you MUST output:
{"tool": "return_answer", "args": {"answer": "…your answer here…"}}

If you cannot proceed, also use `return_answer` with an appropriate message.

⚠️ Never wrap the JSON in code fences (e.g., ```json … ```), never output multiple lines, and never include any text before or after the JSON.
Only output a single valid JSON object that I can parse and execute.
"""
    },
    {
        "role": "user",
        "content": f"Query: {user_query}\n\nDB Description:\n{db_description}"
    }
]

TOOLS = {
    "query_db": query_db,
    "list_dbs": list_entities,
    #"execute_python": execute_python
}


def call_llm(messages):
    resp = client.chat.completions.create(
        model=deployment_name,
        messages=messages,
    )
    content = resp.choices[0].message.content.strip()
    print(f"\n💬 LLM response:\n{content}\n")
    try:
        tool_call = json.loads(content)
        if "tool" not in tool_call or "args" not in tool_call:
            raise ValueError("Missing 'tool' or 'args' in LLM output.")
        return tool_call
    except Exception as e:
        raise ValueError(f"❌ Failed to parse LLM response:\n{content}") from e


step = 1
while True:
    print(f"=== 🔄 Step {step} ===")
    tool_call = call_llm(messages)
    tool_name = tool_call["tool"]
    tool_args = tool_call["args"]

    print(f"🤖 Agent chose tool: {tool_name}")
    print(f"🔷 Args: {tool_args}")

    if tool_name == "return_answer":
        print(f"\n✅ Final Answer: {tool_args['answer']}")
        break

    if tool_name not in TOOLS:
        raise ValueError(f"❌ Unknown tool: {tool_name}")

    if not tool_args:
        raise ValueError(f"❌ LLM returned incomplete arguments for tool {tool_name}: {tool_call}")


    result = TOOLS[tool_name](**tool_args)

    print(f"📄 Tool result:\n{result}\n")


    messages.append({
        "role": "tool",
        "content": f"Result of {tool_name}: {str(result)[:500]}…"
    })

    step += 1