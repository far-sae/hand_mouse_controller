
# Hand Mouse Controller

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

## Overview

This project uses a webcam to track hand movements and control the mouse on your screen. The application leverages `MediaPipe` for hand tracking, `OpenCV` for image processing, and `PyAutoGUI` to simulate mouse movements.

### Features

- **Real-time Hand Tracking**: Detects hand gestures using your webcam.
- **Mouse Control**: Moves the mouse cursor based on hand gestures.
- **Simple and Intuitive**: Easy to set up and use.

## Installation

Follow these steps to set up the project locally.

### Prerequisites

- Python 3.8 or higher
- A webcam

### Clone the Repository

\`\`\`bash
git clone https://github.com/far-sae/hand_mouse_controller.git
cd hand_mouse_controlle
\`\`\`

### Create a Virtual Environment

\`\`\`bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scriptsctivate`
\`\`\`

### Install Dependencies

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### Running the Application

\`\`\`bash
python hand_mouse_controller.py
\`\`\`

Make sure your webcam is connected and working. The application will start tracking your hand and moving the mouse cursor accordingly.

## Usage

- **Start the application**: Run the script to begin tracking.
- **Move your hand**: Use your hand in front of the webcam to control the mouse cursor.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

### How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your changes to your fork.
5. Submit a pull request.
