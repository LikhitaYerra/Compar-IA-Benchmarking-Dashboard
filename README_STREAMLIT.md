# ComparAI Benchmarking Dashboard

A comprehensive Streamlit dashboard for LLM benchmarking with Mistral AI integration.

## Features

- 🤖 **AI-Powered Insights**: Mistral AI integration for intelligent analysis
- 📊 **Performance Metrics**: Quality, latency, energy, and environmental impact
- 📈 **Interactive Visualizations**: Plotly charts and heatmaps
- 🔍 **Model Comparison**: Side-by-side performance analysis
- 🌍 **Environmental Tracking**: CO2 emissions and energy consumption

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/LikhitaYerra/Compar-IA-Benchmarking-Dashboard.git
   cd Compar-IA-Benchmarking-Dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run streamlit_app.py
   ```

## Streamlit Cloud Deployment

This app is configured for Streamlit Cloud deployment. The main entry point is `streamlit_app.py`.

### Environment Variables

- `MISTRAL_API_KEY`: Your Mistral AI API key (optional, will show offline mode if not provided)

### Setting up Environment Variables

1. **For Local Development:**
   ```bash
   # Copy the example file
   cp env.example .env
   
   # Edit .env and add your API key
   MISTRAL_API_KEY=your_actual_api_key_here
   ```

2. **For Streamlit Cloud:**
   - Go to your app settings in Streamlit Cloud
   - Add the environment variable `MISTRAL_API_KEY` with your API key value
   - Redeploy your app

### Getting a Mistral API Key

1. Visit [Mistral AI Console](https://console.mistral.ai/)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it to your environment variables

## Data Format

The dashboard expects data with the following columns:
- `Model`: Model name
- `Model_Size`: Small, Medium, or Large
- `Quality_Score`: Performance score (1-5)
- `Latency_ms`: Response time in milliseconds
- `Energy_Wh`: Energy consumption in watt-hours
- `CO2_g`: CO2 emissions in grams

## Units

- **Energy**: Watt-hours (Wh)
- **CO2**: Grams (g)
- **Latency**: Milliseconds (ms)
- **Quality**: Score 1-5

## License

MIT License
