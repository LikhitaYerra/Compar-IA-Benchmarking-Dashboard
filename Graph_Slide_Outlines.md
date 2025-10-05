# Compar'IA Dashboard: Graph-Specific Slide Outlines
## Ready-to-Use Outlines for Each Streamlit Visualization

---

## SLIDE 1: Overview Metrics Cards
### **Title: "Key Performance Indicators"**

**What to Show:**
- 4 metric cards from dashboard
- Total Models: 6
- Average Quality: 3.7/5
- Total Energy: 8.3 Wh
- Total CO₂: 5.7g

**Key Message:**
"Quick overview of our 6-model benchmark results"

**Speaker Notes:**
"These cards give us an immediate snapshot of our study scope and initial findings."

---

## SLIDE 2: Quality vs Energy Scatter Plot
### **Title: "Quality vs Energy Efficiency Analysis"**

**What to Show:**
- Interactive scatter plot from dashboard
- X-axis: Energy (0.6-2.1 Wh)
- Y-axis: Quality (3.2-4.2)
- Bubble size: Latency
- Color: Model size

**Key Points to Highlight:**
- GPT-5: High quality (4.2), High energy (2.1 Wh)
- Gemma 8B: Lower quality (3.2), Lowest energy (0.6 Wh)
- 3x energy difference between smallest and largest

**Key Message:**
"Clear trade-off between quality and energy consumption - 3x difference is significant"

**Speaker Notes:**
"Point to the top-right for GPT-5 and bottom-left for Gemma 8B to show the trade-off."

---

## SLIDE 3: Quality vs Latency Scatter Plot
### **Title: "Speed vs Quality Performance"**

**What to Show:**
- Interactive scatter plot from dashboard
- X-axis: Latency (520-1,200ms)
- Y-axis: Quality (3.2-4.2)
- Bubble size: Energy
- Color: Model size

**Key Points to Highlight:**
- Gemma 8B: Fastest (520ms), Lower quality (3.2)
- GPT-5: Slowest (1,200ms), Highest quality (4.2)
- More gradual trade-off than energy vs quality

**Key Message:**
"Speed vs quality trade-off is more gradual than energy vs quality"

**Speaker Notes:**
"Show how the spread is less dramatic than the energy plot - speed is more forgiving."

---

## SLIDE 4: Task Category Bar Chart
### **Title: "Performance by Task Category"**

**What to Show:**
- Grouped bar chart from dashboard
- X-axis: 5 task categories
- Y-axis: Quality scores
- Groups: 6 different models

**Key Points to Highlight:**
- Easy Factual: Mistral Small leads (3.8)
- Programming: DeepSeek R1 leads (4.1)
- Creative: GPT-5 leads (4.4)
- Different models excel at different tasks

**Key Message:**
"Task-specific optimization is crucial - one size doesn't fit all"

**Speaker Notes:**
"Point out how different models lead in different categories - this is a key insight."

---

## SLIDE 5: Model Comparison Bar Chart
### **Title: "Multi-Metric Model Comparison"**

**What to Show:**
- Grouped bar chart with multiple y-axes
- X-axis: 6 model names
- Y-axis 1: Quality (left)
- Y-axis 2: Energy (right)
- Y-axis 3: Latency (right)

**Key Points to Highlight:**
- Quality: GPT-5 > DeepSeek R1 > GPT-OSS 20B
- Energy: Gemma 8B < LLaMA 3.1 8B < Mistral Small
- No single model dominates all metrics

**Key Message:**
"Each model has distinct strengths - comprehensive evaluation reveals optimal use cases"

**Speaker Notes:**
"Show how the bars go in different directions - this proves no single model is best for everything."

---

## SLIDE 6: Performance Rankings Tables
### **Title: "Top Performers by Category"**

