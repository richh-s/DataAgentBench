import sqlite3
import duckdb
import pandas as pd
import os

GT_TABLE = "/home/ruiying/DataAgentBench/query_music_brainz_20k/musicbrainz-20-A01.csv"
DUCKDB_DB = "/home/ruiying/DataAgentBench/query_music_brainz_20k/query_dataset/sales.duckdb"
QUERY_FOLDER_ROOT = "/home/ruiying/DataAgentBench/query_music_brainz_20k"

df = pd.read_csv(GT_TABLE)

# Connect to DuckDB (sales)
duck = duckdb.connect(DUCKDB_DB)

# Sales table
sales_df = duck.execute("SELECT * FROM sales").fetchdf()


def write_query(query_folder, query, answer):
    os.makedirs(query_folder, exist_ok=True)
    with open(os.path.join(query_folder, "query.json"), "w") as f:
        f.write(f'"{query}"')
    with open(os.path.join(query_folder, "ground_truth.csv"), "w") as f:
        f.write(answer)

def create_query1():
    query_folder = os.path.join(QUERY_FOLDER_ROOT, "query1")
    query = "How much revenue in USD did Apple Music make from Beyoncé's song 'Get Me Bodied' in Canada?"
    halo_cid = 2750
    store = "Apple Music"
    country = "Canada"
    gt_q1 = (
        sales_df
        .merge(df[["TID", "CID"]], left_on="track_id", right_on="TID")
        .query("CID == @halo_cid and country == @country and store == @store")["revenue_usd"]
        .sum()
    )
    # print related sales entries
    related_sales = sales_df.merge(df[["TID", "CID"]], left_on="track_id", right_on="TID").query("CID == @halo_cid")
    print(related_sales)
    return query_folder, query, str(round(float(gt_q1), 2))

def create_query2():
    query_folder = os.path.join(QUERY_FOLDER_ROOT, "query2")
    query = "Which store earned the most revenue in USD from Brucqe Maginnis' song 'Street Hype' across all countries?"
    halo_cid = 2136

    sales = (
        sales_df
        .merge(df[["TID", "CID"]], left_on="track_id", right_on="TID")
        .query("CID == @halo_cid")
    )
    #print the related sales entries
    print(sales)
    top_store = sales.groupby("store")["revenue_usd"].sum().idxmax()
    answer = f"{top_store}"
    return query_folder, query, answer

def create_query3():
    query_folder = os.path.join(QUERY_FOLDER_ROOT, "query3")
    query = "Which song generated the highest total revenue in USD across all stores and countries?"
    # the songs are identical if and only if they have the same CID
    sales = (
        sales_df
        .merge(df[["TID", "CID", "title"]], left_on="track_id", right_on="TID")
    )
    # group the songs by their CID and sum up the revenue
    # top song = the group with the highest total revenue
    # return all titles of the songs in the top song group
    top_song_group = sales.groupby("CID")["revenue_usd"].sum().idxmax()
    top_songs = sales.query("CID == @top_song_group")["title"].unique().tolist()
    answer = "\n".join(top_songs)

    return query_folder, query, answer

query_folder, query, answer = create_query3()
write_query(query_folder, query, answer)