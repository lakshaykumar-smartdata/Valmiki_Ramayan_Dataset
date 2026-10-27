# 📜 Valmiki Ramayana Dataset

A structured, machine-readable JSON dataset of the complete Valmiki Ramayana, comprising Sanskrit shlokas, Romanized transliterations, English translations, and detailed explanations.

---

## 📌 Dataset Overview

- **Total Verses / Records**: 23,291
- **Kandas Included**: 7 (Bala, Ayodhya, Aranya, Kishkindha, Sundara, Yuddha, Uttara)
- **Format**: JSON (complete dataset + individual Kanda parts)
- **Encoding**: UTF-8

---

## 📂 Repository Structure

```
Valmiki_Ramayan_Dataset/
├── data/
│   ├── Valmiki_Ramayan_Shlokas.json   # Full dataset (23,291 shlokas, ~29.8 MB)
│   └── kandas/                        # Dataset partitioned by Kanda
│       ├── 01_Bala_Kanda.json         # 2,217 shlokas (77 sargas, ~2.66 MB)
│       ├── 02_Ayodhya_Kanda.json      # 4,262 shlokas (119 sargas, ~5.08 MB)
│       ├── 03_Aranya_Kanda.json       # 2,439 shlokas (75 sargas, ~2.82 MB)
│       ├── 04_Kishkindha_Kanda.json   # 2,445 shlokas (67 sargas, ~3.05 MB)
│       ├── 05_Sundara_Kanda.json      # 2,772 shlokas (68 sargas, ~3.54 MB)
│       ├── 06_Yuddha_Kanda.json       # 5,693 shlokas (131 sargas, ~6.82 MB)
│       └── 07_Uttara_Kanda.json       # 3,463 shlokas (111 sargas, ~3.63 MB)
├── split_by_kanda.py                  # Python script to split JSON by Kanda
├── requirements.txt                   # Dependencies (pandas)
├── .gitignore                         # Git ignore rules
└── README.md                          # Documentation and schema guide
```

---

## 📊 Kanda Breakdown

| # | Kanda | Sargas | Shlokas | File |
|---|---|---|---|---|
| 1 | **Bala Kanda** | 77 | 2,217 | [`01_Bala_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/01_Bala_Kanda.json) |
| 2 | **Ayodhya Kanda** | 119 | 4,262 | [`02_Ayodhya_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/02_Ayodhya_Kanda.json) |
| 3 | **Aranya Kanda** | 75 | 2,439 | [`03_Aranya_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/03_Aranya_Kanda.json) |
| 4 | **Kishkindha Kanda** | 67 | 2,445 | [`04_Kishkindha_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/04_Kishkindha_Kanda.json) |
| 5 | **Sundara Kanda** | 68 | 2,772 | [`05_Sundara_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/05_Sundara_Kanda.json) |
| 6 | **Yuddha Kanda** | 131 | 5,693 | [`06_Yuddha_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/06_Yuddha_Kanda.json) |
| 7 | **Uttara Kanda** | 111 | 3,463 | [`07_Uttara_Kanda.json`](file:///d:/DayUsers/LakshayKumar/Projects/POCs/Valmiki_Ramayan_Dataset/data/kandas/07_Uttara_Kanda.json) |
| | **Total** | **648** | **23,291** | |

---

## 🔍 Data Schema & Sample

Each record contains the following fields:

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

## 💡 Usage Example (Python & pandas)

### Loading a Specific Kanda:
```python
import pandas as pd

# Load Sundara Kanda
df_sundara = pd.read_json('data/kandas/05_Sundara_Kanda.json')
print(f"Loaded {len(df_sundara)} shlokas from Sundara Kanda")
print(df_sundara[['sarga', 'shloka', 'shloka_text', 'explanation']].head())
```

### Re-running the Split Script:
```bash
python split_by_kanda.py
```

---

## 🤝 Attribution & Credits

Dataset sourced from the open-source compilation by [Ashutosh-Vijay/Valmiki_Ramayan_Dataset](https://github.com/Ashutosh-Vijay/Valmiki_Ramayan_Dataset).
