import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🛍️ Customer Shopping Behavior Dashboard")

# Load dataset
df = pd.read_csv("customer_shopping_behavior.csv")

# Dataset preview
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# Gender‐wise average spending
if "gender" in df.columns and "purchase_amount" in df.columns:
    st.subheader("💸 Average Spending by Gender")
    gender_spending = df.groupby("gender")["purchase_amount"].mean()
    st.bar_chart(gender_spending)

# Age distribution
if "age" in df.columns:
    st.subheader("🎂 Customer Age Distribution")
    fig, ax = plt.subplots()
    ax.hist(df["age"].dropna(), bins=10, edgecolor="black")
    st.pyplot(fig)

# Payment method usage (if exists)
if "payment_method" in df.columns:
    st.subheader("💳 Payment Method Usage")
    payment_counts = df["payment_method"].value_counts()
    st.bar_chart(payment_counts)

st.success("✅ Dashboard ready! Explore your dataset insights.")
