# Ticket Reservation System

A simple ticket reservation system built using Python and Tkinter, allowing users to submit reservations and view a list of all reservations stored in a SQLite database.

## Features
- Submit ticket reservations with full name, gender, and comments.
- View a list of all reservations in a dynamic table.
- Data is stored persistently using SQLite.

## Project Structure
```
Ticket-Reservation-System/
├── hello.py          # Main application file
├── ListRequist.py   # List reservations functionality
├── dbConnect.py     # Database connection and operations
├── resela.db        # SQLite database (auto-generated)
└── README.md        # Project documentation
```

## Requirements
- Python 3.x
- `tkinter` library (comes pre-installed with Python)
- SQLite3 (comes pre-installed with Python)

## How to Run
1. Clone the repository or download the project files.
2. Open a terminal or command prompt in the project directory.
3. Run the following command:
   ```bash
   python main.py
   ```
4. The application window will open, allowing you to submit and view ticket reservations.

## Usage
### Submitting a Reservation
1. Enter your full name in the "Full Name" field.
2. Select your gender (Male or Female).
3. Add any comments in the "Comments" text box.
4. Click the "Submit" button to save the reservation.

### Viewing Reservations
1. Click the "List Reservations" button.
2. A new window will open displaying all reservations in a table format.

## Developer
**Youssef Boubli**

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Screenshots
### Main Window
![Main Window](screenshot_main.png)

### List Reservations
![List Reservations](screenshot_list.png)

