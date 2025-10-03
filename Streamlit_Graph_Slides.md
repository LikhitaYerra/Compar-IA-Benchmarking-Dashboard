# Compar'IA Dashboard: Graph-Specific Slide Outlines
## Individual Slide Outlines for Each Streamlit Visualization

---

## Slide 1: Overview Metrics Dashboard

### **📊 Title: "Key Performance Indicators"**

### **Content Outline:**
- **4 Key Metrics Cards:**
  - Total Models (6)
  - Average Quality Score (3.7/5)
  - Total Energy Consumption (8.3 Wh)
  - Total CO₂ Emissions (5.7g)

### **Visual Elements:**
- Large metric cards with icons
- Color-coded values (green for efficiency, red for high consumption)
- Comparison to baseline or targets

### **Key Message:**
"Quick overview of our 6-model benchmark results showing performance and environmental impact"

---

## Slide 2: Quality vs Energy Consumption Scatter Plot

### **📊 Title: "Quality vs Energy Efficiency Analysis"**

### **Content Outline:**
- **Chart Type:** Scatter plot with bubbles
- **X-axis:** Energy Consumption (Wh)
- **Y-axis:** Quality Score (1-5)
- **Bubble Size:** Latency (ms)
- **Color:** Model Size (Small/Medium/Large)

### **Data Points:**
- **GPT-5:** High quality (4.2), High energy (2.1 Wh)
- **DeepSeek R1:** High quality (4.0), High energy (1.8 Wh)
- **GPT-OSS 20B:** Good quality (3.8), Medium energy (1.2 Wh)
- **Mistral Small:** Good quality (3.6), Low energy (0.9 Wh)
- **LLaMA 3.1 8B:** Moderate quality (3.4), Very low energy (0.7 Wh)
- **Gemma 8B:** Lower quality (3.2), Lowest energy (0.6 Wh)

### **Key Insights:**
- Clear trade-off between quality and energy consumption
- 3x energy difference between smallest and largest models
- Sweet spot in medium models for balanced performance

### **Key Message:**
"Larger models deliver higher quality but consume significantly more energy - strategic model selection is crucial"

---

## Slide 3: Quality vs Latency Scatter Plot

### **📊 Title: "Speed vs Quality Performance"**

### **Content Outline:**
- **Chart Type:** Scatter plot with bubbles
- **X-axis:** Latency (ms)
- **Y-axis:** Quality Score (1-5)
- **Bubble Size:** Energy Consumption (Wh)
- **Color:** Model Size (Small/Medium/Large)

### **Data Points:**
- **Gemma 8B:** Fastest (520ms), Lower quality (3.2)
- **LLaMA 3.1 8B:** Fast (580ms), Moderate quality (3.4)
- **Mistral Small:** Medium speed (650ms), Good quality (3.6)
- **GPT-OSS 20B:** Slower (750ms), Good quality (3.8)
- **DeepSeek R1:** Slow (980ms), High quality (4.0)
- **GPT-5:** Slowest (1,200ms), Highest quality (4.2)

### **Key Insights:**
- Speed vs quality trade-off is less pronounced than energy vs quality
- Small models are fastest but sacrifice quality
- Large models are slowest but deliver highest quality

### **Key Message:**
"Speed and quality show a more gradual trade-off - small models excel at speed, large models at quality"

---

## Slide 4: Task Category Performance Bar Chart

### **📊 Title: "Performance by Task Category"**

### **Content Outline:**
- **Chart Type:** Grouped bar chart
- **X-axis:** Task Categories
- **Y-axis:** Average Quality Score
- **Groups:** Different models
- **Categories:** Easy Factual, Reasoning, Programming, Complex Knowledge, Creative

### **Data Structure:**
- **Easy Factual:** Mistral Small leads (3.8)
- **Reasoning:** GPT-OSS 20B leads (3.9)
- **Programming:** DeepSeek R1 leads (4.1)
- **Complex Knowledge:** GPT-5 leads (4.3)
- **Creative Tasks:** GPT-5 leads (4.4)

### **Key Insights:**
- Different models excel at different task types
- Task-specific optimization is crucial
- One-size-fits-all approach is suboptimal

### **Key Message:**
"Model performance varies significantly by task type - strategic task routing maximizes efficiency"

---

## Slide 5: Model Performance Comparison Bar Chart

### **📊 Title: "Multi-Metric Model Comparison"**

### **Content Outline:**
- **Chart Type:** Grouped bar chart with multiple y-axes
- **X-axis:** Model names
- **Y-axis 1:** Quality Score (left)
- **Y-axis 2:** Energy Consumption (right)
- **Y-axis 3:** Latency (right, offset)

### **Data Visualization:**
- **Quality Bars:** GPT-5 (4.2) > DeepSeek R1 (4.0) > GPT-OSS 20B (3.8)
- **Energy Bars:** Gemma 8B (0.6) < LLaMA 3.1 8B (0.7) < Mistral Small (0.9)
- **Latency Bars:** Gemma 8B (520ms) < LLaMA 3.1 8B (580ms) < Mistral Small (650ms)

### **Key Insights:**
- Clear performance hierarchy across metrics
- Trade-offs between different performance dimensions
- No single model dominates all metrics

### **Key Message:**
"Each model has distinct strengths - comprehensive evaluation reveals optimal use cases"

---

## Slide 6: Model Performance Data Table

### **📊 Title: "Detailed Performance Metrics"**

