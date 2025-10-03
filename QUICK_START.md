# 🚀 Quick Start Guide - Compar'IA Dashboard

## ⚡ Launch the Dashboard (3 Options)

### Option 1: Python Launcher (Recommended)
```bash
cd /Users/likhitayerra/TP1
python launch.py
```

### Option 2: Bash Script
```bash
cd /Users/likhitayerra/TP1
./run_dashboard.sh
```

### Option 3: Manual Launch
```bash
cd /Users/likhitayerra/TP1
streamlit run dashboard.py
```

## 📊 What You'll See

The dashboard opens at `http://localhost:8501` with 5 main tabs:

1. **📈 Overview** - Key metrics and efficiency radar chart
2. **⚡ Quality vs Energy** - Energy consumption analysis
3. **💰 Quality vs Cost** - Cost efficiency analysis  
4. **⏱️ Performance** - Latency and speed analysis
5. **🏆 Rankings** - Overall model rankings and recommendations

## 📋 Data Collection

### Using Excel Template (Recommended)
1. Open `compar_ia_data_collection_template.xlsx`
2. Follow instructions in the "Instructions" sheet
3. Record results in the "Data Collection" sheet
4. Save as `data_collection_results.csv`
5. Replace the template CSV with your data

### Using CSV Template
1. Edit `data_collection_template.csv`
2. Fill in your benchmarking results
3. Save the file
4. Dashboard will automatically load your data

## 🎯 Key Features

- **Interactive Visualizations**: Hover for details, filter by model/category
- **Sample Data**: Realistic demo data included for testing
- **Export Capabilities**: Download processed data and visualizations
- **Automatic Insights**: AI-powered recommendations and analysis
- **Responsive Design**: Works on desktop, tablet, and mobile

## 🔧 Troubleshooting

### If dashboard won't start:
```bash
pip install -r requirements.txt
```

### If data won't load:
- Check CSV format matches template
- Ensure all required columns are present
- Verify data types (numbers for metrics)

### If visualizations are empty:
- Check that quality scores are between 1-5
- Ensure numeric columns contain valid numbers
- Verify model names match exactly

## 📈 Sample Data Included

The dashboard includes realistic sample data showing:
- 6 models across 3 size categories
- 30 tasks across 5 categories
- 180 total test runs with complete metrics
- Realistic performance characteristics

## 🎨 Customization

- **Filters**: Use sidebar to focus on specific models/categories
- **Export**: Download data and visualizations
- **Analysis**: Explore different efficiency metrics
- **Recommendations**: Get AI-powered insights

## 📱 Mobile Friendly

The dashboard is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones
- Different screen sizes

## 🆘 Need Help?

1. Check `README.md` for detailed documentation
2. Review `PROJECT_OVERVIEW.md` for complete setup
3. Use sample data to test functionality
4. Export data for external analysis

---

**Ready to start benchmarking? Launch the dashboard and explore! 🎉**
