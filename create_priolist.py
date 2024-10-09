import os
import json
import pandas as pd
import numpy as np
import csv

org_names =[]
df = pd.read_csv("prio_list_of_companies.csv")
for name in df["Name"]:
    org_path = f"test_data/{name}"

    if not os.path.exists(org_path):
        os.makedirs(org_path)