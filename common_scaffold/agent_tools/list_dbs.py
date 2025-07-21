from common_scaffold.db_utils.loader import list_entities
import pandas as pd

def list_dbs(db_name: str, db_clients: dict) -> dict:
    """
    Agent-friendly wrapper for list_entities.
    """
    client = db_clients.get(db_name)
    if not client:
        raise ValueError(f"Unknown db_name: {db_name}")
    
    db_type = client["db_type"]

    if db_type == "mysql":
        tables_df = list_entities(db_type, db_name=client["db_name"])
    elif db_type == "postgres":
        tables_df = list_entities(db_type, db_name=client["db_name"])
    elif db_type in {"sqlite", "duckdb"}:
        if not client.get("db_path"):
            raise ValueError(f"{db_type} db_path missing for {db_name}")
        tables_df = list_entities(db_type, db_path=client["db_path"])
    elif db_type == "mongo":
        tables_df = list_entities(db_type, db_name=client["db_name"])
    else:
        raise ValueError(f"Unsupported db_type: {db_type}")
    
    # standardize output
    if isinstance(tables_df, pd.DataFrame):
        tables = tables_df.iloc[:, 0].tolist()
    else:
        tables = tables_df

    return {
        "db_name": db_name,
        "db_type": db_type,
        "tables": tables
    }
