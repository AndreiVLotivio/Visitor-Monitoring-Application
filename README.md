# Visitor Monitoring Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-80%25-blue.svg)](https://www.python.org/)
[![HTML](https://img.shields.io/badge/HTML-20%25-orange.svg)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Repository](https://img.shields.io/badge/GitHub-AndreiVLotivio%2FVisitor--Monitoring--Application-black.svg)](https://github.com/AndreiVLotivio/Visitor-Monitoring-Application)

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Contributing](#contributing)
- [Support](#support)

---

## 🎯 Overview

The **Visitor Monitoring Application** is a comprehensive solution designed to track, monitor, and manage visitor information and statistics. This application combines a robust Python backend with an intuitive HTML/CSS frontend to provide real-time monitoring capabilities and detailed analytics.

The system enables organizations to:
- Track visitor arrivals and departures
- Monitor visitor patterns and trends
- Generate comprehensive reports
- Manage visitor data efficiently
- Provide secure access control

---

## ✨ Features

### Core Functionality
- **Real-Time Visitor Tracking**: Monitor active visitors in real-time
- **Check-in/Check-out System**: Automated visitor entry and exit logging
- **Visitor Database**: Comprehensive storage of visitor information
- **Analytics Dashboard**: Visual representation of visitor data and trends
- **Report Generation**: Export visitor statistics and reports

### User Interface
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Intuitive Dashboard**: Easy-to-use interface for monitoring activities
- **Search & Filter**: Quickly find visitor information
- **Real-time Updates**: Live data synchronization

### Security Features
- **Access Control**: Role-based permissions for different user types
- **Data Validation**: Input sanitization and verification
- **Secure Storage**: Protected visitor data management

---

## 🛠️ Technology Stack

### Backend
- **Python**
  - Web framework for API development
  - Database operations and business logic
  - Data processing and analytics

### Frontend
- **HTML**
  - User interface and templates
  - Responsive web design
  - Data visualization

### Additional Technologies
- Database management system
- RESTful API architecture
- Client-side scripting (JavaScript)
- CSS styling

---

## 📁 Project Structure

```
Visitor-Monitoring-Application/
├── README.md                 # Project documentation
├── LICENSE                   # MIT License
├── backend/                  # Python backend
│   ├── app.py               # Main application file
│   ├── models/              # Database models
│   ├── routes/              # API endpoints
│   ├── utils/               # Utility functions
│   └── config.py            # Configuration settings
├── frontend/                # HTML/CSS frontend
│   ├── index.html           # Home page
│   ├── dashboard.html       # Main dashboard
│   ├── css/                 # Stylesheets
│   └── js/                  # JavaScript files
├── database/                # Database files
├── requirements.txt         # Python dependencies
└── .gitignore              # Git ignore rules
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Modern web browser
- Git

### Setup Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AndreiVLotivio/Visitor-Monitoring-Application.git
   cd Visitor-Monitoring-Application
   ```

2. **Create Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Application**
   - Update `backend/config.py` with your settings
   - Set up database connection parameters
   - Configure API endpoints

5. **Run the Application**
   ```bash
   python backend/app.py
   ```

6. **Access the Application**
   - Open your browser and navigate to `http://localhost:5000`
   - Login with your credentials

---

## 📖 Usage

### Basic Operations

#### Check-in Visitor
1. Navigate to the Check-in section
2. Enter visitor information (name, company, purpose)
3. Click "Check-in" to log arrival

#### Check-out Visitor
1. Search for the visitor using their ID or name
2. Click "Check-out" to log departure

#### View Dashboard
- Access real-time statistics of current visitors
- View historical trends and patterns
- Monitor visitor flow throughout the day

#### Generate Reports
1. Select date range
2. Choose report type
3. Click "Generate" to download report

---

## ⚙️ Configuration

### Environment Variables
Create a `.env` file in the root directory:

```
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///visitors.db
SECRET_KEY=your_secret_key_here
API_PORT=5000
API_HOST=0.0.0.0
```

### Database Configuration
Update database settings in `backend/config.py`:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///visitors.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
```

---

## 🔌 API Endpoints

### Visitor Management
- `GET /api/visitors` - Get all visitors
- `POST /api/visitors` - Create new visitor record
- `GET /api/visitors/<id>` - Get specific visitor
- `PUT /api/visitors/<id>` - Update visitor information
- `DELETE /api/visitors/<id>` - Delete visitor record

### Check-in/Check-out
- `POST /api/checkin` - Record visitor check-in
- `POST /api/checkout/<id>` - Record visitor check-out
- `GET /api/active-visitors` - Get currently active visitors

### Reports
- `GET /api/reports/daily` - Daily visitor report
- `GET /api/reports/monthly` - Monthly statistics
- `GET /api/reports/export` - Export visitor data

---

## 🗄️ Database

### Tables

#### Visitors
- `id` (Primary Key)
- `name` (String)
- `company` (String)
- `email` (String)
- `phone` (String)
- `purpose` (String)
- `created_at` (DateTime)
- `updated_at` (DateTime)

#### Check-in Records
- `id` (Primary Key)
- `visitor_id` (Foreign Key)
- `check_in_time` (DateTime)
- `check_out_time` (DateTime)
- `location` (String)
- `notes` (Text)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/AndreiVLotivio/Visitor-Monitoring-Application.git
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Write clean, readable code
   - Follow PEP 8 for Python code
   - Add comments for complex logic

4. **Commit Changes**
   ```bash
   git commit -m "Add your descriptive commit message"
   ```

5. **Push to Branch**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open Pull Request**
   - Provide clear description of changes
   - Reference any related issues

---

## 📞 Support

For support and inquiries:

- **GitHub Issues**: [Report bugs or request features](https://github.com/AndreiVLotivio/Visitor-Monitoring-Application/issues)
- **Email**: Contact via GitHub profile
- **Documentation**: Check the [docs](./docs) folder for detailed guides

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Primary Language | HTML (55%) |
| Backend Language | Python (45%) |
| Repository ID | 1244461591 |
| License | MIT |

---

## 🔒 License Information

```
MIT License

Copyright (c) 2026 Andrei V Lotivio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🎉 Acknowledgments

Thank you for your interest in the Visitor Monitoring Application! This project demonstrates best practices in web application development with modern Python and HTML technologies.

---

**Last Updated**: May 20, 2026  
**Repository**: [AndreiVLotivio/Visitor-Monitoring-Application](https://github.com/AndreiVLotivio/Visitor-Monitoring-Application)
