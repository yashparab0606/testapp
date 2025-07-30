# 🏥 MediTrack - Medical Store Inventory Management System

MediTrack is a Django-based web application that simplifies inventory management, prescription processing, billing, and medicine recommendation for medical stores. It also helps patients find the nearest stores stocking the required medicines, saving time during emergencies.

## 🚀 Features

### 🧾 Prescription Image-to-Text Conversion
- Upload handwritten prescriptions.
- Uses OCR (Tesseract or similar) to extract medicine names from prescription images.

### 💊 Medicine Recommendation System
- Suggests alternative medicines based on chemical composition or brand.
- Helps when prescribed medicine is unavailable.

### 🛒 Billing Dashboard
- Add medicines to cart with selected quantity.
- Automatically calculates bill.
- Printable invoice generation.
- Transaction history saved in the database.

### 🗺️ Nearby Store Finder
- Integration with Google Maps API.
- Users can find nearby pharmacies that stock the required medicines.
- Displays distance and directions.

### 📈 Stock & Profit Analysis
- Monthly profit/loss graphs for medical stores.
- Alerts on low stock or expiring medicines.

### 💬 Chatbot Support
- AI-based assistant to answer basic medicine or store queries.

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **APIs**: Google Maps API
- **OCR**: Tesseract OCR / pytesseract (for prescription text extraction)
- **ML**: Scikit-learn / Custom models for recommendation & expiry prediction
