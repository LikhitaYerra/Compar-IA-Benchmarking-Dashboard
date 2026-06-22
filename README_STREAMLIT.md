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
   Or directly:
   ```bash
   streamlit run dashboard.py
   ```

## Streamlit Cloud Deployment

This app is configured for Streamlit Cloud deployment. The entry point is `streamlit_app.py`, which loads the main Compar'IA dashboard from `dashboard.py`.

No API keys are required. The app reads bundled CSV data (`comparai_metrics_detailed.csv`) and works fully offline.

After pushing changes to GitHub, open your app on Streamlit Cloud and click **Reboot app** (or wait for automatic redeploy).

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
