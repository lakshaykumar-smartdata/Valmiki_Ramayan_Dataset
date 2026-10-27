"""
Split Valmiki Ramayana JSON Dataset by Sarga (Chapter/Canto).

This script reads the complete Valmiki Ramayana JSON dataset using pandas and json,
then breaks down each Kanda into individual JSON files for every Sarga (648 total sargas),
preserving UTF-8 Devanagari text, transliteration, and English meanings.
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

KANDAS_INFO = [
    (1, "Bala Kanda", "01_Bala_Kanda"),
    (2, "Ayodhya Kanda", "02_Ayodhya_Kanda"),
    (3, "Aranya Kanda", "03_Aranya_Kanda"),
    (4, "Kishkindha Kanda", "04_Kishkindha_Kanda"),
    (5, "Sundara Kanda", "05_Sundara_Kanda"),
    (6, "Yuddha Kanda", "06_Yuddha_Kanda"),
    (7, "Uttara Kanda", "07_Uttara_Kanda"),
]

def split_by_sarga(
    input_file: str = "data/Valmiki_Ramayan_Shlokas.json",
    output_base_dir: str = "data/sargas",
):
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    print(f"📖 Loading dataset from: {input_file}")
    df = pd.read_json(input_file)
    total_records = len(df)
    print(f"✅ Loaded {total_records:,} shlokas.\n")

    os.makedirs(output_base_dir, exist_ok=True)

    print("✂️  Partitioning dataset by Sarga...")
    print("-" * 80)
    print(f"{'#':<3} {'Kanda Name':<20} {'Folder':<22} {'Sargas':<10} {'Shlokas':<10}")
    print("-" * 80)

    total_sargas_created = 0
    total_shlokas_written = 0

    for order, kanda_name, folder_name in KANDAS_INFO:
        kanda_dir = os.path.join(output_base_dir, folder_name)
        os.makedirs(kanda_dir, exist_ok=True)

        kanda_df = df[df["kanda"] == kanda_name]
        sarga_numbers = sorted(kanda_df["sarga"].unique())
        kanda_shlokas = len(kanda_df)

        for sarga_num in sarga_numbers:
            sarga_df = kanda_df[kanda_df["sarga"] == sarga_num]
            sarga_records = (
                sarga_df.replace({float("nan"): None})
                .to_dict(orient="records")
            )

            filename = f"sarga_{sarga_num:03d}.json"
            filepath = os.path.join(kanda_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(sarga_records, f, ensure_ascii=False, indent=2)

            total_shlokas_written += len(sarga_records)
            total_sargas_created += 1

        print(f"{order:<3} {kanda_name:<20} {folder_name:<22} {len(sarga_numbers):<10} {kanda_shlokas:<10,}")

    print("-" * 80)
    print(f"Total Sarga Files Generated: {total_sargas_created:,}")
    print(f"Total Shlokas Written:       {total_shlokas_written:,} / {total_records:,}")

    # Integrity verification
    assert total_shlokas_written == total_records, (
        f"Mismatch: written {total_shlokas_written} vs total {total_records}"
    )
    assert total_sargas_created == 648, (
        f"Expected 648 sargas, got {total_sargas_created}"
    )

    print("🎉 All 648 Sarga JSON files generated and verified successfully!\n")


if __name__ == "__main__":
    split_by_sarga()
