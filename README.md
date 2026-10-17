# 🎓 Triage

Triage is a ticket management system designed to help campuses manage, prioritize, assign, and track reported issues efficiently.

## 🎯 Project Goal

The goal of Triage is to provide a simple and organized way to manage campus-related issues, ensuring that important problems are prioritized and resolved efficiently.

## ✨ Features

- 🎫 **Ticket Management:** Create, view, and list tickets.
- 🚦 **Priority Calculation:** Automatically determine ticket priority based on urgency and the number of affected users.
- 👥 **Ticket Assignment:** Assign tickets to staff members.
- 📋 **Work Queue:** Display open tickets in priority order.
- 🔄 **Workflow Management:** Track tickets through their lifecycle: `Open → In Progress → Resolved`.
- 📊 **Ticket Reports:** Generate summaries showing the total number of tickets, status breakdowns, and priority breakdowns.
- 💾 **Data Persistence:** Save and load ticket data using JSON.

## 🛠️ Technologies

- 🐍 Python
- 📄 JSON
- 🌿 Git & GitHub

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ev0l009/triage.git
```

### 2. Navigate to the Project Directory

```bash
cd triage
```

### 3. Run the Application

Start the application using its entry-point script:

```bash
python3 main.py
```

## 🔮 Future Implementations

The following features are planned for future versions of Triage.

### 🔐 Authentication and Access Control

- Implement authentication for staff and fellows.
- Restrict ticket creation and updates to staff members.
- Allow fellows to view tickets, list tickets, and access the work queue.

### 💡 Additional Features

- 📝 **Complaint Logging:** Allow fellows to log complaints about campus-related issues.
- 🔗 **Complaint Correlation:** Allow staff to review logged complaints and correlate them into tickets.
- 💬 **Ticket Comments:** Enable staff to leave comments on tickets.
```