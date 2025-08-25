 # Classroom Automation System

This project uses **Computer Vision** and **Deep Learning (YOLOv3)** to automate classroom appliances (lights, fans, etc.) based on student presence.  
If no students are detected, the system automatically turns off unused appliances to save energy.

---

## 🚀 Features
- Real-time **person detection** using YOLOv3
- **Automatic light/fan control** based on occupancy
- Tracks **people entering and exiting**
- Visualizes **trajectories** of detected persons
- Customizable thresholds and door coordinates

---

## 🛠️ Tech Stack
- **Python 3**
- **OpenCV**
- **YOLOv3**
- **NumPy**
- **Arduino UNO**
- **Relay**
---



## Project Structure
├── base.py                 
├── base2.py  
├── cameratest.py  
├── coco.names  
├── main.py  
├── personTrackingV1.py  
├── personTrackingV2.py  
├── yolov3.cfg  
├── README.md  


---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/darshand36/Classroom_automation_system.git
   cd Classroom_automation_system
2. Change directory:
   ```bash
   cd Classroom_automation_system
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Download YOLOv3 weights:
   ```bash
   wget https://pjreddie.com/media/files/yolov3.weights

---
## 🛠️Connection Details
1. **Relay to arduino**
- Relay VCC to arduino 5v
- Relay GND to arduino GND
- In signal to Pin 7 of arduino

2. **Light to relay**
- Positive termiinal of battery to LED positive terminal
- LED negative to COM pin of relay
- Battery Negative to Normal open

3. **Connect to USB port to type B connector to specified port to PC**
Push the arduino code in the arduino

4. Clone this repository:
   ```bash
   python main.py
   press q to quit



## 📸 Demo Output

Detects people in real time

Draws bounding boxes & trajectories

Updates count of entered/exited persons

Turns ON appliances when students are present

Turns OFF appliances when room is empty

## 📌 Future Improvements

Integrate with IoT (MQTT / Firebase) for remote monitoring

Optimize detection for low-end hardware

Add GUI dashboard for real-time classroom status
