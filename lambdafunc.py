
import json

def lambda_handler(event, context):
    print(event)

    employee_data = [
        {
            "EmpID": "E001",
            "Name": "John Doe",
            "Email": "john.doe@example.com",
            "Role": "Software Developer",
            "Skills": "Java, Spring Boot, SQL",
            "Achievements": "Employee of the Month - Jan 2023, Certified Java Developer",
            "Experience": "5 years"
        },
        {
            "EmpID": "E002",
            "Name": "Jane Smith",
            "Email": "jane.smith@example.com",
            "Role": "Data Engineer",
            "Skills": ["Python", "Apache Spark", "Hadoop"],
            "Achievements": ["Best Innovator Award - 2022", "Certified Data Engineer"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E003",
            "Name": "Alice Johnson",
            "Email": "alice.johnson@example.com",
            "Role": "Data Scientist",
            "Skills": ["Python", "Machine Learning", "TensorFlow"],
            "Achievements": ["Employee of the Month - Mar 2023", "Certified Data Scientist"],
            "Experience": "3 years"
        },
        {
            "EmpID": "E004",
            "Name": "Bob Brown",
            "Email": "bob.brown@example.com",
            "Role": "Cloud Engineer",
            "Skills": ["AWS", "Kubernetes", "Docker"],
            "Achievements": ["Top Performer - 2022", "Certified AWS Solutions Architect"],
            "Experience": "6 years"
        },
        {
            "EmpID": "E005",
            "Name": "Eve Davis",
            "Email": "eve.davis@example.com",
            "Role": "HR",
            "Skills": ["Recruitment", "Employee Relations", "Payroll"],
            "Achievements": ["Employee of the Year - 2022", "Certified HR Professional"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E006",
            "Name": "Frank Wilson",
            "Email": "frank.wilson@example.com",
            "Role": "Database Engineer",
            "Skills": ["MySQL", "PostgreSQL", "Oracle"],
            "Achievements": ["Best Database Engineer - 2023", "Certified Database Administrator"],
            "Experience": "5 years"
        },
        {
            "EmpID": "E007",
            "Name": "Grace Lee",
            "Email": "grace.lee@example.com",
            "Role": "Full Stack Developer",
            "Skills": ["JavaScript", "React", "Node.js"],
            "Achievements": ["Top Full Stack Developer - 2022", "Certified Full Stack Developer"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E008",
            "Name": "Hank Green",
            "Email": "hank.green@example.com",
            "Role": "Data Analyst",
            "Skills": ["SQL", "Tableau", "R"],
            "Achievements": ["Best Data Analyst - 2023", "Certified Data Analyst"],
            "Experience": "3 years"
        },
        {
            "EmpID": "E009",
            "Name": "Ivy White",
            "Email": "ivy.white@example.com",
            "Role": "IT Specialist",
            "Skills": ["Network Security", "Linux", "Windows Server"],
            "Achievements": ["Employee of the Month - Apr 2023", "Certified IT Specialist"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E010",
            "Name": "Uma Patel",
            "Email": "uma.patel@example.com",
            "Role": "Data Analyst",
            "Skills": ["Excel", "Python", "Power BI"],
            "Achievements": ["Employee of the Month - Sep 2023", "Certified Data Analyst"],
            "Experience": "3 years"
        },
        {
            "EmpID": "E011",
            "Name": "Victor Scott",
            "Email": "victor.scott@example.com",
            "Role": "IT Specialist",
            "Skills": ["Network Administration", "Cybersecurity", "Linux"],
            "Achievements": ["Best IT Specialist - 2023",
                             "Certified Information Systems Security Professional (CISSP)"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E012",
            "Name": "Wendy Moore",
            "Email": "wendy.moore@example.com",
            "Role": "Tech Support",
            "Skills": ["Technical Troubleshooting", "Customer Support", "CRM"],
            "Achievements": ["Top Support Specialist - 2022", "Certified Help Desk Technician"],
            "Experience": "5 years"
        },
        {
            "EmpID": "E013",
            "Name": "Xander Brooks",
            "Email": "xander.brooks@example.com",
            "Role": "Java Developer",
            "Skills": ["Java", "Spring Boot", "Microservices"],
            "Achievements": ["Employee of the Month - Oct 2023", "Certified Java Developer"],
            "Experience": "6 years"
        },
        {
            "EmpID": "E014",
            "Name": "Yara Cooper",
            "Email": "yara.cooper@example.com",
            "Role": "Business Analyst",
            "Skills": ["Requirements Analysis", "SQL", "Agile Methodologies"],
            "Achievements": ["Top Business Analyst - 2023", "Certified Business Analyst Professional (CBAP)"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E015",
            "Name": "Zachary Fisher",
            "Email": "zachary.fisher@example.com",
            "Role": "Senior Vice President",
            "Skills": ["Leadership", "Strategic Planning", "Financial Management"],
            "Achievements": ["Executive of the Year - 2023", "Certified Executive Leader"],
            "Experience": "15 years"
        },
        {
            "EmpID": "E016",
            "Name": "Abigail Reed",
            "Email": "abigail.reed@example.com",
            "Role": "Software Developer",
            "Skills": ["C#", ".NET Core", "Azure"],
            "Achievements": ["Employee of the Month - Nov 2023", "Certified .NET Developer"],
            "Experience": "5 years"
        },
        {
            "EmpID": "E017",
            "Name": "Brandon Kim",
            "Email": "brandon.kim@example.com",
            "Role": "Data Engineer",
            "Skills": ["Python", "Apache Kafka", "SQL"],
            "Achievements": ["Top Data Engineer - 2023", "Certified Data Engineer"],
            "Experience": "4 years"
        },
        {
            "EmpID": "E018",
            "Name": "Charlotte White",
            "Email": "charlotte.white@example.com",
            "Role": "Data Scientist",
            "Skills": ["Python", "Scikit-Learn", "Big Data"],
            "Achievements": ["Employee of the Month - Dec 2023", "Certified Data Scientist"],
            "Experience": "3 years"
        },
        {
            "EmpID": "E019",
            "Name": "Daniel Lee",
            "Email": "daniel.lee@example.com",
            "Role": "Cloud Engineer",
            "Skills": ["AWS", "Terraform", "Docker"],
            "Achievements": ["Best Cloud Engineer - 2023", "Certified AWS Solutions Architect"],
            "Experience": "6 years"
        },
        {
            "EmpID": "E020",
            "Name": "Sunny SH",
            "Email": "sunny.sh@example.com",
            "Role": "Business Analyst",
            "Skills": ["PowerBI"],
            "Achievements": ["Certified Power BI Analyst"],
            "Experience": "4 years"
        }
    ]

    def get_named_parameter(event, name):
        return next(item for item in event['parameters'] if item['name'] == name)['value']

    def get_named_property(event, name):
        return next(item for item in event['requestBody']['content']['application/json']['properties'] if item['name'] == name)['value']

    def employeeDetails(event):
        companyName = get_named_parameter(event, 'name').lower()
        print("NAME PRINTED: ", companyName)

        for company_info in company_data:
            if company_info["companyName"].lower() == companyName:
                return company_info

        return None
