import pandas as pd
import os

# Let's take our cleaned parquet data and 'send' it to a sheet
# (In a real setup, you would use the Google Sheets API)
def export_to_automation_hub(df_to_export):
    # Filter only for 'Opportunities' that need a reply
    opportunity_df = df_to_export[df_to_export['text'].str.contains('?', regex=False)]

    # Ensure the 'data' directory exists
    output_dir = "data"
    os.makedirs(output_dir, exist_ok=True)

    # Save as a CSV that we will upload to Google Sheets
    opportunity_df.to_csv(os.path.join(output_dir, "to_relay_app.csv"), index=False)
    print("🚀 Data ready for Relay.app automation!")

# Ensure the 'data' directory exists
output_dir = "data"
os.makedirs(output_dir, exist_ok=True)

# Use the existing 'cleaned_df' from the kernel state and save it to parquet
cleaned_df.to_parquet(os.path.join(output_dir, "comments_clean.parquet"))

# Now, pass the existing cleaned_df directly to the export function.
export_to_automation_hub(cleaned_df)
