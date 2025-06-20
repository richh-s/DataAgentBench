import pandas as pd
from datetime import datetime

def closes_after_6pm(hours_list):
    """
    Determine whether a business operates past 6PM on any day.

    Args:
        hours_list (list): A list of [day, time_range] pairs, e.g., [["Monday", "9AM–5PM"]]

    Returns:
        bool: True if any day ends after 6PM, otherwise False
    """
    if not isinstance(hours_list, list):
        return False

    for day_info in hours_list:
        if not (isinstance(day_info, list) and len(day_info) == 2):
            continue

        _, time_range = day_info
        if not isinstance(time_range, str) or time_range.lower() == "closed":
            continue

        parts = time_range.replace("–", "-").split("-")
        if len(parts) != 2:
            continue

        _, end_time_str = parts
        try:
            fmt = "%I:%M%p" if ":" in end_time_str else "%I%p"
            end_time = datetime.strptime(end_time_str.upper(), fmt)
            if end_time.hour > 18 or (end_time.hour == 18 and end_time.minute > 0):
                return True
        except:
            continue

    return False

def get_top_late_open_businesses(meta_path, review_path, top_k=5):
    """
    Get the top-rated businesses that operate past 6PM on any day.

    Args:
        meta_path (str): Path to the business metadata JSONL file.
        review_path (str): Path to the review dataset JSONL file.
        top_k (int): Number of top businesses to return based on average rating.

    Returns:
        pd.DataFrame: A DataFrame with business names, hours, and average ratings.
    """
    # Load metadata and review datasets
    df_meta = pd.read_json(meta_path, lines=True)
    df_review = pd.read_json(review_path, lines=True)

    # Identify businesses open after 6PM
    df_meta['open_after_6pm'] = df_meta['hours'].apply(closes_after_6pm)
    df_open_late = df_meta[df_meta['open_after_6pm']].copy()

    # Merge metadata with reviews
    df_merged = pd.merge(
        df_open_late[['gmap_id', 'name', 'hours']],
        df_review[['gmap_id', 'rating']],
        on='gmap_id',
        how='inner'
    )

    # Group by business and calculate average rating
    df_avg = df_merged.groupby(
        ['gmap_id', 'name', df_merged['hours'].astype(str)]
    ).agg(avg_score=('rating', 'mean')).reset_index()

    # Sort by average rating and select top-K
    df_top = df_avg.sort_values(by='avg_score', ascending=False).head(top_k)

    return df_top[['name', 'hours', 'avg_score']]

# Example usage
if __name__ == "__main__":
    meta_file = "../ground_truth_dataset/meta_gt.json"
    review_file = "../ground_truth_dataset/review_gt.json"

    # Get top 5 highest-rated businesses that operate after 6PM
    top_businesses = get_top_late_open_businesses(meta_file, review_file, top_k=5)

    # Print results without index
    print("Top-rated businesses open after 6PM:")
    print(top_businesses.to_string(index=False))

    # Optional: save to CSV
    # top_businesses.to_csv("top_late_open_businesses.csv", index=False)
