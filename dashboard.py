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
    "Small": "#12b886",
    "Medium": "#4dabf7",
    "Large": "#ff6b6b",
}


st.set_page_config(
    page_title="Compar'IA | Sustainable LLM Dashboard",
    page_icon="IA",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        :root {
            --comparia-bg: #0b1020;
            --comparia-card: #111827;
            --comparia-soft: #1f2937;
            --comparia-text: #f8fafc;
            --comparia-muted: #94a3b8;
            --comparia-green: #12b886;
            --comparia-blue: #4dabf7;
            --comparia-red: #ff6b6b;
        }
        .block-container {
            padding-top: 1.2rem;
            padding-bottom: 2.4rem;
        }
        .hero {
            background: radial-gradient(circle at top left, rgba(18,184,134,.28), transparent 30%),
                        linear-gradient(135deg, #0f172a 0%, #111827 52%, #0b1020 100%);
            border: 1px solid rgba(148,163,184,.18);
            border-radius: 28px;
            padding: 28px 30px;
            margin-bottom: 20px;
            box-shadow: 0 22px 50px rgba(15,23,42,.18);
        }
        .hero h1 {
            color: #f8fafc;
            font-size: 3.1rem;
            line-height: 1.02;
            margin: 0;
            letter-spacing: -0.06em;
        }
        .hero p {
            color: #cbd5e1;
            max-width: 880px;
            margin: 12px 0 0 0;
            font-size: 1.05rem;
        }
        .pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 18px;
        }
        .pill {
            color: #d1fae5;
            background: rgba(18,184,134,.12);
            border: 1px solid rgba(18,184,134,.38);
            border-radius: 999px;
            padding: 6px 12px;
            font-size: .82rem;
            font-weight: 650;
        }
        .metric-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 20px;
            padding: 18px 18px 14px 18px;
            min-height: 120px;
            box-shadow: 0 10px 25px rgba(15,23,42,.05);
        }
        .metric-label {
            color: #64748b;
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .05em;
            text-transform: uppercase;
        }
        .metric-value {
            color: #0f172a;
            font-size: 2rem;
            font-weight: 800;
            margin-top: 6px;
        }
        .metric-help {
            color: #64748b;
            font-size: .8rem;
            margin-top: 4px;
        }
        .novelty-card {
            background: linear-gradient(135deg, #ecfeff 0%, #f0fdf4 100%);
            border: 1px solid #a7f3d0;
            border-radius: 18px;
            padding: 18px;
            margin-top: 10px;
        }
        .novelty-card h4 {
            color: #064e3b;
            margin: 0 0 8px 0;
        }
        .novelty-card p, .novelty-card li {
            color: #155e75;
            font-size: .94rem;
        }
        div[data-testid="stMetricValue"] {
            font-weight: 800;
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


def metric_card(label: str, value: str, help_text: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-help">{help_text}</div>
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


def render_recommendation_card(title: str, row: pd.Series) -> None:
    st.markdown(
        f"""
        <div class="novelty-card">
            <h4>{title}: {row['Model']}</h4>
            <p>
                Score <b>{row['Sustainability_Score']:.2f}</b> | Quality <b>{row['Quality_Score_mean']:.2f}</b> |
                Energy <b>{row['Energy_kWh_mean']:.3f} kWh</b> | Latency <b>{row['Latency_sec_mean']:.2f}s</b>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


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

    st.markdown(
        """
        <div class="hero">
            <h1>Compar'IA Sustainability Dashboard</h1>
            <p>
                A modern multi-objective benchmarking interface for choosing large language models
                by quality, latency, energy, CO2, and cost rather than by accuracy alone.
            </p>
            <div class="pill-row">
                <span class="pill">Sustainability matrix</span>
                <span class="pill">Normalized score</span>
                <span class="pill">CO2-aware ranking</span>
                <span class="pill">Extensible to new LLMs</span>
                <span class="pill">Exportable evidence</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.title("Controls")
    st.sidebar.caption(source_message)

    available_sizes = [size for size in SIZE_ORDER if size in set(base_metrics["Model_Size"].astype(str))]
    selected_sizes = st.sidebar.multiselect("Model size", available_sizes, default=available_sizes)
    available_models = sorted(base_metrics.loc[base_metrics["Model_Size"].astype(str).isin(selected_sizes), "Model"].map(clean_model_name).unique())
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

    st.sidebar.divider()
    st.sidebar.subheader("Composite score weights")
    weight_quality = st.sidebar.slider("Quality", 0.0, 1.0, 0.40, 0.05)
    weight_energy = st.sidebar.slider("Energy efficiency", 0.0, 1.0, 0.25, 0.05)
    weight_cost = st.sidebar.slider("Cost efficiency", 0.0, 1.0, 0.15, 0.05)
    weight_speed = st.sidebar.slider("Speed efficiency", 0.0, 1.0, 0.20, 0.05)
    weights = {
        "quality": weight_quality,
        "energy": weight_energy,
        "cost": weight_cost,
        "speed": weight_speed,
    }

    metrics = prepare_metrics(base_metrics, weights)
    if metrics.empty:
        st.warning("No model-level metrics available after filtering.")
        return

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        metric_card("Models", f"{metrics['Model'].nunique()}", "Compared in the current filter")
    with col2:
        metric_card("Best score", f"{metrics['Sustainability_Score'].max():.2f}", "Normalized multi-objective score")
    with col3:
        metric_card("Lowest energy", f"{metrics['Energy_kWh_mean'].min():.2f}", "Mean kWh per task")
    with col4:
        metric_card("Average CO2", f"{metrics['CO2_kg_mean'].mean():.2f}", "Mean kg CO2e per task")

    tabs = st.tabs(
        [
            "Sustainability Matrix",
            "Dashboard Insights",
            "Recommendations",
            "Data & Extensibility",
        ]
    )

    with tabs[0]:
        st.subheader("Quality, footprint, and latency in one view")
        st.plotly_chart(build_matrix(metrics), use_container_width=True)
        st.markdown(
            """
            <div class="novelty-card">
                <h4>What is novel here?</h4>
                <p>
                    Standard leaderboards usually sort by quality alone. Compar'IA instead places quality,
                    energy, CO2, latency, and cost in a shared decision interface. This makes it possible
                    to see when a lower-footprint model is nearly as useful as a larger model.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with tabs[1]:
        left, right = st.columns([1.1, 0.9])
        with left:
            st.plotly_chart(build_parallel_coordinates(metrics), use_container_width=True)
        with right:
            st.plotly_chart(build_metric_heatmap(metrics), use_container_width=True)

        st.subheader("Ranking")
        st.plotly_chart(build_ranking_chart(metrics), use_container_width=True)

    with tabs[2]:
        st.subheader("Automatic model-selection recommendations")
        recommendations = build_recommendations(metrics)
        rec_cols = st.columns(2)
        for i, (title, row) in enumerate(recommendations.items()):
            with rec_cols[i % 2]:
                render_recommendation_card(title, row)

        st.info(
            "Cost recommendations are shown only when non-zero cost measurements are present. "
            "If costs are placeholders, the score is automatically reweighted over the valid components."
        )

    with tabs[3]:
        st.subheader("Extensible benchmark table")
        display_cols = [
            "Model",
            "Model_Size",
            "Quality_Score_mean",
            "Latency_sec_mean",
            "Energy_kWh_mean",
            "CO2_kg_mean",
            "Cost_EUR_mean",
            "Quality_Efficiency",
            "Speed_Efficiency",
            "Sustainability_Score",
            "Footprint_Index",
            "Operational_Readiness",
        ]
        existing_cols = [col for col in display_cols if col in metrics.columns]
        st.dataframe(
            metrics[existing_cols].round(4),
            use_container_width=True,
            hide_index=True,
        )

        st.markdown(
            """
            <div class="novelty-card">
                <h4>How it expands over time</h4>
                <ul>
                    <li>Add a newly released LLM by adding rows to the CSV template.</li>
                    <li>Add task domains by introducing new task-category labels.</li>
                    <li>Add sustainability metrics such as water usage, memory footprint, or regional carbon intensity as new columns.</li>
                    <li>Export filtered results for papers, reports, and institutional procurement decisions.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        csv = metrics[existing_cols].to_csv(index=False).encode("utf-8")
        st.download_button(
            "Download filtered metrics CSV",
            data=csv,
            file_name="comparia_sustainability_metrics.csv",
            mime="text/csv",
        )


if __name__ == "__main__":
    main()
