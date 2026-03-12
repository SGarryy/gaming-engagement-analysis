# Gaming Engagement & Performance Analysis

## 🎯 Project Overview
This repository contains a professional-grade behavioral analysis of 40,000+ user records from a cloud-based gaming platform. By leveraging **Unsupervised Machine Learning (K-Means Clustering)**, this project segments users into actionable personas to assist in server load balancing, resource optimization, and targeted retention strategies.

## 📊 Final Results & Insights
Through K-Means clustering, we successfully segmented the user base into 4 actionable personas. This provides the following business value:
* **Infrastructure Optimization:** Identified peak load times for "Power User" segments to optimize server allocation.
* **Churn Prediction:** Framework established to flag "At-Risk" segments for proactive retention.
* **Targeted Marketing:** Enabled customized reward structures based on player behavior (Grinder vs. Casual).

### 👤 User Persona Definitions
| Persona | Behavioral Profile | Strategic Recommendation |
| :--- | :--- | :--- |
| **Hardcore Grinders** | High Session Hours / High Milestones | Allocate high-priority server bandwidth. |
| **Weekend Casuals** | Low Weekly Frequency / Moderate Sessions | Trigger "Weekend Warrior" event notifications. |
| **Social Butterflies** | High Frequency / Short Sessions | Focus on low-latency social features. |
| **Idle/At-Risk Users** | Low engagement across all metrics | Deploy automated re-engagement campaigns. |

---

## 🏗 Project Structure
```plaintext
├── data/
│   ├── raw/                            # Immutable source data dumps
│   └── processed/                      # Cleaned data and scaled features (.npy)
├── models/                             # Serialized ML models (.pkl)
├── notebooks/
│   └── 01_initial_exploration.ipynb    # Interactive EDA, Elbow Method, and Cluster Discovery
├── src/                                # Production-grade Python utilities
│   ├── check_env.py                    # Environment and dependency verification
│   ├── cluster_model.py                # K-Means implementation and model persistence
│   ├── data_loader.py                  # Secure data ingestion logic
│   ├── feature_engineering.py          # Schema standardization and cleaning
│   ├── summary_stats.py                # Automated reporting of descriptive statistics
│   ├── validate_data.py                # Integrity, null-check, and data health scripts
│   └── visualize_trends.py             # Distribution plotting and trend visualization
├── reports/
│   └── cluster_analysis_report.md      # Executive persona analysis and business strategy
├── requirements.txt                    # Project dependencies
└── README.md                           # Project documentation
```

---

### **Directory Descriptions**
* **src/**: Houses modular Python scripts. Moving logic from notebooks to scripts ensures the analysis is reproducible and scalable.
* **notebooks/**: Contains the interactive discovery phase where initial visualizations and model parameter tuning (Elbow Method) occurred.
* **reports/**: The destination for executive-facing documentation summarizing the analytical findings.

---

## 🛠 Technical Methodology & Data Schema
### Processed Data Schema
| Internal Name | Original Name | Description |
| :--- | :--- | :--- |
| session_duration_hr | PlayTimeHours | Total hours logged |
| weekly_frequency | SessionsPerWeek | Login count per week |
| milestones_reached | AchievementsUnlocked | In-game progression |

### Data Validation Results
* **Integrity Check:** 40,000+ records validated with 0% null values.
* **Feature Engineering:** Implemented **StandardScaler** for $z$-score normalization to ensure distance-based clustering accuracy.
* **Optimization:** Utilized the **Elbow Method** to verify the optimal cluster count ($k=4$).

---

## 🛠 Project Progress Tracking
- [x] Project Initialization & Git Setup
- [x] Environment Configuration (Python 3.13 Fixes)
- [x] Data Ingestion & Schema Standardization
- [x] Exploratory Data Analysis (EDA) & Outlier Detection
- [x] Feature Scaling & Elbow Method Optimization
- [x] K-Means Clustering Implementation & Model Saving
- [x] Cluster Profiling & Persona Development
- [x] Quality Assurance & Unit Testing
- [x] Business Impact & Recommendations (Finalized)

---

## 🚀 Setup & Usage

**1. Clone the repo:**
```bash
git clone <repo-url>
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run Environment Check:**
```bash
python src/check_env.py
```

**4. Run Modeling Pipeline:**
```bash
python src/cluster_model.py
```

## 🚀 Production Workflow
To run the full analytical pipeline from scratch, execute the following commands in order:

1. **Validate Data Health:**
```bash
python src/validate_data.py
```

2. **Generate User Segments:**
```bash
python src/cluster_model.py
```

3. **Export Behavioral Reports:**
```bash
python src/summary_stats.py
```
## ✅ Quality Assurance
To verify the stability of the analytical pipeline, run the automated test suite:

```bash
python tests/test_pipeline.py
```