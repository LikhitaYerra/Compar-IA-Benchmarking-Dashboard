# Compar'IA Benchmarking Dashboard

## Live demos

| Version | URL |
|---------|-----|
| **Static HTML** (paper-style UI) | https://likhitayerra.github.io/Compar-IA-Benchmarking-Dashboard/ |
| **Streamlit** (interactive filters + export) | https://compar-ia-lyerra-aivancity.streamlit.app |

Local: `streamlit run dashboard.py` → http://localhost:8501 · or open `comparia_dashboard.html` in a browser.

---

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

The dashboard supports analysis across 5 task categories (30 prompts; each run once on 6 models = 180 measurements):

### Factual & Rewriting (1–10)
1. Who is the current UN Secretary-General?
2. Summarise a 150-word news article in one sentence.
3. Translate a paragraph about climate change into French.
4. Classify sentiment of 3 tweets (positive/negative).
5. Extract email & phone number from a text.
6. Explain the difference between RAM and ROM.
7. Name three renewable energy sources.
8. Turn a dense paragraph into bullet points.
9. Rewrite a sentence in a formal business tone.
10. Create a catchy blog title about electric cars.

### Reasoning & Quantitative (11–15)
11. Train A leaves at 10:00 at 100 km/h, Train B at 11:00 at 120 km/h — when do they meet?
12. Solve a system: 2x+3y=12 and x-y=4.
13. Give the derivative of x³+2x²-5x+7.
14. Explain 'overfitting' simply.
15. Convert 1500 W to kWh for 24 h and to yearly cost at 0.20 €/kWh.

### Programming & Debugging (16–20)
16. Write Python code reversing a string.
17. Fix the bug in `for i in range(5) print(i)`.
18. Explain what this recursive Python function returns.
19. Suggest an optimisation for a slow SQL query.
20. Explain Big-O complexity of binary search.

### Knowledge & Reasoning (21–25)
21. Compare nuclear vs solar energy (3 pros / 3 cons each).
22. Explain GDPR compliance steps for a SaaS startup.
23. Summarise a Wikipedia article on climate change into 5 key bullet points.
24. Describe in detail the transformer architecture (attention, encoder/decoder).
25. List and explain three differences between supervised, unsupervised, and reinforcement learning.

### Advanced & Creative (26–30)
26. Write a project plan for deploying AI to monitor deforestation using satellites.
27. Draft a LinkedIn post convincing a company to adopt green AI.
28. Create a short legal disclaimer about data privacy for an AI chatbot.
29. Imagine and explain a new business model that uses AI to reduce carbon emissions in logistics.
30. Analyse a research abstract and rewrite it for a non-technical policymaker.

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
