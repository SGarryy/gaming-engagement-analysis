# Gaming Engagement & Performance Analysis

## Project Overview
This repository contains a performance analysis of user engagement metrics for a cloud-based gaming platform. The objective is to identify 
usage patterns to assist in server load balancing and resource optimization.

## 🔒 Data Privacy & Security
To ensure compliance with internal security protocols, this project utilizes a **Synthetic Dataset**. No proprietary company data or PII 
(Personally Identifiable Information) has been used or uploaded.

## Business Requirements
As a contract data analyst, I have been tasked with:
* Identifying "Peak Usage" behaviors across the user base.
* Cleaning and validating raw session logs for downstream reporting.
* Visualizing the correlation between game achievements and session length.

## 💡 Project Inspiration & Context
This project is inspired by real-world analytical challenges encountered during my contract-based role at a cloud-focused technology firm. While the methodologies and workflows mirror my professional approach to data analysis, this repository utilizes an **independently sourced, public dataset** to ensure full compliance with non-disclosure agreements (NDAs) and data privacy standards. 

The goal here is to demonstrate the end-to-end analytical lifecycle—from raw ingestion to business insights—in a sanitized, public-facing environment.

## Analytical Assumptions
To simulate a corporate environment, the following assumptions were made:
* **User Engagement:** High milestones with low play-time are treated as "High Efficiency" users.
* **Infrastructure Cost:** Server load is assumed to scale linearly with concurrent sessions.
* **Data Integrity:** Outliers exceeding the 99th percentile are flagged for investigation rather than immediate deletion.

## Project Structure
```text
├── data/
│   ├── raw/                                # Original, immutable data dumps
│   └── processed/                          # Cleaned data ready for analysis
├── notebooks/                              # Interactive EDA and discovery
├── src/                                    # Production-grade Python utilities
│   ├── data_loader.py                      # Secure data ingestion logic
│   ├── validate_data.py                    # Integrity and null-check scripts
│   ├── feature_engineering.py              # Schema standardization
│   ├── summary_stats.py                    # Automated reporting logic
│   └── visualize_trends.py                 # Distribution plotting utilities
├── reports/                                # Generated charts and summary text files
├── .env.example                            # Environment configuration template
├── requirements.txt                        # Project dependencies
└── README.md                               # Project documentation and roadmap
```
### Directory Descriptions
* **data/raw**: Contains the initial CSV ingestions. These files are never modified directly to ensure data lineage.
* **src/**: Houses modular Python scripts. Moving logic from notebooks to scripts ensures the analysis is reproducible.
* **reports/**: The destination for all non-code outputs, including statistical summaries and PNG visualizations for stakeholders.

## Processed Data Schema
| Internal Name | Original Name | Description |
| :--- | :--- | :--- |
| session_duration_hr | PlayTimeHours | Total hours logged |
| weekly_frequency | SessionsPerWeek | Login count per week |
| milestones_reached | AchievementsUnlocked | In-game progression |

## Project Progress Tracking
- [x] Project Initialization & Git Setup
- [x] Environment Configuration
- [x] Data Loading Utility Template
- [x] Data Directory Architecture
- [x] Data Dictionary Documentation
- [x] Data Ingestion & Validation
- [x] Feature Engineering (Column Standardization)
- [x] Initial Summary Reporting
- [x] Exploratory Data Analysis
- [x] Data Scaling & Clustering Preparation
- [x] Outlier & Correlation Analysis
- [x] Feature Scaling & Elbow Optimization
- [/] K-Means Clustering & Persona Mapping (In Progress)
- [ ] Business Impact & Recommendations (Scheduled)

## Data Validation Results
* **Integrity Check:** Successfully loaded 40,000+ records. Validated file existence and non-empty dataset.
* **Missing Values:** Null value detection completed across all columns.
* **Data Types:** Verified numeric column detection and data integrity.
* **Output Artifacts:** Processed data saved to `data/processed/gaming_data_cleaned.csv` and scaled features exported to `data/processed/scaled_gaming_data.npy` for downstream modeling.