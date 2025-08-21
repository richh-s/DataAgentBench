import pandas as pd
import os

base_path = "../ground_truth_dataset"

# Load CSVs
df_files = pd.read_csv(os.path.join(base_path, "SAMPLE_FILES.csv"))
df_contents = pd.read_csv(os.path.join(base_path, "SAMPLE_CONTENTS.csv"))
df_langs = pd.read_csv(os.path.join(base_path, "LANGUAGES.csv"))

print("Step 0: raw counts")
print("  SAMPLE_FILES:", len(df_files))
print("  SAMPLE_CONTENTS:", len(df_contents))
print("  LANGUAGES:", len(df_langs))

# Step 1: select relevant columns from SAMPLE_FILES
df_selected = df_files[["id", "repo_name", "path"]]

# Step 2: deduplicate by id (take min repo_name, min path for each id)
df_deduped = df_selected.groupby("id", as_index=False).agg({
    "repo_name": "min",
    "path": "min"
})
print("Step 2: deduped files:", len(df_deduped))

# Step 3: merge with contents
df_merged = df_deduped.merge(df_contents, on="id", how="inner")
print("Step 3: merged:", len(df_merged))

# Step 4: filter non-binary and .swift files
df_filtered = df_merged[(df_merged["binary"] == False) & (df_merged["path"].str.endswith(".swift"))]
print("Step 4: filtered non-binary .swift files:", len(df_filtered))

# Step 5: join with LANGUAGES to ensure repo has Swift
df_with_lang = df_filtered.merge(df_langs, on="repo_name", how="inner")
df_with_lang = df_with_lang[df_with_lang["language"].str.lower().str.contains("swift")]
print("Step 5: after language filter (contains Swift):", len(df_with_lang))

# Step 6: sort by copies desc, take top 1
df_top = df_with_lang.sort_values("copies", ascending=False).head(1)
print("Step 6: top file:", df_top[["repo_name", "path", "copies", "language"]].to_dict(orient="records"))

# Step 7: save ground truth
if len(df_top) > 0:
    result = pd.DataFrame([{
        "repo_name": df_top.iloc[0]["repo_name"]
    }])
    output_path = "ground_truth.csv"
    result.to_csv(output_path, index=False)
    print(f"✅ Saved result to {output_path}")
else:
    print("❌ No matching Swift repo found")
