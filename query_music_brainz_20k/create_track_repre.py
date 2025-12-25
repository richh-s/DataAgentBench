import pandas as pd
import numpy as np
from pathlib import Path

SEED = 42
np.random.seed(SEED)

RAW_CSV = "/home/ruiying/DataAgentBench/query_music_brainz_20k/musicbrainz-20-A01.csv"


# Load raw dataset
df = pd.read_csv(RAW_CSV)

# Create a mapping from duplicate track records to one sale entry
# Records having the same CID are duplicate
# Select one random representative record for each CID
cid_to_records = {}
for _, row in df.iterrows():
    cid = row["CID"]
    if cid not in cid_to_records:
        cid_to_records[cid] = []
    cid_to_records[cid].append(row)

cid_to_representative = {}
for cid, records in cid_to_records.items():
    representative = records[np.random.randint(0, len(records))]
    cid_to_representative[cid] = representative

# Write cid_to_representative to a csv file for future reference (sorted by CID)
cid_rep_df = pd.DataFrame.from_dict(cid_to_representative, orient="index")
cid_rep_df = cid_rep_df.sort_index()
cid_rep_df.to_csv("/home/ruiying/DataAgentBench/query_music_brainz_20k/track_repre.csv", index_label="CID")


