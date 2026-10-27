# 📜 Valmiki Ramayana Dataset

A structured, machine-readable JSON dataset of the complete Valmiki Ramayana, comprising Sanskrit shlokas, Romanized transliterations, English translations, and detailed explanations.

---

## 📌 Dataset Overview

- **Total Verses / Records**: 23,291
- **Kandas Included**: 7 (Bala, Ayodhya, Aranya, Kishkindha, Sundara, Yuddha, Uttara)
- **Total Sargas (Chapters)**: 648
- **Granularity Levels**:
  1. **Full Epic**: Single monolithic JSON dataset (~29.8 MB)
  2. **By Kanda**: 7 individual Kanda JSON files
  3. **By Sarga**: 648 individual Sarga JSON files organized into Kanda folders
- **Encoding**: UTF-8 (Devanagari script + IAST transliteration + English)

---

## 📂 Repository Folder Structure

```
Valmiki_Ramayan_Dataset/
├── data/
│   ├── Valmiki_Ramayan_Shlokas.json    # Complete dataset (23,291 shlokas, ~29.8 MB)
│   │
│   ├── kandas/                         # Level 1: Partitioned by Kanda (7 files)
│   │   ├── 01_Bala_Kanda.json          # 2,217 shlokas (77 sargas, ~2.66 MB)
│   │   ├── 02_Ayodhya_Kanda.json       # 4,262 shlokas (119 sargas, ~5.08 MB)
│   │   ├── 03_Aranya_Kanda.json        # 2,439 shlokas (75 sargas, ~2.82 MB)
│   │   ├── 04_Kishkindha_Kanda.json    # 2,445 shlokas (67 sargas, ~3.05 MB)
│   │   ├── 05_Sundara_Kanda.json       # 2,772 shlokas (68 sargas, ~3.54 MB)
│   │   ├── 06_Yuddha_Kanda.json        # 5,693 shlokas (131 sargas, ~6.82 MB)
│   │   └── 07_Uttara_Kanda.json        # 3,463 shlokas (111 sargas, ~3.63 MB)
│   │
│   └── sargas/                         # Level 2: Partitioned by Sarga (648 files)
│       ├── 01_Bala_Kanda/              # sarga_001.json ... sarga_077.json (77 files)
│       ├── 02_Ayodhya_Kanda/           # sarga_001.json ... sarga_119.json (119 files)
│       ├── 03_Aranya_Kanda/            # sarga_001.json ... sarga_075.json (75 files)
│       ├── 04_Kishkindha_Kanda/        # sarga_001.json ... sarga_067.json (67 files)
│       ├── 05_Sundara_Kanda/           # sarga_001.json ... sarga_068.json (68 files)
│       ├── 06_Yuddha_Kanda/            # sarga_001.json ... sarga_131.json (131 files)
│       └── 07_Uttara_Kanda/            # sarga_001.json ... sarga_111.json (111 files)
│
├── split_by_kanda.py                   # Splits dataset into 7 Kanda files
├── split_by_sarga.py                   # Splits dataset into 648 Sarga files
├── requirements.txt                    # Python dependencies (pandas)
├── .gitignore                          # Git ignore rules
└── README.md                           # Documentation and schema guide
```

---

## 📊 Kanda & Sarga Breakdown

