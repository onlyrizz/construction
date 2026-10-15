import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Generate 250 days of daily date indices
date_range = pd.date_range(start="2026-01-01", periods=250, freq="D")

base_subscribers = 5000
trend = np.linspace(0, 3500, 250)  # Upward growth of ~3,500 subscribers
noise_holt = np.random.normal(loc=0, scale=80, size=250)

subscribers = base_subscribers + trend + noise_holt
df_holt = pd.DataFrame(
    {
        "date": date_range.strftime("%Y-%m-%d"),
        "active_subscribers": np.round(subscribers).astype(int),
    }
)

df_holt.to_csv("media_daily_subscribers.csv", index=False)
print("✅ 'media_daily_subscribers.csv' created successfully! (250 rows)")

base_hours = 12000
trend_hw = np.linspace(0, 6000, 250)  # Upward trend in viewing hours

weekly_pattern = np.array([-400, -500, -300, -100, 400, 700, 200])
seasonality = np.tile(weekly_pattern, int(np.ceil(250 / 7)))[:250]
noise_hw = np.random.normal(loc=0, scale=150, size=250)

watch_hours = base_hours + trend_hw + seasonality + noise_hw
df_hw = pd.DataFrame(
    {
        "date": date_range.strftime("%Y-%m-%d"),
        "daily_watch_hours": np.round(watch_hours, 2),
    }
)

df_hw.to_csv("media_streaming_hours.csv", index=False)
print("✅ 'media_streaming_hours.csv' created successfully! (250 rows)")