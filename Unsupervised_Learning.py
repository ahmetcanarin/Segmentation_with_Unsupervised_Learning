import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import random
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from yellowbrick.cluster import KElbowVisualizer
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.preprocessing import StandardScaler

pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.max_rows", None)
pd.set_option("display.float_format", lambda x: "%.2f" % x)

# =========================
# 1. DATA PREPARATION
# =========================

# Load dataset
df = pd.read_csv("flo_data_20k.csv")

# Convert date columns to datetime
date_cols = df.columns[df.columns.str.contains("date", case=False)]
df[date_cols] = df[date_cols].apply(pd.to_datetime)

# Reference date for recency
today_date = df["last_order_date"].max() + dt.timedelta(days=2)

# Feature engineering
df["total_customer_value"] = df["customer_value_total_ever_offline"] + df["customer_value_total_ever_online"]
df["total_order_num"] = df["order_num_total_ever_online"] + df["order_num_total_ever_offline"]
df["recency"] = (today_date - df["last_order_date"]).dt.days
df["tenure"] = (df["last_order_date"] - df["first_order_date"]).dt.days

# =========================
# 2. K-MEANS CLUSTERING
# =========================

cluster_cols = ["total_customer_value", "total_order_num", "recency", "tenure"]
X = df[cluster_cols]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method
ssd = []
K = range(1, 30)
for k in K:
    model = KMeans(n_clusters=k).fit(X_scaled)
    ssd.append(model.inertia_)

plt.plot(K, ssd, "bx-")
plt.xlabel("Farklı K Değerlerine Karşılık SSE/SSR/SSD")
plt.title("Optimum Küme sayısı için Elbow Yöntemi")
plt.show()

kmeans = KMeans()
elbow = KElbowVisualizer(kmeans, k=(2, 20))
elbow.fit(X_scaled)
elbow.show()

elbow.elbow_value_

# Fit optimal model
kmeans = KMeans(n_clusters=4, random_state=1).fit(X_scaled)
df["k_cluster"] = kmeans.labels_ + 1

# =========================
# 3. HIERARCHICAL CLUSTERING
# =========================

hc = linkage(X_scaled, "complete")

plt.figure(figsize=(7, 5))
plt.title("Dendrograms")
dend = dendrogram(hc,
                  truncate_mode="lastp",
                  p=10,
                  show_contracted=True,
                  leaf_font_size=10)
plt.axhline(y=1.2, color="r", linestyle="--")
plt.show(block=True)

cluster = AgglomerativeClustering(n_clusters=5)
df["hi_cluster"] = cluster.fit_predict(X_scaled) + 1

# =========================
# 4. CLUSTER ANALYSIS
# =========================

df.groupby("k_cluster", observed=True)[cluster_cols].describe()
df.groupby("hi_cluster", observed=True)[cluster_cols].describe()

# =========================
# BUSINESS INTERPRETATION OF CLUSTERS
# =========================

# Calculate cluster-level summary statistics for interpretation
df.groupby("hi_cluster", observed=True)[["total_customer_value", "total_order_num", "recency", "tenure"]].mean()

hi_cluster_map = {
    1: "High Value Active Customers",
    2: "Loyal Customers",
    3: "New Customers",
    4: "Potential Loyalists",
    5: "At-Risk / Passive Customers"
}

df["hi_segment_name"] = df["hi_cluster"].map(hi_cluster_map)
df[["master_id", "hi_cluster", "hi_segment_name"]].head()

