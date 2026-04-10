# Project 1: Alveus Animals and Sightings

**CS178: Cloud and Database Systems — Project #1**
**Author:** Camille Thoms
**GitHub:** camillethoms

---

## Overview

- This project is my fan site for Alveus Sanctuary, a real animal sanctuary and educational streaming platform that teaches through their animal ambassadors. The site has a table of a bunch of all the sanctuary's animals from a mysql datebase and a community sighting log where myself or anyone can submit, update, delete, and view animal sightings from a DynamoDB table. 

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for [describe what you stored]
- **AWS DynamoDB** — non-relational database for [describe what you stored]
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push
- **Bootstrap** - all the styling and responsive layout
- **GitHub**
- **boto3** - python library for dynamodb
- **pysql** - python library for mysql rds 

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dynamoCode.py          # dynamoDB functions
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page with links 
│   ├── sightings.html   # shows dynamoDB table of sighting logs
│   ├── animals.html     # shows RDS table of animals
│   ├── add_sighting.html     # submit new sighting form on dynamoDB
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://100.24.10.27:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://100.24.10.27:8080 
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

<!-- Briefly describe your relational database schema. What tables do you have? What are the key relationships? -->

**Example:**

- `animals` — stores [description]; primary key is `[key]`
- `ambassador_topics` — stores [description]; foreign key links to `[other table]`

The JOIN query used in this project: <!-- describe it in plain English -->

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

- **Table name:** `[SanctuaryLog`
- **Partition key:** `display_name`
- **Sort key:** 'timestamp'
- **Attributes:** 'animal_tag', 'sighting'
- **Used for:** [description]

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/add-sighting` | [what it does] |
| Read      | `/sightings` | [what it does] |
| Update    | `/update-sighting` | [what it does] |
| Delete    | `/delete-sighting` | [what it does] |

---

## Challenges and Insights

Biggest challenge - deployment pipeline working. My edits weren't going to the right place because my auto-deploy kept pulling old versions of files because I accidently cloned the repo into the wrong folder. Management issues like this regularly caused stalls in progress. As did re-designing the dynamoDB table after I confused the project instructions; a mistake surely not necessary if I had done the labs as previously intended instead of having to use them as learning tools along the way of this projects proceedings. I learned what kind of factors would make me choose NoSQL over SQl for data that needs more rigid rules for unpredictable data. 

---

## AI Assistance

Claude Sonnet 4.6 was used throughout this project for: 
   - debugging flask routes
   - writing/rewriting teh 'dbCode.py" mysql functions to include group_concat join properly
   - writing/rewriting my dynamoCode CRUD functions, specifially the update one was difficult because of the unique keys like the timestamp
   - any implementation of that frustrating timestamp. i don't even think it records the right hour. 
   - writing and styling all the html templates with bootstrap. 
   - troubleshooting EC2 deployment and workflow
   - SQL schema creation 

I tried to use Claude as a collaborator, mainly for debugging, troubleshooting implementation, and a tutor. I tried to use it to understand what each part of the code actually does and why as I wrote it. So everytime i didn't get what was happening when it broke or get code, it's like we would work through it like a tutor trailing off a sentence so I could finish it with what I was learning. 
