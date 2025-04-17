import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px

# Helper functions for data analysis

def detect_outliers(data: pd.DataFrame):
    """Detect outliers using Z-score"""
    numeric_data = data.select_dtypes(include=[np.number])
    z_scores = stats.zscore(numeric_data)
    outliers = (np.abs(z_scores) > 3).all(axis=1)
    return outliers

def generate_data_summary(data: pd.DataFrame):
    """Generate basic data summary: mean, median, min, max"""
    summary = {}
    numeric_data = data.select_dtypes(include=[np.number])
    
    summary['mean'] = numeric_data.mean(numeric_only=True).to_dict()
    summary['median'] = numeric_data.median(numeric_only=True).to_dict()
    summary['min'] = numeric_data.min(numeric_only=True).to_dict()
    summary['max'] = numeric_data.max(numeric_only=True).to_dict()
    return summary

def plot_data_distribution(data: pd.DataFrame):
    """Generate distribution plots for numerical columns using matplotlib"""
    numeric_data = data.select_dtypes(include=[np.number])
    
    if len(numeric_data.columns) == 0:
        st.error("No numeric columns found in the dataset.")
        return
    
    fig, ax = plt.subplots(len(numeric_data.columns), 1, figsize=(10, 6 * len(numeric_data.columns)))
    
    if len(numeric_data.columns) == 1:
        ax = [ax]

    for i, col in enumerate(numeric_data.columns):
        sns.histplot(numeric_data[col], kde=True, ax=ax[i])
        ax[i].set_title(f'Distribution of {col}')
        ax[i].set_xlabel(col)
        ax[i].set_ylabel('Frequency')

    st.pyplot(fig)

def plot_correlation_heatmap(data: pd.DataFrame):
    """Generate a simple correlation heatmap using seaborn"""
    numeric_data = data.select_dtypes(include=[np.number])
    
    if numeric_data.shape[1] == 0:
        st.error("No numeric columns to calculate correlations.")
        return
    
    corr_matrix = numeric_data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', ax=ax, fmt=".2f")
    st.pyplot(fig)

# Streamlit app UI

st.title("AI Data Explainer")
st.subheader("Upload a CSV or Excel file for data analysis.")

# File uploader for browsing and uploading a file
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file:
    # Try to load and process the file based on user input file path
    try:
        with st.spinner("Processing your file..."):
            if uploaded_file.name.endswith("csv"):
                data = pd.read_csv(uploaded_file, encoding='utf-8', parse_dates=True)
            elif uploaded_file.name.endswith("xlsx"):
                data = pd.read_excel(uploaded_file, engine='openpyxl', parse_dates=True)
            else:
                st.error("Unsupported file format. Please upload a CSV or Excel file.")
                data = None

            if data is not None:
                st.success("File loaded successfully!")

                # Display dataset preview
                st.subheader("Dataset Preview")
                st.write(data.head())

                # Generate data summary
                st.subheader("Data Summary")
                summary = generate_data_summary(data)
                st.write(f"**Mean**: {summary['mean']}")
                st.write(f"**Median**: {summary['median']}")
                st.write(f"**Min**: {summary['min']}")
                st.write(f"**Max**: {summary['max']}")

                # Detect and show outliers
                st.subheader("Detected Outliers")
                outliers = detect_outliers(data)
                if outliers.any():
                    st.write("Outliers detected in the following rows:")
                    st.write(data[outliers])
                else:
                    st.write("No significant outliers detected.")

                # Plot data distribution
                st.subheader("Data Distribution")
                plot_data_distribution(data)

                # Plot correlation heatmap
                st.subheader("Correlation Heatmap")
                plot_correlation_heatmap(data)

    except Exception as e:
        st.error(f"Error while reading the file: {e}")

else:
    st.warning("Please upload a CSV or Excel file.")

# Footer with a custom message
st.markdown("""
    <footer>
        <p>Created by Sid - AI Data Explainer</p>
        <p>Check the <a href="https://github.com/sid-2672" target="_blank">GitHub Repo</a> for more details and contribute!</p>
    </footer>
    """, unsafe_allow_html=True)

