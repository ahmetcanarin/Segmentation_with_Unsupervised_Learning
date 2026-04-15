# 👟 Customer Segmentation with Unsupervised Learning

A customer segmentation project developed for FLO using **unsupervised learning techniques** to identify behavior-based customer groups and support data-driven marketing strategies.

---

## 🧩 Business Problem

FLO aims to segment its customers and define marketing strategies tailored to each segment.

Instead of relying on predefined labels, this project identifies customer groups by analyzing behavioral patterns and discovering natural clusters in the data.

The objective is to answer questions such as:

- Which customers are the most valuable?
- Which customers are still new and developing?
- Which customers are at risk of becoming inactive?
- How can marketing actions be customized based on behavioral segments?

---

## 🎯 Project Objectives

- Prepare customer-level behavioral data for clustering
- Create meaningful behavioral features such as **recency** and **tenure**
- Segment customers using:
  - **K-Means Clustering**
  - **Hierarchical Clustering**
- Compare clustering approaches
- Interpret clusters from a business perspective
- Translate technical cluster outputs into actionable marketing strategies

---

## 📊 Dataset Overview

The dataset consists of historical shopping behavior of FLO customers who made their last purchases in **2020–2021** through **OmniChannel** channels (both online and offline).

### Dataset Information
- **Observations:** 19,945
- **Variables:** 12

### Variables

| Variable | Description |
|----------|-------------|
| `master_id` | Unique customer ID |
| `order_channel` | The shopping platform/channel used |
| `last_order_channel` | The channel of the most recent purchase |
| `first_order_date` | Date of the first purchase |
| `last_order_date` | Date of the last purchase |
| `last_order_date_online` | Date of the last online purchase |
| `last_order_date_offline` | Date of the last offline purchase |
| `order_num_total_ever_online` | Total online purchase count |
| `order_num_total_ever_offline` | Total offline purchase count |
| `customer_value_total_ever_offline` | Total offline spend |
| `customer_value_total_ever_online` | Total online spend |
| `interested_in_categories_12` | Categories purchased in the last 12 months |

---

## 🛠️ Data Preparation

To make the data suitable for clustering, new behavioral variables were created:

- **total_customer_value**  
  Total amount spent across online and offline channels

- **total_order_num**  
  Total number of purchases across online and offline channels

- **recency**  
  Number of days since the customer’s last purchase

- **tenure**  
  Customer lifetime in days between first and last purchase

These variables were selected because they capture core dimensions of customer behavior:
- value
- frequency
- recency
- relationship duration

---

## ⚙️ Methodology

### 1. Feature Standardization
Clustering algorithms are distance-based, so all clustering variables were standardized using **StandardScaler**.

### 2. K-Means Clustering
K-Means was used to detect customer groups based on behavioral similarity.

Steps:
- Standardize variables
- Determine the optimal number of clusters using the **Elbow Method**
- Fit the final K-Means model
- Assign customer cluster labels

### 3. Hierarchical Clustering
Hierarchical clustering was also applied to compare segmentation structure.

Steps:
- Use the same standardized dataframe
- Build a dendrogram using **complete linkage**
- Select the number of clusters visually
- Fit the final agglomerative clustering model

---

## 📈 Clustering Features

The segmentation was built on the following variables:

- `total_customer_value`
- `total_order_num`
- `recency`
- `tenure`

These features represent both **customer value** and **customer lifecycle behavior**, making them highly suitable for behavioral clustering.

---

## 🔍 Cluster Interpretation

After clustering, each segment was analyzed statistically using summary metrics such as:

- average customer value
- average purchase frequency
- average recency
- average tenure

This made it possible to translate technical clusters into business-friendly segments.

### Example Segment Labels

- **High Value Active Customers**
- **Loyal Customers**
- **New Customers**
- **At-Risk / Passive Customers**
- **Potential Loyalists** *(if using 5-cluster structure)*

> Final segment names should be assigned based on cluster-level summary statistics.

---

## 💼 Business Strategies by Segment

### High Value Active Customers
Customers with high spending, high purchase frequency, and recent activity.

**Recommended actions:**
- VIP campaigns
- Exclusive product launches
- Loyalty rewards
- Personalized recommendations

### Loyal Customers
Customers with strong tenure and stable purchasing behavior.

**Recommended actions:**
- Retention campaigns
- Cross-sell and upsell offers
- Loyalty program benefits
- Category-based recommendations

### New Customers
Customers with short tenure and recent first purchases.

**Recommended actions:**
- Welcome journeys
- First-repeat-purchase incentives
- Introductory offers
- Onboarding campaigns

### At-Risk / Passive Customers
Customers with weak recent activity and long time since last purchase.

**Recommended actions:**
- Win-back campaigns
- Reactivation discounts
- Reminder emails and SMS
- Personalized category offers

### Potential Loyalists
Customers showing good recent activity but not yet fully matured.

**Recommended actions:**
- Loyalty-building promotions
- Bundle offers
- Personalized engagement campaigns

---

## 📊 Visualization

The project includes:

- **Elbow chart** for K-Means cluster selection
- **Dendrogram** for hierarchical clustering

These visualizations make the segmentation easier to interpret from both technical and business perspectives.

---

## 🛠️ Tech Stack

### Language
- Python

### Libraries
- pandas
- numpy
- scikit-learn
- scipy
- yellowbrick
- matplotlib
- seaborn

---

## 🔍 Key Strengths of the Project

- Behavior-based customer segmentation
- Strong feature engineering with recency and tenure
- Dual clustering approach:
  - K-Means
  - Hierarchical Clustering
- Business interpretation of technical outputs
- Actionable segment-based marketing recommendations

---

## 💡 What Makes This Project Stand Out?

This is not just a clustering exercise.

It demonstrates:

- how to transform raw customer data into behavioral features,
- how to apply unsupervised learning in a business context,
- and how to convert cluster outputs into real marketing actions.

In other words:

> this project does not stop at segmentation —  
> it turns segmentation into a decision-support tool.

---

## 🚀 Future Improvements

- Add PCA / t-SNE / UMAP visualizations for cluster separation
- Validate clusters using silhouette score and Davies-Bouldin index
- Build a dashboard for interactive segment exploration
- Combine clustering with RFM-based segmentation
- Deploy a segmentation scoring workflow for new customers
