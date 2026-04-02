import pandas as pd
import glob

def load_data():
    files = glob.glob("data/raw/*.csv")

    if not files:
        return pd.DataFrame()

    df = pd.concat([pd.read_csv(f) for f in files], ignore_index=True)
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date")


def validate_data(df):
    issues = []

    if df.empty:
        issues.append("No data available")
        return issues, df

    # Null check
    if df["revenue"].isnull().sum() > 0:
        issues.append("Null values found in revenue")

    # Users spike check
    df["users_change"] = df["users"].pct_change()

    spikes = df[df["users_change"].abs() > 2]
    if not spikes.empty:
        issues.append(f"User spikes detected: {len(spikes)} times")

    return issues, df


def anomaly_detection(df):
    if df.empty:
        return pd.DataFrame(), df

    df = df.copy()

    df["rolling_mean"] = df["revenue"].rolling(window=5, min_periods=1).mean()
    df["std"] = df["revenue"].rolling(window=5, min_periods=1).std()

    # Avoid division by zero
    df["std"] = df["std"].replace(0, 1)

    df["z_score"] = (df["revenue"] - df["rolling_mean"]) / df["std"]

    anomalies = df[df["z_score"].abs() > 2]

    return anomalies, df
