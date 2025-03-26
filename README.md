# 🎹 Virtual Piano using OpenVINO & Pygame

This project is a **Virtual AI-powered Piano** that uses **OpenVINO for hand tracking** and **Pygame for sound playback**. The model detects hand gestures and maps them to piano keys, allowing users to play a virtual piano in real-time.

## 🛠️ **Technologies Used**
- **Python**
- **OpenVINO** (for hand tracking)
- **Pygame** (for sound and UI rendering)
- **OpenCV** (for real-time camera input processing)
- **NumPy** (for efficient computations)

## 🚀 **Features**
✅ **AI Hand Tracking** – Detects fingers & maps them to piano keys  
✅ **Real-time Sound Playback** – Plays corresponding notes using Pygame  
✅ **Smooth & Interactive UI** – Displays piano keys and user interactions  
✅ **Gesture-Based Control** – Play notes by moving fingers over the keys  
✅ **Runs on Google Colab** – Works in a cloud environment (optional)  

## 🔧 **Installation & Setup**
To run the Virtual Piano on your local machine:

1. **Clone this repository:**
   ```sh
   git clone https://github.com/rupak1005/virtual_piano.git
   ```
2. **Navigate to the project folder:**
   ```sh
   cd virtual_piano
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Virtual Piano:**
   ```sh
   python virtual_piano.py
   ```

## 🎹 **How It Works**
1. The camera captures **hand movements**.
2. OpenVINO detects **finger positions**.
3. The corresponding **piano key is activated**.
4. Pygame plays the **associated sound** in real-time.

## 📂 **Folder Structure**
```
virtual_piano/
│── models/
│   ├── hand_tracking_model.xml
│── sounds/
│   ├── C_note.wav
│   ├── D_note.wav
│── assets/
│   ├── piano_ui.png
│── virtual_piano.py
│── requirements.txt
│── README.md
```

## 🤝 **Contributing**
We welcome contributions! 🛠️
1. Fork the repository 🍴
2. Create a new branch: `git checkout -b feature-new-functionality`
3. Commit your changes: `git commit -m "Added new feature"`
4. Push to your fork and create a Pull Request

## ⚡ **Resources**
- [OpenVINO Documentation](https://docs.openvino.ai/)
- [Pygame Guide](https://www.pygame.org/docs/)
- [OpenCV Python Docs](https://docs.opencv.org/master/)

## 📜 **License**
This project is licensed under the **MIT License**. Feel free to use and modify it! 🚀

---

🎵 **Star this repo** if you find it useful! ⭐  
🎹 Enjoy playing music with AI! 🎶

