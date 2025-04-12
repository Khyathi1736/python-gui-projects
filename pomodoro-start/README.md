# Pomodoro Timer ⏱️🍅

A simple and visually appealing Pomodoro Timer built using Python's `tkinter` library. This timer helps you follow the Pomodoro Technique — a time management method that improves productivity by alternating focused work sessions with short and long breaks.

---

## 🧠 Features

- 24-minute customizable work sessions
- 4-minute short breaks
- 19-minute long breaks after every 4 work sessions
- Visual timer countdown with a tomato-themed interface
- Checkmarks for completed work sessions
- Reset functionality to restart the cycle

---

## 💡 Requirements

- Python 3.x
- `tkinter` (comes pre-installed with most Python distributions)
- `tomato.png` image in the project directory

---

## 🕹️ Controls

- **Start**: Begins the Pomodoro cycle and disables itself to prevent multiple activations.
- **Reset**: Stops the current timer, clears checkmarks, and resets the interface.

---

## 🚀 How to Run

1. Clone this repository or download the files.

2. Make sure `tomato.png` is in the same folder as your Python script.

3. Run the following command:

   ```bash
   python pomodoro_timer.py
   ```

4. Click **Start** to begin your first work session. The app will guide you through the cycle of work and breaks.

---

## 📘 Notes

- The timer starts with a 24-minute work session.
- After each session, a short or long break is triggered automatically.
- Completed sessions are shown using ✔ marks.
- Customize the durations by modifying `WORK_MIN`, `SHORT_BREAK_MIN`, and `LONG_BREAK_MIN` constants in the code.

---

## 📄 License

This project is free to use and modify for personal or educational purposes.

---
``` 

