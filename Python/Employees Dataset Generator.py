import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialize Faker
fake = Faker('en_NZ')
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# Dataset Size
num_records = 1472

# Regions & Locations
regions_locations = {
    'Auckland': ['Auckland City', 'New Lynn', 'Albany', 'Manukau'],
    'Christchurch': ['Cathedral Square', 'Colombo Street'],
    'Wellington': ['Wellington City', 'Porirua', 'Lower Hutt'],

}
regions = list(regions_locations.keys())
region_prob = [0.5, 0.2, 0.3]
assigned_regions = np.random.choice(regions, size=num_records, p=region_prob)
assigned_locations = [np.random.choice(regions_locations[region]) for region in assigned_regions]

# Departments & Roles
departments = ['HR', 'IT', 'Sales', 'Marketing', 'Finance', 'Operations', 'Customer Service']
departments_prob = [0.02, 0.15, 0.21, 0.08, 0.05, 0.30, 0.19]
jobtitles = {
    'HR': ['HR Manager', 'HR Coordinator', 'Recruiter', 'HR Assistant'],
    'IT': ['IT Manager', 'Software Developer', 'System Administrator', 'IT Support Specialist'],
    'Sales': ['Sales Manager', 'Sales Consultant', 'Sales Specialist', 'Sales Representative'],
    'Marketing': ['Marketing Manager', 'SEO Specialist', 'Content Creator', 'Marketing Coordinator'],
    'Finance': ['Finance Manager', 'Accountant', 'Financial Analyst', 'Accounts Payable Specialist'],
    'Operations': ['Operations Manager', 'Operations Analyst', 'Logistics Coordinator', 'Inventory Specialist'],
    'Customer Service': ['Customer Service Manager', 'Customer Service Representative', 'Support Specialist', 'Help Desk Technician']
}
jobtitles_prob = {
    'HR': [0.03, 0.3, 0.47, 0.2],  # HR Manager, HR Coordinator, Recruiter, HR Assistant
    'IT': [0.02, 0.47, 0.2, 0.31],  # IT Manager, Software Developer, System Administrator, IT Support Specialist
    'Sales': [0.03, 0.25, 0.32, 0.4],  # Sales Manager, Sales Consultant, Sales Specialist, Sales Representative
    'Marketing': [0.04, 0.25, 0.41, 0.3],  # Marketing Manager, SEO Specialist, Content Creator, Marketing Coordinator
    'Finance': [0.03, 0.37, 0.4, 0.2],  # Finance Manager, Accountant, Financial Analyst, Accounts Payable Specialist
    'Operations': [0.02, 0.2, 0.4, 0.38],  # Operations Manager, Operations Analyst, Logistics Coordinator, Inventory Specialist
    'Customer Service': [0.04, 0.3, 0.38, 0.28]  # Customer Service Manager, Customer Service Representative, Support Specialist, Help Desk Technician
}

# Education Levels
educations = ['High School', "Bachelor", "Master", 'PhD']

education_mapping = {
    'HR Manager': ["Master", "PhD"],
    'HR Coordinator': ["Bachelor", "Master"],
    'Recruiter': ["High School", "Bachelor"],
    'HR Assistant': ["High School", "Bachelor"],
    'IT Manager': ["PhD", "Master"],
    'Software Developer': ["Bachelor", "Master"],
    'System Administrator': ["Bachelor", "Master"],
    'IT Support Specialist': ["High School", "Bachelor"],
    'Sales Manager': ["Master","PhD"],
    'Sales Consultant': ["Bachelor", "Master", "PhD"],
    'Sales Specialist': ["Bachelor", "Master", "PhD"],
    'Sales Representative': ["Bachelor"],
    'Marketing Manager': ["Bachelor", "Master","PhD"],
    'SEO Specialist': ["High School", "Bachelor"],
    'Content Creator': ["High School", "Bachelor"],
    'Marketing Coordinator': ["Bachelor"],
    'Finance Manager': ["Master", "PhD"],
    'Accountant': ["Bachelor"],
    'Financial Analyst': ["Bachelor", "Master", "PhD"],
    'Accounts Payable Specialist': ["Bachelor"],
    'Operations Manager': ["Bachelor", "Master"],
    'Operations Analyst': ["Bachelor", "Master"],
    'Logistics Coordinator': ["Bachelor"],
    'Inventory Specialist': ["High School", "Bachelor"],
    'Customer Service Manager': ["Bachelor", "Master", "PhD"],
    'Customer Service Representative': ["High School", "Bachelor"],
    'Support Specialist': ["High School", "Bachelor"],
    'Customer Success Manager': ["Bachelor", "Master", "PhD"],
    'Help Desk Technician': ["High School", "Bachelor"]
}

