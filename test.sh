#!/bin/bash

echo "Running UI tests..."

pytest tests \
  --junitxml=test_reports/report.xml \
  --html=test_reports/report.html \
  --self-contained-html
