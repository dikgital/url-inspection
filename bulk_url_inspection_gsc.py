import csv
import json
from time import sleep
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# --- SETUP ---
# Path ke file credentials
SERVICE_ACCOUNT_FILE = "account.json"
SCOPES = ['https://www.googleapis.com/auth/webmasters.readonly']
SITE_URL = 'sc-domain:example.com'  # Ganti dengan domain kamu
CSV_INPUT = "cek_status_url.csv"
CSV_OUTPUT = "cek_status_url_INDEX-STATUS.csv"

# Setup credentials dan API client
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('searchconsole', 'v1', credentials=credentials)

# Fungsi untuk inspeksi URL dan log status response


def inspect_url(url):
    try:
        request = {
            'inspectionUrl': url,
            'siteUrl': SITE_URL
        }
        response = service.urlInspection().index().inspect(body=request).execute()
        print(f'✅ [200] Success: {url}')
        result = response.get('inspectionResult', {}).get(
            'indexStatusResult', {})
        return {
            'url': url,
            'coverageState': result.get('coverageState'),
            'lastCrawlTime': result.get('lastCrawlTime'),
            'pageFetchState': result.get('pageFetchState'),
            'robotsTxtState': result.get('robotsTxtState'),
            'verdict': result.get('verdict'),
            'error': ''
        }
    except HttpError as e:
        status_code = e.resp.status
        print(f'❌ [{status_code}] HTTP Error on: {url}')
        return {
            'url': url,
            'coverageState': '',
            'lastCrawlTime': '',
            'pageFetchState': '',
            'robotsTxtState': '',
            'verdict': '',
            'error': f'HTTP {status_code} - {e.error_details}'
        }
    except Exception as e:
        print(f'⚠️  Error (non-HTTP) on {url}: {e}')
        return {
            'url': url,
            'coverageState': '',
            'lastCrawlTime': '',
            'pageFetchState': '',
            'robotsTxtState': '',
            'verdict': '',
            'error': str(e)
        }


# Proses semua URL dari CSV dan simpan hasil
results = []
with open(CSV_INPUT, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        url = row['url']
        print(f'🔍 Inspecting: {url}')
        result = inspect_url(url)
        results.append(result)
        sleep(1)  # Hindari rate limit

# Simpan ke file CSV
fieldnames = ['url', 'coverageState', 'lastCrawlTime',
              'pageFetchState', 'robotsTxtState', 'verdict', 'error']
with open(CSV_OUTPUT, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print(f"\n✅ Selesai! Hasil disimpan ke '{CSV_OUTPUT}'")


