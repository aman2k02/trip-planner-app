# 🚛 Truck Trip Planner (Full Stack Application)

A production-ready full-stack web application that generates optimized truck trip plans using **Hours of Service (HOS)** rules, visualizes routes on an interactive map, and dynamically creates **ELD (Electronic Logging Device) logs**.

---

## 🌐 Live Application

* 🔗 **Frontend (Vercel):** https://trip-planner-app-jade.vercel.app/
* 🔗 **Backend (Render):** https://trip-planner-backend.onrender.com/
* 🔗 **GitHub Repository:** https://github.com/aman2k02/trip-planner-app/

---

## 🎥 Demo Video

* 📹 Loom Video: 

  https://www.loom.com/share/7c79c836d2de43a48ecca57cab544553

---

## 🎯 Objective

This application simulates real-world trucking logistics by:

* Accepting trip inputs
* Generating optimized routes
* Applying HOS compliance rules
* Producing daily ELD logs

---

## 🧩 Features

### 🔹 User Inputs

* Current Location
* Pickup Location
* Dropoff Location
* Cycle Used (Hours)

---

### 🔹 Outputs

#### 🗺️ Route Visualization

* Interactive map using Leaflet
* Real-time route plotting

#### 📊 Trip Plan (HOS Based)

* 11-hour driving limit
* 8-hour break rule (30 min)
* 10-hour mandatory rest
* Multi-day trip breakdown

#### 📋 ELD Logs

* Dynamically generated logs for each day
* Visual representation using image processing
* Fully compliant with HOS structure

---

## 🧠 HOS Logic Implemented

* ✅ 11-hour daily driving limit
* ✅ 8-hour break rule (30 minutes)
* ✅ 10-hour rest period
* ✅ 70-hour / 8-day cycle limit
* ✅ 34-hour reset when cycle exceeded

---

## ⛽ Assumptions

* Property-carrying driver
* Fuel stop every ~1000 miles (~1600 km)
* Pickup time = 1 hour
* Dropoff time = 1 hour
* No adverse driving conditions

---

## 🏗️ Tech Stack

### 🔹 Backend

* Python
* Django
* Django REST Framework
* Pillow (ELD log generation)

### 🔹 Frontend

* React.js
* Axios
* React Leaflet (Map rendering)

### 🔹 APIs

* OpenRouteService API (Geocoding + Routing)

---

## 📁 Project Structure

```
trip-planner-app/
│
├── backend/
│   ├── api/            # APIs (views, routes)
│   ├── hos/            # HOS logic engine
│   ├── logs/           # ELD log generator
│   └── trip_planner/   # Django settings
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
```

---

## ⚙️ Local Setup

### 🔹 Backend Setup

```bash
cd backend
pip install -r requirements.txt
python manage.py runserver
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🚀 Deployment

| Service  | Platform |
| -------- | -------- |
| Backend  | Render   |
| Frontend | Vercel   |

---

## 💡 Key Highlights

* 🚀 Full-stack production-ready app
* 📍 Real-time route calculation
* 📊 Accurate HOS compliance engine
* 🖼️ Dynamic ELD log generation (image-based)
* ⚡ Clean and responsive UI
* 🌐 Fully deployed and live

---

## 🧠 Challenges Solved

* Handling multi-day trip logic
* Implementing real-world HOS rules
* Generating ELD logs dynamically
* Managing API failures and edge cases
* Fixing deployment issues (media, CORS, etc.)

---

## 🔮 Future Improvements

* User authentication & profiles
* Trip history saving
* Cloud storage (AWS S3 / Cloudinary)
* Advanced UI/UX improvements
* Real-time traffic integration

---

## 👨‍💻 Author

**Aman Verma**
Python Backend Developer | Django | React

---

## 🙌 Acknowledgements

* OpenRouteService API
* React Leaflet
* Django REST Framework

---

## ⭐ Final Note

This project was built as part of a full-stack assessment to demonstrate:

* Backend architecture
* API integration
* Frontend development
* Real-world problem solving

---

🔥 *Thank you for reviewing this project!*
