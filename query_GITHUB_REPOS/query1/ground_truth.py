import pandas as pd
import os

base_path = "../ground_truth_dataset"

# Load CSV files
df_contents = pd.read_csv(os.path.join(base_path, "SAMPLE_CONTENTS.csv"))
df_files = pd.read_csv(os.path.join(base_path, "SAMPLE_FILES.csv"))
df_languages = pd.read_csv(os.path.join(base_path, "LANGUAGES.csv"))

print("Step 0: raw counts")
print("  SAMPLE_CONTENTS:", len(df_contents))
print("  SAMPLE_FILES:", len(df_files))
print("  LANGUAGES:", len(df_languages))

# Step 1: Filter README.md files
df_readme = df_files[df_files["path"].str.lower().str.contains("readme.md")]
print("Step 1: README.md files:", len(df_readme))

# Step 2: Find repos that use Python
repos_with_python = df_languages[df_languages["language"].str.lower().str.contains("python", na=False)]["repo_name"].unique()
print("Step 2: repos_with_python:", len(repos_with_python))

# Step 3: Keep only repos WITHOUT Python
df_readme = df_readme[~df_readme["repo_name"].isin(repos_with_python)]
print("Step 3: README.md files without Python repos:", len(df_readme))

# Step 4: Merge with contents
df = df_readme.merge(df_contents, on="id", how="inner")
print("Step 4: merged README + contents:", len(df))

# Step 5: Compute proportion with copyright (case-insensitive)
total_readmes = len(df)
copyright_readmes = df["content"].str.contains("copyright", case=False, na=False).sum()
proportion = copyright_readmes / total_readmes if total_readmes > 0 else 0
print("Step 5: copyright_readmes:", copyright_readmes)
print("Step 5: total_readmes:", total_readmes)
print("Step 5: proportion:", proportion)

# Step 6: Save ground truth
result = pd.DataFrame([{
    "total_readmes": total_readmes,
    "copyright_readmes": copyright_readmes,
    "proportion": proportion
}])

output_path = "ground_truth.csv"
result.to_csv(output_path, index=False)
print(f"✅ Saved result to {output_path}")
