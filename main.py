from places import PlacesToVisit

def prompt_for_place_details():
    name = input("Enter place name: ")
    location = input("Enter place location: ")
    description = input("Enter place description: ")
    category = input("Enter place category: ")
    return name, location, description, category

def prompt_for_search_details():
    search_key = input("Enter search key (Name, Location, Description, Category, Visited): ")
    search_value = input("Enter search value: ")
    return search_key, search_value

def display_places(places):
    if places.empty:
        print("No places found.")
    else:
        print(places.to_string(index=False))

def main():
    manager = PlacesToVisit()

    while True:
        print("\nChoose an operation:")
        print("1. Add a place")
        print("2. Remove a place")
        print("3. Update a place")
        print("4. List all places")
        print("5. Search for a place")
        print("6. Mark a place as visited")
        print("7. Exit")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            name, location, description, category = prompt_for_place_details()
            manager.add_place(name, location, description, category)
            print(f"\nAdded place: {name}")
            print("Updated list of places:")
            display_places(manager.list_places())

        elif choice == '2':
            name = input("Enter the name of the place to remove: ")
            manager.remove_place(name)
            print(f"\nRemoved place: {name}")
            print("Updated list of places:")
            display_places(manager.list_places())

        elif choice == '3':
            name = input("Enter the name of the place to update: ")
            update_data = {}
            print("Leave the field empty if you don't want to update it.")
            location = input("Enter new location: ")
            if location:
                update_data['Location'] = location
            description = input("Enter new description: ")
            if description:
                update_data['Description'] = description
            category = input("Enter new category: ")
            if category:
                update_data['Category'] = category
            visited = input("Enter visited status (True/False): ")
            if visited:
                update_data['Visited'] = visited.lower() == 'true'
            manager.update_place(name, **update_data)
            print(f"\nUpdated place: {name}")
            print("Updated list of places:")
            display_places(manager.list_places())

        elif choice == '4':
            print("Listing all places:")
            display_places(manager.list_places())

        elif choice == '5':
            search_key, search_value = prompt_for_search_details()
            result = manager.search_places(**{search_key: search_value})
            print("Search results:")
            display_places(result)

        elif choice == '6':
            name = input("Enter the name of the place to mark as visited: ")
            visited = input("Enter visited status (True/False): ")
            manager.mark_visited(name, visited.lower() == 'true')
            print(f"\nMarked place '{name}' as {'visited' if visited.lower() == 'true' else 'unvisited'}.")
            print("Updated list of places:")
            display_places(manager.list_places())

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
