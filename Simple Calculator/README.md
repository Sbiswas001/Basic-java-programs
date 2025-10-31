
## 🧮 Simple Calculator (Java)

A basic **command-line calculator** written in **Java** using a **switch-case** structure.
It performs simple arithmetic operations such as addition, subtraction, multiplication, and division.

---

### 🚀 **Features**

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division (with zero-check)
* 🧩 Simple and easy-to-understand code

---

### 📁 **Project Structure**

```
java-calculator/
│
├── Calculator.java   # Main program file
└── README.md         # Project documentation
```

---

### 💻 **How to Run the Program**

1. **Save the code** in a file named `Calculator.java`
2. **Open terminal / command prompt**
3. **Compile the program:**

   ```bash
   javac Calculator.java
   ```
4. **Run the program:**

   ```bash
   java Calculator
   ```
5. **Example Output:**

   ```
   === Simple Calculator ===
   Enter first number: 10
   Enter second number: 5
   Enter an operator (+, -, *, /): *
   Result: 50.0
   ```

---

### 🧠 **How It Works**

* The program uses the `Scanner` class to take user input.
* A `switch` statement performs the operation based on the operator entered (`+`, `-`, `*`, `/`).
* Division by zero is handled safely with an error message.

---

### 🛠️ **Technologies Used**

* **Java** (JDK 8 or above)
* **Command-Line Interface (CLI)**

---

### 📅 **Future Improvements**

* Add modulus (%) operation
* Create GUI version using **Java Swing**
* Support multiple continuous operations
