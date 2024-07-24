import json

def lambda_handler(event, context):
    print(event)

    employee_data = [
    {
        "EmpID": 1,
        "Name": "John Doe",
        "Email": "john.doe@example.com",
        "Role": "Software Developer",
        "Skills": "Java, Spring Boot, SQL",
        "Achievements": "Employee of the Month - Jan 2023, Certified Java Developer",
        "Experience": "5 years"
    },
    {
        "EmpID": 2,
        "Name": "Jane Smith",
        "Email": "jane.smith@example.com",
        "Role": "Data Engineer",
        "Skills": "Python, Apache Spark, Hadoop",
        "Achievements": "Best Innovator Award - 2022, Certified Data Engineer",
        "Experience": "4 years"
    },
    {
        "EmpID": 3,
        "Name": "Alice Johnson",
        "Email": "alice.johnson@example.com",
        "Role": "Data Scientist",
        "Skills": "Python, Machine Learning, TensorFlow",
        "Achievements": "Employee of the Month - Mar 2023, Certified Data Scientist",
        "Experience": "3 years"
    },
    {
        "EmpID": 4,
        "Name": "Bob Brown",
        "Email": "bob.brown@example.com",
        "Role": "Cloud Engineer",
        "Skills": "AWS, Kubernetes, Docker",
        "Achievements": "Top Performer - 2022, Certified AWS Solutions Architect",
        "Experience": "6 years"
    },
    {
        "EmpID": 5,
        "Name": "Eve Davis",
        "Email": "eve.davis@example.com",
        "Role": "HR",
        "Skills": "Recruitment, Employee Relations, Payroll",
        "Achievements": "Employee of the Year - 2022, Certified HR Professional",
        "Experience": "4 years"
    },
    {
        "EmpID": 6,
        "Name": "Frank Wilson",
        "Email": "frank.wilson@example.com",
        "Role": "Database Engineer",
        "Skills": "MySQL, PostgreSQL, Oracle",
        "Achievements": "Best Database Engineer - 2023, Certified Database Administrator",
        "Experience": "5 years"
    },
    {
        "EmpID": 7,
        "Name": "Grace Lee",
        "Email": "grace.lee@example.com",
        "Role": "Full Stack Developer",
        "Skills": "JavaScript, React, Node.js",
        "Achievements": "Top Full Stack Developer - 2022, Certified Full Stack Developer",
        "Experience": "4 years"
    },
    {
        "EmpID": 8,
        "Name": "Hank Green",
        "Email": "hank.green@example.com",
        "Role": "Data Analyst",
        "Skills": "SQL, Tableau, R",
        "Achievements": "Best Data Analyst - 2023, Certified Data Analyst",
        "Experience": "3 years"
    },
    {
        "EmpID": 9,
        "Name": "Ivy White",
        "Email": "ivy.white@example.com",
        "Role": "IT Specialist",
        "Skills": "Network Security, Linux, Windows Server",
        "Achievements": "Employee of the Month - Apr 2023, Certified IT Specialist",
        "Experience": "4 years"
    },
    {
        "EmpID": 10,
        "Name": "Uma Patel",
        "Email": "uma.patel@example.com",
        "Role": "Data Analyst",
        "Skills": "Excel, Python, Power BI",
        "Achievements": "Employee of the Month - Sep 2023, Certified Data Analyst",
        "Experience": "3 years"
    },
    {
        "EmpID": 11,
        "Name": "Victor Scott",
        "Email": "victor.scott@example.com",
        "Role": "IT Specialist",
        "Skills": "Network Administration, Cybersecurity, Linux",
        "Achievements": "Best IT Specialist - 2023, Certified Information Systems Security Professional (CISSP)",
        "Experience": "4 years"
    },
    {
        "EmpID": 12,
        "Name": "Wendy Moore",
        "Email": "wendy.moore@example.com",
        "Role": "Tech Support",
        "Skills": "Technical Troubleshooting, Customer Support, CRM",
        "Achievements": "Top Support Specialist - 2022, Certified Help Desk Technician",
        "Experience": "5 years"
    },
    {
        "EmpID": 13,
        "Name": "Xander Brooks",
        "Email": "xander.brooks@example.com",
        "Role": "Java Developer",
        "Skills": "Java, Spring Boot, Microservices",
        "Achievements": "Employee of the Month - Oct 2023, Certified Java Developer",
        "Experience": "6 years"
    },
    {
        "EmpID": 14,
        "Name": "Yara Cooper",
        "Email": "yara.cooper@example.com",
        "Role": "Business Analyst",
        "Skills": "Requirements Analysis, SQL, Agile Methodologies",
        "Achievements": "Top Business Analyst - 2023, Certified Business Analyst Professional (CBAP)",
        "Experience": "4 years"
    },
    {
        "EmpID": 15,
        "Name": "Zachary Fisher",
        "Email": "zachary.fisher@example.com",
        "Role": "Senior Vice President",
        "Skills": "Leadership, Strategic Planning, Financial Management",
        "Achievements": "Executive of the Year - 2023, Certified Executive Leader",
        "Experience": "15 years"
    },
    {
        "EmpID": 16,
        "Name": "Abigail Reed",
        "Email": "abigail.reed@example.com",
        "Role": "Software Developer",
        "Skills": "C#, .NET Core, Azure",
        "Achievements": "Employee of the Month - Nov 2023, Certified .NET Developer",
        "Experience": "5 years"
    },
    {
        "EmpID": 17,
        "Name": "Brandon Kim",
        "Email": "brandon.kim@example.com",
        "Role": "Data Engineer",
        "Skills": "Python, Apache Kafka, SQL",
        "Achievements": "Top Data Engineer - 2023, Certified Data Engineer",
        "Experience": "4 years"
    },
    {
        "EmpID": 18,
        "Name": "Charlotte White",
        "Email": "charlotte.white@example.com",
        "Role": "Data Scientist",
        "Skills": "Python, Scikit-Learn, Big Data",
        "Achievements": "Employee of the Month - Dec 2023, Certified Data Scientist",
        "Experience": "3 years"
    },
    {
        "EmpID": 19,
        "Name": "Daniel Lee",
        "Email": "daniel.lee@example.com",
        "Role": "Cloud Engineer",
        "Skills": "AWS, Terraform, Docker",
        "Achievements": "Best Cloud Engineer - 2023, Certified AWS Solutions Architect",
        "Experience": "6 years"
    },
    {
        "EmpID": 20,
        "Name": "Sunny SH",
        "Email": "sunny.sh@example.com",
        "Role": "Business Analyst",
        "Skills": "PowerBI",
        "Achievements": "Certified Power BI Analyst",
        "Experience": "4 years"
    }
 ]

    def get_named_parameter(event, name):
        return next(item for item in event['parameters'] if item['name'] == name)['value']

    def get_named_property(event, name):
        return next(item for item in event['requestBody']['content']['application/json']['properties'] if item['name'] == name)['value']

    def employeeDetails(event):
        EmpId = get_named_parameter(event, 'name')
        print("Employee Id: ", EmpId)
        for emp_info in employee_data:
            if emp_info["EmpID"] == EmpId:
                return emp_info
        return None

    result = ''
    response_code = 200
    action_group = event['actionGroup']
    api_path = event['apiPath']

    print("api_path: ", api_path)

    if api_path == '/employeeDetails':
        result = employeeDetails(event)
    else:
        response_code = 404
        result = f"Unrecognized api path: {action_group}::{api_path}"

    response_body = {
        'application/json': {
            'body': result
        }
    }

    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': event['apiPath'],
        'httpMethod': event['httpMethod'],
        'httpStatusCode': response_code,
        'responseBody': response_body
    }

    api_response = {'messageVersion': '1.0', 'response': action_response}
    return api_response
