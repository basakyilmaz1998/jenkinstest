import psycopg2
from junitparser import JUnitXml
import os

# PostgreSQL bağlantı ayarları
conn = psycopg2.connect(
    dbname="testdb",
    user="testuser",
    password="testpass",
    host="localhost",
    port="5432"
)

def insert_test_result(cursor, test_name, status, duration):
    cursor.execute("""
        INSERT INTO ui_test_results (test_name, status, duration)
        VALUES (%s, %s, %s)
    """, (test_name, status, duration))

def main():
    xml_path = "test_reports/report.xml"

    if not os.path.exists(xml_path):
        print(f"XML raporu bulunamadı: {xml_path}")
        return

    xml = JUnitXml.fromfile(xml_path)

    with conn:
        with conn.cursor() as cur:
            # Her test case için
            for suite in xml:
                for case in suite:
                    test_name = case.name
                    duration = case.time or 0
                    status = "PASS"
                    if case.result and case.result._tag != "success":
                        status = "FAIL"

                    print(f"Test: {test_name} | Durum: {status} | Süre: {duration}s")

                    insert_test_result(cur, test_name, status, duration)

if __name__ == "__main__":
    main()
