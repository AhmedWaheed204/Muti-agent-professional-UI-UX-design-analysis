# AI Design Analysis Platform 🎨🤖  
**Multi-agent system for professional UI/UX design analysis using Gemini AI**

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🌟 Features

### Triple Agent Architecture
- 🖼️ **Visual Design Analyzer**: Identifies design elements, patterns, and visual hierarchy
- 👥 **UX Flow Inspector**: Evaluates user flows, interactions, and accessibility
- 📈 **Market Intelligence Engine**: Provides market trends and competitor insights

### Multi-modal Analysis
- Combines **image analysis**, **text prompts**, and **market data**

### Professional Reporting
- Markdown-formatted insights
- Actionable design recommendations

### Competitor Benchmarking
- Side-by-side design comparisons
- Market positioning analysis

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- [Gemini API Key](https://aistudio.google.com/app/apikey)

### Installation
```bash
git clone https://github.com/yourusername/design-analysis-platform.git
cd design-analysis-platform
```

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
```bash
pip install -r requirements.txt
cp .env.example .env
```

Edit .env file:
```bash
GEMINI_API_KEY=your_actual_api_key_here
```

Running the Application
```bash
streamlit run app/main.py
```