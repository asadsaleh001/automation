import os
import pandas as pd
from datetime import datetime, date

folder_path = r"\\192.168.200.3\Centralized Invoice Processing\Vinay\Raw Transformation"

today = date.today()

for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.lower().endswith(".csv"):
            file_path = os.path.join(root, filename)

            # Get modified timestamp
            modified_ts = os.path.getmtime(file_path)
            modified_date = datetime.fromtimestamp(modified_ts).date()

            # Process only if modified today
            if modified_date == today:
                print(f"Processing (modified today): {file_path}")

                df = pd.read_csv(file_path, dtype=str, keep_default_na=False)

                df = df.replace("No Contract", "No Date", regex=False)
                df = df.replace("No Contract ", "No Date", regex=False)

                df.to_csv(file_path, index=False)

print("✅ Files modified today have been processed successfully.")
