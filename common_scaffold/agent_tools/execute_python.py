import pandas as pd
from typing import Any


def execute_python(code: str, var_store: "VariableStore" = None) -> dict:
    """
    Execute LLM-provided Python code in the context of var_store.
    The code MUST assign its result to a variable named `result`.

    Args:
        code (str): Python code from LLM.
        var_store (VariableStore): The current variable context.

    Returns:
        dict: {
            "success": True, "data": result
        } or {
            "success": False, "error": error_message
        }
    """
    if var_store != None:
        context = var_store.copy()
        context.update({"pd": pd})
    else:
        context = {"pd": pd}

    try:
        exec(code, context)
    except IndexError as e:
        error_msg = f"IndexError during code execution: {str(e)} (e.g., `.iloc[0]` on empty DataFrame?)"
        return {"success": False, "error": error_msg}
    except Exception as e:
        error_msg = f"Error executing Python code: {type(e).__name__}: {str(e)}"
        return {"success": False, "error": error_msg}

    if var_store != None:
        var_store.update(context)

    if "result" in context:
        if var_store != None:
            var_store["result"] = context["result"]
        return {"success": True, "data": context["result"]}
    else:
        return {"success": False, "error": "`result` was not defined in executed code."}






###

#def execute_python(code: str, var_store: "VariableStore") -> pd.DataFrame | Any:
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
    except IndexError as e:
        print(f"⚠️ IndexError during code execution: {e}")
        print(f"💡 Hint: Maybe tried to access `.iloc[0]` on an empty DataFrame. Returning None.")
        context["result"] = None
    except Exception as e:
        print(f"⚠️ Error executing code: {e}")
        context["result"] = None


    var_store.update(context)


    if "result" in context:
        var_store["result"] = context["result"]
        return context["result"]

    return var_store
###