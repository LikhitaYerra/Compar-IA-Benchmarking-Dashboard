# Compar'IA Benchmarking Project - Complete Setup

## 🎯 Project Overview

This project provides a comprehensive dashboard system for benchmarking Large Language Models (LLMs) across multiple dimensions: quality, cost, energy consumption, and performance. It's designed for TP 1 of the Compar'IA benchmarking assignment.

## 📁 Project Structure

```
/Users/likhitayerra/TP1/
├── dashboard.py                              # Main Streamlit dashboard application
├── data_collection_template.csv              # CSV template for data collection
├── compar_ia_data_collection_template.xlsx   # Excel template with instructions
├── requirements.txt                          # Python dependencies
├── launch.py                                 # Simple launcher script
├── run_dashboard.sh                          # Bash launcher script
├── create_excel_template.py                  # Script to generate Excel template
├── README.md                                 # Project documentation
└── PROJECT_OVERVIEW.md                      # This overview file
```

## 🚀 Quick Start Guide

### Option 1: Using the Python Launcher (Recommended)
```bash
cd /Users/likhitayerra/TP1
python launch.py
```

### Option 2: Using the Bash Script
```bash
cd /Users/likhitayerra/TP1
./run_dashboard.sh
```

### Option 3: Manual Launch
```bash
cd /Users/likhitayerra/TP1
pip install -r requirements.txt
streamlit run dashboard.py
```

## 📊 Dashboard Features

### 1. **Overview Tab**
- Key metrics summary
- Total tasks, average quality, energy, and cost
- Interactive efficiency radar chart
- Model comparison across all dimensions

### 2. **Quality vs Energy Tab**
- Scatter plot showing quality vs energy consumption
- Bubble size represents latency
- Color coding by model size
- Automatic insights and recommendations

### 3. **Quality vs Cost Tab**
- Cost analysis with efficiency rankings
- Scatter plot with energy consumption as bubble size
- Cost efficiency table
- Financial optimization insights

### 4. **Performance Tab**
- Latency comparison bar chart
- Speed efficiency analysis
- Model performance rankings
- Response time optimization

### 5. **Rankings Tab**
- Overall composite scoring
- Weighted ranking system
- Detailed metrics table
- Use-case specific recommendations

## 📋 Data Collection Process

### Step 1: Use the Excel Template
1. Open `compar_ia_data_collection_template.xlsx`
2. Follow the instructions in the "Instructions" sheet
3. Record results in the "Data Collection" sheet
4. Use the "Summary" sheet to track progress

### Step 2: Import Data
1. Save your results as `data_collection_results.csv`
2. Replace the template CSV with your actual data
3. The dashboard will automatically load your data

### Step 3: Analyze Results
1. Use the dashboard filters to focus on specific models/categories
2. Explore different visualizations
3. Export processed data for further analysis

## 🎯 Models to Benchmark

### Small Models (8B parameters)
- **LLaMA 3.1 8B**: Meta's efficient small model
- **Gemma 8B**: Google's lightweight model

### Medium Models (20B parameters)
- **Mistral Small**: Mistral AI's balanced model
- **GPT-OSS 20B**: Open-source GPT variant

### Large Models (70B+ parameters)
- **GPT-5**: OpenAI's flagship model
- **DeepSeek R1**: Advanced reasoning model

## 📊 Task Categories (30 Total)

### 1. Factual & Rewriting (Tasks 1-10)
- Basic factual questions
- Text summarization
- Translation tasks
- Sentiment analysis
- Information extraction

### 2. Reasoning & Quantitative (Tasks 11-15)
- Mathematical problems
- System of equations
- Calculus derivatives
- Conceptual explanations
- Unit conversions

### 3. Programming & Debugging (Tasks 16-20)
- Code generation
- Bug fixing
- Algorithm explanations
- SQL optimization
- Complexity analysis

### 4. Knowledge & Reasoning (Tasks 21-25)
- Comparative analysis
- Compliance procedures
- Technical summaries
- Architecture descriptions
- Learning paradigms

### 5. Advanced & Creative (Tasks 26-30)
- Project planning
- Content creation
- Legal documentation
- Business model innovation
- Technical communication

## 🔧 Technical Specifications

### Metrics Collected
- **Quality Score**: 1-5 scale (manual rating)
- **Latency**: Response time in seconds
- **Energy**: Power consumption in kWh
- **CO₂**: Carbon footprint in kg CO₂ equivalent
- **Cost**: Financial cost per task in euros

### Efficiency Calculations
- **Quality Efficiency**: Quality points per kWh
- **Cost Efficiency**: Quality points per euro
- **Speed Efficiency**: Quality points per second

### Composite Scoring
- Quality Score: 40%
- Energy Efficiency: 20%
- Cost Efficiency: 20%
- Speed Efficiency: 20%

## 📈 Sample Data

The dashboard includes realistic sample data for demonstration:
- Generated using statistical distributions
- Reflects realistic model characteristics
- Includes task difficulty adjustments
- Provides immediate visualization

## 🎨 Customization Options

### Visual Customization
- Color schemes for different model sizes
- Interactive hover information
- Responsive design for different screen sizes
- Export capabilities for all visualizations

### Analysis Customization
- Adjustable composite scoring weights
- Filterable data views
- Customizable efficiency metrics
- Flexible recommendation system

## 📱 Usage Tips

### For Data Collection
1. Test models in consistent conditions
2. Record metrics immediately after each test
3. Use consistent quality scoring criteria
4. Note any technical issues or anomalies

### For Analysis
1. Use filters to focus on specific aspects
2. Compare models within the same size category
3. Consider task-specific performance patterns
4. Export data for external analysis

### For Presentations
1. Use the ranking table for key findings
2. Export visualizations for slides
3. Focus on efficiency trade-offs
4. Highlight cost-benefit analysis

## 🔍 Troubleshooting

### Common Issues
1. **Missing dependencies**: Run `pip install -r requirements.txt`
2. **Port conflicts**: Streamlit will automatically find an available port
3. **Data not loading**: Check CSV format and column names
4. **Visualization errors**: Ensure all required data columns are present

### Support
- Check the README.md for detailed documentation
- Review the Excel template instructions
- Use the sample data to test functionality

## 🎯 Expected Outcomes

### Deliverables
1. **Spreadsheet**: Complete data collection with all metrics
2. **Dashboard**: Interactive visualizations and analysis
3. **Presentation**: Key findings and recommendations
4. **Report**: Detailed analysis of model performance

### Key Insights
- Model size vs performance trade-offs
- Cost-effectiveness analysis
- Energy efficiency comparisons
- Use-case specific recommendations

## 🚀 Next Steps

1. **Begin Testing**: Start with the Compar'IA platform
2. **Collect Data**: Use the provided templates
3. **Analyze Results**: Explore the dashboard
4. **Prepare Presentation**: Use insights for your slides
5. **Submit Deliverables**: Complete all required components

---

**Good luck with your benchmarking project! 🎉**

This comprehensive system will help you efficiently collect, analyze, and present your LLM benchmarking results with professional-quality visualizations and insights.
