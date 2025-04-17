# AI Data Explainer

Welcome to the **AI Data Explainer** project! This is an open-source tool designed to help users perform advanced data analysis on CSV and Excel files with a simple, user-friendly interface using **Streamlit**.

## Features

- **Data Summary**: Calculates the mean, median, minimum, and maximum values for numerical columns.
- **Outlier Detection**: Automatically detects outliers using the Z-Score method.
- **Data Distribution**: Visualizes the distribution of numerical columns with histograms.
- **Correlation Heatmap**: Displays a correlation heatmap to understand relationships between numerical columns.

## Installation Instructions

Follow these steps to get **AI Data Explainer** up and running on your local machine.

### Step 1: Clone the Repository

To get started, you'll need to clone the repository to your local machine.

1. Open your terminal (or command prompt).
2. Run the following command to clone the repository:
               
        git clone https://github.com/sid-2672/ai-data-explainer.git

### Step 2: Navigate to the Project Directory

Once the repository is cloned, navigate into the project directory:

    cd ai-data-explainer

### Step 3: Set Up a Virtual Environment (Recommended)

Setting up a virtual environment ensures that your project dependencies don’t interfere with your system’s Python installation.
Here’s how you can set up a virtual environment:
Create the virtual environment:

    python3 -m venv venv

Activate the virtual environment:

  On Windows:

    venv\Scripts\activate

On macOS/Linux:

    source venv/bin/activate

### Step 4: Install Dependencies

Once the virtual environment is activated, you need to install the required dependencies for the project. Run the following command:

    pip install -r requirements.txt

This will install the necessary libraries like streamlit, pandas, numpy, matplotlib, seaborn, and plotly.
### Step 5: Run the Streamlit App

To start the AI Data Explainer application, run the following command:

    streamlit run app.py

This will open a new browser window where you can upload your CSV or Excel files for data analysis.
### Step 6: Upload Your CSV or Excel File

    1. Once the app is running, you’ll see an interface to upload your CSV or Excel file.

    2. Click on the "Browse file" button, select your file, and watch the magic happen!

### Step 7: Explore the Data Insights

After uploading a file, you can explore the following:

    1. Dataset Preview: View a preview of the first few rows of your dataset.

    2. Data Summary: View summary statistics for numerical columns (mean, median, min, max).

    3. Outlier Detection: Check if any outliers are detected in your data.

    4. Data Distribution: Visualize the distribution of numerical columns with histograms.

    5. Correlation Heatmap: Explore the relationships between numerical columns with a correlation heatmap.

### Step 8: Contributing

Feel free to contribute to this project! Here's how:

  Fork the repository to your own GitHub account.

  Clone your forked repository:

    git clone https://github.com/yourusername/ai-data-explainer.git

Create a new branch to work on your changes:

    git checkout -b feature-branch

Make your changes and commit them:

    git add .
    git commit -m "Add your changes"

Push your changes to your fork:

    git push origin feature-branch

    Create a pull request (PR) from your fork's feature-branch to the main branch of the original repository.

Your contributions are welcome!

### Acknowledgements

    This project uses Streamlit for the frontend, making it easy to create interactive web apps with Python.

    Pandas and NumPy for data manipulation.

    Matplotlib, Seaborn, and Plotly for data visualization.

    SciPy for statistical analysis (outlier detection).

### Additional Notes

    The app currently supports only CSV and Excel file uploads.

    If you have any issues or find bugs, please open an issue on GitHub Issues.

    Be sure to update requirements.txt with any new dependencies you add to the project.

Thank you for using the AI Data Explainer!
