"""
Split Valmiki Ramayana JSON Dataset by Kanda.

This script reads the complete Valmiki Ramayana JSON dataset using pandas and json,
then splits it into individual JSON files for each of the 7 Kandas in canonical order.
"""

import os
import sys
import json
import pandas as pd

# Ensure console output supports Unicode on Windows terminals
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Canonical order of Valmiki Ramayana Kandas
KANDAS_ORDER = [
    (1, "Bala Kanda", "01_Bala_Kanda.json"),
    (2, "Ayodhya Kanda", "02_Ayodhya_Kanda.json"),
    (3, "Aranya Kanda", "03_Aranya_Kanda.json"),
    (4, "Kishkindha Kanda", "04_Kishkindha_Kanda.json"),
    (5, "Sundara Kanda", "05_Sundara_Kanda.json"),
    (6, "Yuddha Kanda", "06_Yuddha_Kanda.json"),
    (7, "Uttara Kanda", "07_Uttara_Kanda.json"),
]

def split_dataset(
    input_file: str = "data/Valmiki_Ramayan_Shlokas.json",
    output_dir: str = "data/kandas",
):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    os.makedirs(output_dir, exist_ok=True)
    print(f"📖 Loading complete dataset from: {input_file}")

    # Load with pandas
    df = pd.read_json(input_file)
    total_records = len(df)
    print(f"✅ Successfully loaded {total_records:,} shlokas into DataFrame.\n")

    summary = []
    total_written = 0

    print("✂️  Splitting into individual Kanda files...")
    print("-" * 75)
    print(f"{'#':<3} {'Kanda Name':<20} {'Sargas':<8} {'Shlokas':<10} {'File Name':<25}")
    print("-" * 75)

    for order, kanda_name, filename in KANDAS_ORDER:
        # Filter dataframe for this kanda
        kanda_df = df[df["kanda"] == kanda_name]
        shloka_count = len(kanda_df)
        sarga_count = kanda_df["sarga"].nunique()
        total_written += shloka_count

        # Convert to records (preserving None / null for empty comments)
        records = (
            kanda_df.replace({float("nan"): None})
            .to_dict(orient="records")
        )

        out_path = os.path.join(output_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)

        file_size_mb = os.path.getsize(out_path) / (1024 * 1024)

        summary.append({
            "order": order,
            "kanda": kanda_name,
            "sargas": sarga_count,
            "shlokas": shloka_count,
            "filename": filename,
            "size_mb": round(file_size_mb, 2),
        })

        print(f"{order:<3} {kanda_name:<20} {sarga_count:<8} {shloka_count:<10,} {filename:<25} ({file_size_mb:.2f} MB)")

    print("-" * 75)
    print(f"Total Shlokas Written: {total_written:,} / {total_records:,}")

    # Integrity verification
    assert total_written == total_records, (
        f"Mismatch: written {total_written} vs total {total_records}"
    )
    print("🎉 All 7 Kanda files created and verified successfully!\n")

    return summary


if __name__ == "__main__":
    split_dataset()