# Hiring Date
# Define custom probability weights for each year
year_weights = {
    2015: 2,   
    2016: 6,  
    2017: 17,  
    2018: 9,  
    2019: 10,  
    2020: 11,  
    2021: 5,  
    2022: 12,  
    2023: 14,  
    2024: 9,   
    2025: 5   
}


# Generate a random date based on custom probabilities
def generate_custom_date(year_weights):
    year = random.choices(list(year_weights.keys()), weights=list(year_weights.values()))[0]
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Assuming all months have 28 days for simplicity
    return fake.date_time_between(start_date=datetime(year, 1, 1), end_date=datetime(year, 12, 31))


def generate_salary(department, job_title):
    def salary_steps(min_sal, max_sal):
        return random.choice(list(range(min_sal, max_sal+1, 1000)))

    salary_dict = {
            'HR': {
                'HR Manager': salary_steps(70000, 110000),
                'HR Coordinator': salary_steps(50000, 60000),
                'Recruiter': salary_steps(50000, 70000),
                'HR Assistant': salary_steps(50000, 60000)
            },
            'IT': {
                'IT Manager': salary_steps(80000, 120000),
                'Software Developer': salary_steps(70000, 95000),
                'System Administrator': salary_steps(60000, 90000),
                'IT Support Specialist': salary_steps(50000, 60000)
            },
            'Sales': {
                'Sales Manager': salary_steps(70000, 110000),
                'Sales Consultant': salary_steps(60000, 90000),
                'Sales Specialist': salary_steps(50000, 80000),
                'Sales Representative': salary_steps(50000, 70000)
            },
            'Marketing': {
                'Marketing Manager': salary_steps(70000, 100000),
                'SEO Specialist': salary_steps(50000, 80000),
                'Content Creator': salary_steps(50000, 60000),
                'Marketing Coordinator': salary_steps(50000, 70000)
            },
            'Finance': {
                'Finance Manager': salary_steps(80000, 120000),
                'Accountant': salary_steps(50000, 80000),
                'Financial Analyst': salary_steps(60000, 90000),
                'Accounts Payable Specialist': salary_steps(50000, 60000)
            },
            'Operations': {
                'Operations Manager': salary_steps(70000, 100000),
                'Operations Analyst': salary_steps(50000, 80000),
                'Logistics Coordinator': salary_steps(50000, 60000),
                'Inventory Specialist': salary_steps(50000, 60000)
            },
            'Customer Service': {
                'Customer Service Manager': salary_steps(60000, 90000),
                'Customer Service Representative': salary_steps(50000, 60000),
                'Support Specialist': salary_steps(50000, 60000),
                'Help Desk Technician': salary_steps(50000, 80000)
            }
        }
    return salary_dict[department][job_title]

# Generate the dataset
data = []
used_employee_ids = set()  # Track used IDs to ensure uniqueness

for _ in range(num_records):
    # Generate a unique employee ID
    while True:
        employee_id = f"00-{random.randint(10000, 99999)}"
        if employee_id not in used_employee_ids:
            used_employee_ids.add(employee_id)
            break
    
    last_name = fake.last_name()
    gender = np.random.choice(['Female', 'Male'], p=[0.46, 0.54])
    first_name = fake.first_name_female() if gender == 'Female' else fake.first_name_male()
    # Rest of the employee data generation stays the same
    region = np.random.choice(regions, p=region_prob)
    city = np.random.choice(regions_locations[region])
    hiredate = generate_custom_date(year_weights)
    department = np.random.choice(departments, p=departments_prob)
    job_title = np.random.choice(jobtitles[department], p=jobtitles_prob[department])
    education_level = np.random.choice(education_mapping[job_title])
    performance_rating = np.random.choice(['Excellent', 'Good', 'Satisfactory', 'Needs Improvement'], p=[0.12, 0.5, 0.3, 0.08])
    overtime_bonus = np.random.choice(['Yes', 'No'], p=[0.3, 0.7])
    salary = generate_salary(department, job_title)

    data.append([
        employee_id,
        first_name,
        last_name,
        gender,
        region,
        city,
        hiredate,
        department,
        job_title,
        education_level,
        salary,
        performance_rating,
        overtime_bonus
    ])

