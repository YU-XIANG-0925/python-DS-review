"""
generate_vdata.py
-----------------
Generates 100 practice fake-data files under ./vData/.
File-type breakdown:
  25 x .txt   – plain text paragraphs
  25 x .json  – JSON objects / arrays
  20 x .csv   – tabular sales / user data
  15 x .log   – application log lines
  10 x .xml   – simple XML documents
   5 x .yaml  – YAML configuration snippets
"""

import csv
import json
import os
import random
import string
from datetime import datetime, timedelta

VDATA_DIR = os.path.join(os.path.dirname(__file__), "vData")
os.makedirs(VDATA_DIR, exist_ok=True)

# ── helpers ───────────────────────────────────────────────────────────────────

FIRST_NAMES = [
    "Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Henry",
    "Ivy", "Jack", "Karen", "Leo", "Mia", "Noah", "Olivia", "Peter",
    "Quinn", "Rose", "Sam", "Tina", "Uma", "Victor", "Wendy", "Xander",
    "Yara", "Zoe",
]
LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Wilson", "Anderson", "Taylor", "Thomas", "Jackson", "White",
    "Harris", "Martin", "Thompson", "Young", "Robinson", "Lewis",
]
DEPARTMENTS = ["Engineering", "Marketing", "Sales", "HR", "Finance", "Operations"]
PRODUCTS = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headset", "Webcam", "Tablet",
            "Printer", "Scanner", "Router"]
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
LOG_MESSAGES = [
    "Application started successfully.",
    "Database connection established.",
    "User authentication failed.",
    "Request timed out after 30s.",
    "Cache miss for key '{}'.",
    "File '{}' not found.",
    "Memory usage exceeded 80%.",
    "Scheduled job '{}' completed.",
    "API rate limit reached.",
    "Configuration reloaded.",
    "Service health check passed.",
    "Unexpected exception in module '{}'.",
    "Retrying connection attempt {}/3.",
    "Batch processing finished: {} records.",
    "New session started for user '{}'.",
]
CITIES = ["Taipei", "Tokyo", "Seoul", "Singapore", "New York", "London",
          "Berlin", "Paris", "Sydney", "Toronto"]
LOREM = (
    "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod "
    "tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam "
    "quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo "
    "consequat Duis aute irure dolor in reprehenderit in voluptate velit esse "
    "cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat "
    "non proident sunt in culpa qui officia deserunt mollit anim id est laborum"
).split()


def rand_name():
    return f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"


def rand_email(name: str) -> str:
    domains = ["example.com", "mail.io", "test.org", "demo.net"]
    local = name.lower().replace(" ", ".")
    return f"{local}@{random.choice(domains)}"


def rand_date(start_year=2020, end_year=2025) -> str:
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    return (start + timedelta(days=random.randint(0, (end - start).days))).strftime(
        "%Y-%m-%d"
    )


def rand_datetime() -> str:
    base = datetime(2024, 1, 1)
    return (base + timedelta(
        days=random.randint(0, 365),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )).strftime("%Y-%m-%d %H:%M:%S")


def lorem_paragraph(sentences=5) -> str:
    words = random.choices(LOREM, k=sentences * random.randint(8, 15))
    chunk_size = len(words) // sentences or 1
    return " ".join(
        " ".join(words[i * chunk_size:(i + 1) * chunk_size]).capitalize() + "."
        for i in range(sentences)
    )


def rand_ip() -> str:
    return ".".join(str(random.randint(1, 254)) for _ in range(4))


def rand_id(length=8) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))


# ── generators ────────────────────────────────────────────────────────────────

def write_txt(path: str, index: int) -> None:
    name = rand_name()
    lines = [
        f"=== Record #{index:03d} ===",
        f"Name       : {name}",
        f"Email      : {rand_email(name)}",
        f"Department : {random.choice(DEPARTMENTS)}",
        f"City       : {random.choice(CITIES)}",
        f"Joined     : {rand_date()}",
        f"Employee ID: {rand_id()}",
        "",
        "Notes:",
    ]
    for _ in range(random.randint(2, 4)):
        lines.append(lorem_paragraph(random.randint(3, 6)))
        lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_json(path: str, index: int) -> None:
    records = []
    for i in range(random.randint(5, 15)):
        name = rand_name()
        records.append({
            "id": index * 100 + i,
            "name": name,
            "email": rand_email(name),
            "age": random.randint(20, 60),
            "department": random.choice(DEPARTMENTS),
            "city": random.choice(CITIES),
            "salary": round(random.uniform(30_000, 150_000), 2),
            "active": random.choice([True, False]),
            "joined": rand_date(),
            "skills": random.sample(
                ["Python", "Java", "SQL", "Docker", "Kubernetes",
                 "React", "Go", "Rust", "TypeScript", "C++"],
                k=random.randint(2, 5),
            ),
        })
    payload = {
        "meta": {
            "file_index": index,
            "generated_at": rand_datetime(),
            "total_records": len(records),
        },
        "data": records,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def write_csv(path: str, index: int) -> None:
    headers = ["order_id", "date", "product", "quantity", "unit_price",
               "total", "customer", "city", "status"]
    statuses = ["Shipped", "Pending", "Delivered", "Cancelled", "Processing"]
    rows = []
    for i in range(random.randint(20, 50)):
        qty = random.randint(1, 20)
        price = round(random.uniform(10, 999), 2)
        rows.append([
            f"ORD-{index:03d}-{i:04d}",
            rand_date(),
            random.choice(PRODUCTS),
            qty,
            price,
            round(qty * price, 2),
            rand_name(),
            random.choice(CITIES),
            random.choice(statuses),
        ])
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)


