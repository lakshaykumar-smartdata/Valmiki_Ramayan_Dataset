# 📜 Valmiki Ramayana Dataset

A structured, machine-readable JSON dataset of the complete Valmiki Ramayana, comprising Sanskrit shlokas, Romanized transliterations, English translations, and detailed explanations.

---

## 📌 Dataset Overview

- **Total Verses / Records**: 23,291
- **Kandas Included**: 7 (Bala Kanda, Ayodhya Kanda, Aranya Kanda, Kishkindha Kanda, Sundara Kanda, Yuddha Kanda, Uttara Kanda)
- **Format**: JSON (`data/Valmiki_Ramayan_Shlokas.json`)
- **Encoding**: UTF-8

---

## 📂 Repository Structure

```
Valmiki_Ramayan_Dataset/
├── data/
│   └── Valmiki_Ramayan_Shlokas.json   # Primary JSON dataset (~29.8 MB)
└── README.md                          # Documentation and schema guide
```

---

## 🔍 Data Schema & Sample

Each record in `Valmiki_Ramayan_Shlokas.json` contains the following fields:

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

## 💡 Usage Example (Python)

```python
import json

# Load dataset
with open('data/Valmiki_Ramayan_Shlokas.json', 'r', encoding='utf-8') as f:
    shlokas = json.load(f)

print(f"Total shlokas loaded: {len(shlokas)}")

# Access first shloka
first_shloka = shlokas[0]
print(f"Kanda: {first_shloka['kanda']}")
print(f"Verse: {first_shloka['sarga']}.{first_shloka['shloka']}")
print(f"Text: {first_shloka['shloka_text']}")
print(f"Translation: {first_shloka['explanation']}")
```

---

## 🤝 Attribution & Credits

Dataset sourced from the open-source compilation by [Ashutosh-Vijay/Valmiki_Ramayan_Dataset](https://github.com/Ashutosh-Vijay/Valmiki_Ramayan_Dataset).
