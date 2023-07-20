import json
import psycopg2
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)
        return super().default(o)

def get_data_as_json():
    # Connect to the PostgreSql database
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="5432",
        database="postgres_db",
        user="postgres",
        password="jk3191"

    )
    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the SELECT query with ORDER BY user_id
    cursor.execute("SELECT * FROM public.user_table ORDER BY user_id ASC")

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Define a list to store the data rows as dictionaries
    data = []

     # Iterate over the rows and convert each row to a dictionary
    for row in rows:
        # Create a dictionary from the row data
        row_data = {
            "user_id": row[0],
            "name": row[1],
            "age": row[2],
            "phone": row[3]
        }

        # Append the row dictionary to the data list
        data.append(row_data)

    # Close the cursor and the database connection
    cursor.close()
    conn.close()

    # Create a dictionary containing the status code and data
    result = {
        "status_code": 200,
        "data": data
    }

    # Convert the result dictionary to a JSON string using the custom DecimalEncoder
    json_result = json.dumps(result, cls=DecimalEncoder)

    # Return the JSON string
    return json_result

if __name__ == '__main__':
    # Call the get_data_as_json() function and print the result
    json_output = get_data_as_json()
    print(json_output)