| # | Kanda | Sargas | Shlokas | Kanda File | Sarga Directory |
|---|---|---|---|---|---|
| 1 | **Bala Kanda** | 77 | 2,217 | [`01_Bala_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/01_Bala_Kanda.json) | [`01_Bala_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/01_Bala_Kanda) |
| 2 | **Ayodhya Kanda** | 119 | 4,262 | [`02_Ayodhya_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/02_Ayodhya_Kanda.json) | [`02_Ayodhya_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/02_Ayodhya_Kanda) |
| 3 | **Aranya Kanda** | 75 | 2,439 | [`03_Aranya_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/03_Aranya_Kanda.json) | [`03_Aranya_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/03_Aranya_Kanda) |
| 4 | **Kishkindha Kanda** | 67 | 2,445 | [`04_Kishkindha_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/04_Kishkindha_Kanda.json) | [`04_Kishkindha_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/04_Kishkindha_Kanda) |
| 5 | **Sundara Kanda** | 68 | 2,772 | [`05_Sundara_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/05_Sundara_Kanda.json) | [`05_Sundara_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/05_Sundara_Kanda) |
| 6 | **Yuddha Kanda** | 131 | 5,693 | [`06_Yuddha_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/06_Yuddha_Kanda.json) | [`06_Yuddha_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/06_Yuddha_Kanda) |
| 7 | **Uttara Kanda** | 111 | 3,463 | [`07_Uttara_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/07_Uttara_Kanda.json) | [`07_Uttara_Kanda/`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/sargas/07_Uttara_Kanda) |
| | **Total** | **648** | **23,291** | | |

---

## 🔍 Data Schema & Sample

Each record in every JSON file contains the following structure:

| Field | Type | Description |
|---|---|---|
| `kanda` | `string` | The section/book of Ramayana (e.g., `Bala Kanda`) |
| `sarga` | `integer` | Chapter / Canto number |
| `shloka` | `integer` | Shloka / Verse number within the Sarga |
| `shloka_text` | `string` | Original Sanskrit text in Devanagari script |
| `transliteration` | `string` | Romanized IAST transliteration of the shloka |
| `translation` | `string` | Word-by-word Sanskrit-to-English translation |
| `explanation` | `string` | English sentence explanation/meaning |
| `comments` | `string` / `null` | Contextual commentary or summary for sarga openers |

### Sample Entry

```json
{
  "kanda": "Bala Kanda",
  "sarga": 1,
  "shloka": 1,
  "shloka_text": "तपस्स्वाध्यायनिरतं तपस्वी वाग्विदां वरम् । नारदं परिपप्रच्छ वाल्मीकिर्मुनिपुङ्गवम् ।।1.1.1।।",
  "transliteration": "tapassvādhyāyanirataṁ tapasvī vāgvidāṁ varam। nāradaṁ paripapraccha vālmīkir munipuṅgavam।।",
  "translation": "तपस्वी ascetic, वाल्मीकि: Valmiki, तप: स्वाध्यायनिरतम् highly delighted in the practice of religious austerities and study of vedas, वाग्विदां वरम् eloquent among the knowledgeable, मुनिपुङ्गवम् preeminent among sages, नारदम् Narada, परिपप्रच्छ enquired.",
  "explanation": "Ascetic Valmiki enquired of Narada, preeminent among the sages ever engaged in the practice of religious austerities or study of the Vedas and best among the eloquent.",
  "comments": "Saint Narada visits hermitage of Valmiki -- Valmiki queries about a single perfect individual bestowed with all good qualities enumerated by him -- Narada, knower of past, present and future, identifies such a man -- describes virtues, qualities of Sri Rama -- narrates briefly the story of his life."
}
```

---

## 💡 Usage Examples (Python & pandas)

### 1. Load an Individual Sarga
```python
import json

# Load Bala Kanda, Sarga 1
with open('data/sargas/01_Bala_Kanda/sarga_001.json', 'r', encoding='utf-8') as f:
    sarga_1 = json.load(f)

print(f"Verses in Sarga 1: {len(sarga_1)}")
print(f"First verse: {sarga_1[0]['shloka_text']}")
```

### 2. Load an Entire Kanda with pandas
```python
import pandas as pd

# Load Sundara Kanda
df_sundara = pd.read_json('data/kandas/05_Sundara_Kanda.json')
print(f"Sundara Kanda verses: {len(df_sundara)}")
```

### 3. Re-generate Partitions
```bash
# Split into 7 Kanda files:
python split_by_kanda.py

# Split into 648 Sarga files:
python split_by_sarga.py
```

---

## 🤝 Attribution & Credits

Dataset sourced from the open-source compilation by [Ashutosh-Vijay/Valmiki_Ramayan_Dataset](https://github.com/Ashutosh-Vijay/Valmiki_Ramayan_Dataset).
