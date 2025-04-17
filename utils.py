# utils.py
import pandas as pd
import numpy as np

def summarize_column(series: pd.Series):
    return {
        "Data Type": str(series.dtype),
        "Count": series.count(),
        "Unique": series.nunique(),
        "Missing": series.isnull().sum(),
        "Mean": round(series.mean(), 2),
        "Median": round(series.median(), 2),
        "Std Dev": round(series.std(), 2),
        "Min": series.min(),
        "Max": series.max(),
    }

def detect_outliers(series: pd.Series):
    mean = series.mean()
    std = series.std()
    threshold = 3 * std
    outliers = series[(abs(series - mean) > threshold)]
    return outliers.to_frame(name='Outlier Value')

