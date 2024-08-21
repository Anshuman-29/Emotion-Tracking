## Emotion Tracking Analysis Web Application (For Psychological Analysis)

### Overview

This project is a Flask-based web application that allows users to track and analyze button presses over time. The application features a 2x2 grid of buttons labeled "HH", "HD", "DH", and "DD". Each button press is recorded with a timestamp, and users can generate various analysis reports based on the frequency of these presses.

### Features

- **Button Tracking**: Four buttons ("HH", "HD", "DH", "DD") are displayed in a 2x2 grid. Every time a button is pressed, the event is recorded with the current timestamp.
- **Graphical Analysis**: Users can generate graphical reports that visualize the number of button presses:
  - **Daily Analysis**: Number of button presses vs. Time of Day.
  - **Weekly Analysis**: Number of button presses vs. Day of the Week.
  - **Monthly Analysis**: Number of button presses vs. Day of the Month.
  - **Yearly Analysis**: Number of button presses vs. Month of the Year.
- **Dynamic Visualization**: The analysis reports are presented as dynamically generated graphs using `matplotlib`, embedded directly into the web page.
- **User-Friendly Interface**: The application is built with simplicity in mind, providing an intuitive interface for users to interact with.

### Technologies Used

- **Python**: The core programming language used to build the application.
- **Flask**: A lightweight web framework used to handle routing and server-side logic.
- **Pandas**: For managing and processing the timestamp data.
- **Matplotlib**: For generating the graphical analysis reports.
- **HTML/CSS**: For the front-end interface.

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/button-press-analysis.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd button-press-analysis
   ```
3. **Create and activate a virtual environment**:
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # On Windows
   # or
   source myenv/bin/activate  # On Linux/Mac
   ```
4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the Flask application**:
   ```bash
   python app.py
   ```
6. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to interact with the application.

### Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have suggestions for improving the project.


---
