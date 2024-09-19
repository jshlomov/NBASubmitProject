d

ef get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)