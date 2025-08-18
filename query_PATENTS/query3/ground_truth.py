import pandas as pd
import json

# -------------------------------
# 1. Load input datasets
# -------------------------------
df_pub = pd.read_csv("../ground_truth_dataset/PUBLICATIONS.csv")
df_cpc_def = pd.read_csv("../ground_truth_dataset/CPC_DEFINITION.csv")

# -------------------------------
# 2. Expand citations, assignees, and CPCs
# -------------------------------
def safe_json_load(x):
    try:
        return json.loads(x) if pd.notna(x) else []
    except:
        return []

# Expand citation list
df_pub["citation_list"] = df_pub["citation"].apply(safe_json_load)
df_pub["assignee_list"] = df_pub["assignee_harmonized"].apply(safe_json_load)
df_pub["cpc_list"] = df_pub["cpc"].apply(safe_json_load)

# Explode to get citing publications, assignees, and CPCs
df_exploded = df_pub.explode("citation_list").explode("assignee_list").explode("cpc_list")

# Keep only CPCs where "first" = True
df_exploded = df_exploded[df_exploded["cpc_list"].apply(lambda c: isinstance(c, dict) and c.get("first") is True)]

# Extract fields
df_exploded["citing_publication_number"] = df_exploded["publication_number"]
df_exploded["cited_publication_number"] = df_exploded["citation_list"].apply(lambda x: x.get("publication_number") if isinstance(x, dict) else None)
df_exploded["citing_assignee"] = df_exploded["assignee_list"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)
df_exploded["citing_cpc_subclass"] = df_exploded["cpc_list"].apply(lambda x: str(x.get("code"))[:4] if isinstance(x, dict) else None)

# -------------------------------
# 3. Build refs (cited publication -> assignee)
# -------------------------------
df_refs = df_pub.copy()
df_refs["assignee_list"] = df_refs["assignee_harmonized"].apply(safe_json_load)
df_refs = df_refs.explode("assignee_list")
df_refs["cited_publication_number"] = df_refs["publication_number"]
df_refs["cited_assignee"] = df_refs["assignee_list"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)

# -------------------------------
# 4. Join citing side with cited side
# -------------------------------
df_join = df_exploded.merge(
    df_refs[["cited_publication_number", "cited_assignee"]],
    on="cited_publication_number",
    how="inner"
)

# -------------------------------
# 5. Filter for cited_assignee = 'UNIV CALIFORNIA' and exclude self-citations
# -------------------------------
df_join = df_join[
    (df_join["cited_assignee"] == "UNIV CALIFORNIA") &
    (df_join["citing_assignee"] != "UNIV CALIFORNIA")
]

# -------------------------------
# 6. Join with CPC_DEFINITION to get full CPC title
# -------------------------------
df_join = df_join.merge(
    df_cpc_def[["symbol", "titleFull"]],
    left_on="citing_cpc_subclass",
    right_on="symbol",
    how="inner"
)

# -------------------------------
# 7. Drop duplicates (no count)
# -------------------------------
result = (
    df_join[["citing_assignee", "titleFull"]]
    .drop_duplicates()
    .sort_values(["citing_assignee", "titleFull"])
)

# -------------------------------
# 8. Save ground truth
# -------------------------------
result.to_csv("ground_truth.csv", index=False, encoding="utf-8")

print("✅ Ground truth generated and saved to ground_truth.csv")
print(result.head(10))
