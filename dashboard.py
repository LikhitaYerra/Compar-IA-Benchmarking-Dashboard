import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import io

# Page configuration
st.set_page_config(
    page_title="Compar'IA Benchmarking Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f77b4;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

def load_data():
    """Load data from CSV file or create sample data if file doesn't exist"""
    try:
        df = pd.read_csv('data_collection_template.csv')
        # Check if data has been filled (non-empty quality scores)
        if df['Quality_Score'].isna().all():
            return create_sample_data()
        return df
    except FileNotFoundError:
        return create_sample_data()

def create_sample_data():
    """Create sample data for demonstration purposes"""
    models = ['LLaMA 3.1 8B', 'Gemma 8B', 'Mistral Small', 'GPT-OSS 20B', 'GPT-5', 'DeepSeek R1']
    model_sizes = ['Small', 'Small', 'Medium', 'Medium', 'Large', 'Large']
    categories = ['Factual', 'Reasoning', 'Programming', 'Knowledge', 'Advanced']
    
    data = []
    np.random.seed(42)  # For reproducible results
    
    for task_id in range(1, 31):
        category = categories[(task_id - 1) // 6] if task_id <= 25 else 'Advanced'
        
        for i, model in enumerate(models):
            # Generate realistic sample data based on model characteristics
            if 'Small' in model_sizes[i]:
                quality = np.random.normal(3.2, 0.8)
                latency = np.random.normal(2.5, 0.5)
                energy = np.random.normal(0.15, 0.03)
                cost = np.random.normal(0.02, 0.005)
            elif 'Medium' in model_sizes[i]:
                quality = np.random.normal(3.8, 0.6)
                latency = np.random.normal(4.2, 0.8)
                energy = np.random.normal(0.35, 0.07)
                cost = np.random.normal(0.08, 0.015)
            else:  # Large
                quality = np.random.normal(4.3, 0.5)
                latency = np.random.normal(6.8, 1.2)
                energy = np.random.normal(0.85, 0.15)
                cost = np.random.normal(0.25, 0.05)
            
            # Adjust for task difficulty
            if task_id > 20:  # Advanced tasks
                quality *= 0.9
                latency *= 1.3
                energy *= 1.2
                cost *= 1.4
            
            co2 = energy * 0.5  # Rough conversion factor
            
            data.append({
                'Task_ID': task_id,
                'Task_Category': category,
                'Model': model,
                'Model_Size': model_sizes[i],
                'Quality_Score': max(1, min(5, quality)),
                'Latency_sec': max(0.5, latency),
                'Energy_kWh': max(0.01, energy),
                'CO2_kg': max(0.005, co2),
                'Cost_EUR': max(0.001, cost),
                'Notes': ''
            })
    
    return pd.DataFrame(data)

def calculate_metrics(df):
    """Calculate aggregated metrics by model"""
    metrics = df.groupby(['Model', 'Model_Size']).agg({
        'Quality_Score': ['mean', 'std'],
        'Latency_sec': ['mean', 'std'],
        'Energy_kWh': ['mean', 'sum'],
        'CO2_kg': ['mean', 'sum'],
        'Cost_EUR': ['mean', 'sum']
    }).round(3)
    
    # Flatten column names
    metrics.columns = ['_'.join(col).strip() for col in metrics.columns]
    metrics = metrics.reset_index()
    
    # Calculate efficiency scores
    metrics['Quality_Efficiency'] = metrics['Quality_Score_mean'] / metrics['Energy_kWh_mean']
    metrics['Cost_Efficiency'] = metrics['Quality_Score_mean'] / metrics['Cost_EUR_mean']
    metrics['Speed_Efficiency'] = metrics['Quality_Score_mean'] / metrics['Latency_sec_mean']
    
    return metrics

def create_quality_energy_plot(df):
    """Create quality vs energy scatter plot"""
    fig = px.scatter(
        df, 
        x='Energy_kWh_mean', 
        y='Quality_Score_mean',
        color='Model_Size',
        size='Latency_sec_mean',
        hover_data=['Model', 'Cost_EUR_mean', 'CO2_kg_mean'],
        title="Quality vs Energy Consumption",
        labels={
            'Energy_kWh_mean': 'Average Energy Consumption (kWh)',
            'Quality_Score_mean': 'Average Quality Score (1-5)',
            'Model_Size': 'Model Size'
        }
    )
    
    fig.update_layout(
        title_font_size=16,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_title_font_size=12
    )
    
    return fig

def create_quality_cost_plot(df):
    """Create quality vs cost scatter plot"""
    fig = px.scatter(
        df, 
        x='Cost_EUR_mean', 
        y='Quality_Score_mean',
        color='Model_Size',
        size='Energy_kWh_mean',
        hover_data=['Model', 'Latency_sec_mean', 'CO2_kg_mean'],
        title="Quality vs Cost per Task",
        labels={
            'Cost_EUR_mean': 'Average Cost per Task (€)',
            'Quality_Score_mean': 'Average Quality Score (1-5)',
            'Model_Size': 'Model Size'
        }
    )
    
    fig.update_layout(
        title_font_size=16,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_title_font_size=12
    )
    
    return fig

def create_latency_comparison(df):
    """Create latency comparison bar chart"""
    fig = px.bar(
        df, 
        x='Model', 
        y='Latency_sec_mean',
        color='Model_Size',
        title="Average Latency by Model",
        labels={
            'Latency_sec_mean': 'Average Latency (seconds)',
            'Model': 'Model'
        }
    )
    
    fig.update_layout(
        title_font_size=16,
        xaxis_title_font_size=14,
        yaxis_title_font_size=14,
        legend_title_font_size=12,
        xaxis_tickangle=-45
    )
    
    return fig

def create_efficiency_radar(df):
    """Create efficiency radar chart"""
    # Normalize metrics for radar chart (0-1 scale)
    df_normalized = df.copy()
    for col in ['Quality_Score_mean', 'Quality_Efficiency', 'Cost_Efficiency', 'Speed_Efficiency']:
        df_normalized[col] = (df_normalized[col] - df_normalized[col].min()) / (df_normalized[col].max() - df_normalized[col].min())
    
    fig = go.Figure()
    
    for _, row in df_normalized.iterrows():
        fig.add_trace(go.Scatterpolar(
            r=[row['Quality_Score_mean'], row['Quality_Efficiency'], 
               row['Cost_Efficiency'], row['Speed_Efficiency']],
            theta=['Quality', 'Energy Efficiency', 'Cost Efficiency', 'Speed Efficiency'],
            fill='toself',
            name=row['Model']
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )),
        showlegend=True,
        title="Model Efficiency Comparison (Normalized)"
    )
    
    return fig

def create_ranking_table(df):
    """Create overall ranking table"""
    # Calculate composite score
    df['Composite_Score'] = (
        df['Quality_Score_mean'] * 0.4 +
        df['Quality_Efficiency'] * 0.2 +
        df['Cost_Efficiency'] * 0.2 +
        df['Speed_Efficiency'] * 0.2
    )
    
    # Sort by composite score
    ranking_df = df.sort_values('Composite_Score', ascending=False).reset_index(drop=True)
    ranking_df['Rank'] = range(1, len(ranking_df) + 1)
    
    # Select relevant columns for display
    display_cols = [
        'Rank', 'Model', 'Model_Size', 'Quality_Score_mean', 
        'Latency_sec_mean', 'Energy_kWh_mean', 'Cost_EUR_mean', 
        'Composite_Score'
    ]
    
    return ranking_df[display_cols]

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 Compar\'IA Benchmarking Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("**TP 1 – Benchmarking Small vs Large LLMs on Cost, Energy & Performance**")
    
    # Load data
    df = load_data()
    metrics_df = calculate_metrics(df)
    
    # Sidebar
    st.sidebar.header("📊 Dashboard Controls")
    
    # Model filter
    selected_models = st.sidebar.multiselect(
        "Select Models to Display",
        options=df['Model'].unique(),
        default=df['Model'].unique()
    )
    
    # Category filter
    selected_categories = st.sidebar.multiselect(
        "Select Task Categories",
        options=df['Task_Category'].unique(),
        default=df['Task_Category'].unique()
    )
    
    # Filter data
    filtered_df = df[df['Model'].isin(selected_models) & df['Task_Category'].isin(selected_categories)]
    filtered_metrics = calculate_metrics(filtered_df)
    
    # Main content tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Overview", 
        "⚡ Quality vs Energy", 
        "💰 Quality vs Cost", 
        "⏱️ Performance", 
        "🏆 Rankings"
    ])
    
    with tab1:
        st.header("📊 Overview Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                "Total Tasks", 
                f"{len(filtered_df['Task_ID'].unique())}",
                delta=None
            )
        
        with col2:
            avg_quality = filtered_metrics['Quality_Score_mean'].mean()
            st.metric(
                "Avg Quality Score", 
                f"{avg_quality:.2f}",
                delta=None
            )
        
        with col3:
            total_energy = filtered_metrics['Energy_kWh_sum'].sum()
            st.metric(
                "Total Energy (kWh)", 
                f"{total_energy:.3f}",
                delta=None
            )
        
        with col4:
            total_cost = filtered_metrics['Cost_EUR_sum'].sum()
            st.metric(
                "Total Cost (€)", 
                f"{total_cost:.3f}",
                delta=None
            )
        
        # Efficiency radar chart
        st.subheader("🎯 Model Efficiency Comparison")
        radar_fig = create_efficiency_radar(filtered_metrics)
        st.plotly_chart(radar_fig, use_container_width=True)
    
    with tab2:
        st.header("⚡ Quality vs Energy Consumption")
        
        # Quality vs Energy plot
        quality_energy_fig = create_quality_energy_plot(filtered_metrics)
        st.plotly_chart(quality_energy_fig, use_container_width=True)
        
        # Insights
        st.subheader("💡 Insights")
        best_energy_efficiency = filtered_metrics.loc[filtered_metrics['Quality_Efficiency'].idxmax()]
        st.info(f"**Most Energy Efficient:** {best_energy_efficiency['Model']} with {best_energy_efficiency['Quality_Efficiency']:.2f} quality points per kWh")
    
    with tab3:
        st.header("💰 Quality vs Cost Analysis")
        
        # Quality vs Cost plot
        quality_cost_fig = create_quality_cost_plot(filtered_metrics)
        st.plotly_chart(quality_cost_fig, use_container_width=True)
        
        # Cost efficiency table
        st.subheader("💵 Cost Efficiency Rankings")
        cost_efficiency = filtered_metrics.nlargest(6, 'Cost_Efficiency')[['Model', 'Quality_Score_mean', 'Cost_EUR_mean', 'Cost_Efficiency']]
        st.dataframe(cost_efficiency, use_container_width=True)
    
    with tab4:
        st.header("⏱️ Performance Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Latency comparison
            latency_fig = create_latency_comparison(filtered_metrics)
            st.plotly_chart(latency_fig, use_container_width=True)
        
        with col2:
            # Speed efficiency
            speed_fig = px.bar(
                filtered_metrics.sort_values('Speed_Efficiency', ascending=True),
                x='Speed_Efficiency',
                y='Model',
                orientation='h',
                color='Model_Size',
                title="Speed Efficiency (Quality/Time)",
                labels={'Speed_Efficiency': 'Quality Points per Second'}
            )
            st.plotly_chart(speed_fig, use_container_width=True)
    
    with tab5:
        st.header("🏆 Overall Rankings")
        
        # Ranking table
        ranking_df = create_ranking_table(filtered_metrics)
        st.dataframe(ranking_df, use_container_width=True)
        
        # Recommendations
        st.subheader("🎯 Recommendations")
        
        best_overall = ranking_df.iloc[0]
        best_cost_effective = ranking_df.loc[ranking_df['Cost_EUR_mean'].idxmin()]
        best_energy_efficient = ranking_df.loc[ranking_df['Energy_kWh_mean'].idxmin()]
        fastest = ranking_df.loc[ranking_df['Latency_sec_mean'].idxmin()]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.success(f"**🥇 Best Overall:** {best_overall['Model']} (Score: {best_overall['Composite_Score']:.2f})")
            st.info(f"**💰 Most Cost-Effective:** {best_cost_effective['Model']} (€{best_cost_effective['Cost_EUR_mean']:.3f}/task)")
        
        with col2:
            st.warning(f"**⚡ Most Energy-Efficient:** {best_energy_efficient['Model']} ({best_energy_efficient['Energy_kWh_mean']:.3f} kWh/task)")
            st.success(f"**🏃 Fastest:** {fastest['Model']} ({fastest['Latency_sec_mean']:.1f}s/task)")
    
    # Data export
    st.sidebar.header("📥 Export Data")
    
    if st.sidebar.button("Download Processed Data"):
        csv = filtered_metrics.to_csv(index=False)
        st.sidebar.download_button(
            label="Download CSV",
            data=csv,
            file_name="compar_ia_benchmark_results.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    main()
