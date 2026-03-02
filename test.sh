#!/bin/bash
set -e  # Hata olursa dur
echo "=== Running UI tests ==="

# Sanal ortam aktif et
. venv/bin/activate

# Test raporlarını temizle
rm -rf test_reports
mkdir -p test_reports

# Testleri verbose ve HTML + JUnit XML raporu ile çalıştır
pytest -v tests \
  --junitxml=test_reports/report.xml \
  --html=test_reports/report.html \
  --self-contained-html
