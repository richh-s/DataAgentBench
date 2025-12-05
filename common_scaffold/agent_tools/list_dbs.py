from common_scaffold.db_utils.loader import list_entities
import pandas as pd

def list_dbs(db_name: str, db_clients: dict) -> dict:
    """
    Agent-friendly wrapper for list_entities.
    Args:
        db_name (str): The name of the database to list tables from.
        db_clients (dict): A dictionary of database client configurations.
    Returns:
        {"success": bool, "data": dict | "error": str}
    """
    if db_name not in db_clients:
        return {"success": False, "error": f"Unknown db_name: {db_name}"}
    
    client = db_clients[db_name]
    db_type = client["db_type"]

    try:
        if db_type in {"sqlite", "duckdb"}:
            tables_df = list_entities(db_type, db_path=client["db_path"])
        else:
            tables_df = list_entities(db_type, db_name=client["db_name"])
    except Exception as e:
        return {"success": False, "error": f"{type(e).__name__}: {str(e)}"}
    
    # standardize output
    if isinstance(tables_df, pd.DataFrame):
        table_names = tables_df.iloc[:, 0].tolist()
    elif isinstance(tables_df, list):
        table_names = tables_df
    else:
        return {"success": False, "error": f"Unrecognized table format: {type(tables_df)}"}

    return {
        "success": True,
        "data": {
            "db_name": db_name,
            "db_type": db_type,
            "tables": table_names  # ✅ now it's a plain list
        }
    }