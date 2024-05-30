import sqlalchemy
from sqlalchemy import create_engine

def setup_database(db_url):
    engine = create_engine(db_url)
    return engine

def save_to_database(df, table_name, engine):
    df.to_sql(table_name, engine, if_exists='append', index=False)

if __name__ == "__main__":
    engine = setup_database("postgresql://username:password@localhost:5432/advertisex")
    # Example usage
    sample_df = pd.DataFrame({
        'user_id': [1, 2, 3],
        'event': ['click', 'conversion', 'click'],
        'timestamp': pd.to_datetime(['2023-05-01', '2023-05-02', '2023-05-03'])
    })
    save_to_database(sample_df, 'events', engine)