## Create DataFrame
columns = [
     'employee_id',
     'first_name',
     'last_name',
     'gender',
     'region',
     'city',
     'hiredate',
     'department',
     'job_title',
     'education_level',
     'salary',
     'performance_rating',
     'overtime_bonus'
    ]


df = pd.DataFrame(data, columns=columns)

# Add Birthdate
def generate_birthdate(row):
    age_distribution = {
        'under_25': 0.11,
        '25_34': 0.25,
        '35_44': 0.31,
        '45_54': 0.24,
        'over_55': 0.09
    }
    age_groups = list(age_distribution.keys())
    age_probs = list(age_distribution.values())
    age_group = np.random.choice(age_groups, p=age_probs)

    if any('Manager' in title for title in row['job_title']):
        age = np.random.randint(30, 65)
    elif row['education_level'] == 'PhD':
        age = np.random.randint(27, 65)
    elif age_group == 'under_25':
         age = np.random.randint(20, 25)
    elif age_group == '25_34':
        age = np.random.randint(25, 35)
    elif age_group == '35_44':
        age = np.random.randint(35, 45)
    elif age_group == '45_54':
        age = np.random.randint(45, 55)
    else:
        age = np.random.randint(56, 65)

    birthdate = fake.date_of_birth(minimum_age=age, maximum_age=age)
    return birthdate

# Apply the function to generate birthdates
df['birthdate'] = df.apply(generate_birthdate, axis=1)

# Terminations
# Define termination distribution
year_weights = {
    2015: 5,
    2016: 7,
    2017: 10,
    2018: 12,
    2019: 9,
    2020: 10,
    2021: 20,
    2022: 10,
    2023: 7,
    2024: 10
}

# Calculate the total number of terminated employees
total_employees = num_records
termination_percentage = 0.23  # 11.2%
total_terminated = int(total_employees * termination_percentage)

# Generate termination dates based on distribution
termination_dates = []
for year, weight in year_weights.items():
    num_terminations = int(total_terminated * (weight / 100))
    termination_dates.extend([year] * num_terminations)

# Randomly shuffle the termination dates
random.shuffle(termination_dates)

# Assign termination dates to terminated employees
terminated_indices = df.index[:total_terminated]
for i, year in enumerate(termination_dates[:total_terminated]):
    df.at[terminated_indices[i], 'termination_date'] = datetime(year, 1, 1) + timedelta(days=random.randint(0, 365))


# Assign None to termination_date for employees who are not terminated
df['termination_date'] = df['termination_date'].where(df['termination_date'].notnull(), None)

# Ensure termination_date is at least 6 months after hiredate
df['termination_date'] = df.apply(lambda row: row['hiredate'] + timedelta(days=180) if row['termination_date'] and row['termination_date'] < row['hiredate'] + timedelta(days=180) else row['termination_date'], axis=1)

education_multiplier = {
    'High School': {'Male': 1.03, 'Female': 1.0},
    "Bachelor": {'Male': 1.115, 'Female': 1.0},
    "Master": {'Male': 1.0, 'Female': 1.07},
    'PhD': {'Male': 1.0, 'Female': 1.17}
}


# Function to calculate age from birthdate
def calculate_age(birthdate):
    today = pd.Timestamp('today')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Function to calculate the adjusted salary
def calculate_adjusted_salary(row):
    base_salary = row['salary']
    gender = row['gender']
    education = row['education_level']
    age = calculate_age(row['birthdate'])

    # Apply education multiplier
    multiplier = education_multiplier.get(education, {}).get(gender, 1.0)
    adjusted_salary = base_salary * multiplier

    # Apply age increment (between 0.1% and 0.3% per year of age)
    age_increment = 1 + np.random.uniform(0.001, 0.003) * age
    adjusted_salary *= age_increment

    # Ensure the adjusted salary is not lower than the base salary
    adjusted_salary = max(adjusted_salary, base_salary)

    # Round the adjusted salary to the nearest integer
    return round(adjusted_salary/1000) * 1000

# Apply the function to the DataFrame
df['salary'] = df.apply(calculate_adjusted_salary, axis=1)

# Convert 'hiredate' and 'birthdate' to datetime
df['hiredate'] = pd.to_datetime(df['hiredate']).dt.date
df['birthdate'] = pd.to_datetime(df['birthdate']).dt.date
df['termination_date'] = pd.to_datetime(df['termination_date']).dt.date

print(df)

# Save to CSV
df.to_csv('EternaEmployees.csv', index=False)