# Project 2 — Weather Data Analyzer
# Analyzes monthly weather data using Pandas and visualizes
# temperature and rainfall trends with Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt


def create_dataset():
    data = {
        "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "temperature": [3, 5, 9, 13, 17, 21, 24, 23, 19, 14, 8, 4],
        "rainfall": [55, 45, 50, 40, 45, 35, 30, 35, 45, 60, 65, 60]
    }
    return pd.DataFrame(data)


def analyze(df):
    print(df)
    print(f"Hottest month: {df.loc[df['temperature'].idxmax(), 'month']}")
    print(f"Coldest month: {df.loc[df['temperature'].idxmin(), 'month']}")
    print(f"Average temperature: {df['temperature'].mean():.1f}°C")
    print(f"Wettest month: {df.loc[df['rainfall'].idxmax(), 'month']}")


def plot(df):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.plot(df['month'], df['temperature'], color='red', marker='o')
    ax1.set_title("Temperature by month")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Temperature (°C)")
    ax2.bar(df['month'], df['rainfall'], color='blue')
    ax2.set_title("Rainfall by month")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Rainfall (mm)")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    df = create_dataset()
    analyze(df)
    plot(df)