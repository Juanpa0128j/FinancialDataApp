# Financial Data App

A comprehensive Django web application for financial data analysis and stock portfolio management. This application fetches real-time financial data from Yahoo Finance, calculates custom financial scores, and provides an intuitive interface for organizing and analyzing stock investments.

## 🚀 Features

### Core Functionality
- **Real-time Stock Data**: Fetch current financial metrics from Yahoo Finance API
- **Custom Financial Scoring**: Proprietary algorithm that evaluates stocks based on multiple financial indicators
- **Category Management**: Organize stocks into custom categories for better portfolio management
- **Data Visualization**: Clean, sortable tables displaying comprehensive financial metrics
- **Bulk Operations**: Add multiple stocks simultaneously and perform batch operations

### Financial Metrics Tracked
- **Debt to Equity Ratio**: Company's financial leverage
- **Insider Holdings**: Percentage of shares held by company insiders
- **Price Analysis**: Current price vs. target price with upside calculation
- **Valuation Ratios**: Trailing and forward P/E ratios
- **Earnings Data**: Trailing and forward earnings per share (EPS)
- **Profitability Metrics**: Return on Assets (ROA), Return on Equity (ROE), and profit margins
- **Custom Score**: Weighted composite score based on all financial factors

### User Interface Features
- **Interactive Tables**: Sort by any financial metric
- **Category Filtering**: View stocks by category or all stocks
- **Bulk Selection**: Select multiple stocks for batch operations
- **Real-time Updates**: Refresh financial data with a single click
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Backend**: Django 5.0
- **Database**: MySQL (configured for production) / SQLite (development)
- **Financial Data API**: Yahoo Finance via `yfinance` library
- **Data Processing**: pandas, numpy
- **Frontend**: HTML5, CSS3, JavaScript
- **Web Scraping**: BeautifulSoup4, lxml
- **HTTP Requests**: requests library

## 📋 Prerequisites

- Python 3.8+
- MySQL (for production) or SQLite (for development)
- Internet connection (for fetching financial data)

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Juanpa0128j/FinancialDataApp.git
cd FinancialDataApp
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration

#### For Development (SQLite)
Update `webSite/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### For Production (MySQL)
The application is pre-configured for MySQL. Update the database credentials in `webSite/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'HOST': 'your_host',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'PORT': 3306,
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Start Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📖 Usage Guide

### Adding Stocks

1. **Single Stock**: Enter a stock symbol (e.g., "AAPL") in the create tag form
2. **Multiple Stocks**: Enter comma-separated symbols (e.g., "AAPL, GOOGL, MSFT")
3. The application will automatically fetch financial data and calculate scores

### Managing Categories

1. **Create Category**: Use the dropdown menu to add new categories
2. **Add Stocks to Category**: Select stocks and choose target categories
3. **Transfer Between Categories**: Move stocks from one category to another
4. **Delete Categories**: Remove categories and their associations

### Analyzing Data

1. **Sorting**: Click on any column header to sort by that metric
2. **Filtering**: Use category dropdown to filter stocks
3. **Updating**: Click "Update data from tag/s" to refresh financial information
4. **Custom Score**: Higher scores indicate better financial performance based on the algorithm

### Understanding the Financial Score

The custom scoring algorithm evaluates stocks based on:
- **Debt Management**: Lower debt-to-equity ratios score higher
- **Insider Confidence**: Higher insider ownership indicates confidence
- **Growth Potential**: Positive difference between target and current price
- **Valuation**: Reasonable P/E ratios and improving earnings
- **Profitability**: Strong ROA, ROE, and profit margins

## 🏗️ Project Structure

```
FinancialDataApp/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── webSite/                 # Django project settings
│   ├── settings.py          # Application configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
└── webApp/                  # Main application
    ├── models.py            # Database models (Tag, Category)
    ├── views.py             # Business logic and request handling
    ├── forms.py             # Django forms
    ├── admin.py             # Django admin configuration
    ├── cron.py              # Scheduled tasks
    ├── templates/           # HTML templates
    │   ├── home.html        # Main dashboard
    │   ├── create_tag.html  # Stock creation form
    │   └── ...
    ├── static/              # CSS, JavaScript, images
    │   ├── css/
    │   ├── js/
    │   └── favicon.png
    └── yahoo_query/         # Financial data fetching module
        └── financial_analysis.py
```

## 🔄 API Endpoints

- `/` - Main dashboard (home)
- `/create_tag/` - Add new stocks
- `/visualize_category/` - Filter by category
- `/delete_tag/` - Remove stocks
- `/delete_category/` - Remove categories
- `/tag_ordering/` - Sort functionality
- `/update_tag/` - Refresh financial data
- `/add_tag_to_category/` - Category management
- `/transfer_tag_between_categories/` - Move stocks between categories

## 🚀 Deployment

### PythonAnywhere (Recommended)

The application is pre-configured for PythonAnywhere deployment:

1. Upload code to PythonAnywhere
2. Configure MySQL database
3. Update `ALLOWED_HOSTS` in settings.py
4. Set up static files serving
5. Configure WSGI file

### Other Platforms

For deployment on other platforms:

1. Update `ALLOWED_HOSTS` in settings.py
2. Configure database settings
3. Set `DEBUG = False` for production
4. Configure static files serving
5. Set up environment variables for sensitive data

## 🔧 Configuration

### Environment Variables (Recommended for Production)

Create a `.env` file:
```
SECRET_KEY=your-secret-key
DEBUG=False
DATABASE_URL=mysql://user:password@host:port/database
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### Scheduled Updates

The application includes a cron job script (`webApp/cron.py`) for automated data updates. Configure your server's cron to run:
```bash
0 9 * * 1-5 python /path/to/your/app/webApp/cron.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Disclaimer

This application is for educational and informational purposes only. The financial data and scores provided should not be considered as investment advice. Always consult with qualified financial advisors before making investment decisions.

## 🐛 Known Issues

- Financial data depends on Yahoo Finance API availability
- Some stocks may not have complete financial data
- Scores are calculated based on available data only

## 📞 Support

For support, please open an issue on GitHub or contact the development team.

## 🔮 Future Enhancements

- [ ] Add more financial metrics and ratios
- [ ] Implement user authentication and personal portfolios
- [ ] Add data visualization charts and graphs
- [ ] Include news sentiment analysis
- [ ] Add export functionality (CSV, PDF)
- [ ] Implement real-time price alerts
- [ ] Add mobile app support
- [ ] Include cryptocurrency support

---

**Built with ❤️ for financial analysis enthusiasts**