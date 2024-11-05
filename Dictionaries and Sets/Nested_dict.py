complex_nested_dict = {
    "company": {
        "name": "Tech Solutions",
        "location":  {
            "city": "New York",
            "address": {
                "street": "123 Innovation Drive",
                "postal_code": "10001"
            }
        },
        "employees": [
            {
                "name": "Alice",
                "age": 30,
                "role": "Developer",
                "skills": ["Python", "Django", "React"],
                "projects": {
                    "ongoing": ["AI Assistant", "E-Commerce App"],
                    "completed": ["Weather App", "Finance Tracker"]
                }
            },
            {
                "name": "Bob",
                "age": 28,
                "role": "Data Scientist",
                "skills": ["Python", "Pandas", "Machine Learning"],
                "projects": {
                    "ongoing": ["Customer Insights", "Ad Optimization"],
                    "completed": ["Sales Forecasting", "Churn Prediction"]
                }
            }
        ],
        "departments": {
           "development": {
                "team_lead": "Charlie",
                "budget": 200000,
                "team_size": 5
            },
            "marketing": {
                "team_lead": "Diana",
                "budget": 150000,
                "team_size": 3
            }
        },
        "partnerships": [
            {
                "partner_name": "FinTech Corp",
                "since": 2018,
                "services": ["Payment Processing", "Fraud Detection"]
            },
            {
                "partner_name": "Data Analytics Ltd",
                "since": 2020,
                "services": ["Big Data Analysis", "Cloud Storage"]
            }
        ]
    }
}
