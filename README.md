# Bulk URL Inspection - Google Search Console API (Python)

Script ini dibuat untuk melakukan **bulk URL inspection** di Google Search Console menggunakan **Python** + **Search Console API**.  
Cocok untuk praktisi SEO yang butuh cek status indexing ribuan URL tanpa harus manual lewat GSC.

---

## 🚀 Fitur
- Input daftar URL dari file CSV.
- Menggunakan **Google Search Console API - URL Inspection**.
- Output hasil ke file CSV dengan informasi:
  - `coverageState`
  - `lastCrawlTime`
  - `pageFetchState`
  - `robotsTxtState`
  - `verdict`
  - `error`

---

## 📦 Instalasi

1. Clone repo ini:
   ```
   git clone https://github.com/username/bulk-url-inspection-gsc.git
   cd bulk-url-inspection-gsc
   ```
2. Buat virtual environment (opsional, tapi disarankan):

  ```
  python -m venv venv
  source venv/bin/activate  # macOS / Linux
  venv\Scripts\activate     # Windows
  ```

3. Install dependencies:

  `pip install -r requirements.txt`

## 🔑 Setup Google API Credentials

1. Buka Google [Cloud Console](https://console.cloud.google.com/).

2. Buat project baru atau pakai project yang sudah ada. 

3. Aktifkan Search Console API.

4. Buat Service Account dan generate file JSON credentials. Kalau bingung cara integrasiin Google API, Bisa [baca di artikelku ini](https://dikgital.com/technical-seo/google-cloud-api)

5. Simpan file JSON credentials (misalnya account.json) di root project.

6. Pastikan Service Account ini ditambahkan sebagai user (restricted role) di property Google Search Console dengan minimal permission read-only.

## 📂 Struktur File

```
bulk-url-inspection-gsc/
├── bulk_url_inspection.py   # script utama
├── cek_status_url.csv       # input daftar URL (contoh)
├── requirements.txt
├── README.md
└── account.json                # file credentials (JANGAN diupload ke repo publik!)
```

## 📥 Input File (CSV)

File CSV input minimal berisi header url dan daftar URL.
Contoh cek_status_url.csv:

| url |
| --- |
| https://example.com/page-1 |
| https://example.com/page-2 |
| https://example.com/page-3 |

## 📤 Output File (CSV)

Script akan membuat file CSV baru (cek_status_url_INDEX-STATUS.csv) dengan struktur seperti ini:

| url | coverageState | lastCrawlTime | pageFetchState | robotsTxtState | verdict | error |
| --- | ------------- | ------------- | -------------- | -------------- | ------- | ----- |
| https://example.com/page-1 | Indexed | 2025-07-01T12:00Z | SUCCESSFUL | ALLOWED | PASS | |
| https://example.com/page-2 | Crawled - currently not indexed | 2025-07-01T12:00Z | SUCCESSFUL | ALLOWED | NEUTRAL | |

## ⚠️ Quota Limitation

- Maksimum 2000 request per property per hari.

- Maksimum 600 request per menit per property.

- Jika kena error 429 atau Quota Exceeded, script akan otomatis log di kolom error.

## ▶️ Cara Menjalankan

Pastikan sudah menaruh daftar URL di cek_status_url.csv.

Jalankan script:

`python bulk_url_inspection.py`

Tunggu proses selesai, hasil akan tersimpan di cek_status_url_INDEX-STATUS.csv.

## 📌 Catatan
- `auth.json` jangan pernah diupload ke publik.
- Script ini untuk kebutuhan monitoring SEO, jangan dipakai untuk abuse API.

📝 Lisensi
MIT License. Silakan gunakan, modifikasi, atau kembangkan script ini sesuai kebutuhan.