### **Content Outline:**
- **Table Type:** Sortable data table
- **Columns:** Model, Size, Quality, Latency, Energy, CO₂
- **Rows:** 6 models with complete metrics
- **Features:** Sorting, filtering, search

### **Data Structure:**
| Model | Size | Quality | Latency | Energy | CO₂ |
|-------|------|---------|---------|--------|-----|
| GPT-5 | Large | 4.2/5 | 1,200ms | 2.1 Wh | 1.3g |
| DeepSeek R1 | Large | 4.0/5 | 980ms | 1.8 Wh | 1.1g |
| GPT-OSS 20B | Medium | 3.8/5 | 750ms | 1.2 Wh | 0.8g |
| Mistral Small | Medium | 3.6/5 | 650ms | 0.9 Wh | 0.6g |
| LLaMA 3.1 8B | Small | 3.4/5 | 580ms | 0.7 Wh | 0.5g |
| Gemma 8B | Small | 3.2/5 | 520ms | 0.6 Wh | 0.4g |

### **Key Message:**
"Complete performance data enables informed decision-making for model selection"

---

## Slide 7: Model Rankings Tables

### **📊 Title: "Performance Rankings by Category"**

### **Content Outline:**
- **3 Ranking Tables:**
  - Best Quality (Top 3)
  - Most Energy Efficient (Top 3)
  - Fastest (Top 3)

### **Best Quality Rankings:**
1. **GPT-5:** 4.2/5
2. **DeepSeek R1:** 4.0/5
3. **GPT-OSS 20B:** 3.8/5

### **Most Energy Efficient Rankings:**
1. **Gemma 8B:** 0.6 Wh
2. **LLaMA 3.1 8B:** 0.7 Wh
3. **Mistral Small:** 0.9 Wh

### **Fastest Rankings:**
1. **Gemma 8B:** 520ms
2. **LLaMA 3.1 8B:** 580ms
3. **Mistral Small:** 650ms

### **Key Message:**
"Different models lead in different performance categories - context matters for selection"

---

## Slide 8: Raw Data View Table

### **📊 Title: "Individual Task Results"**

### **Content Outline:**
- **Table Type:** Detailed task results
- **Columns:** Model, Task Category, Quality, Latency, Energy, CO₂
- **Rows:** All 180 individual task results
- **Features:** Filtering, sorting, search

### **Data Structure:**
- **180 rows** of individual task results
- **6 models** × **30 tasks** each
- **5 task categories** represented
- **Complete metrics** for each task

### **Key Message:**
"Granular data enables detailed analysis and pattern identification across all tasks"

---

## Slide 9: AI Insights Section

### **📊 Title: "AI-Powered Analysis & Recommendations"**

### **Content Outline:**
- **Generate AI Insights Button:** Comprehensive analysis
- **Ask a Question Input:** Interactive Q&A
- **AI Response Display:** Intelligent recommendations

### **AI Analysis Features:**
- **Key Performance Insights:** Best/worst performers
- **Model Recommendations:** Use case optimization
- **Trade-off Analysis:** Quality vs efficiency
- **Pattern Recognition:** Notable trends and outliers

### **Sample Questions:**
- "Which model is best for code generation?"
- "What's the most energy-efficient model?"
- "How do different task categories perform?"

### **Key Message:**
"AI-powered insights provide intelligent recommendations for optimal model selection"

---

## Slide 10: Dashboard Summary

### **📊 Title: "Interactive Dashboard Features"**

### **Content Outline:**
- **Real-time Data:** Live Excel integration
- **Interactive Filters:** Model and category selection
- **Multiple Visualizations:** Scatter plots, bar charts, tables
- **AI Integration:** Mistral API insights
- **Responsive Design:** Mobile-friendly interface

### **Key Features:**
- **Data Source:** Direct Excel file reading
- **Visualization Types:** 6 different chart types
- **Interactivity:** Hover, click, filter, sort
- **AI Analysis:** Intelligent recommendations
- **Export Options:** Data download capabilities

### **Key Message:**
"Comprehensive dashboard enables data-driven decision-making for sustainable AI deployment"

---

## Presentation Flow Recommendations

### **Option 1: Technical Deep Dive (10 slides)**
1. Overview Metrics
2. Quality vs Energy Analysis
3. Speed vs Quality Performance
4. Task Category Performance
5. Multi-Metric Comparison
6. Detailed Performance Data
7. Performance Rankings
8. Raw Data Analysis
9. AI-Powered Insights
10. Dashboard Summary

### **Option 2: Executive Summary (5 slides)**
1. Overview Metrics
2. Quality vs Energy Analysis
3. Task Category Performance
4. Performance Rankings
5. AI-Powered Insights

### **Option 3: Focused Analysis (7 slides)**
1. Overview Metrics
2. Quality vs Energy Analysis
3. Speed vs Quality Performance
4. Task Category Performance
5. Multi-Metric Comparison
6. Performance Rankings
7. AI-Powered Insights

---

## Visual Design Guidelines

### **Color Scheme:**
- **Green:** Efficiency, low energy, good performance
- **Red:** High consumption, poor performance
- **Blue:** Quality, reliability
- **Orange:** Warning, moderate performance

### **Chart Styling:**
- **Consistent fonts:** Arial or similar
- **Clear labels:** Descriptive axis titles
- **Legible text:** Minimum 12pt font
- **High contrast:** Easy to read in presentations

### **Interactive Elements:**
- **Hover effects:** Show detailed data
- **Click actions:** Filter or drill down
- **Responsive design:** Works on all devices
- **Loading states:** Smooth user experience
