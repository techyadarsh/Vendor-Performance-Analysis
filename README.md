
# Vendor Performance Analysis

## Project Overview

This project provides a comprehensive framework for analyzing vendor performance, offering critical insights into purchasing patterns, sales effectiveness, and profitability. By integrating data from various sources (purchases, sales, and vendor invoices), we aim to identify top-performing vendors, understand factors influencing profit margins, and ultimately optimize supply chain strategies.

## ✨ Features

  * **Automated Data Ingestion:** Seamlessly loads raw CSV data into a SQLite database.
  * **Unified Vendor Summary:** Merges disparate datasets (purchases, sales, vendor invoices) to create a holistic view of vendor activities.
  * **Key Performance Indicators (KPIs):** Calculates essential metrics such as `gross_profit`, `profit_margin`, `stock_turnover`, and `sales_to_purchase_ratio` for a 360-degree performance evaluation.
  * **Statistical Analysis:** Employs two-sample T-tests to compare profit margins between top and low-performing vendors, providing data-driven conclusions.
  * **Interactive Visualizations:** Utilizes `matplotlib` and `seaborn` to generate insightful plots, aiding in trend identification and decision-making.
  * **Modular Codebase:** Organized into distinct Python scripts for data ingestion, summary generation, and analysis, promoting maintainability and scalability.

## 🛠️ Technologies Used

  * Python
  * Pandas
  * NumPy
  * Matplotlib
  * Seaborn
  * SQLite3
  * SQLAlchemy
  * SciPy (for statistical analysis)

## 📁 Project Structure

```
.
├── data/
│   └── (Your raw CSV data files - e.g., purchases.csv, sales.csv, vendor_invoice.csv)
├── logs/
│   └── (Log files generated during data ingestion and processing)
├── ingestion_db_Small_dataset.py
├── get_vendor_summary.py
├── Vendor_Performance_Analysis.ipynb
├── inventory_database.db (Generated SQLite database)
└── README.md
```

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed (3.7+) along with the following libraries:

```bash
pip install pandas numpy matplotlib seaborn sqlalchemy scipy
```

### Database Setup and Data Ingestion

The `ingestion_db_Small_dataset.py` script is responsible for loading your raw data into a SQLite database.

1.  **Place your raw CSV files** (e.g., `purchases.csv`, `sales.csv`, `vendor_invoice.csv`) into the `data/` directory. If you don't have this directory, create it.
2.  **Run the ingestion script:**
    ```bash
    python ingestion_db_Small_dataset.py
    ```
    This will create an `inventory_database.db` file in your project directory and ingest the data into respective tables.

### Generating Vendor Summary

The `get_vendor_summary.py` script combines the data from different tables and calculates the essential KPIs.

1.  **Run the vendor summary script:**
    ```bash
    python get_vendor_summary.py
    ```
    This will generate a comprehensive vendor summary and store it in a DataFrame, ready for analysis.

### Performing Analysis and Visualization

The `Vendor_Performance_Analysis.ipynb` Jupyter Notebook contains the core analysis and visualization steps.

1.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
2.  **Open `Vendor_Performance_Analysis.ipynb`** and run the cells sequentially to:
      * Load the processed vendor summary data.
      * Perform statistical tests (e.g., Two-Sample T-Test for profit margins).
      * Generate various plots and charts to visualize vendor performance.

## 💡 Key Insights from Analysis (Example)

Based on the `Vendor_Performance_Analysis.ipynb` notebook, an example key finding is:

  * **Significant Difference in Profit Margins:** A Two-Sample T-Test conducted between top-performing and low-performing vendors (based on total sales dollars) revealed a statistically significant difference in their profit margins (e.g., T-Statistic: -17.67, P-Value: 0.0000). This suggests that high-sales vendors tend to have different profit structures compared to their lower-performing counterparts.

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for improvements, new features, or bug fixes, please feel free to open an issue or submit a pull request.
For more details visit https://techyadarsh.in/

## 📄 License

This project is open-sourced under the MIT License.

-----
