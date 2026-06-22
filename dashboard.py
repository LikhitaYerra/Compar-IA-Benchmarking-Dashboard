from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


APP_TITLE = "Compar'IA"
DATA_FILES = (
    "data_collection_results.csv",
    "data_collection_template.csv",
)
AGGREGATED_DATA_FILE = "comparai_metrics_detailed.csv"
SIZE_ORDER = ["Small", "Medium", "Large"]
SIZE_COLORS = {
    "Small": "#10b981",
    "Medium": "#38bdf8",
    "Large": "#f43f5e",
}
PAGES_URL = "https://likhitayerra.github.io/Compar-IA-Benchmarking-Dashboard/"


st.set_page_config(
    page_title="Compar'IA | Sustainable LLM Dashboard",
    page_icon="IA",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
        html, body, [class*="css"] {
            font-family: 'Inter', system-ui, sans-serif;
        }
        .stApp {
            background: linear-gradient(180deg, #050a17 0, #050a17 180px, #f1f5f9 180px, #f1f5f9 100%);
        }
        header[data-testid="stHeader"] {
            background: rgba(5, 10, 23, 0.92);
        }
        .block-container {
            padding-top: 0.8rem;
            padding-bottom: 2.4rem;
            max-width: 1280px;
        }
        .comparia-topbar {
            background: rgba(5, 10, 23, 0.92);
            border: 1px solid rgba(148,163,184,.18);
            border-radius: 16px;
            padding: 12px 18px;
            margin-bottom: 18px;
            color: #e2e8f0;
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .comparia-mark {
            width: 30px; height: 30px; border-radius: 9px;
            background: conic-gradient(from 220deg, #10b981, #38bdf8, #818cf8, #10b981);
            display: inline-flex; align-items: center; justify-content: center;
            color: #0b1220; font-weight: 900; font-size: 0.72rem;
        }
        .comparia-brand { font-weight: 800; letter-spacing: -.04em; font-size: 1.1rem; }
        .hero-wrap {
            color: #f8fafc;
            padding: 8px 0 20px 0;
        }
        .hero-kicker {
            color: #99f6e4;
            font-weight: 700;
            letter-spacing: .14em;
            text-transform: uppercase;
            font-size: .78rem;
        }
        .hero-title {
            font-size: clamp(1.8rem, 3.6vw, 2.8rem);
            letter-spacing: -.06em;
            line-height: 1.05;
            margin: 8px 0 12px 0;
            color: #f8fafc;
        }
        .hero-copy { color: #cbd5e1; font-size: 1rem; max-width: 720px; }
        .pill-row { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 14px; }
        .pill {
            font-size: .78rem; padding: 6px 12px; border-radius: 999px;
            border: 1px solid rgba(16,185,129,.45); color: #d1fae5;
            background: rgba(16,185,129,.12); font-weight: 600;
        }
        .stat {
            background: rgba(15,23,42,.6);
            border: 1px solid rgba(148,163,184,.22);
            border-radius: 18px;
            padding: 14px 16px;
            color: #e2e8f0;
            min-height: 92px;
        }
        .stat-label {
            color: #94a3b8; text-transform: uppercase; font-size: .68rem;
            letter-spacing: .12em; font-weight: 700;
        }
        .stat-value {
            font-size: 1.55rem; font-weight: 800; letter-spacing: -.04em; margin-top: 4px;
        }
        .stat-meta { color: #94a3b8; font-size: .82rem; margin-top: 2px; }
        .panel-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 22px;
            padding: 18px 20px;
            box-shadow: 0 18px 45px rgba(15, 23, 42, .08);
            margin-bottom: 12px;
        }
        .panel-card h3 {
            margin: 0 0 4px 0;
            font-size: 1.05rem;
            color: #0f172a;
        }
        .panel-desc { color: #64748b; font-size: .88rem; margin-bottom: 10px; }
        .control-bar {
            display: flex; flex-wrap: wrap; gap: 14px; align-items: center;
            background: white; border: 1px solid #e5e7eb; border-radius: 18px;
            padding: 14px 18px; margin-bottom: 14px;
            box-shadow: 0 18px 45px rgba(15, 23, 42, .08);
        }
        .rec-card {
            border-radius: 18px; padding: 18px 20px; margin-bottom: 10px;
        }
        .rec-green { background: linear-gradient(135deg, #ecfdf5 0%, #f0fdfa 100%); border: 1px solid #d1fae5; }
        .rec-blue  { background: linear-gradient(135deg, #eff6ff 0%, #ecfeff 100%); border: 1px solid #bae6fd; }
        .rec-amber { background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%); border: 1px solid #fcd34d; }
        .rec-purple{ background: linear-gradient(135deg, #fdf4ff 0%, #fce7f3 100%); border: 1px solid #f5d0fe; }
        .rec-title { color: #047857; font-size: .78rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; }
        .rec-model { color: #0f172a; font-size: 1.35rem; font-weight: 800; margin: 6px 0; }
        .rec-meta { color: #334155; font-size: .88rem; }
        .size-badge {
            display: inline-block; padding: 4px 10px; border-radius: 999px;
            font-size: .74rem; font-weight: 700; margin-bottom: 8px;
        }
        .badge-small { background: #ecfdf5; color: #047857; border: 1px solid #a7f3d0; }
        .badge-medium { background: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; }
        .badge-large { background: #fef2f2; color: #b91c1c; border: 1px solid #fecaca; }
        div[data-testid="stTabs"] button[data-baseweb="tab"] {
            font-weight: 600;
        }
        section[data-testid="stSidebar"] {
            background: #0b1220;
            color: #e2e8f0;
        }
        section[data-testid="stSidebar"] * {
            color: #e2e8f0 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def clean_model_name(name: str) -> str:
    return (
        str(name)
        .replace("Meta LLaMA 3.1 8B", "LLaMA 3.1 8B")
        .replace("GPT-OSS 20B", "GPT-OSS 20B")
    )


def safe_divide(numerator: pd.Series, denominator: pd.Series) -> pd.Series:
    denominator = denominator.replace({0: np.nan})
    return numerator / denominator


def minmax(series: pd.Series, higher_is_better: bool = True) -> pd.Series:
    values = pd.to_numeric(series, errors="coerce").replace([np.inf, -np.inf], np.nan)
    if not higher_is_better:
        values = -values
    min_value = values.min(skipna=True)
    max_value = values.max(skipna=True)
    if pd.isna(min_value) or pd.isna(max_value) or max_value == min_value:
        return pd.Series(0.5, index=series.index)
    return (values - min_value) / (max_value - min_value)


def create_sample_data(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    models = [
        ("LLaMA 3.1 8B", "Small"),
        ("Gemma 8B", "Small"),
        ("Mistral Small", "Medium"),
        ("GPT-OSS 20B", "Medium"),
        ("GPT-5", "Large"),
        ("DeepSeek R1", "Large"),
    ]
    categories = [
        "Factual & Rewriting",
        "Reasoning & Quantitative",
        "Programming & Debugging",
        "Knowledge & Synthesis",
        "Advanced & Creative",
    ]

    rows = []
    for task_id in range(1, 31):
        category = categories[min((task_id - 1) // 6, len(categories) - 1)]
        difficulty = 1.0 + (0.1 if task_id > 20 else 0.0)

        for model, size in models:
            if size == "Small":
                quality, latency, energy, cost = 3.7, 2.6, 0.16, 0.02
            elif size == "Medium":
                quality, latency, energy, cost = 4.1, 4.4, 0.34, 0.08
            else:
                quality, latency, energy, cost = 4.45, 6.8, 0.88, 0.26

            rows.append(
                {
                    "Task_ID": task_id,
                    "Task_Category": category,
                    "Model": model,
                    "Model_Size": size,
                    "Quality_Score": np.clip(rng.normal(quality, 0.45) / difficulty, 1, 5),
                    "Latency_sec": max(0.2, rng.normal(latency * difficulty, latency * 0.18)),
                    "Energy_kWh": max(0.01, rng.normal(energy * difficulty, energy * 0.18)),
                    "CO2_kg": max(0.005, rng.normal(energy * difficulty * 0.45, energy * 0.08)),
                    "Cost_EUR": max(0.001, rng.normal(cost * difficulty, cost * 0.16)),
                    "Notes": "Synthetic demonstration row",
                }
            )
    return pd.DataFrame(rows)


def load_raw_data() -> tuple[pd.DataFrame | None, str]:
    for file_name in DATA_FILES:
        path = Path(file_name)
        if path.exists():
            df = pd.read_csv(path)
            if "Quality_Score" in df.columns and not df["Quality_Score"].isna().all():
                return df, f"Loaded raw task-level data from {file_name}"

    return None, "No populated task-level CSV found"


def load_aggregated_data() -> tuple[pd.DataFrame | None, str]:
    path = Path(AGGREGATED_DATA_FILE)
    if not path.exists():
        return None, f"{AGGREGATED_DATA_FILE} not found"

    metrics = pd.read_csv(path)
    required = {"Model", "Model_Size", "Quality_Score_mean", "Latency_sec_mean", "Energy_kWh_mean", "CO2_kg_mean"}
    if required.issubset(metrics.columns):
        return metrics, f"Loaded aggregated metrics from {AGGREGATED_DATA_FILE}"
    return None, f"{AGGREGATED_DATA_FILE} is missing required columns"


def infer_model_size(model: str) -> str:
    model = str(model)
    if "8B" in model or "Gemma" in model:
        return "Small"
    if "Small" in model or "20B" in model or "Mistral" in model:
        return "Medium"
    return "Large"


def standardize_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    column_aliases = {
        "Quality (1-5)": "Quality_Score",
        "Latency (sec)": "Latency_sec",
        "Energy": "Energy_kWh",
        "co2": "CO2_kg",
        "Prompt Category": "Task_Category",
        "Task ID": "Task_ID",
    }
    df = df.rename(columns={old: new for old, new in column_aliases.items() if old in df.columns})
    if "Model_Size" not in df.columns:
        df["Model_Size"] = df["Model"].apply(infer_model_size)
    if "Cost_EUR" not in df.columns:
        df["Cost_EUR"] = np.nan
    if "Task_Category" not in df.columns:
        df["Task_Category"] = "Uncategorized"
    for col in ["Quality_Score", "Latency_sec", "Energy_kWh", "CO2_kg", "Cost_EUR"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["Model", "Quality_Score", "Latency_sec", "Energy_kWh"])


def aggregate_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_raw_data(df)
    metrics = (
        df.groupby(["Model", "Model_Size"], dropna=False)
        .agg(
            Quality_Score_mean=("Quality_Score", "mean"),
            Quality_Score_std=("Quality_Score", "std"),
            Quality_Score_count=("Quality_Score", "count"),
            Latency_sec_mean=("Latency_sec", "mean"),
            Latency_sec_std=("Latency_sec", "std"),
            Energy_kWh_mean=("Energy_kWh", "mean"),
            Energy_kWh_sum=("Energy_kWh", "sum"),
            CO2_kg_mean=("CO2_kg", "mean"),
            CO2_kg_sum=("CO2_kg", "sum"),
            Cost_EUR_mean=("Cost_EUR", "mean"),
            Cost_EUR_sum=("Cost_EUR", "sum"),
        )
        .reset_index()
    )
    return metrics


def prepare_metrics(metrics: pd.DataFrame, weights: dict[str, float]) -> pd.DataFrame:
    metrics = metrics.copy()
    metrics["Model"] = metrics["Model"].map(clean_model_name)
    metrics["Model_Size"] = pd.Categorical(metrics["Model_Size"], SIZE_ORDER, ordered=True)

    for col in [
        "Quality_Score_mean",
        "Latency_sec_mean",
        "Energy_kWh_mean",
        "CO2_kg_mean",
        "Cost_EUR_mean",
        "Quality_Efficiency",
        "Cost_Efficiency",
        "Speed_Efficiency",
    ]:
        if col in metrics.columns:
            metrics[col] = pd.to_numeric(metrics[col], errors="coerce").replace([np.inf, -np.inf], np.nan)

    metrics["Quality_Efficiency"] = metrics.get(
        "Quality_Efficiency",
        safe_divide(metrics["Quality_Score_mean"], metrics["Energy_kWh_mean"]),
    )
    metrics["Speed_Efficiency"] = metrics.get(
        "Speed_Efficiency",
        safe_divide(metrics["Quality_Score_mean"], metrics["Latency_sec_mean"]),
    )
    if "Cost_EUR_mean" in metrics.columns:
        metrics["Cost_Efficiency"] = safe_divide(metrics["Quality_Score_mean"], metrics["Cost_EUR_mean"])
    else:
        metrics["Cost_EUR_mean"] = np.nan
        metrics["Cost_Efficiency"] = np.nan

    metrics["Quality_norm"] = minmax(metrics["Quality_Score_mean"])
    metrics["EnergyEfficiency_norm"] = minmax(metrics["Quality_Efficiency"])
    metrics["CostEfficiency_norm"] = minmax(metrics["Cost_Efficiency"])
    metrics["SpeedEfficiency_norm"] = minmax(metrics["Speed_Efficiency"])
    metrics["LowEnergy_norm"] = minmax(metrics["Energy_kWh_mean"], higher_is_better=False)
    metrics["LowCO2_norm"] = minmax(metrics["CO2_kg_mean"], higher_is_better=False)
    metrics["LowLatency_norm"] = minmax(metrics["Latency_sec_mean"], higher_is_better=False)

    components = {
        "Quality_norm": weights["quality"],
        "EnergyEfficiency_norm": weights["energy"],
        "CostEfficiency_norm": weights["cost"],
        "SpeedEfficiency_norm": weights["speed"],
    }
    numerator = pd.Series(0.0, index=metrics.index)
    denominator = pd.Series(0.0, index=metrics.index)
    for col, weight in components.items():
        valid = metrics[col].notna()
        numerator = numerator.add(metrics[col].where(valid, 0) * weight, fill_value=0)
        denominator = denominator.add(valid.astype(float) * weight, fill_value=0)

    metrics["Sustainability_Score"] = safe_divide(numerator, denominator).fillna(0)
    metrics["Footprint_Index"] = (0.55 * metrics["LowEnergy_norm"] + 0.45 * metrics["LowCO2_norm"]).fillna(0)
    metrics["Operational_Readiness"] = (
        0.45 * metrics["Quality_norm"] + 0.35 * metrics["LowLatency_norm"] + 0.20 * metrics["Footprint_Index"]
    ).fillna(0)

    return metrics.sort_values("Sustainability_Score", ascending=False).reset_index(drop=True)


def render_topbar() -> None:
    st.markdown(
        """
        <div class="comparia-topbar">
            <span class="comparia-mark">IA</span>
            <span class="comparia-brand">Compar'IA</span>
            <span style="margin-left:auto;color:#94a3b8;font-size:.85rem;">
                Sustainable LLM benchmarking dashboard
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero(metrics: pd.DataFrame) -> None:
    left, right = st.columns([1.5, 1])
    with left:
        st.markdown(
            """
            <div class="hero-wrap">
                <div class="hero-kicker">Sustainability-Aware LLM Benchmarking</div>
                <div class="hero-title">Choose LLMs that balance quality with energy, CO₂, latency and cost.</div>
                <div class="hero-copy">
                    Compar'IA replaces accuracy-only leaderboards with an interactive interface that links
                    task quality to operational and environmental footprint.
                </div>
                <div class="pill-row">
                    <span class="pill">Sustainability Matrix</span>
                    <span class="pill">Normalized Multi-Metric Score</span>
                    <span class="pill">CO₂-Aware Recommendations</span>
                    <span class="pill">Extensible Schema</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        stats = [
            ("Models", f"{metrics['Model'].nunique()}", "in current dataset"),
            ("Avg quality", f"{metrics['Quality_Score_mean'].mean():.2f}/5", "across all tasks"),
            ("Avg energy", f"{metrics['Energy_kWh_mean'].mean():.2f} kWh", "per task"),
            ("Avg CO₂", f"{metrics['CO2_kg_mean'].mean():.2f} kg", "per task"),
        ]
        r1c1, r1c2 = st.columns(2)
        r2c1, r2c2 = st.columns(2)
        for col, (label, value, meta) in zip([r1c1, r1c2, r2c1, r2c2], stats):
            with col:
                st.markdown(
                    f"""
                    <div class="stat">
                        <div class="stat-label">{label}</div>
                        <div class="stat-value">{value}</div>
                        <div class="stat-meta">{meta}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )


def size_badge_class(size: str) -> str:
    return {"Small": "badge-small", "Medium": "badge-medium", "Large": "badge-large"}.get(str(size), "badge-medium")


def render_top_model_card(row: pd.Series) -> None:
    badge = size_badge_class(row["Model_Size"])
    st.markdown(
        f"""
        <div class="panel-card">
            <h3>Top model overall</h3>
            <div class="panel-desc">Best balanced choice under the current weights.</div>
            <div class="rec-model">{row['Model']}</div>
            <span class="size-badge {badge}">{row['Model_Size']}</span>
            <div class="rec-meta" style="margin-top:10px;">
                Score <b>{row['Sustainability_Score']:.2f}</b> ·
                Quality <b>{row['Quality_Score_mean']:.2f}</b><br>
                Energy <b>{row['Energy_kWh_mean']:.2f} kWh</b> ·
                Latency <b>{row['Latency_sec_mean']:.1f}s</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def build_energy_bar(metrics: pd.DataFrame) -> go.Figure:
    ordered = metrics.sort_values("Energy_kWh_mean")
    fig = px.bar(
        ordered,
        x="Energy_kWh_mean",
        y="Model",
        orientation="h",
        color="Model_Size",
        color_discrete_map=SIZE_COLORS,
        text=ordered["Energy_kWh_mean"].map(lambda x: f"{x:.2f}"),
        labels={"Energy_kWh_mean": "kWh per task", "Model": ""},
        title="Energy footprint by model",
    )
    fig.update_layout(height=320, template="plotly_white", margin=dict(l=20, r=20, t=50, b=20), showlegend=False)
    fig.update_traces(textposition="outside")
    return fig


def build_latency_bar(metrics: pd.DataFrame) -> go.Figure:
    ordered = metrics.sort_values("Latency_sec_mean")
    fig = px.bar(
        ordered,
        x="Latency_sec_mean",
        y="Model",
        orientation="h",
        color="Model_Size",
        color_discrete_map=SIZE_COLORS,
        text=ordered["Latency_sec_mean"].map(lambda x: f"{x:.1f}"),
        labels={"Latency_sec_mean": "seconds per task", "Model": ""},
        title="Latency by model",
    )
    fig.update_layout(height=320, template="plotly_white", margin=dict(l=20, r=20, t=50, b=20), showlegend=False)
    fig.update_traces(textposition="outside")
    return fig


def render_recommendation_card(title: str, row: pd.Series, style: str) -> None:
    badge = size_badge_class(row["Model_Size"])
    st.markdown(
        f"""
        <div class="rec-card {style}">
            <div class="rec-title">{title}</div>
            <div class="rec-model">{row['Model']}</div>
            <span class="size-badge {badge}">{row['Model_Size']}</span>
            <div class="rec-meta">
                Score <b>{row['Sustainability_Score']:.2f}</b> ·
                Quality <b>{row['Quality_Score_mean']:.2f}</b> ·
                Energy <b>{row['Energy_kWh_mean']:.2f} kWh</b> ·
                Latency <b>{row['Latency_sec_mean']:.1f}s</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, help_text: str) -> None:
    st.markdown(
        f"""
        <div class="stat" style="background:#fff;color:#0f172a;border-color:#e5e7eb;">
            <div class="stat-label" style="color:#64748b;">{label}</div>
            <div class="stat-value" style="color:#0f172a;">{value}</div>
            <div class="stat-meta" style="color:#64748b;">{help_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def build_matrix(metrics: pd.DataFrame) -> go.Figure:
    fig = px.scatter(
        metrics,
        x="Energy_kWh_mean",
        y="Quality_Score_mean",
        size="Latency_sec_mean",
        color="Model_Size",
        text="Model",
        color_discrete_map=SIZE_COLORS,
        hover_data={
            "Sustainability_Score": ":.2f",
            "Energy_kWh_mean": ":.3f",
            "CO2_kg_mean": ":.3f",
            "Latency_sec_mean": ":.2f",
            "Cost_EUR_mean": ":.4f",
        },
        labels={
            "Energy_kWh_mean": "Mean energy per task (kWh)",
            "Quality_Score_mean": "Mean quality score (1-5)",
            "Model_Size": "Size class",
        },
        title="Sustainability Matrix: quality vs footprint",
    )
    fig.update_traces(textposition="top center", marker=dict(line=dict(width=1, color="white"), opacity=0.82))
    fig.add_vline(x=metrics["Energy_kWh_mean"].median(), line_dash="dash", line_color="#94a3b8")
    fig.add_hline(y=metrics["Quality_Score_mean"].median(), line_dash="dash", line_color="#94a3b8")
    fig.update_layout(
        height=560,
        template="plotly_white",
        legend_title_text="Model size",
        margin=dict(l=20, r=20, t=70, b=20),
    )
    return fig


def build_parallel_coordinates(metrics: pd.DataFrame) -> go.Figure:
    plot_df = metrics.copy()
    plot_df["Size_Code"] = plot_df["Model_Size"].astype(str).map({"Small": 1, "Medium": 2, "Large": 3})
    fig = go.Figure(
        data=go.Parcoords(
            line=dict(
                color=plot_df["Sustainability_Score"],
                colorscale="Tealgrn",
                showscale=True,
                cmin=0,
                cmax=1,
                colorbar=dict(title="Score"),
            ),
            dimensions=[
                dict(label="Quality", values=plot_df["Quality_Score_mean"]),
                dict(label="Latency", values=plot_df["Latency_sec_mean"]),
                dict(label="Energy", values=plot_df["Energy_kWh_mean"]),
                dict(label="CO2", values=plot_df["CO2_kg_mean"]),
                dict(label="Footprint", values=plot_df["Footprint_Index"]),
                dict(label="Score", values=plot_df["Sustainability_Score"]),
            ],
        )
    )
    fig.update_layout(
        title="Sustainability signature across evaluation dimensions",
        height=430,
        template="plotly_white",
        margin=dict(l=30, r=30, t=60, b=25),
    )
    return fig


def build_ranking_chart(metrics: pd.DataFrame) -> go.Figure:
    ranking = metrics.sort_values("Sustainability_Score", ascending=True)
    fig = px.bar(
        ranking,
        x="Sustainability_Score",
        y="Model",
        orientation="h",
        color="Model_Size",
        color_discrete_map=SIZE_COLORS,
        text=ranking["Sustainability_Score"].map(lambda x: f"{x:.2f}"),
        title="Normalized sustainability-aware ranking",
        labels={"Sustainability_Score": "Composite score (0-1)", "Model": ""},
    )
    fig.update_layout(height=390, template="plotly_white", margin=dict(l=20, r=20, t=60, b=20))
    fig.update_traces(textposition="outside")
    return fig


def build_metric_heatmap(metrics: pd.DataFrame) -> go.Figure:
    heatmap_cols = [
        "Quality_norm",
        "EnergyEfficiency_norm",
        "SpeedEfficiency_norm",
        "Footprint_Index",
        "Operational_Readiness",
    ]
    z = metrics.set_index("Model")[heatmap_cols]
    fig = px.imshow(
        z,
        aspect="auto",
        color_continuous_scale="YlGnBu",
        zmin=0,
        zmax=1,
        text_auto=".2f",
        labels=dict(color="Normalized value"),
        title="Metric contribution heatmap",
    )
    fig.update_xaxes(
        ticktext=["Quality", "Energy eff.", "Speed eff.", "Low footprint", "Readiness"],
        tickvals=list(range(len(heatmap_cols))),
    )
    fig.update_layout(height=430, template="plotly_white", margin=dict(l=20, r=20, t=60, b=20))
    return fig


def build_recommendations(metrics: pd.DataFrame) -> dict[str, pd.Series]:
    recommendations = {
        "Best balanced model": metrics.loc[metrics["Sustainability_Score"].idxmax()],
        "Lowest energy footprint": metrics.loc[metrics["Energy_kWh_mean"].idxmin()],
        "Fastest response": metrics.loc[metrics["Latency_sec_mean"].idxmin()],
        "Highest quality": metrics.loc[metrics["Quality_Score_mean"].idxmax()],
    }
    if metrics["Cost_EUR_mean"].notna().any() and (metrics["Cost_EUR_mean"] > 0).any():
        recommendations["Lowest measured cost"] = metrics.loc[metrics["Cost_EUR_mean"].replace(0, np.nan).idxmin()]
    return recommendations


def main() -> None:
    raw_df, raw_message = load_raw_data()
    aggregated_df, aggregated_message = load_aggregated_data()

    if raw_df is not None:
        raw_df = standardize_raw_data(raw_df)
        base_metrics = aggregate_raw_data(raw_df)
        source_message = raw_message
    elif aggregated_df is not None:
        raw_df = None
        base_metrics = aggregated_df
        source_message = aggregated_message
    else:
        raw_df = create_sample_data()
        base_metrics = aggregate_raw_data(raw_df)
        source_message = "Using reproducible synthetic demonstration data"

    st.sidebar.title("Filters")
    st.sidebar.caption(source_message)
    st.sidebar.markdown(f"[Open static HTML version]({PAGES_URL})")

    available_sizes = [size for size in SIZE_ORDER if size in set(base_metrics["Model_Size"].astype(str))]
    selected_sizes = st.sidebar.multiselect("Model size", available_sizes, default=available_sizes)
    available_models = sorted(
        base_metrics.loc[base_metrics["Model_Size"].astype(str).isin(selected_sizes), "Model"]
        .map(clean_model_name)
        .unique()
    )
    selected_models = st.sidebar.multiselect("Models", available_models, default=available_models)

    if raw_df is not None and "Task_Category" in raw_df.columns:
        available_categories = sorted(raw_df["Task_Category"].dropna().astype(str).unique())
        selected_categories = st.sidebar.multiselect("Task categories", available_categories, default=available_categories)
        filtered_raw = raw_df[
            raw_df["Model"].map(clean_model_name).isin(selected_models)
            & raw_df["Model_Size"].astype(str).isin(selected_sizes)
            & raw_df["Task_Category"].astype(str).isin(selected_categories)
        ]
        if filtered_raw.empty:
            st.warning("No rows match the current filters.")
            return
        base_metrics = aggregate_raw_data(filtered_raw)
    else:
        base_metrics = base_metrics[
            base_metrics["Model"].map(clean_model_name).isin(selected_models)
            & base_metrics["Model_Size"].astype(str).isin(selected_sizes)
        ]

    default_weights = {"quality": 0.40, "energy": 0.25, "cost": 0.15, "speed": 0.20}
    metrics = prepare_metrics(base_metrics, default_weights)
    if metrics.empty:
        st.warning("No model-level metrics available after filtering.")
        return

    render_topbar()
    render_hero(metrics)

    tabs = st.tabs(["Overview", "Sustainability Matrix", "Insights", "Recommendations", "Data & Extensibility"])

    with tabs[0]:
        left, right = st.columns([1.6, 1])
        with left:
            st.markdown('<div class="panel-card"><h3>Sustainability Matrix</h3><div class="panel-desc">Quality vs energy with latency as marker size and size class as colour.</div></div>', unsafe_allow_html=True)
            st.plotly_chart(build_matrix(metrics), width="stretch", key="overview_matrix")
        with right:
            render_top_model_card(metrics.iloc[0])
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(build_energy_bar(metrics), width="stretch", key="overview_energy")
        with c2:
            st.plotly_chart(build_latency_bar(metrics), width="stretch", key="overview_latency")

    with tabs[1]:
        st.markdown('<div class="control-bar"><strong>Composite score weights</strong> — adjust and re-rank models</div>', unsafe_allow_html=True)
        w1, w2, w3, w4 = st.columns(4)
        with w1:
            weight_quality = st.slider("Quality", 0.0, 1.0, 0.40, 0.05, key="weight_quality")
        with w2:
            weight_energy = st.slider("Energy", 0.0, 1.0, 0.25, 0.05, key="weight_energy")
        with w3:
            weight_speed = st.slider("Speed", 0.0, 1.0, 0.20, 0.05, key="weight_speed")
        with w4:
            weight_cost = st.slider("Cost", 0.0, 1.0, 0.15, 0.05, key="weight_cost")
        weights = {"quality": weight_quality, "energy": weight_energy, "cost": weight_cost, "speed": weight_speed}
        metrics = prepare_metrics(base_metrics, weights)
        st.plotly_chart(build_matrix(metrics), width="stretch", key="matrix_main")

    with tabs[2]:
        left, right = st.columns(2)
        with left:
            st.plotly_chart(build_metric_heatmap(metrics), width="stretch", key="insights_heatmap")
        with right:
            st.plotly_chart(build_parallel_coordinates(metrics), width="stretch", key="insights_parallel")
        st.plotly_chart(build_ranking_chart(metrics), width="stretch", key="insights_ranking")

    with tabs[3]:
        recs = build_recommendations(metrics)
        styles = ["rec-green", "rec-green", "rec-blue", "rec-amber"]
        keys = list(recs.keys())[:4]
        row1 = st.columns(2)
        row2 = st.columns(2)
        for i, title in enumerate(keys):
            target = row1[i % 2] if i < 2 else row2[i - 2]
            with target:
                render_recommendation_card(title, recs[title], styles[i % len(styles)])
        st.info("Cost recommendations appear only when non-zero cost data is available.")

    with tabs[4]:
        display_cols = [
            "Model", "Model_Size", "Quality_Score_mean", "Latency_sec_mean",
            "Energy_kWh_mean", "CO2_kg_mean", "Cost_EUR_mean",
            "Sustainability_Score", "Footprint_Index",
        ]
        existing_cols = [col for col in display_cols if col in metrics.columns]
        st.dataframe(metrics[existing_cols].round(4), width="stretch", hide_index=True, key="data_table")
        st.markdown(
            """
            **Extending the dashboard**
            1. Add a row in the CSV template for each new model and task.
            2. Optionally add columns for water usage, regional carbon intensity, or memory footprint.
            3. Reload the app — aggregations, scoring, and recommendations recompute automatically.
            """
        )
        csv = metrics[existing_cols].to_csv(index=False).encode("utf-8")
        st.download_button(
            "Export CSV",
            data=csv,
            file_name="comparia_sustainability.csv",
            mime="text/csv",
            key="export_csv",
        )

    st.caption(f"Static HTML mirror: {PAGES_URL}")


if __name__ == "__main__":
    main()
