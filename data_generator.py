import pandas as pd
import numpy as np
from datetime import datetime
import os

os.makedirs("data/raw", exist_ok=True)

def generate_data():
    dates = pd.date_range(end=datetime.today(), periods=30)

    data = pd.DataFrame({
        "date": dates,
        "revenue": np.random.randint(1000, 5000, size=30).astype(float),
        "users": np.random.randint(50, 300, size=30)
    })

    # Inject bad data
    if np.random.rand() > 0.7:
        idx = np.random.randint(0, 30)
        data.loc[idx, "revenue"] = np.nan

    if np.random.rand() > 0.7:
        idx = np.random.randint(0, 30)
        data.loc[idx, "users"] *= np.random.randint(5, 10)

    filename = f"data/raw/data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    data.to_csv(filename, index=False)
    print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_data()
