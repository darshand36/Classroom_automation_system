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
- 

---

## 📂 Project Structure
├── base.py
├── base2.py
├── cameratest.py
├── coco.names
├── main.py
├── personTrackingV1.py
├── personTrackingV2.py
├── yolov3.cfg
├── yolov3.weights  ##cannot push it on git huge file download it manually 
├── README.md

wget https://pjreddie.com/media/files/yolov3.weights


##Connection detail's



python main.py

python cameratest.py






