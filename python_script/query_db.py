import sqlparse
from sqlparse.sql import IdentifierList, Identifier, Function, Where
from sqlparse.tokens import Keyword, DML
import matplotlib.pyplot as plt
from pathlib import Path
import os
import json

# Define operation categories
SQL_OPERATIONS = [
    "projection", 
    "aggregation", 
    "filtering", 
    "joining",
    "grouping", 
    "sorting", 
    "limiting", 
    "subquery",
    "set_operation", 
    "window_function", 
    "insert_update_delete", 
    "ddl"
]

READ_OPERATIONS = [
    "projection", 
    "aggregation", 
    "filtering", 
    "joining",
    "grouping", 
    "sorting", 
    "limiting", 
    "subquery",
    "set_operation", 
    "window_function",
]

def analyze_mongo_ops(mongo_query):
    ops = set()
    if 'filter' in mongo_query and mongo_query['filter']:
        ops.add("filtering")
    if 'projection' in mongo_query and mongo_query['projection']:
        ops.add("projection")
    if 'limit' in mongo_query:
        ops.add("limiting")
    return ops

def analyze_sql_ops(sql):
    parsed = sqlparse.parse(sql)[0]
    tokens = parsed.tokens
    ops = set()
    select_seen = False
    
    for token in tokens:
        tval = str(token).upper()
        if token.ttype is DML:
            if tval in ["INSERT", "UPDATE", "DELETE"]:
                ops.add("insert_update_delete")
            elif tval == "SELECT":
                select_seen = True
                ops.add("projection")
        if isinstance(token, Function):
            func_name = token.get_name()
            if func_name and func_name.upper() in ["SUM","COUNT","AVG","MIN","MAX"]:
                ops.add("aggregation")
            if "OVER" in tval:
                ops.add("window_function")
        if isinstance(token, Where):
            ops.add("filtering")
        if token.ttype is Keyword and "JOIN" in tval:
            # print("Found JOIN in query:", sql)
            ops.add("joining")
        if token.ttype is Keyword and "GROUP BY" in tval:
            ops.add("grouping")
        if token.ttype is Keyword and "ORDER BY" in tval:
            ops.add("sorting")
        if token.ttype is Keyword and "LIMIT" in tval:
            ops.add("limiting")
        if token.ttype is Keyword and tval in ["UNION", "INTERSECT", "EXCEPT"]:
            ops.add("set_operation")
        if token.ttype is Keyword.DDL:
            ops.add("ddl")
        if token.is_group and "SELECT" in tval:
            ops.add("subquery")
        if select_seen and isinstance(token, IdentifierList):
            for identifier in token.get_identifiers():
                if "(" in str(identifier) and ")" in str(identifier):
                    ops.add("aggregation")
    
    return ops

def analyze_query_ops(query):
    if isinstance(query, str):
        return analyze_sql_ops(query)
    elif isinstance(query, dict):
        return analyze_mongo_ops(query)
    else:
        raise ValueError("Unsupported query format")

def analyze_query_set(query_list):
    op_counts = {op: 0 for op in SQL_OPERATIONS}
    total_queries = len(query_list)
    
    for query in query_list:
        ops = analyze_query_ops(query)
        for op in ops:
            op_counts[op] += 1
    
    op_proportions = {op: count / total_queries for op, count in op_counts.items()}
    return op_proportions



def load_queries(result_dir: Path):
    queries = []
    tool_call_path = result_dir / "tool_calls.jsonl"
    if not tool_call_path.exists():
        return queries
    with open(tool_call_path, 'r') as f:
        for line in f:
            tool_call = json.loads(line)
            if tool_call['tool_name'] == 'query_db' and tool_call['result']['success']:
                query = tool_call['args']['query']
                db_type = tool_call['val_args']['db_type']
                if db_type == "mongo":
                    query_dict = json.loads(query)
                    assert isinstance(query_dict, dict)
                    queries.append(query_dict)
                else:
                    assert isinstance(query, str)
                    queries.append(query)
    return queries

if __name__ == "__main__":
    # MODEL = "gpt5.1"
    MODEL = "gemini-3-pro"
    QUERY_ROOT = Path("/home/ruiying/DataAgentBench")
    RESULT_ROOT = Path(f"/home/ruiying/DataAgentBench/results-{MODEL}")
    FIG_NAME = f"qeury_db_{MODEL}_all"

    mongo_queries = []
    sql_queries = []
    for task in [
        "bookreview",
        "crmarenapro",
        "DEPS_DEV_V1",
        "GITHUB_REPOS",
        "googlelocal",
        "PANCANCER_ATLAS",
        "PATENTS",
        "stockindex",
        "stockmarket",
        "yelp"
    ]:
        print(task)
        result_dir = RESULT_ROOT / f"query_{task}"
        for folder_name in sorted(os.listdir(result_dir)):
            if folder_name.startswith("query"):
                try:
                    query_id = int(folder_name.replace("query", ""))
                    # print(query_id)
                except Exception as e:
                    continue
                runs = list(range(50))
                for rid in runs:
                    if MODEL == "gpt5.1":
                        run_dir = result_dir / f"query{query_id}" / f"run_{rid}"
                    elif MODEL == "gemini-3-pro":
                        run_dir = result_dir / f"query{query_id}" / "data_agent" / f"run_{rid}"
                    queries = load_queries(run_dir)
                    for query in queries:
                        if isinstance(query, dict):
                            mongo_queries.append(query)
                        elif isinstance(query, str):
                            sql_queries.append(query)

    print(f"Loaded {len(mongo_queries)} mongo queries and {len(sql_queries)} sql queries.")
    mongo_op_proportions = analyze_query_set(mongo_queries)
    sql_op_proportions = analyze_query_set(sql_queries)

    # # a 1x2 figures, one for sql and one for mongo
    # fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    # # Mongo plot
    # ops = list(mongo_op_proportions.keys())
    # proportions = [mongo_op_proportions[op] for op in ops]
    # axs[0].barh(ops, proportions, color='lightgreen')
    # axs[0].set_xlabel("Proportion of Queries")
    # axs[0].set_title("MongoDB Operation Proportions")
    # axs[0].set_xlim(0,1)
    # # SQL plot
    # ops = list(sql_op_proportions.keys())
    # proportions = [sql_op_proportions[op] for op in ops]
    # axs[1].barh(ops, proportions, color='skyblue')
    # axs[1].set_xlabel("Proportion of Queries")
    # axs[1].set_title("SQL Operation Proportions")
    # axs[1].set_xlim(0,1)
    # plt.tight_layout()
    # plt.savefig(f"figures/{FIG_NAME}.png")
    

    # one figure, two bars side by side for each operation
    fig, ax = plt.subplots(figsize=(6, 3))
    ops = READ_OPERATIONS
    mongo_proportions = [mongo_op_proportions[op] for op in ops]
    sql_proportions = [sql_op_proportions[op] for op in ops]
    x = range(len(ops))
    ax.barh([i - 0.2 for i in x], mongo_proportions, height=0.4, label='Mongo')
    ax.barh([i + 0.2 for i in x], sql_proportions, height=0.4, label='SQL')
    ax.set_yticks(x)
    ax.set_yticklabels(ops)
    ax.set_xlabel("Proportion of Queries")
    ax.set_title("Database Operation Proportions")
    ax.set_xlim(0,1)
    
    ax.legend()
    plt.savefig(f"figures/{FIG_NAME}.png", bbox_inches='tight')