**What to Show:**
- 3 ranking tables from dashboard
- Best Quality: GPT-5 (4.2) > DeepSeek R1 (4.0) > GPT-OSS 20B (3.8)
- Most Efficient: Gemma 8B (0.6 Wh) < LLaMA 3.1 8B (0.7 Wh) < Mistral Small (0.9 Wh)
- Fastest: Gemma 8B (520ms) < LLaMA 3.1 8B (580ms) < Mistral Small (650ms)

**Key Message:**
"Different models lead in different categories - context matters for selection"

**Speaker Notes:**
"These rankings reinforce that model selection should be context-specific."

---

## SLIDE 7: Raw Data Table
### **Title: "Detailed Performance Data"**

**What to Show:**
- Sortable data table from dashboard
- All 6 models with complete metrics
- Interactive filtering and sorting

**Sample Data to Highlight:**
| Model | Size | Quality | Latency | Energy | CO₂ |
|-------|------|---------|---------|--------|-----|
| GPT-5 | Large | 4.2/5 | 1,200ms | 2.1 Wh | 1.3g |
| DeepSeek R1 | Large | 4.0/5 | 980ms | 1.8 Wh | 1.1g |
| GPT-OSS 20B | Medium | 3.8/5 | 750ms | 1.2 Wh | 0.8g |

**Key Message:**
"Complete performance data enables informed decision-making"

**Speaker Notes:**
"Show the interactive features - sorting, filtering - this gives users full control."

---

## SLIDE 8: AI Insights Section
### **Title: "AI-Powered Analysis & Recommendations"**

**What to Show:**
- AI insights section from dashboard
- Generate AI Insights button
- Ask a Question input field
- AI response display

**Demo Questions:**
- "Which model is best for code generation?"
- "What's the most energy-efficient model?"
- "How do different task categories perform?"

**Key Message:**
"AI provides intelligent recommendations for optimal model selection"

**Speaker Notes:**
"Actually demonstrate the AI features - this shows the advanced capabilities of the dashboard."

---

## PRESENTATION FLOW OPTIONS

### **Quick Demo (5 slides):**
1. Overview Metrics Cards
2. Quality vs Energy Scatter Plot
3. Task Category Bar Chart
4. Performance Rankings Tables
5. AI Insights Section

### **Full Demo (8 slides):**
1. Overview Metrics Cards
2. Quality vs Energy Scatter Plot
3. Quality vs Latency Scatter Plot
4. Task Category Bar Chart
5. Model Comparison Bar Chart
6. Performance Rankings Tables
7. Raw Data Table
8. AI Insights Section

### **Executive Summary (4 slides):**
1. Overview Metrics Cards
2. Quality vs Energy Scatter Plot
3. Task Category Bar Chart
4. AI Insights Section

---

## DEMO PREPARATION CHECKLIST

### **Before the Presentation:**
- [ ] Dashboard is running at http://localhost:8501
- [ ] All graphs are loading correctly
- [ ] AI insights are working (test with sample question)
- [ ] Have backup screenshots ready
- [ ] Know key numbers by heart

### **During the Demo:**
- [ ] Actually navigate the dashboard
- [ ] Use hover effects to show details
- [ ] Demonstrate filtering and sorting
- [ ] Show AI question/answer
- [ ] Point to specific data points
- [ ] Explain what each graph reveals

### **Key Numbers to Remember:**
- 3x energy difference (0.6 Wh to 2.1 Wh)
- Quality range (3.2 to 4.2)
- Latency range (520ms to 1,200ms)
- 6 models, 30 tasks, 180 results

---

## SPEAKER TIPS

### **Opening:**
"Let me show you our interactive dashboard that analyzes 6 different LLM models across 30 diverse tasks."

### **For Each Graph:**
1. **Point to the visualization**
2. **Explain what it shows**
3. **Highlight key insights**
4. **Connect to business impact**

### **Closing:**
"This dashboard enables data-driven decision-making for sustainable AI deployment through strategic model selection."

### **Backup Plan:**
If dashboard doesn't work, use the slide outlines with static images and explain what the interactive features would show.
