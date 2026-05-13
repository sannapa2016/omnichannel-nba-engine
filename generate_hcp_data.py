import pandas as pd
import numpy as np

def generate_hcp_nba_data(n_hcp=5000):
    np.random.seed(42)
    
    specialties = ['Oncology', 'Cardiology', 'Endocrinology', 'Rheumatology']
    channels = ['Rep Visit', 'Email', 'Webinar', 'Direct Mail']
    
    data = {
        'hcp_id': range(101, 101 + n_hcp),
        'specialty': np.random.choice(specialties, n_hcp),
        'rx_decile': np.random.randint(1, 11, n_hcp), # 10 = High Prescriber
        'years_in_practice': np.random.randint(2, 35, n_hcp),
        'last_interaction_type': np.random.choice(channels, n_hcp),
        'email_open_rate': np.random.uniform(0, 0.4, n_hcp),
        'webinar_attendance_count': np.random.randint(0, 5, n_hcp),
        'distance_from_clinic_km': np.random.uniform(1, 50, n_hcp)
    }
    
    df = pd.DataFrame(data)
    
    # Logic for Next Best Action (NBA) Target
    # High RX Decile + Low Email Open = Needs Rep Visit
    # High Webinar Attendance = Needs Webinar Invite
    conditions = [
        (df['webinar_attendance_count'] >= 3),
        (df['rx_decile'] >= 8) & (df['email_open_rate'] < 0.1),
        (df['email_open_rate'] >= 0.25),
    ]
    choices = ['Webinar', 'Rep Visit', 'Email']
    df['next_best_action'] = np.select(conditions, choices, default='Direct Mail')
    
    return df

if __name__ == "__main__":
    df = generate_hcp_nba_data()
    df.to_csv('hcp_engagement_data.csv', index=False)
    print("Success: 'hcp_engagement_data.csv' generated with 5,000 HCP profiles.")
