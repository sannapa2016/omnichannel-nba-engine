import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Pharma NBA Dashboard", layout="wide")

# 1. Data Generation Logic (Moving this inside for the live demo)
def get_data():
    specialties = ['Oncology', 'Cardiology', 'Endocrinology', 'Rheumatology']
    channels = ['Rep Visit', 'Email', 'Webinar', 'Direct Mail']
    n_hcp = 1000
    np.random.seed(42)
    data = {
        'hcp_id': range(101, 101 + n_hcp),
        'specialty': np.random.choice(specialties, n_hcp),
        'rx_decile': np.random.randint(1, 11, n_hcp),
        'email_open_rate': np.random.uniform(0, 0.4, n_hcp),
        'webinar_attendance': np.random.randint(0, 5, n_hcp),
    }
    df = pd.DataFrame(data)
    # Simple logic for the demo recommendations
    conditions = [
        (df['webinar_attendance'] >= 3),
        (df['rx_decile'] >= 8) & (df['email_open_rate'] < 0.1),
        (df['email_open_rate'] >= 0.25),
    ]
    choices = ['Webinar', 'Rep Visit', 'Email']
    df['next_best_action'] = np.select(conditions, choices, default='Direct Mail')
    return df

# 2. UI Layout
st.title("🚀 Omnichannel Next-Best-Action (NBA) Engine")
st.markdown("### Territory Optimization & HCP Engagement Insights")

st.sidebar.header("Territory Filters")
specialty_filter = st.sidebar.multiselect("Select Specialty", 
                                        ['Oncology', 'Cardiology', 'Endocrinology', 'Rheumatology'], 
                                        default=['Oncology', 'Cardiology'])

df = get_data()
filtered_df = df[df['specialty'].isin(specialty_filter)]

# Display Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total HCPs", len(filtered_df))
col2.metric("High-Value Targets", len(filtered_df[filtered_df['rx_decile'] >= 9]))
col3.metric("Projected Lift", "14.2%", "+2.1%")

st.divider()

# Display Table
st.subheader("Daily Action Queue: Priority Recommendations")
st.dataframe(filtered_df[['hcp_id', 'specialty', 'rx_decile', 'next_best_action']].sort_values(by='rx_decile', ascending=False), use_container_width=True)

st.success("Strategy Insight: Priority 'Rep Visits' are suggested for high-volume prescribers with low digital engagement.")
