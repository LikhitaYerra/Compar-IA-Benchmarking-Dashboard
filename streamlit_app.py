import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
from mistralai import Mistral

# Page configuration
st.set_page_config(
    page_title="ComparAI Benchmarking Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Mistral AI setup
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

@st.cache_resource
def get_mistral_client():
    """Get Mistral client with caching"""
    if MISTRAL_API_KEY:
        return Mistral(api_key=MISTRAL_API_KEY)
    return None

def call_mistral_api(prompt, model="mistral-small-latest"):
    """Call Mistral API with error handling"""
    try:
        client = get_mistral_client()
        if not client:
            return "Mistral API key not found. Please set MISTRAL_API_KEY environment variable."
        
        response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Mistral API: {e}"

def generate_ai_insights(metrics_df, raw_df):
    """Generate AI insights from the data"""
    try:
        # Prepare data summary for AI
        data_summary = f"""
        Model Performance Data:
        - Total Models: {len(metrics_df)}
        - Models: {', '.join(metrics_df['Model'].tolist())}
        
        Quality Scores (1-5):
        - Best: {metrics_df['Quality_Score_mean'].max():.2f} ({metrics_df.loc[metrics_df['Quality_Score_mean'].idxmax(), 'Model']})
        - Worst: {metrics_df['Quality_Score_mean'].min():.2f} ({metrics_df.loc[metrics_df['Quality_Score_mean'].idxmin(), 'Model']})
        - Average: {metrics_df['Quality_Score_mean'].mean():.2f}
        
        Energy Consumption (Wh):
        - Most Efficient: {metrics_df['Energy_Wh_mean'].min():.2f} ({metrics_df.loc[metrics_df['Energy_Wh_mean'].idxmin(), 'Model']})
        - Least Efficient: {metrics_df['Energy_Wh_mean'].max():.2f} ({metrics_df.loc[metrics_df['Energy_Wh_mean'].idxmax(), 'Model']})
        - Average: {metrics_df['Energy_Wh_mean'].mean():.2f}
        
        Latency (ms):
        - Fastest: {metrics_df['Latency_ms_mean'].min():.2f} ({metrics_df.loc[metrics_df['Latency_ms_mean'].idxmin(), 'Model']})
        - Slowest: {metrics_df['Latency_ms_mean'].max():.2f} ({metrics_df.loc[metrics_df['Latency_ms_mean'].idxmax(), 'Model']})
        - Average: {metrics_df['Latency_ms_mean'].mean():.2f}
        
        Task Categories: {', '.join(raw_df['Task_Category'].unique())}
        """
        
        prompt = f"""
        Analyze this AI model benchmarking data and provide insights:
        
        {data_summary}
        
        Please provide:
        1. Key performance insights
        2. Model recommendations for different use cases
        3. Trade-offs between quality, speed, and energy efficiency
        4. Notable patterns or outliers
        
        Keep the response concise and actionable.
        """
        
        return call_mistral_api(prompt)
    except Exception as e:
        return f"Error generating AI insights: {e}"

def load_excel_data():
    """Load data from Excel file"""
    try:
        excel_file = 'ComparAI_Benchmark_Template_v2 (3).xlsx'
        if os.path.exists(excel_file):
            # Read the 'Runs' sheet which contains the detailed data
            df = pd.read_excel(excel_file, sheet_name='Runs')
            
            # Clean the data
            df = df.dropna(subset=['Model', 'Quality (1-5)', 'Latency (milli sec)', 'Energy(wh)', 'co2 (g)'])
            
            # Rename columns for consistency
            df = df.rename(columns={
                'Quality (1-5)': 'Quality_Score',
                'Latency (milli sec)': 'Latency_ms',
                'Energy(wh)': 'Energy_Wh',
                'co2 (g)': 'CO2_g',
                'Prompt Category': 'Task_Category'
            })
            
            # Add model size based on model name
            def get_model_size(model):
                if 'GPT-5' in model or 'DeepSeek' in model:
                    return 'Large'
                elif 'GPT-OSS' in model or '8B' in model:
                    return 'Medium'
                else:
                    return 'Small'
            
            df['Model_Size'] = df['Model'].apply(get_model_size)
            
            return df
        else:
            st.error("Excel file not found!")
            return None
    except Exception as e:
        st.error(f"Error loading Excel data: {e}")
        return None

def calculate_metrics(df):
    """Calculate aggregated metrics"""
    metrics = df.groupby('Model').agg({
        'Quality_Score': ['mean', 'std', 'min', 'max', 'count'],
        'Latency_ms': ['mean', 'std', 'min', 'max'],
        'Energy_Wh': ['mean', 'std', 'sum'],
        'CO2_g': ['mean', 'std', 'sum'],
        'Model_Size': 'first'
    }).round(2)
    
    # Flatten column names
    metrics.columns = ['_'.join(col).strip() for col in metrics.columns.values]
    metrics = metrics.reset_index()
    
    # Calculate efficiency metrics
    metrics['Quality_Efficiency'] = metrics['Quality_Score_mean'] / metrics['Energy_Wh_mean']
    metrics['Speed_Efficiency'] = metrics['Quality_Score_mean'] / metrics['Latency_ms_mean']
    metrics['Environmental_Impact'] = metrics['CO2_g_mean'] / metrics['Quality_Score_mean']
    
    return metrics

def main():
    st.title("🤖 ComparAI Benchmarking Dashboard")
    st.markdown("**Real Data from Excel File**")
    
    # Load data
    df = load_excel_data()
    if df is None:
        st.stop()
    
    # Calculate metrics
    metrics_df = calculate_metrics(df)
    
    # Sidebar
    st.sidebar.header("📊 Dashboard Controls")
    
    # Model selection
    selected_models = st.sidebar.multiselect(
        "Select Models",
        options=df['Model'].unique(),
        default=df['Model'].unique()
    )
    
    # Task category filter
    selected_categories = st.sidebar.multiselect(
        "Select Task Categories",
        options=df['Task_Category'].unique(),
        default=df['Task_Category'].unique()
    )
    
    # Filter data
    filtered_df = df[
        (df['Model'].isin(selected_models)) & 
        (df['Task_Category'].isin(selected_categories))
    ]
    
    filtered_metrics = metrics_df[metrics_df['Model'].isin(selected_models)]
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Models", len(filtered_metrics))
    
    with col2:
        avg_quality = filtered_metrics['Quality_Score_mean'].mean()
        st.metric("Avg Quality", f"{avg_quality:.2f}/5")
    
    with col3:
        total_energy = filtered_metrics['Energy_Wh_sum'].sum()
        st.metric("Total Energy (Wh)", f"{total_energy:.0f}")
    
    with col4:
        total_co2 = filtered_metrics['CO2_g_sum'].sum()
        st.metric("Total CO₂ (g)", f"{total_co2:.0f}")
    
    # Quality vs Energy plot
    st.header("⚡ Quality vs Energy Consumption")
    fig1 = px.scatter(
        filtered_metrics, 
        x='Energy_Wh_mean', 
        y='Quality_Score_mean',
        color='Model_Size_first',
        size='Latency_ms_mean',
        hover_data=['Model', 'Latency_ms_mean', 'CO2_g_mean'],
        title="Quality vs Energy Consumption",
        labels={
            'Energy_Wh_mean': 'Average Energy Consumption (Wh)',
            'Quality_Score_mean': 'Average Quality Score (1-5)',
            'Model_Size_first': 'Model Size'
        }
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    # Quality vs Latency plot
    st.header("⏱️ Quality vs Latency")
    fig2 = px.scatter(
        filtered_metrics, 
        x='Latency_ms_mean', 
        y='Quality_Score_mean',
        color='Model_Size_first',
        size='Energy_Wh_mean',
        hover_data=['Model', 'Energy_Wh_mean', 'CO2_g_mean'],
        title="Quality vs Latency",
        labels={
            'Latency_ms_mean': 'Average Latency (ms)',
            'Quality_Score_mean': 'Average Quality Score (1-5)',
            'Model_Size_first': 'Model Size'
        }
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Task category analysis
    st.header("📊 Performance by Task Category")
    
    category_metrics = filtered_df.groupby(['Model', 'Task_Category']).agg({
        'Quality_Score': 'mean',
        'Latency_ms': 'mean',
        'Energy_Wh': 'mean',
        'CO2_g': 'mean'
    }).reset_index()
    
    fig3 = px.bar(
        category_metrics,
        x='Task_Category',
        y='Quality_Score',
        color='Model',
        title="Quality Score by Task Category",
        labels={
            'Quality_Score': 'Average Quality Score',
            'Task_Category': 'Task Category'
        }
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    # Performance comparison
    st.header("📊 Model Performance Comparison")
    
    # Create comparison chart
    fig4 = go.Figure()
    
    # Add bars for each metric
    fig4.add_trace(go.Bar(
        name='Quality Score',
        x=filtered_metrics['Model'],
        y=filtered_metrics['Quality_Score_mean'],
        yaxis='y',
        offsetgroup=1
    ))
    
    fig4.add_trace(go.Bar(
        name='Energy (Wh)',
        x=filtered_metrics['Model'],
        y=filtered_metrics['Energy_Wh_mean'],
        yaxis='y2',
        offsetgroup=2
    ))
    
    fig4.add_trace(go.Bar(
        name='Latency (ms)',
        x=filtered_metrics['Model'],
        y=filtered_metrics['Latency_ms_mean'],
        yaxis='y3',
        offsetgroup=3
    ))
    
    fig4.update_layout(
        title="Model Performance Comparison",
        xaxis_title="Model",
        yaxis=dict(title="Quality Score", side="left"),
        yaxis2=dict(title="Energy (Wh)", side="right", overlaying="y"),
        yaxis3=dict(title="Latency (ms)", side="right", overlaying="y", position=0.85),
        barmode='group'
    )
    
    st.plotly_chart(fig4, use_container_width=True)
    
    # Data table
    st.header("📋 Model Performance Data")
    display_df = filtered_metrics[['Model', 'Model_Size_first', 'Quality_Score_mean', 'Latency_ms_mean', 'Energy_Wh_mean', 'CO2_g_mean']].round(2)
    display_df.columns = ['Model', 'Size', 'Quality (1-5)', 'Latency (ms)', 'Energy (Wh)', 'CO2 (g)']
    st.dataframe(display_df, use_container_width=True)
    
    # Model rankings
    st.header("🏆 Model Rankings")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Best Quality")
        best_quality = filtered_metrics.nlargest(3, 'Quality_Score_mean')[['Model', 'Quality_Score_mean']]
        st.dataframe(best_quality, use_container_width=True)
    
    with col2:
        st.subheader("Most Energy Efficient")
        most_efficient = filtered_metrics.nsmallest(3, 'Energy_Wh_mean')[['Model', 'Energy_Wh_mean']]
        st.dataframe(most_efficient, use_container_width=True)
    
    with col3:
        st.subheader("Fastest")
        fastest = filtered_metrics.nsmallest(3, 'Latency_ms_mean')[['Model', 'Latency_ms_mean']]
        st.dataframe(fastest, use_container_width=True)
    
    # AI Insights section
    st.header("🤖 AI-Powered Insights & Analysis")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("🔍 Generate AI Insights", type="primary"):
            with st.spinner("Generating AI insights..."):
                insights = generate_ai_insights(filtered_metrics, filtered_df)
                st.markdown("### 📊 AI Analysis")
                st.markdown(insights)
    
    with col2:
        st.markdown("### 💬 Ask a Question")
        user_question = st.text_input("Ask about the data:", placeholder="Which model is best for code generation?")
        
        if user_question and st.button("Ask AI"):
            with st.spinner("Thinking..."):
                # Prepare context for the question
                context = f"""
                Based on this data:
                {filtered_metrics[['Model', 'Quality_Score_mean', 'Latency_ms_mean', 'Energy_Wh_mean', 'CO2_g_mean']].to_string()}
                
                Task categories available: {', '.join(filtered_df['Task_Category'].unique())}
                
                Question: {user_question}
                """
                
                answer = call_mistral_api(context)
                st.markdown("### 🤖 AI Response")
                st.markdown(answer)
    
    # Raw data view
    st.header("🔍 Raw Data View")
    st.subheader("Individual Task Results")
    raw_display = filtered_df[['Model', 'Task_Category', 'Quality_Score', 'Latency_ms', 'Energy_Wh', 'CO2_g']].round(2)
    st.dataframe(raw_display, use_container_width=True)

if __name__ == "__main__":
    main()
