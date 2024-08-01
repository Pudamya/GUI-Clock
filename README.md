# GUI-Clock

A simple digital clock application built with Python's Tkinter library. This GUI-based clock displays the current time, updating every second.

## Features

- **Real-Time Clock**: Displays the current time in the format `HH : MM : SS AM/PM`.
- **Customizable Appearance**: The clock has a black background and yellow text, displayed in a large font.

## Requirements

- Python 3.x
- Tkinter (usually included with Python installations)

## How to Run

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd GUI-Clock
   ```

3. **Run the script**:
   ```bash
   python clock.py
   ```

## Code Overview

The application uses Tkinter to create a graphical user interface. The key components are:

- **Window Setup**: A window is created with the title "My Clock".
- **Label**: The time is displayed using a Label widget, with a custom font, background, and foreground color.
- **Time Update Function (`dis_time`)**: This function fetches the current time using the `strftime` function and updates the label every second using the `after` method.

## Usage

- **Running the Clock**: Simply run the script, and the clock will start displaying the current time. The time is updated every second.

## Customization

You can customize the appearance of the clock by changing the font, background, and foreground color in the code.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
