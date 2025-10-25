 # ==============================================================
# student_portfolio_manager.py
# --------------------------------------------------------------
# Author: Agnibesh Maity
# Description:
#   A beginner-friendly Python program to manage student portfolios.
#   It allows users to add, view, and search student profiles,
#   storing them in a local text file.
# --------------------------------------------------------------
# Version: 1.0
# Created: October 2025
# ==============================================================

import os
import time

DATA_FILE = "students_data.txt"

# --------------------------------------------------------------
# Utility Functions
# --------------------------------------------------------------
def clear_screen():
    """Clears the console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def slow_print(text, delay=0.03):
    """Prints text slowly to create a typing effect."""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def banner():
    """Displays a stylized banner."""
    print("=" * 60)
    print("🎓  STUDENT PORTFOLIO MANAGER  🎓".center(60))
    print("=" * 60)


# --------------------------------------------------------------
# Core Features
# --------------------------------------------------------------
def add_student():
    """Adds a new student record."""
    clear_screen()
    banner()
    slow_print("Enter student details below:\n")

    name = input("Name: ").strip().title()
    age = input("Age: ").strip()
    department = input("Department: ").strip().title()
    email = input("Email: ").strip()

    with open(DATA_FILE, "a") as file:
        file.write(f"{name},{age},{department},{email}\n")

    slow_print(f"\n✅ Record for {name} added successfully!")
    input("\nPress Enter to continue...")


def view_students():
    """Displays all student records."""
    clear_screen()
    banner()

    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        slow_print("⚠️ No student records found!")
    else:
        with open(DATA_FILE, "r") as file:
            students = file.readlines()

        print(f"\n{'Name':20} | {'Age':5} | {'Department':15} | {'Email':25}")
        print("-" * 70)
        for student in students:
            name, age, dept, email = student.strip().split(",")
            print(f"{name:20} | {age:5} | {dept:15} | {email:25}")

    input("\nPress Enter to continue...")


def search_student():
    """Searches for a student by name."""
    clear_screen()
    banner()
    search_name = input("Enter the name to search: ").strip().title()

    found = False
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                name, age, dept, email = line.strip().split(",")
                if search_name in name:
                    print(f"\n🎯 Found: {name} | {age} | {dept} | {email}")
                    found = True

    if not found:
        slow_print(f"\n❌ No record found for '{search_name}'.")
    input("\nPress Enter to continue...")


# --------------------------------------------------------------
# Main Menu
# --------------------------------------------------------------
def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        clear_screen()
        banner()
        print("1️⃣  Add Student Record")
        print("2️⃣  View All Students")
        print("3️⃣  Search Student")
        print("4️⃣  Exit")
        print("-" * 60)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            slow_print("\n👋 Exiting... Goodbye!")
            time.sleep(1)
            break
        else:
            slow_print("⚠️ Invalid choice! Please try again.")
            time.sleep(1)


# --------------------------------------------------------------
# Program Entry Point
# --------------------------------------------------------------
if __name__ == "__main__":
    main_menu()

