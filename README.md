# Insurance Risk Analytics

## Table of Contents 
1.[Project Overview](#project-overview)
2.[Business Objective](#business-objective)
3.[Data](#data)
4.[Tasks](#Tasks)
5.[Installation](#installation)
6.[Usage](#usage)
7.[Directory Structure](#directory-structure)
8.[Contributing](#contributing)

## Project Overview 
Welcome to the Insurance Risk Analytics project. This initiative is aimed at optimizing car insurance strategies for AlphaCare Insurance Solutions. By leveraging advanced data analytics and machine learning techniques, this project focuses on analyzing historical insurance claim data to identify low-risk clients, optimize marketing strategies, and ultimately improve business effectiveness.

## Business Objective 
AlphaCare Insurance Solutions aims to develop cutting-edge risk and predictive analytics to optimize car insurance planning and marketing in South Africa. This project will:
- Analyze historical insurance claim data
- Help optimize marketing strategies
- Discover low-risk clients for potential premium reductions

  ## Data
The historical insurance claim data spans from February 2014 to August 2015. It includes various features related to insurance policies, clients, locations, vehicles, plans, and payments.

## Tasks
### Task 1: Git and GitHub
- **Create a Git Repository**.
- **Git Version Control**: Use Git for version control, commit changes regularly.
- -**CI/CD with GitHub Actions**: Implement CI/CD pipelines.
-**Project Planning - EDA & Stats**:
- **Data Understanding**
- **Exploratory Data Analysis (EDA)**
- **Statistical Thinking**

### Task 2: Data Version Control (DVC) 
- **Install and Initialize DVC**: Set up DVC to manage datasets.
**Set Up Local Remote Storage**: Create storage for data tracking.
- **Add Data and Commit Changes**: Track datasets with DVC and commit changes to version control.
- **Push Data to Local Remote**: Ensure data is pushed to remote storage.

  ### Task 3: A/B Hypothesis Testing
- **Accept or Reject Null Hypotheses**:
- No risk differences across provinces.
- No risk differences between zip codes.
- No significant margin difference between zip codes.
- No significant risk difference between Women and Men.

### Task 4: Statistical Modeling 
- **Data Preparation**: Handle missing data, perform feature engineering, encode categorical data, and split data into train/test sets.
-**Modeling Techniques**: Implement models like Linear Regression, Decision Trees, Random Forests, and XGBoost.
- **Model Evaluation**: Evaluate models using metrics like accuracy, precision, recall, and F1-score.
- **Feature Importance Analysis**: Use SHAP or LIME to interpret model

  ## Installation
To get started, clone the repository and install the required dependencies.

```bash 
git clone https://github.com/dagiteferi/insurance-risk-analytics.git
```
```bash 
cd insurance-risk-analytics
```
```bash 
python -m venv venv source venv/bin/activate
```
# On Windows use
```bash 
`.\venv\Scripts\activate`
```
```bash 
 pip install -r requirements.txt
```


### Usage
Run the analysis scripts to perform data analysis and model training. Detailed instructions for each task can be found in the respective directories.

### Directory Structure
```
insurance-risk-analytics/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── data/
│   
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── scripts/
│   ├── __init__.py
│   └── README.md
├── src/

│   ├── __init__.py
├── tests/
│   └── __init__.py
├── .gitignore
├── requirements.txt
├── README.md
```
### Contributing
Contributions are welcome! Please fork the repository and create a pull request to propose changes.
