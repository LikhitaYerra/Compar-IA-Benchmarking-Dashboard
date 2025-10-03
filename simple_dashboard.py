import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

# Page configuration
st.set_page_config(
    page_title="ComparAI Benchmarking Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def load_data():
    """Load data from CSV file"""
    try:
        if os.path.exists('comparai_metrics_detailed.csv'):
            df = pd.read_csv('comparai_metrics_detailed.csv')
            # Convert units
            df['Latency_ms_mean'] = df['Latency_sec_mean'] * 1000  # Convert to ms
            df['Energy_Wh_mean'] = df['Energy_kWh_mean'] * 1000  # Convert to Wh
            df['CO2_g_mean'] = df['CO2_kg_mean'] * 1000  # Convert to g
            return df
        else:
            st.error("CSV file not found!")
            return None
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

def main():
    st.title("🤖 ComparAI Benchmarking Dashboard")
    st.markdown("**Real Data from Excel File**")
    
    # Load data
    df = load_data()
    if df is None:
        st.stop()
    
    # Sidebar
    st.sidebar.header("📊 Dashboard Controls")
    
    # Model selection
    selected_models = st.sidebar.multiselect(
        "Select Models",
        options=df['Model'].unique(),
        default=df['Model'].unique()
    )
    
    # Filter data
    filtered_df = df[df['Model'].isin(selected_models)]
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Models", len(filtered_df))
    
    with col2:
        avg_quality = filtered_df['Quality_Score_mean'].mean()
        st.metric("Avg Quality", f"{avg_quality:.2f}/5")
    
    with col3:
        total_energy = filtered_df['Energy_Wh_mean'].sum()
        st.metric("Total Energy (Wh)", f"{total_energy:.0f}")
    
    with col4:
        total_co2 = filtered_df['CO2_g_mean'].sum()
        st.metric("Total CO₂ (g)", f"{total_co2:.0f}")
    
    # Quality vs Energy plot
    st.header("⚡ Quality vs Energy Consumption")
    fig1 = px.scatter(
        filtered_df, 
        x='Energy_Wh_mean', 
        y='Quality_Score_mean',
        color='Model_Size',
        size='Latency_ms_mean',
        hover_data=['Model', 'Latency_ms_mean', 'CO2_g_mean'],
        title="Quality vs Energy Consumption",
        labels={
            'Energy_Wh_mean': 'Average Energy Consumption (Wh)',
            'Quality_Score_mean': 'Average Quality Score (1-5)',
            'Model_Size': 'Model Size'
        }
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Quality vs Latency plot
    st.header("⏱️ Quality vs Latency")
    fig2 = px.scatter(
        filtered_df, 
        x='Latency_ms_mean', 
        y='Quality_Score_mean',
        color='Model_Size',
        size='Energy_Wh_mean',
        hover_data=['Model', 'Energy_Wh_mean', 'CO2_g_mean'],
        title="Quality vs Latency",
        labels={
            'Latency_ms_mean': 'Average Latency (ms)',
            'Quality_Score_mean': 'Average Quality Score (1-5)',
            'Model_Size': 'Model Size'
        }
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Performance comparison
    st.header("📊 Performance Comparison")
    
    # Create comparison chart
    fig3 = go.Figure()
    
    # Add bars for each metric
    fig3.add_trace(go.Bar(
        name='Quality Score',
        x=filtered_df['Model'],
        y=filtered_df['Quality_Score_mean'],
        yaxis='y',
        offsetgroup=1
    ))
    
    fig3.add_trace(go.Bar(
        name='Energy (Wh)',
        x=filtered_df['Model'],
        y=filtered_df['Energy_Wh_mean'],
        yaxis='y2',
        offsetgroup=2
    ))
    
    fig3.add_trace(go.Bar(
        name='Latency (ms)',
        x=filtered_df['Model'],
        y=filtered_df['Latency_ms_mean'],
        yaxis='y3',
        offsetgroup=3
    ))
    
    fig3.update_layout(
        title="Model Performance Comparison",
        xaxis_title="Model",
        yaxis=dict(title="Quality Score", side="left"),
        yaxis2=dict(title="Energy (Wh)", side="right", overlaying="y"),
        yaxis3=dict(title="Latency (ms)", side="right", overlaying="y", position=0.85),
        barmode='group'
    )
    
    st.plotly_chart(fig3, use_container_width=True)
    
    # Data table
    st.header("📋 Model Performance Data")
    display_df = filtered_df[['Model', 'Model_Size', 'Quality_Score_mean', 'Latency_ms_mean', 'Energy_Wh_mean', 'CO2_g_mean']].round(2)
    display_df.columns = ['Model', 'Size', 'Quality (1-5)', 'Latency (ms)', 'Energy (Wh)', 'CO2 (g)']
    st.dataframe(display_df, use_container_width=True)
    
    # Model rankings
    st.header("🏆 Model Rankings")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Best Quality")
        best_quality = filtered_df.nlargest(3, 'Quality_Score_mean')[['Model', 'Quality_Score_mean']]
        st.dataframe(best_quality, use_container_width=True)
    
    with col2:
        st.subheader("Most Energy Efficient")
        most_efficient = filtered_df.nsmallest(3, 'Energy_Wh_mean')[['Model', 'Energy_Wh_mean']]
        st.dataframe(most_efficient, use_container_width=True)
    
    with col3:
        st.subheader("Fastest")
        fastest = filtered_df.nsmallest(3, 'Latency_ms_mean')[['Model', 'Latency_ms_mean']]
        st.dataframe(fastest, use_container_width=True)

if __name__ == "__main__":
    main()
