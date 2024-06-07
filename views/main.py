import argparse
from places import PlacesToVisit

def main():
    parser = argparse.ArgumentParser(destination="places to Visit Manager")
    parser.add_argument('operation', choices=['add', 'remove', 'update', 'list', 'search', 'mark'], help="Operation to perform")
    parser.add_argument('operation', choices=['add', 'remove', 'update', 'list', 'search', 'mark'], help="Operation to perform")
    parser.add_argument('--name', type=str, help="Place name")
    parser.add_argument('--location', type=str, help="Place location")
    parser.add_argument('--description', type=str, help="Place description")
    parser.add_argument('--category', type=str, help="Place category")
    parser.add_argument('--visited', type=bool, help="Visited status")
    parser.add_argument('--search_key', type=str, help="Search key")
    parser.add_argument('--search_value', type=str, help="Search value")
    
    args = parser.parse_args()
    manager = PlacesToVisit()
    
