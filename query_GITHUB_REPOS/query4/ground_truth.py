import pandas as pd
import os

# Base path where ground truth dataset CSVs are stored
base_path = "../ground_truth_dataset"

# Load datasets
df_languages = pd.read_csv(os.path.join(base_path, "LANGUAGES.csv"))
df_commits = pd.read_csv(os.path.join(base_path, "SAMPLE_COMMITS.csv"))

print("Step 0: Raw counts")
print("  LANGUAGES:", len(df_languages))
print("  SAMPLE_COMMITS:", len(df_commits))

# Step 1: Expand language JSON-like column (assuming it's stored as list of dicts)
# Here we assume "language" is a JSON string
import json

expanded_rows = []
for _, row in df_languages.iterrows():
    try:
        langs = json.loads(row["language"])
        for lang in langs:
            expanded_rows.append({
                "repo_name": row["repo_name"],
                "language": lang.get("name"),
                "bytes": lang.get("bytes", 0)
            })
    except Exception as e:
        pass

df_lang_expanded = pd.DataFrame(expanded_rows)
print("Step 1: Expanded languages:", len(df_lang_expanded))

# Step 2: Get the primary language per repo (largest bytes)
df_lang_expanded["rank"] = df_lang_expanded.groupby("repo_name")["bytes"].rank(method="first", ascending=False)
df_primary_lang = df_lang_expanded[df_lang_expanded["rank"] == 1]
print("Step 2: Primary languages:", len(df_primary_lang))

# Step 3: Filter repos with JavaScript as primary language
df_js_repo = df_primary_lang[df_primary_lang["language"] != "Python"]
print("Step 3: JavaScript repos:", len(df_js_repo))

# Step 4: Join with commits and count per repo
df_commits_js = df_commits[df_commits["repo_name"].isin(df_js_repo["repo_name"])]
df_commit_counts = df_commits_js.groupby("repo_name")["commit"].count().reset_index(name="num_commits")

# Step 5: Sort and take top 2
df_top2 = df_commit_counts.sort_values(by="num_commits", ascending=False).head(5)
print("Step 4: Top 2 repos with commit counts")
print(df_top2)

# Step 6: Save result
output_path = "ground_truth.csv"
df_top2.to_csv(output_path, index=False)
print(f"✅ Saved result to {output_path}")
