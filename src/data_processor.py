import pandas as pd
import re

def run_dpk_cleaning(input_file):
    # Load the 'unstructured' data
    df = pd.read_csv(input_file)
    print(f"Initial Comment Count: {len(df)}")

    # 1. DPK Transform: Exact Deduplication
    # Masterclass 2 teaches that AI shouldn't process the same data twice.
    df_cleaned = df.drop_duplicates(subset=['text'])

    # 2. DPK Transform: Language/Noise Filtering
    # We remove links and comments that are too short (noise)
    def is_clean(text):
        text = str(text)
        if len(text) < 10: return False # Filter 'NICE!!'
        if "http" in text: return False # Filter spam links
        return True

    df_cleaned = df_cleaned[df_cleaned['text'].apply(is_clean)]
    
    # 3. Export to Parquet (DPK standard for efficient AI training)
    output_path = "data/processed/comments_cleaned.parquet"
    df_cleaned.to_parquet(output_path)
    
    print(f"Final Cleaned Count: {len(df_cleaned)}")
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    run_dpk_cleaning("data/raw/comments_unclean.csv")
