import psycopg2

conn = psycopg2.connect(
    dsn='postgresql://postgres:abhajkhan@localhost:5432/abc_company'
)