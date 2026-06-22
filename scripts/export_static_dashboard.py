#!/usr/bin/env python3
"""Regenerate comparia_dashboard.html embedded data from dashboard.py scoring."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dashboard import load_aggregated_data, prepare_metrics  # noqa: E402

DEFAULT_WEIGHTS = {"quality": 0.40, "energy": 0.25, "cost": 0.15, "speed": 0.20}


def export_records(metrics: pd.DataFrame) -> list[dict]:
    ranked = metrics.copy()
    ranked["Rank"] = ranked["Sustainability_Score"].rank(ascending=False, method="first").astype(int)
    records: list[dict] = []
    for _, row in ranked.sort_values("Sustainability_Score", ascending=False).iterrows():
        records.append(
            {
                "Model": row["Model"],
                "Model_Size": str(row["Model_Size"]),
                "Quality_Score_mean": round(float(row["Quality_Score_mean"]), 3),
                "Latency_sec_mean": round(float(row["Latency_sec_mean"]), 3),
                "Energy_kWh_mean": round(float(row["Energy_kWh_mean"]), 3),
                "CO2_kg_mean": round(float(row["CO2_kg_mean"]), 3),
                "Cost_EUR_mean": round(float(row.get("Cost_EUR_mean", 0) or 0), 4),
                "QualityEfficiency": round(float(row["Quality_Efficiency"]), 4),
                "SpeedEfficiency": round(float(row["Speed_Efficiency"]), 4),
                "QualityNorm": round(float(row["Quality_norm"]), 4),
                "EnergyEffNorm": round(float(row["EnergyEfficiency_norm"]), 4),
                "SpeedEffNorm": round(float(row["SpeedEfficiency_norm"]), 4),
                "LowEnergyNorm": round(float(row["LowEnergy_norm"]), 4),
                "LowCO2Norm": round(float(row["LowCO2_norm"]), 4),
                "LowLatencyNorm": round(float(row["LowLatency_norm"]), 4),
                "FootprintIndex": round(float(row["Footprint_Index"]), 4),
                "SustainabilityScore": round(float(row["Sustainability_Score"]), 4),
                "Rank": int(row["Rank"]),
            }
        )
    return records


def patch_html(html_path: Path, records: list[dict]) -> str:
    content = html_path.read_text(encoding="utf-8")
    payload = json.dumps(records, separators=(",", ":"))
    updated, count = re.subn(r"const data = \[.*?\];", f"const data = {payload};", content, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Could not patch embedded data in {html_path}")
    return updated


def main() -> None:
    aggregated_df, message = load_aggregated_data()
    if aggregated_df is None:
        raise SystemExit(message)

    metrics = prepare_metrics(aggregated_df, DEFAULT_WEIGHTS)
    records = export_records(metrics)

    html_source = ROOT / "comparia_dashboard.html"
    patched = patch_html(html_source, records)
    html_source.write_text(patched, encoding="utf-8")

    docs_index = ROOT / "docs" / "index.html"
    docs_index.write_text(patched, encoding="utf-8")

    print(f"Updated {html_source.name} and docs/index.html ({len(records)} models)")
    print(f"Top model: {records[0]['Model']} (score {records[0]['SustainabilityScore']})")


if __name__ == "__main__":
    main()
