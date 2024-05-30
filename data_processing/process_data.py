import pandas as pd

def process_data(df, data_type):
    if data_type == 'ad_impressions':
        # Standardize and enrich ad impressions data
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    elif data_type == 'clicks_conversions':
        # Standardize and enrich clicks/conversions data
        df['event_timestamp'] = pd.to_datetime(df['event_timestamp'])
    elif data_type == 'bid_requests':
        # Standardize and enrich bid requests data
        df['auction_timestamp'] = pd.to_datetime(df['auction_timestamp'])
    # Add further processing as needed
    return df

if __name__ == "__main__":
    # Example usage
    ad_impressions_df = pd.read_json("path/to/sample_ad_impressions.json")
    processed_df = process_data(ad_impressions_df, 'ad_impressions')
    print(processed_df.head())
