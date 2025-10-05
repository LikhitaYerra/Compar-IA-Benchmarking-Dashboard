# Compar'IA Dashboard: Graph Summaries for Slides
## Concise Summaries of What Each Graph Shows

---

## Graph 1: Overview Metrics Cards
### **What it shows:**
- **Total Models:** 6 LLM models tested
- **Average Quality:** 3.7/5 across all models
- **Total Energy:** 8.3 Wh consumed by all models
- **Total CO₂:** 5.7g environmental impact

### **Key insight:**
Quick snapshot showing we tested 6 diverse models with varying performance levels and significant energy differences.

---

## Graph 2: Quality vs Energy Scatter Plot
### **What it shows:**
- **X-axis:** Energy consumption (0.6 to 2.1 Wh)
- **Y-axis:** Quality scores (3.2 to 4.2 out of 5)
- **Bubble size:** Latency (520ms to 1,200ms)
- **Colors:** Model sizes (Small/Medium/Large)

### **Key insight:**
Clear trade-off between quality and energy consumption. Large models (GPT-5, DeepSeek R1) deliver high quality but consume 3x more energy than small models (Gemma 8B, LLaMA 3.1 8B).

---

## Graph 3: Quality vs Latency Scatter Plot
### **What it shows:**
- **X-axis:** Response time (520ms to 1,200ms)
- **Y-axis:** Quality scores (3.2 to 4.2 out of 5)
- **Bubble size:** Energy consumption
- **Colors:** Model sizes (Small/Medium/Large)

### **Key insight:**
Speed vs quality trade-off is more gradual than energy vs quality. Small models are fastest but sacrifice quality, while large models are slowest but deliver highest quality.

---

## Graph 4: Task Category Performance Bar Chart
### **What it shows:**
- **X-axis:** 5 task categories (Easy Factual, Reasoning, Programming, Complex Knowledge, Creative)
- **Y-axis:** Average quality scores
- **Bars:** Different models for each category

### **Key insight:**
Different models excel at different task types. GPT-5 leads in complex tasks, DeepSeek R1 excels at programming, while Mistral Small performs well on simple factual tasks.

---

## Graph 5: Model Performance Comparison Bar Chart
### **What it shows:**
- **X-axis:** 6 model names
- **Y-axis 1:** Quality scores (left)
- **Y-axis 2:** Energy consumption (right)
- **Y-axis 3:** Latency (right, offset)

### **Key insight:**
No single model dominates all performance dimensions. Each model has distinct strengths - some excel at quality, others at efficiency, others at speed.

---

## Graph 6: Performance Rankings Tables
### **What it shows:**
- **Best Quality:** GPT-5 (4.2) > DeepSeek R1 (4.0) > GPT-OSS 20B (3.8)
- **Most Energy Efficient:** Gemma 8B (0.6 Wh) < LLaMA 3.1 8B (0.7 Wh) < Mistral Small (0.9 Wh)
- **Fastest:** Gemma 8B (520ms) < LLaMA 3.1 8B (580ms) < Mistral Small (650ms)

### **Key insight:**
Different models lead in different performance categories. Context matters for model selection - choose based on your priority (quality, efficiency, or speed).

---

## Graph 7: Raw Data Table
### **What it shows:**
- Complete performance metrics for all 6 models
- Sortable columns: Model, Size, Quality, Latency, Energy, CO₂
- Interactive filtering and search capabilities

### **Key insight:**
Detailed data enables informed decision-making. Users can sort by any metric to find the best model for their specific needs.

---

## Graph 8: AI Insights Section
### **What it shows:**
- AI-powered analysis of the data
- Interactive Q&A about model performance
- Intelligent recommendations for model selection

### **Key insight:**
AI provides smart recommendations based on the data. Users can ask questions like "Which model is best for code generation?" and get intelligent answers.

---

## Summary for Presentation Slides

### **Slide 1: Overview Metrics**
"These cards show our study scope: 6 models tested with an average quality of 3.7/5 and significant energy consumption differences."

### **Slide 2: Quality vs Energy**
"This scatter plot reveals the fundamental trade-off: larger models deliver higher quality but consume 3x more energy than smaller models."

### **Slide 3: Quality vs Latency**
"Speed vs quality shows a more gradual trade-off. Small models are fastest but sacrifice quality, while large models are slowest but deliver highest quality."

### **Slide 4: Task Categories**
"Different models excel at different task types. This proves that one-size-fits-all model selection is suboptimal - we need task-specific strategies."

### **Slide 5: Multi-Metric Comparison**
"No single model dominates all performance dimensions. Each model has distinct strengths, requiring strategic selection based on priorities."

### **Slide 6: Performance Rankings**
"Different models lead in different categories. Context matters - choose GPT-5 for quality, Gemma 8B for efficiency, or Mistral Small for speed."

### **Slide 7: Raw Data**
"Complete performance data enables informed decision-making. Users can sort and filter to find the best model for their specific requirements."

### **Slide 8: AI Insights**
"AI provides intelligent recommendations based on our data. Users can ask questions and get smart answers about model selection."

---

## Key Messages for Each Graph

1. **Overview Metrics:** "Study scope and initial findings"
2. **Quality vs Energy:** "Clear 3x energy trade-off"
3. **Quality vs Latency:** "More gradual speed trade-off"
4. **Task Categories:** "Task-specific optimization needed"
5. **Multi-Metric:** "No single best model"
6. **Rankings:** "Context-dependent selection"
7. **Raw Data:** "Enables informed decisions"
8. **AI Insights:** "Intelligent recommendations"
