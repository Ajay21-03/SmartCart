# 🛒 Smart Cart Pro - GrocMed

A Smart Grocery & Medicine Interaction Alert System designed to simplify inventory management and ensure safe purchases for customers. This web application helps small retail store owners track stock, manage expiry alerts, and warn customers about medicine interactions.

---

## 🚀 Features

### 🛍️ For Store Owners:
- Intelligent inventory tracking
- Expiry date alerts for groceries & medicines
- Low stock detection with restock logs
- Product category and supplier management
- Admin panel with secure login

### 👨‍⚕️ For Customers:
- Easy browsing and ordering of groceries/medicines
- Real-time expiry warnings
- Medicine interaction alerts (based on predefined interaction rules)
- Safe shopping experience

---

## 🗃️ Database Design

Built on **PostgreSQL**, the schema uses:
- ✅ **Triggers**
- ✅ **Views**
- ✅ **Stored Procedures**
- ✅ **Normalization**

### 📌 Key Tables:
- `Customer`, `Product`, `Category`, `Supplier`
- `Sales`, `Sale_Items` (weak entity)
- `Restock_Log`, `Inventory`
- `Expiry_Alert`, `Login_Log`
- `User` (admin or staff)

---

## 🛠️ Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Frontend     | HTML, CSS, Jinja2      |
| Backend      | Python (Flask)         |
| Database     | PostgreSQL + psycopg2  |
| Styling      | Bootstrap (optional)   |
| Versioning   | Git, GitHub            |

---

## 📷 Screenshots :
Front Page
![image](https://github.com/user-attachments/assets/c46b9420-2a26-4018-8126-072a572a8404)

Admin Login:
![image](https://github.com/user-attachments/assets/484f209f-896e-4e4a-9de0-88603525cbe5)

---

## 🧪 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/SmartCartPro.git
   cd SmartCartPro
   ```

2. **Create & Activate Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL DB**
   - Create a PostgreSQL database.
   - Update your DB credentials in `config.py` or `.env`.

5. **Run the App**
   ```bash
   python app.py
   ```

6. **Visit in Browser**
   ```
   http://127.0.0.1:5000/
   ```

---

## ✅ Future Enhancements
- Medicine barcode scanning
- Email notifications for expiry/restock
- Role-based access control
- Docker containerization
- REST API for mobile app integration

---

## 🙋 About the Developer

**Ajay**  
B.Tech IT Student, PSG College of Technology  
> Passionate about building intelligent systems that make everyday tasks easier.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## ⭐ Don't forget to star the repo if you find it helpful!
