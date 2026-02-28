import sqlite3
import os
import random
from datetime import datetime, timedelta

# Ensure data directory exists
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(DATA_DIR, exist_ok=True)

DB_PATH = os.path.join(DATA_DIR, 'school_district.db')

SCHOOLS = [
    (1, 'Lincoln Elementary School',    'Oak Street, Northview',       412),
    (2, 'Jefferson Middle School',       'Maple Avenue, Northview',     687),
    (3, 'Washington High School',        'Cedar Blvd, Northview',      1243),
    (4, 'Roosevelt Elementary School',   'Pine Road, Eastfield',        388),
    (5, 'Kennedy Middle/High School',    'Elm Drive, Westpark',         921),
]

DEVICE_TYPES = ['Chromebook', 'iPad', 'Windows Laptop', 'MacBook', 'Desktop PC', 'Smart Board']
DEVICE_TYPE_WEIGHTS = [40, 20, 20, 5, 10, 5]

STATUSES = ['active', 'active', 'active', 'active', 'inactive', 'repair', 'retired']

SOFTWARE = {
    1: [  # Lincoln Elementary
        ('Google Workspace for Education', 450, None, 2),
        ('Clever SSO Platform',            450, None, 2),
        ('Seesaw Learning Journal',        430, 408, 1),
        ('Reading Eggs',                   250, 219, 1),
        ('DreamBox Math',                  250, 201, 1),
        ('Canva for Education',            450, 312, 2),
    ],
    2: [  # Jefferson Middle
        ('Google Workspace for Education', 750, None, 2),
        ('Clever SSO Platform',            750, None, 2),
        ('Khan Academy',                   700, 634, 1),
        ('Newsela',                        700, 589, 1),
        ('Desmos Classroom',               700, 512, 1),
        ('Minecraft Education Edition',    150, 98,  1),
    ],
    3: [  # Washington High
        ('Google Workspace for Education', 1350, None, 2),
        ('Clever SSO Platform',            1350, None, 2),
        ('College Board AP Classroom',     1200, 1089, 1),
        ('Turnitin',                       1200, 1001, 1),
        ('Adobe Creative Cloud',           200,  187,  1),
        ('Naviance (College Planning)',    1300, 1178, 1),
    ],
    4: [  # Roosevelt Elementary
        ('Google Workspace for Education', 420, None, 2),
        ('Clever SSO Platform',            420, None, 2),
        ('Seesaw Learning Journal',        400, 371, 1),
        ('Reading Eggs',                   220, 198, 1),
        ('DreamBox Math',                  220, 183, 1),
        ('Prodigy Math',                   420, 354, 1),
    ],
    5: [  # Kennedy Middle/High
        ('Google Workspace for Education', 1000, None, 2),
        ('Clever SSO Platform',            1000, None, 2),
        ('Khan Academy',                   900,  812,  1),
        ('Turnitin',                       800,  701,  1),
        ('Desmos Classroom',               900,  788,  1),
        ('Adobe Creative Cloud',           100,  87,   1),
    ],
}

# Expiry date buckets: 1 = ~1yr, 2 = ~2yrs
def expiry(years_out: int) -> str:
    base = datetime(2026, 7, 1)
    delta = timedelta(days=365 * years_out + random.randint(-30, 30))
    return (base + delta).strftime('%Y-%m-%d')

def random_serial(prefix: str) -> str:
    return f"{prefix}-{''.join(random.choices('ABCDEFGHJKLMNPQRSTUVWXYZ0123456789', k=8))}"

def random_last_active(status: str) -> str:
    if status == 'retired':
        days_ago = random.randint(180, 730)
    elif status == 'repair':
        days_ago = random.randint(7, 60)
    elif status == 'inactive':
        days_ago = random.randint(30, 180)
    else:
        days_ago = random.randint(0, 14)
    dt = datetime.now() - timedelta(days=days_ago)
    return dt.strftime('%Y-%m-%d')