def write_log(path: str, index: int) -> None:
    lines = []
    base_ts = datetime(2024, random.randint(1, 12), random.randint(1, 28),
                       random.randint(0, 23), 0, 0)
    for i in range(random.randint(40, 80)):
        ts = base_ts + timedelta(seconds=i * random.randint(1, 120))
        level = random.choices(
            LOG_LEVELS, weights=[10, 50, 20, 15, 5]
        )[0]
        msg_template = random.choice(LOG_MESSAGES)
        token = random.choice(
            [rand_name(), rand_id(6), str(random.randint(1, 1000)),
             random.choice(PRODUCTS)]
        )
        msg = msg_template.format(token) if "{}" in msg_template else msg_template
        lines.append(
            f"{ts.strftime('%Y-%m-%d %H:%M:%S')} [{level:<8}] "
            f"[pid:{random.randint(1000,9999)}] "
            f"[{rand_ip()}] {msg}"
        )
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def write_xml(path: str, index: int) -> None:
    items = []
    for i in range(random.randint(5, 12)):
        name = rand_name()
        price = round(random.uniform(5, 500), 2)
        items.append(
            f"  <product id=\"{rand_id(6)}\">\n"
            f"    <name>{random.choice(PRODUCTS)} {random.choice(string.ascii_uppercase)}</name>\n"
            f"    <price currency=\"USD\">{price}</price>\n"
            f"    <stock>{random.randint(0, 500)}</stock>\n"
            f"    <supplier>{name}</supplier>\n"
            f"    <last_updated>{rand_date()}</last_updated>\n"
            f"  </product>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<catalog index="{index}" generated="{rand_datetime()}">\n'
        + "\n".join(items)
        + "\n</catalog>\n"
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(xml)


def write_yaml(path: str, index: int) -> None:
    port = random.randint(1024, 65535)
    db_port = random.randint(3306, 5432)
    env = random.choice(["development", "staging", "production"])
    # debug mode should only be enabled in non-production environments
    debug = random.choice([True, False]) if env != "production" else False
    lines = [
        f"# Auto-generated config #{index:03d}",
        f"app_name: service-{rand_id(4).lower()}",
        f"version: \"1.{random.randint(0,9)}.{random.randint(0,20)}\"",
        f"environment: {env}",
        "",
        "server:",
        f"  host: {rand_ip()}",
        f"  port: {port}",
        f"  debug: {str(debug).lower()}",
        f"  workers: {random.randint(1, 16)}",
        "",
        "database:",
        f"  host: db-{random.randint(1, 5)}.{random.choice(CITIES).lower()}.internal",
        f"  port: {db_port}",
        f"  name: {random.choice(['app_db', 'prod_db', 'analytics', 'users_db'])}",
        f"  pool_size: {random.randint(5, 50)}",
        "",
        "logging:",
        f"  level: {random.choice(['DEBUG', 'INFO', 'WARNING'])}",
        f"  file: /var/log/service-{rand_id(4).lower()}.log",
        "",
        "features:",
    ]
    features = ["cache_enabled", "rate_limiting", "metrics", "tracing", "auth_v2"]
    for feat in random.sample(features, k=random.randint(2, len(features))):
        lines.append(f"  {feat}: {str(random.choice([True, False])).lower()}")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ── main ──────────────────────────────────────────────────────────────────────

FILE_PLAN = [
    ("txt",  25, write_txt),
    ("json", 25, write_json),
    ("csv",  20, write_csv),
    ("log",  15, write_log),
    ("xml",  10, write_xml),
    ("yaml",  5, write_yaml),
]


def main():
    random.seed(42)
    counter = 1
    created = []
    for ext, count, writer in FILE_PLAN:
        for n in range(1, count + 1):
            filename = f"data_{counter:03d}.{ext}"
            path = os.path.join(VDATA_DIR, filename)
            writer(path, counter)
            created.append(filename)
            counter += 1

    print(f"✅  Generated {len(created)} files in '{VDATA_DIR}':")
    for name in created:
        print(f"   {name}")


if __name__ == "__main__":
    main()
