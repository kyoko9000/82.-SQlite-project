# Import the libraries
import sqlite3
import multiprocessing


# Define a function to query data from SQLite using a process
def query_data(process_id, db_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    # Create a cursor
    cursor = conn.cursor()
    # Print the process id
    print(f"Process {process_id} is querying data from {db_name}.{table_name}")
    # Giả sử bạn muốn lấy dòng có id là 10
    id = process_id
    cursor.execute(f"SELECT * FROM {table_name} WHERE ID = {id}")
    # Fetch the results
    results = cursor.fetchall()
    conn.close()
    return results


# Define the number of processes
num_processes = 3
# Define the database name
db_name = "test.db"
# Define the table name
table_name = "COMPANY"
n = 0
if __name__ == '__main__':
    while True:
        n += 1
        with multiprocessing.Pool(processes=num_processes) as pool:  # start 4 worker processes
            process_ids = list(range(1, num_processes + 1))
            for process_id in process_ids:
                result = pool.apply_async(query_data, (process_id, db_name, table_name))
                print(f"round {n}", result.get(timeout=1))
            print("\n")
        if n == 2:
            break
