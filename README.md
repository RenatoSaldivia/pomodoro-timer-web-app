# 🕒 Pomodoro Timer (Python CLI)

A simple Pomodoro timer built in Python, designed to run in the console with sound alerts between work and break sessions.

This project focuses on basic time control, loops, and user feedback through sound.

---

## 🚀 Features

- ⏱️ 25-minute work sessions and 5-minute breaks (configurable)  
- 🔊 Sound alerts using `winsound`  
- 🔁 Infinite Pomodoro cycles  
- 🖥️ Clean countdown display in the console  

---

## 🧠 Purpose

This project was created to:

- Practice Python fundamentals  
- Work with time-based logic (`time.sleep`)  
- Implement simple automation in the console  

---

## 🛠️ Tech Stack

- Python  
- time module  
- winsound (Windows only)  

---

## ⚠️ Requirements

- Windows OS (required for `winsound`)  
- Python 3  

---

## ▶️ How to Run

```bash
python pomodoro.py
```
- Runs in an infinite loop
- Stop manually with `Ctrl + C`

---

## 🔁 How It Works
- Starts a 25-minute work session
- Plays a sound alert
- Starts a 5-minute break
- Repeats indefinitely
