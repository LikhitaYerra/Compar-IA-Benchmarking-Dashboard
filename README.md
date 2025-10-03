# Compar'IA Benchmarking Dashboard

## TP 1 – Benchmarking Small vs Large LLMs on Cost, Energy & Performance

This project provides a comprehensive dashboard for analyzing and comparing different Large Language Models (LLMs) across multiple dimensions including quality, cost, energy consumption, and performance.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone or download this repository
2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
streamlit run dashboard.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📊 Features

### Interactive Dashboard
- **Overview Tab**: Key metrics and efficiency radar chart
- **Quality vs Energy**: Scatter plot showing quality vs energy consumption
- **Quality vs Cost**: Cost analysis with efficiency rankings
- **Performance**: Latency comparison and speed efficiency
- **Rankings**: Overall model rankings with composite scoring

### Data Collection
- Pre-configured CSV template for data collection
- Support for 6 models across 3 size categories:
  - **Small**: LLaMA 3.1 8B, Gemma 8B
  - **Medium**: Mistral Small, GPT-OSS 20B
  - **Large**: GPT-5, DeepSeek R1

### Analysis Capabilities
- Quality scoring (1-5 scale)
- Latency measurement (seconds)
- Energy consumption (kWh)
- CO₂ emissions (kg eq.)
- Cost analysis (€ per task)
- Composite efficiency scoring

## 📋 Task Categories

The dashboard supports analysis across 5 task categories:

1. **Factual & Rewriting** (Tasks 1-10): Basic factual questions and text processing
2. **Reasoning & Quantitative** (Tasks 11-15): Mathematical and logical reasoning
3. **Programming & Debugging** (Tasks 16-20): Code generation and debugging
4. **Knowledge & Reasoning** (Tasks 21-25): Complex domain knowledge
5. **Advanced & Creative** (Tasks 26-30): Multi-step creative and analytical tasks

## 🔧 Usage

### Data Collection
1. Use the provided `data_collection_template.csv` to record your benchmarking results
2. Fill in the quality scores, latency, energy, CO₂, and cost data for each model-task combination
3. Save the file and the dashboard will automatically load your data

### Dashboard Navigation
- Use the sidebar filters to focus on specific models or task categories
- Navigate between tabs to explore different aspects of the analysis
- Export processed data using the download button in the sidebar

### Key Metrics
- **Quality Score**: Manual rating from 1-5 based on answer quality
- **Latency**: Response time in seconds
- **Energy**: Power consumption in kWh per task
- **CO₂**: Carbon footprint in kg CO₂ equivalent
- **Cost**: Financial cost per task in euros

## 📈 Analysis Features

### Efficiency Metrics
- **Quality Efficiency**: Quality points per kWh consumed
- **Cost Efficiency**: Quality points per euro spent
- **Speed Efficiency**: Quality points per second of latency

### Composite Scoring
The overall ranking uses a weighted composite score:
- Quality Score: 40%
- Energy Efficiency: 20%
- Cost Efficiency: 20%
- Speed Efficiency: 20%

## 🎯 Recommendations

The dashboard provides automatic recommendations for:
- **Best Overall**: Highest composite score
- **Most Cost-Effective**: Lowest cost per task
- **Most Energy-Efficient**: Lowest energy consumption
- **Fastest**: Lowest latency

## 📁 File Structure

```
├── dashboard.py                 # Main Streamlit application
├── data_collection_template.csv # Data collection template
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔄 Sample Data

The dashboard includes realistic sample data for demonstration purposes. This data is automatically generated when no real data is available and can be used to explore the dashboard's features.

## 📊 Visualizations

- **Scatter Plots**: Quality vs Energy, Quality vs Cost
- **Bar Charts**: Latency comparison, efficiency rankings
- **Radar Chart**: Multi-dimensional efficiency comparison
- **Data Tables**: Detailed metrics and rankings

## 🛠️ Customization

The dashboard is designed to be easily customizable:
- Modify the sample data generation in `create_sample_data()`
- Adjust the composite scoring weights in `create_ranking_table()`
- Add new visualizations by extending the tab structure
- Customize the styling through the CSS in the main function

## 📝 Notes

- All monetary values are in euros (€)
- Energy consumption is measured in kilowatt-hours (kWh)
- CO₂ emissions are in kilograms of CO₂ equivalent
- Quality scores should be on a 1-5 scale for consistency

## 🤝 Contributing

This dashboard is designed for educational purposes as part of TP 1. Feel free to extend and modify it for your specific benchmarking needs.

## 📄 License

This project is created for educational purposes as part of the Compar'IA benchmarking assignment.
