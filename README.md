 🎓 Smart Classroom Automation System

An AI + IoT based Classroom Automation Project that automatically controls lights and fans based on student presence detection using cameras. The system is designed to save electricity, reduce manual intervention, and scale easily across multiple classrooms.

📌 Features

🎥 Camera-based Detection – Uses image processing to detect student presence.

⚡ Automatic Appliance Control – Lights and fans turn ON when students are present and OFF when the classroom is empty.

🖧 Centralized Control Hub – A Raspberry Pi/Arduino in the control room manages multiple classrooms.

🔗 Relay-based Switching – Relays installed in each classroom control appliances.

🌐 Scalable Architecture – Easily add new classrooms using wired (RS-485) or wireless (ESP8266/ESP32) modules.

📊 Energy Efficiency – Saves electricity and reduces costs.

🏗️ System Architecture
            +---------------------+
            |   Raspberry Pi Hub  |
            |  (Central Control)  |
            +----------+----------+
                       |
                RS-485 / Wi-Fi
                       |
   ---------------------------------------------------
   |                     |                           |
+--+--+              +---+---+                   +---+---+
|Relay|              | Relay |                   | Relay |
|(Clsrm 1)           | (Clsrm 2)                 | (Clsrm N)
+--+--+              +---+---+                   +---+---+
   |                     |                           |
 Lights & Fans     Lights & Fans               Lights & Fans

🔧 Hardware Used

🖥️ Raspberry Pi (Central Controller)

⚡ Arduino/ESP8266/ESP32 (Optional, for communication)

🔌 Relay Modules (for switching lights & fans)

🎥 Cameras (for presence detection)

🔋 Power Supply

🛠️ Wires, connectors, and enclosures

💻 Software Stack

Python (OpenCV / TensorFlow) → For student presence detection

Arduino IDE → For microcontroller programming

RS-485 / Wi-Fi Communication → For central hub ↔ classrooms

Flask/Django (Optional) → For web-based monitoring dashboard

🚀 Installation & Setup

Clone this repository

git clone https://github.com/your-username/smart-classroom-automation.git
cd smart-classroom-automation


Install Dependencies (on Raspberry Pi)

pip install opencv-python numpy pyserial


Upload Relay Control Code to Arduino/ESP8266 using Arduino IDE.

Connect Cameras & Relays as per wiring diagram.

Run Main Controller

python main.py

📸 Demo

(Add GIFs, images, or YouTube video link here to showcase the project)

🛠️ Future Improvements

📡 Mobile app for remote monitoring & control.

📊 Dashboard with energy usage analytics.

🔒 Security integration with face recognition.

🌍 Integration with IoT cloud platforms.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
