import pandas as pd
import numpy as np
import re

def compute_ground_truth(expr_path, clinical_path, output_path):
    """
    Compute the ground truth for Query 1:
    Average IGF2 expression per histology type among LGG patients.
    """

    # 1. Load input data
    expr = pd.read_csv(expr_path)
    clinical = pd.read_csv(clinical_path)

    # 2. Filter RNA-Seq expression data
    expr_filtered = expr[
        (expr["Study"] == "LGG") &
        (expr["Symbol"] == "IGF2") &
        (expr["normalized_count"].notna())
    ].copy()

    # Compute log10(normalized_count + 1)
    expr_filtered["log_expr"] = np.log10(expr_filtered["normalized_count"] + 1)

    # Aggregate per patient (average log expression if multiple rows exist)
    expr_grouped = expr_filtered.groupby(
        ["ParticipantBarcode", "Symbol"], as_index=False
    )["log_expr"].mean()

    # 3. Filter clinical information
    clinical_filtered = clinical[
        (clinical["acronym"] == "LGG") &
        (clinical["icd_o_3_histology"].notna())
    ].copy()

    # Exclude values enclosed in square brackets
    clinical_filtered = clinical_filtered[
        ~clinical_filtered["icd_o_3_histology"].astype(str).str.match(r'^\[.*\]$')
    ]

    # Select relevant columns
    clinical_filtered = clinical_filtered[["bcr_patient_barcode", "icd_o_3_histology"]]

    # 4. Merge expression data with clinical info
    merged = pd.merge(
        expr_grouped,
        clinical_filtered,
        left_on="ParticipantBarcode",
        right_on="bcr_patient_barcode",
        how="inner"
    )

    # 5. Group by histology type and compute average IGF2 expression
    result = (
        merged.groupby("icd_o_3_histology")["log_expr"]
        .mean()
        .reset_index()
        .rename(columns={
            "icd_o_3_histology": "Histology_Type",
            "log_expr": "Average_Log_Expression"
        })
    )

    # 6. Save result to CSV
    result.to_csv(output_path, index=False)

    return result


if __name__ == "__main__":
    # Paths to input data
    expr_path = "../ground_truth_dataset/RNASeq_Expression.csv"
    clinical_path = "../ground_truth_dataset/Clinical_Info_gt.csv"
    output_path = "ground_truth.csv"

    # Compute and save ground truth
    result = compute_ground_truth(expr_path, clinical_path, output_path)

    # Print results for quick check
    print("Ground truth saved to:", output_path)
    print(result.head())

