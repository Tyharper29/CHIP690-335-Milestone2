import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("/Users/tyishaharper/UNC student/Chip690_335/Milestone 2")

df_2019 = pd.read_csv("mhcld_puf_2019.csv")
df_2020 = pd.read_csv("mhcld_puf_2020.csv")
df_2021 = pd.read_csv("mhcld_puf_2021.csv")

# 2. Filter for African American clients
aa_2019 = df_2019[df_2019["RACE"] == 3].copy()
aa_2020 = df_2020[df_2020["RACE"] == 3].copy()
aa_2021 = df_2021[df_2021["RACE"] == 3].copy()


# 3. Function to compute service rates
def service_rates(df, year):
    total = len(df)
    return {
        "Year": year,
        "Community Based Program": (df["CMPSERVICE"] == 1).sum() / total * 100,
        "State Hospital": (df["SPHSERVICE"] == 1).sum() / total * 100,
        "Inpatient Psychiatric": (df["OPISERVICE"] == 1).sum() / total * 100,
        "Residential": (df["RTCSERVICE"] == 1).sum() / total * 100,
    }


# 4. Compute service rates for each year
rates_2019 = service_rates(aa_2019, 2019)
rates_2020 = service_rates(aa_2020, 2020)
rates_2021 = service_rates(aa_2021, 2021)

df_rates = pd.DataFrame([rates_2019, rates_2020, rates_2021])

#  6. Create a bar chart in notebook
