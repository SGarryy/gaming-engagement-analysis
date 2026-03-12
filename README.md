# Gaming Engagement & Performance Analysis 🎮📊
**Professional Data Science Case Study: User Segmentation & Resource Optimization**

> **Tags:** #DataScience #MachineLearning #KMeans #CustomerAnalytics #CloudGaming #Python

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
│   ├── feature_scaling.py              # Feature normalization (z-score)
│   ├── summary_stats.py                # Automated reporting of descriptive statistics
│   ├── validate_data.py                # Integrity, null-check, and data health scripts
│   └── visualize_trends.py             # Distribution plotting and trend visualization
├── tests/
│   └── test_pipeline.py                # Unit tests for pipeline stability
├── reports/
│   ├── cluster_analysis_report.md      # Clustering findings and recommendations
│   └── Executive_Summary.md            # High-level summary for stakeholders
├── requirements.txt                    # Project dependencies (with versions)
├── demo.py                             # One-command execution of full pipeline
└── README.md                           # Project documentation
```

---

### **Directory Descriptions**
* **src/**: Houses modular Python scripts. Moving logic from notebooks to scripts ensures the analysis is reproducible and scalable.
* **notebooks/**: Contains the interactive discovery phase where initial visualizations and model parameter tuning (Elbow Method) occurred.
* **reports/**: The destination for executive-facing documentation summarizing the analytical findings.
* **tests/**: Unit tests to verify pipeline integrity and data sanity checks.

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
cd gaming-engagement-analysis
```

**2. Create a virtual environment:**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚡ Quick Start: Run Complete Pipeline
The easiest way to execute the entire analysis pipeline is:

```bash
python demo.py
```

This single command will:
1. ✅ Verify environment setup and dependencies
2. 🧹 Clean and standardize raw data
3. 📊 Scale features for clustering (z-score normalization)
4. 🔍 Validate data integrity
5. 🤖 Apply K-Means clustering with $k=4$
6. 📈 Generate business strategy recommendations
7. 📊 Create visualization outputs

---

## 🎯 Manual Workflow (Step-by-Step)
If you prefer to run steps individually:

**Step 0: Verify Environment**
```bash
python src/check_env.py
```

**Step 1: Feature Engineering (Clean & Standardize)**
```bash
python src/feature_engineering.py
```
*Standardizes column names from raw data:*
- `PlayTimeHours` → `session_duration_hr`
- `SessionsPerWeek` → `weekly_frequency`
- `AchievementsUnlocked` → `milestones_reached`

**Step 2: Feature Scaling (Normalization)**
```bash
python src/feature_scaling.py
```
*Applies z-score normalization to ensure fair distance-based clustering.*

**Step 3: Data Validation**
```bash
python src/validate_data.py
```
*Checks for null values, schema consistency, and record count.*

**Step 4: ML Clustering & Model Training**
```bash
python src/cluster_model.py
```
*Fits K-Means model ($k=4$) and saves the trained model to `/models/`.*

**Step 5: Generate Strategy Reports**
```bash
python src/summary_stats.py
```
*Creates persona profiles and business recommendations for each segment.*

**Step 6: Visualize Results**
```bash
python src/visualize_trends.py
```
*Generates cluster comparison charts and saves to `/reports/`.*

---

## ✅ Quality Assurance
To verify the stability of the analytical pipeline, run the automated test suite:

```bash
python -m pytest tests/test_pipeline.py -v
```

Or using unittest:
```bash
python tests/test_pipeline.py
```

Tests verify:
- ✓ File existence and directory structure
- ✓ Required source modules present
- ✓ Missing file handling
- ✓ Required columns defined