import time 
import psycopg2

# STATIC VARIABLES __________________________________________________

database = 'test'
user = 'postgres'
password = 'password'
host = 'postgres'
port_id = '5432'

# _______________________________________ HELPER FUNCTIONS _________________________________________________

# Verbinden mit der Datenbank
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port_id )
#conn = psycopg2.connect(database=cfg.database, user=cfg.user, password=cfg.password, host=cfg.host, port=cfg.port_id, sslmode='require', sslrootcert='server-ca.pem', sslcert='client-cert.pem', sslkey='client-key.pem', options=f'-c statement_timeout={statement_timeout} -c search_path={search_path}', connect_timeout=connect_timeout, keepalives=1, keepalives_idle=30, keepalives_interval=10, keepalives_count=5, gssencmode='prefer', fallback_application_name='Lese App')

cur = conn.cursor()


# Resette alles
def reset_table(cur, conn):
    cur.execute('DROP TABLE IF EXISTS person')

    with open('./person.sql', 'r') as f:
        cur.execute(f.read())
        conn.commit()

# Funktion, um die SQL-Query zu fetchen
def execute_fetchall(query):
    cur.execute(query)
    rows = cur.fetchall()
    return rows

# Funktion, um die SQL-Query auszuführen und die Änderungen zu commiten
def execute_commit(query):
    cur.execute(query)
    conn.commit()

# _____________________________________________ MAIN _______________________________________________________

reset_table(cur, conn)

#Vorgeschichte
print("Auf einer Party waren die Türsteher unaufmerksam und es haben sich Minderjährige eingeschlichen. Nun ist das Ordnungsamt da und damit der Veranstalter keine Probleme kriegt, versucht er nun möglichst schnell alle Kinder zu finden")
time.sleep(5)

# Zeige die Liste
print("Zeige zuerst die vollständige Liste:")
time.sleep(2)

rows = execute_fetchall("SELECT * FROM person;")
for row in rows:
    print(row)

time.sleep(5)

# Lösche alle Einträge vor dem 01.01.2005
print("Alle Minderjährigen raus!")
time.sleep(5)
execute_commit("DELETE FROM person WHERE date_of_birth > '2005-01-01'")

# Zeige die aktualisierte Liste
rows = execute_fetchall("SELECT * FROM person;")
for row in rows:
    print(row)

time.sleep(5)

# Cursor und Datenbankverbindung schließen
cur.close()
conn.close()

print("Alles gut. die Lage wurde rechtzeitig entschärft. Glück gehabt ;D")
