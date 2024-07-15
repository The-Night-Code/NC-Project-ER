# CRM System

## Description

This CRM system was developed to enhance operational efficiency and project management capabilities.

## Functionality

- **Technician Data Entry**: Enables technicians to input various types of data (text, files, etc.) into the system.
  
- **Engineer Workflow**: Facilitates engineers in accessing, working on, and approving data entered by technicians, ensuring streamlined communication and workflow.
  
- **Management Tools**: Provides features for managing workers (technicians, engineers, etc.), tracking project completions, and assigning tasks.

- **Download Options**: Data entered can be downloaded as xlsx or pdf files using specific templates.

## Impact

This system has significantly enhanced operational efficiency and project management capabilities.

## Technologies Used

- Django
- RESTful API
- HTML/CSS
- JavaScript
- jQuery
- AJAX
- JSON
- Bootstrap

## Installation

### Create a Virtual Environment

Using venv (Python 3)
  
`python3 -m venv venv` 

`source venv/bin/activate` or `.\venv\Scripts\activate`


### Install Dependencies

`pip install -r requirements.txt`

### Run Migrations

`python manage.py makemigrations`

`python manage.py migrate`

### Create a Superuser (Admin)
`python manage.py createsuperuser`

### Run the Development Server

`python manage.py runserver`


## Usage

### User Access and Permissions
Access to the CRM system is granted exclusively by management, ensuring secure entry for technicians, engineers, and other authorized personnel. Users are authenticated through a secure login process, managed and controlled by higher management.

### Team Leaders' Role
Team leaders hold administrative capabilities within the system. They are empowered to allocate projects to technicians and engineers, monitor project progress, and oversee workflow efficiencies. Key functionalities include:

Project Allocation: Assigning tasks and projects to technicians and engineers based on workload and expertise.
Workflow Tracking: Monitoring the status of ongoing projects, including tasks in progress and completed assignments.

### Technicians' Responsibilities
Technicians play a critical role in the CRM system by entering various types of data (text, numbers, images, files, etc.) into designated forms. This input serves as foundational information for project management and client engagement processes.

### Engineers' Responsibilities
Engineers leverage the CRM system to retrieve data entered by technicians, which can be downloaded in formats such as xlsx or pdf. This data is processed and subsequently uploaded back into the system, ensuring transparency and accessibility for clients to track project details. Engineers have the flexibility to:

Data Processing: Analyze and manipulate project data as required, ensuring accuracy and relevance.
Project Management: Manage assigned projects comprehensively, ensuring timely completion and client satisfaction.
Client Interaction
Clients benefit from the CRM system by tracking project progress in real-time. This visibility allows clients to stay informed about milestones, deliverables, and overall project status, fostering transparency and trust.

### Real-Time Communication
Each project within the CRM system features a real-time chat functionality. This allows stakeholders, including technicians, engineers, team leaders, and clients, to communicate seamlessly. The chat feature facilitates quick decision-making, collaboration, and resolving project-related queries efficiently.

