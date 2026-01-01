Password Checker Web Application

Overview
The Password Checker Web Application is a lightweight, security-focused tool designed to help users evaluate the strength of their passwords in real-time. Built with Python and Flask, this application provides immediate feedback on password complexity, estimates the time required for brute-force attacks, and offers actionable tips to enhance security. It serves as an educational tool to raise awareness about the importance of strong, unique passwords.

Key Features
- Comprehensive Strength Analysis: The app evaluates passwords based on multiple criteria, including length, uppercase/lowercase letters, numbers, and special characters.
- Real-Time Feedback: Instantly categorizes passwords as WEAK, MEDIUM, or STRONG with a percentage score.
- Crack Time Estimation: Uses an entropy-based algorithm to calculate the theoretical time required to crack the password.
- Common Password Detection: Automatically flags widely used weak passwords like "password" or "admin".
- Actionable Security Tips: Provides specific recommendations to improve password strength.

How to Run
1. Clone the repository.
2. Install dependencies: pip install -r requirements.txt
3. Run the application: python app.py
4. Open your browser and navigate to http://localhost:10000

Technologies
- Backend: Python, Flask
- Frontend: HTML, CSS
- Logic: Custom algorithms for entropy calculation and validation checks.
