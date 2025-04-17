# modules/automl.py

import pandas as pd
import numpy as np

def generate_insights(df: pd.DataFrame):
    insights = []
    numeric_cols = df.select_dtypes(include=np.number).columns

    for col in numeric_cols:
        desc = df[col].describe()
        outliers = detect_outliers(df[col])
        insights.append({
            "column": col,
            "mean": round(desc["mean"], 2),
            "std": round(desc["std"], 2),
            "min": desc["min"],
            "max": desc["max"],
            "outliers": len(outliers),
            "missing": df[col].isna().sum()
        })

    return insights

def detect_outliers(series: pd.Series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    return series[(series < (q1 - 1.5 * iqr)) | (series > (q3 + 1.5 * iqr))]

