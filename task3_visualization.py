import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("netflix.csv")

# Style
sns.set_style("darkgrid")

# Histogram
plt.figure(figsize=(10,6))

sns.histplot(
    df["user_rating_score"].dropna(),
    bins=20,
    color="purple",
    kde=True
)

plt.title("User Rating Score Distribution")
plt.xlabel("Rating Score")
plt.ylabel("Frequency")

plt.show()
# Top 10 Release Years

plt.figure(figsize=(10,6))

df["release_year"].value_counts().head(10).plot(
    kind="bar",
    color="orange"
)

plt.title("Top 10 Release Years")
plt.xlabel("Release Year")
# plt.ylabel("Number of Titles")

plt.show()
# Pie Chart - Content Ratings

plt.figure(figsize=(8,8))

df["rating"].value_counts().head(5).plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Top 5 Content Ratings")
plt.ylabel("")

plt.show()