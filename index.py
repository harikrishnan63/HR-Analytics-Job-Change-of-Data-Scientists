import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn style
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv("job.csv")

# -------------------------------------------------------------------
# Utilities to clean the experience and last_new_job columns
# -------------------------------------------------------------------
def clean_experience(val):
    if val == '<1':
        return 0
    elif val == '>20':
        return 21
    elif pd.isna(val):
        return None
    else:
        return int(val)

def clean_last_new_job(val):
    if val == 'never':
        return 0
    elif val == '>4':
        return 5
    elif pd.isna(val):
        return None
    else:
        return int(val)

df['experience_clean'] = df['experience'].apply(clean_experience)
df['last_new_job_clean'] = df['last_new_job'].apply(clean_last_new_job)

# -------------------------------------------------------------------
# PLOT 1: Gender Distribution
# -------------------------------------------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="gender")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("gender_distribution.png")
plt.show()

# -------------------------------------------------------------------
# PLOT 2: Education Level Count
# -------------------------------------------------------------------
plt.figure(figsize=(6, 4))
order = df["education_level"].value_counts().index
sns.countplot(data=df, x="education_level", order=order)
plt.title("Education Level Count")
plt.tight_layout()
plt.savefig("education_level.png")
plt.show()

# -------------------------------------------------------------------
# PLOT 3: Major Discipline Count
# -------------------------------------------------------------------
plt.figure(figsize=(7, 4))
order = df["major_discipline"].value_counts().index
sns.countplot(data=df, x="major_discipline", order=order)
plt.title("Major Discipline Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("major_discipline_count.png")
plt.show()

# -------------------------------------------------------------------
# PLOT 4: Last Job Change vs Experience (Boxplot)
# -------------------------------------------------------------------
plt.figure(figsize=(7, 4))
sns.boxplot(data=df, x="last_new_job_clean", y="experience_clean")
plt.title("Last New Job vs Experience")
plt.tight_layout()
plt.savefig("last_job_change_vs_experience.png")
plt.show()

# -------------------------------------------------------------------
# PLOT 5: Company Type Count
# -------------------------------------------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="company_type", order=df["company_type"].value_counts().index)
plt.title("Company Type Count")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("company_type_count.png")
plt.show()

print("✅ First 5 plots generated and saved successfully.")
