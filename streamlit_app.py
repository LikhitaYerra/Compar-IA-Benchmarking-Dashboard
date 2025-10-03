import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os
import json
from mistralai import Mistral

# Page configuration
st.set_page_config(
    page_title="ComparAI Benchmarking Dashboard",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Mistral API configuration
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

@st.cache_resource
def get_mistral_client():
    """Initialize and cache Mistral client"""
    try:
        return Mistral(api_key=MISTRAL_API_KEY)
    except Exception as e:
        st.error(f"Error initializing Mistral client: {e}")
        return None

def call_mistral_api(prompt, model="mistral-small-latest"):
    """Call Mistral API with error handling"""
    try:
        client = get_mistral_client()
        if not client:
            return "Error: Mistral client not available"
        
        response = client.chat.complete(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Mistral API: {e}"

def create_sample_data():
    """Create sample data for demonstration"""
    np.random.seed(42)
    
    models = ['GPT-4', 'Claude-3', 'Llama-2', 'Mistral-7B', 'PaLM-2', 'Gemini-Pro']
    model_sizes = ['Large', 'Large', 'Large', 'Small', 'Large', 'Large']
    categories = ['Text Generation', 'Code Generation', 'Question Answering', 'Summarization', 'Translation']
    
    data = []
    for task_id in range(1, 31):
        category = categories[(task_id - 1) // 6] if task_id <= 25 else 'Advanced'
        
        for i, model in enumerate(models):
            if 'Small' in model_sizes[i]:
                quality = np.random.normal(3.2, 0.8)
                latency = np.random.normal(2500, 500)  # ms
                energy = np.random.normal(150, 30)  # Wh
            else:
                quality = np.random.normal(4.3, 0.5)
                latency = np.random.normal(6800, 1200)  # ms
                energy = np.random.normal(850, 150)  # Wh
            
            if task_id > 20:
                quality *= 0.9
                latency *= 1.3
                energy *= 1.2
            
            co2 = energy * 0.5  # Rough conversion factor (Wh to g CO2)
            
            data.append({
                'Task_ID': task_id,
                'Task_Category': category,
                'Model': model,
                'Model_Size': model_sizes[i],
                'Quality_Score': max(1, min(5, quality)),
                'Latency_ms': max(100, latency),
                'Energy_Wh': max(1, energy),
                'CO2_g': max(0.5, co2),
                'Notes': ''
            })
    
    return pd.DataFrame(data)

def calculate_metrics(df):
    """Calculate aggregated metrics by model"""
    metrics = df.groupby(['Model', 'Model_Size']).agg({
        'Quality_Score': ['mean', 'std', 'min', 'max', 'count'],
        'Latency_ms': ['mean', 'std', 'min', 'max'],
        'Energy_Wh': ['mean', 'std', 'sum'],
        'CO2_g': ['mean', 'std', 'sum']
    }).round(3)
    
    # Flatten column names
    metrics.columns = ['_'.join(col).strip() for col in metrics.columns]
    metrics = metrics.reset_index()
    
    # Calculate efficiency scores
    metrics['Quality_Efficiency'] = metrics['Quality_Score_mean'] / (metrics['Energy_Wh_mean'] / 1000)
    metrics['Speed_Efficiency'] = metrics['Quality_Score_mean'] / (metrics['Latency_ms_mean'] / 1000)
    
    # Calculate additional metrics
    metrics['Quality_Consistency'] = 1 - (metrics['Quality_Score_std'] / metrics['Quality_Score_mean'])
    metrics['Latency_Consistency'] = 1 - (metrics['Latency_ms_std'] / metrics['Latency_ms_mean'])
    metrics['Energy_Consistency'] = 1 - (metrics['Energy_Wh_std'] / metrics['Energy_Wh_mean'])
    
    # Calculate environmental impact
    metrics['Environmental_Impact'] = (metrics['CO2_g_mean'] / 1000 * 0.7 + (metrics['Energy_Wh_mean'] / 1000) * 0.3)
    metrics['Energy_Per_Quality_Point'] = (metrics['Energy_Wh_mean'] / 1000) / metrics['Quality_Score_mean']
    
    return metrics

def main():
    st.title("🤖 ComparAI Benchmarking Dashboard")
    st.markdown("**Intelligent LLM Performance Analysis with Mistral AI Integration**")
    
    # Sidebar
    st.sidebar.header("📊 Dashboard Controls")
    
    # AI Status
    ai_status = "✅ Connected" if get_mistral_client() else "❌ Offline"
    st.sidebar.metric("AI Status", ai_status)
    
    # Load data
    df = create_sample_data()
    metrics = calculate_metrics(df)
    
    # Model selection
    selected_models = st.sidebar.multiselect(
        "Select Models",
        options=df['Model'].unique(),
        default=df['Model'].unique()[:3]
    )
    
    # Filter data
    filtered_df = df[df['Model'].isin(selected_models)]
    filtered_metrics = calculate_metrics(filtered_df)
    
    # Main content
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Models", len(filtered_metrics))
    
    with col2:
        avg_quality = filtered_metrics['Quality_Score_mean'].mean()
        st.metric("Avg Quality", f"{avg_quality:.2f}/5")
    
    with col3:
        total_energy = filtered_metrics['Energy_Wh_sum'].sum()
        st.metric("Total Energy (Wh)", f"{total_energy:.1f}")
    
    with col4:
        total_co2 = filtered_metrics['CO2_g_sum'].sum()
        st.metric("Total CO₂ (g)", f"{total_co2:.1f}")
    
    # AI Insights
    st.header("🤖 AI-Powered Insights")
    
    if st.button("Generate AI Insights"):
        with st.spinner("AI is analyzing your data..."):
            prompt = f"""
            Analyze this LLM benchmarking data and provide 3-5 key insights:
            
            Models: {', '.join(filtered_metrics['Model'].tolist())}
            Best Quality: {filtered_metrics.loc[filtered_metrics['Quality_Score_mean'].idxmax(), 'Model']} ({filtered_metrics['Quality_Score_mean'].max():.2f}/5)
            Fastest: {filtered_metrics.loc[filtered_metrics['Latency_ms_mean'].idxmin(), 'Model']} ({filtered_metrics['Latency_ms_mean'].min():.0f}ms)
            Most Energy Efficient: {filtered_metrics.loc[filtered_metrics['Energy_Wh_mean'].idxmin(), 'Model']} ({filtered_metrics['Energy_Wh_mean'].min():.0f}Wh)
            
            Focus on: key findings, best model recommendations, and trade-offs. Keep it concise and actionable.
            """
            
            ai_response = call_mistral_api(prompt)
            
            if "Error calling Mistral API" not in ai_response:
                st.success("✅ AI Analysis Complete")
                st.markdown("### 🎯 **Key Insights**")
                st.markdown(ai_response)
            else:
                st.warning("⚠️ AI temporarily unavailable. Showing basic insights:")
                st.markdown("### 📊 **Basic Analysis**")
                best_quality = filtered_metrics.loc[filtered_metrics['Quality_Score_mean'].idxmax()]
                fastest = filtered_metrics.loc[filtered_metrics['Latency_ms_mean'].idxmin()]
                most_efficient = filtered_metrics.loc[filtered_metrics['Energy_Wh_mean'].idxmin()]
                
                st.markdown(f"• **Best Quality:** {best_quality['Model']} ({best_quality['Quality_Score_mean']:.2f}/5)")
                st.markdown(f"• **Fastest:** {fastest['Model']} ({fastest['Latency_ms_mean']:.0f}ms)")
                st.markdown(f"• **Most Energy Efficient:** {most_efficient['Model']} ({most_efficient['Energy_Wh_mean']:.0f}Wh)")
    
    # Data table
    st.header("📊 Model Performance Data")
    st.dataframe(filtered_metrics[['Model', 'Model_Size', 'Quality_Score_mean', 'Latency_ms_mean', 'Energy_Wh_mean', 'CO2_g_mean']].round(2), use_container_width=True)

if __name__ == "__main__":
    main()