def device_count_for_school(school_id: int) -> int:
    counts = {1: 68, 2: 95, 3: 100, 4: 57, 5: 85}
    return counts[school_id]

def build_devices():
    rows = []
    device_id = 1
    for school_id, name, location, student_count in SCHOOLS:
        count = device_count_for_school(school_id)
        for _ in range(count):
            dtype = random.choices(DEVICE_TYPES, weights=DEVICE_TYPE_WEIGHTS, k=1)[0]
            status = random.choice(STATUSES)
            prefix_map = {
                'Chromebook':     'CB',
                'iPad':           'IP',
                'Windows Laptop': 'WL',
                'MacBook':        'MB',
                'Desktop PC':     'DC',
                'Smart Board':    'SB',
            }
            serial = random_serial(f"S{school_id:02d}-{prefix_map[dtype]}")
            last_active = random_last_active(status)
            rows.append((device_id, school_id, dtype, status, last_active, serial))
            device_id += 1
    return rows

def build_licenses():
    rows = []
    lic_id = 1
    for school_id, entries in SOFTWARE.items():
        student_count = SCHOOLS[school_id - 1][3]
        for software_name, total_seats, used_seats_override, years in entries:
            if used_seats_override is None:
                used_seats = student_count + random.randint(20, 80)  # staff included
            else:
                used_seats = used_seats_override
            exp = expiry(years)
            rows.append((lic_id, school_id, software_name, total_seats, used_seats, exp))
            lic_id += 1
    return rows

def setup():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript('''
        DROP TABLE IF EXISTS licenses;
        DROP TABLE IF EXISTS devices;
        DROP TABLE IF EXISTS schools;

        CREATE TABLE schools (
            id            INTEGER PRIMARY KEY,
            name          TEXT    NOT NULL,
            location      TEXT    NOT NULL,
            student_count INTEGER NOT NULL
        );

        CREATE TABLE devices (
            id           INTEGER PRIMARY KEY,
            school_id    INTEGER NOT NULL,
            device_type  TEXT    NOT NULL,
            status       TEXT    NOT NULL CHECK(status IN ('active','inactive','repair','retired')),
            last_active  TEXT    NOT NULL,
            serial_number TEXT   NOT NULL UNIQUE,
            FOREIGN KEY (school_id) REFERENCES schools(id)
        );

        CREATE TABLE licenses (
            id            INTEGER PRIMARY KEY,
            school_id     INTEGER NOT NULL,
            software_name TEXT    NOT NULL,
            total_seats   INTEGER NOT NULL,
            used_seats    INTEGER NOT NULL,
            expiry_date   TEXT    NOT NULL,
            FOREIGN KEY (school_id) REFERENCES schools(id)
        );
    ''')

    cur.executemany(
        'INSERT INTO schools VALUES (?,?,?,?)',
        SCHOOLS
    )

    devices = build_devices()
    cur.executemany(
        'INSERT INTO devices VALUES (?,?,?,?,?,?)',
        devices
    )

    licenses = build_licenses()
    cur.executemany(
        'INSERT INTO licenses VALUES (?,?,?,?,?,?)',
        licenses
    )

    conn.commit()

    # Summary
    print(f"Database created at: {os.path.abspath(DB_PATH)}\n")
    print(f"{'Table':<12} {'Rows':>6}")
    print('-' * 20)
    for table in ('schools', 'devices', 'licenses'):
        count = cur.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0]
        print(f"{table:<12} {count:>6}")

    print('\nDevices per school:')
    rows = cur.execute('''
        SELECT s.name, COUNT(d.id) as total,
               SUM(d.status = 'active') as active
        FROM schools s
        LEFT JOIN devices d ON d.school_id = s.id
        GROUP BY s.id
    ''').fetchall()
    for name, total, active in rows:
        print(f"  {name}: {total} devices ({active} active)")

    conn.close()

if __name__ == '__main__':
    random.seed(42)
    setup()
