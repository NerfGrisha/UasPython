import requests
from prettytable import PrettyTable

BASE_URL = "http://localhost:8080"  # Update the port if needed

def show_menu():
    print("Menu:")
    print("1. GET data")
    print("2. POST data")
    print("3. PUT data")
    print("4. DELETE data")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def print_matrix(data):

    if not data:
        print("No data available.")
        return

    if isinstance(data, list) and data and isinstance(data[0], list):
        # Create PrettyTable object
        table = PrettyTable()

        # Populate header
        header = ["ID", "Judul", "Pengarang", "Tahun Terbit"]
        table.field_names = header

        # Populate data
        for row in data:
            table.add_row(row)

        # Print the table
        print(table)
    else:
        print("menampilkan data")

# Example usage with the provided data
data = [[3, 'SIKSA KUBUR', 'Anza Mazda', 2023],
        [4, 'Ayam Kampus', 'Afrian Dicky', 2024],
        [5, 'Cinta dua arah', 'Grisha', 2023]]

print_matrix(data)

def get_data():
    response = requests.get(f"{BASE_URL}/showdata")
    if response.status_code == 200:
        try:
            data = response.json()
            print_matrix(data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def post_data():
    judul = input("Enter judul: ")
    pengarang = input("Enter pengarang: ")
    tahun_terbit = input("Enter tahun_terbit: ")

    payload = {
        "judul": judul,
        "pengarang": pengarang,
        "tahun_terbit": tahun_terbit
    }

    response = requests.post(f"{BASE_URL}/add", data=payload)
    print(response.text)

def put_data():
    book_id_data = input("Enter the book_id to update: ")

    # Fetch existing data to display
    response = requests.get(f"{BASE_URL}/showdata?id={book_id_data}")
    if response.status_code == 200:
        data = response.json()
        print("Existing data:")
        print_matrix(data)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return

    # Get updated values
    judul = input("Enter new judul (press Enter to keep the existing value): ")
    pengarang = input("Enter new pengarang (press Enter to keep the existing value): ")
    tahun_terbit = input("Enter new tahun_terbit (press Enter to keep the existing value): ")

    # Prepare payload with updated values
    payload = {"id": book_id_data}
    if judul:
        payload["judul"] = judul
    if pengarang:
        payload["pengarang"] = pengarang
    if tahun_terbit:
        payload["tahun_terbit"] = tahun_terbit

    # Send PUT request
    response = requests.put(f"{BASE_URL}/edit", params=payload)
    print(response.text)

def delete_data():
    book_id = input("Enter the book_id to delete: ")
    response = requests.delete(f"{BASE_URL}/delete?id={book_id}")
    print(response.text)

if __name__ == "__main__":
    while True:
        choice = show_menu()

        if choice == "1":
            get_data()
        elif choice == "2":
            post_data()
        elif choice == "3":
            put_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
