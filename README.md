### README.md

```markdown
# Places to Visit Tracker

This project is a command-line application for tracking places to visit, based on Google Sheets. It allows you to manage a list of places with options to add, update, remove, mark as visited, list, and search for places.

## Features

- **Add places** with details such as name, location, description, and category.
- **Update existing places**.
- **Mark places as visited**.
- **Remove places** from the list.
- **List all places**.
- **Search for places** based on different criteria.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have Python 3 installed on your machine.
- You have a Google account.
- You have created a Google Sheet with the columns: `Name`, `Location`, `Description`, `Category`, `Visited`.

## Setup

### 1. Google Cloud Setup

1. **Create a Project in Google Cloud Console**:
   - Enable the Google Sheets API and Google Drive API.
   - Create credentials for a service account and download the `creds.json` file.

2. **Prepare `creds.json`**:
   - Ensure your `creds.json` file includes the `spreadsheet_id` of your Google Sheet.
   - Example `creds.json` structure:
     ```json
     {
       "type": "service_account",
       "project_id": "your_project_id",
       "private_key_id": "your_private_key_id",
       "private_key": "your_private_key",
       "client_email": "your_client_email",
       "client_id": "your_client_id",
       "auth_uri": "https://accounts.google.com/o/oauth2/auth",
       "token_uri": "https://oauth2.googleapis.com/token",
       "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
       "client_x509_cert_url": "your_client_x509_cert_url",
       "spreadsheet_id": "your_spreadsheet_id"
     }
     ```

3. **Share Your Google Sheet**:
   - Share your Google Sheet with the service account email (`client_email` from `creds.json`) and give it edit permissions.

### 2. Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd places_to_visit
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure `creds.json` is in the project directory**.

### 3. Usage

1. **Run the Application**:
   ```bash
   python main.py
   ```

2. **Follow the interactive prompts to perform various operations**:
   - Add a place
   - Remove a place
   - Update a place
   - List all places
   - Search for a place
   - Mark a place as visited

## Project Structure

```
places_to_visit/
├── venv/
├── main.py
├── run.py
├── places.py
├── requirements.txt
├── README.md
├── .gitignore
└── creds.json  # This file should not be included in version control
```

## Dependencies

- gspread
- google-auth
- pandas
- argparse
- gunicorn

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

### Important Notes

1. **Security**: Ensure `creds.json` is listed in `.gitignore` to prevent it from being committed to the version control system.
2. **Heroku Config**: If you are using environment variables for sensitive data, configure them in Heroku using the Heroku CLI:
   ```bash
   heroku config:set YOUR_ENV_VARIABLE=value
   ```
3. **Testing**: Before deploying to Heroku, ensure all functionalities are tested locally to avoid issues post-deployment.

### Detailed Instructions for Each Operation

#### Add a Place
1. Choose the option to add a place by entering `1`.
2. Follow the prompts to enter the name, location, description, and category of the place.
3. After entering the details, the place will be added, and the updated list of places will be displayed.

#### Remove a Place
1. Choose the option to remove a place by entering `2`.
2. Enter the name of the place you want to remove.
3. The place will be removed, and the updated list of places will be displayed.

#### Update a Place
1. Choose the option to update a place by entering `3`.
2. Enter the name of the place you want to update.
3. Follow the prompts to update the details. Leave the fields empty if you don't want to update them.
4. The place will be updated, and the updated list of places will be displayed.

#### List All Places
1. Choose the option to list all places by entering `4`.
2. The list of all places will be displayed.

#### Search for a Place
1. Choose the option to search for a place by entering `5`.
2. Enter the search key (Name, Location, Description, Category, Visited) and the search value.
3. The search results will be displayed.

#### Mark a Place as Visited
1. Choose the option to mark a place as visited by entering `6`.
2. Enter the name of the place and the visited status (True/False).
3. The place will be marked as visited/unvisited, and the updated list of places will be displayed.

#### Exit
1. Choose the option to exit the application by entering `7`.
2. The application will exit.

Now the application is fully interactive, and each operation displays a summary and the updated list of places, making it easier for users to manage their list of places to visit.
