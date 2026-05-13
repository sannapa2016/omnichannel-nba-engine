import streamlit as st
import pandas as pd
import job_lib # We would save our model here
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Pharma NBA Dashboard", layout="wide")

st.title("🚀 Omnichannel Next-Best-Action (NBA) Engine")
st.markdown("### Territory Optimization & HCP Engagement Insights")

# Sidebar for Filters
st.sidebar.header("Territory Filters")
specialty = st.sidebar.multiselect("Select Specialty", ['Oncology', 'Cardiology', 'Endocrinology', 'Rheumatology'], default=['Oncology'])

# Load the data we generated earlier
df = pd.read_csv('hcp_engagement_data.csv')
filtered_df = df[df['specialty'].isin(specialty)]

# Display Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total HCPs", len(filtered_df))
col2.metric("High-Value Targets (Decile 9-10)", len(filtered_df[filtered_df['rx_decile'] >= 9]))
col3.metric("Projected Lift", "14.2%", "+2.1%")

st.divider()

# Display the Action Queue
st.subheader("Daily Action Queue: Priority Recommendations")
st.dataframe(filtered_df[['hcp_id', 'specialty', 'rx_decile', 'next_best_action']].sort_values(by='rx_decile', ascending=False))

st.success("Strategy Insight: Priority 'Rep Visits' are suggested for high-volume prescribers with low digital engagement.")
