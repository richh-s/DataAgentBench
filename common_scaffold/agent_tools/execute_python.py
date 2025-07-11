import pandas as pd
from typing import Any

def execute_python(code: str, var_store: "VariableStore") -> pd.DataFrame | Any:
    """
    Execute LLM-provided Python code in the context of var_store.
    The code MUST assign its result to a variable named `result`.

    Args:
        code (str): Python code from LLM.
        var_store (VariableStore): The current variable context.

    Returns:
        pd.DataFrame | Any: The value of `result` if present, otherwise the updated var_store.
    """
    context = var_store.copy()
    context.update({"pd": pd})

    try:
        exec(code, context)  # globals == locals == context
    except Exception as e:
        raise RuntimeError(f"Error executing code: {e}")

    # 更新 VariableStore
    var_store.update(context)

    # 返回 result
    if "result" in context:
        var_store["result"] = context["result"]
        return context["result"]

    return var_store
