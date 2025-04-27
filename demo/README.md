# AETHER
## Demo Application

A simple proof-of-concept application that demonstrates core-features by means of a simulated real-world use-case scenario.

### ARCHITECTURE
/demo/
├── app.py/
├── static/
│   ├── style.css
│   └── script.js
└── templates/
    └── index.html

### LOCAL DEPLOYMENT

#### **Ubuntu/Debian/Kali**:
In a new terminal window:

    ```sh

    # Install Python and Git
    
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3-full git
    # Clone this repository and navigate to the 'demo' directory    
    
    git clone https://github.com/seedofyggdrasil/aether.git
    cd aether/demo

    # Install dependencies

    python3 -m pip -r requirements.txt

    # Start the application

    python3 app.py

    ```

The demo app can then be accessed by visiting http://localhost:8080 in a browser window. 
