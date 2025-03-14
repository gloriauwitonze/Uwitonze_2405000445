# -*- coding: utf-8 -*-
"""Gloria_2405000445

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17WS9MeURIaoUs4IRjlpd2mCUkqwNVg8w
"""

import pandas as pd


# Define phishing keywords
phishing_keywords = ["urgent", "password reset", "bank", "verify", "account suspended"]
#These are words commonly found in phishing emails.
#The script will check if an email contains any of these words.

# Load the dataset (uploaded file)
emails = pd.read_csv("/home/2405000445.csv")

# Check if the 'home' column exists
if 'home' in emails.columns:
    # Apply phishing detection
    emails["is_phishing"] = emails["home"].apply(
        lambda x: any(keyword in str(x).lower() for keyword in phishing_keywords)
    )


    # Save the processed file
    emails.to_csv("/home/2405000445.csv", index=False)
    print("Phishing detection complete. ✅")
else:
    print("Error: The 'home' column is missing from the dataset.")