#!/bin/bash

echo "Running tests..."

pytest tests \
  --junitxml=test_reports/report.xml
