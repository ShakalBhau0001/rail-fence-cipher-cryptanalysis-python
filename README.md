# 🔐 Rail Fence Cipher Cryptanalysis (Python)

An educational **Python implementation of Rail Fence Cipher brute-force cryptanalysis.**

This project demonstrates how classical transposition ciphers can be broken using systematic rail reconstruction and exhaustive search.

It is designed strictly as a **learning and academic project** to understand the structural weaknesses of classical ciphers — not as a real-world attack tool.

---

## 🧱 Project Structure

```bash
rail-fence-cipher-cryptanalysis-python/
│
├── app.py            # Rail Fence brute-force cryptanalysis tool (CLI based)
├── LICENSE           # Project license
└── README.md         # Project documentation
```

---

## ✨ Features

### 🔍 Full Brute-Force Rail Search
- Tests all possible rail values from `2` to `n-1`
- Displays all possible plaintext candidates
- Reconstructs zigzag pattern for each rail count

### 🔁 Zigzag Pattern Reconstruction
- Dynamically marks rail positions
- Fills matrix row-wise using ciphertext
- Re-traverses zigzag pattern to rebuild plaintext

### 🧠 Structural Cryptanalysis Focus
- Demonstrates transposition cipher weakness
- Shows how unknown key (rail count) can be recovered
- Reinforces matrix-based algorithmic thinking

### 🧮 Educational Focus
- Clean modular Python functions
- Clear separation between:
  - Decryption logic
  - Brute-force controller
- CLI-based execution

---

## 🛠 Technologies Used


| Technology             | Role                                |
| ---------------------- | ----------------------------------- |
| **Python 3**           | Core programming language           |
| **2D Lists (Matrix)**  | Rail pattern simulation             |
| **Control Flow Logic** | Zigzag traversal and reconstruction |
| **Brute Force Search** | Exhaustive rail testing             |

---

## 📌 Purpose of This Project

This project is built to:
- Understand Rail Fence Cipher weaknesses
- Learn brute-force cryptanalysis for transposition ciphers
- Explore zigzag matrix reconstruction logic
- Simulate attacker perspective ethically
- Strengthen Python control-flow and indexing skills

> ⚠️ This project is intended strictly for educational and cybersecurity learning purposes.

---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone https://github.com/ShakalBhau0001/rail-fence-cipher-cryptanalysis-python.git
```

### 2️⃣ Navigate to the project folder
```bash
cd rail-fence-cipher-cryptanalysis-python
```

### 3️⃣ Run the program
```bash
python app.py
```

### 4️⃣ Enter Cipher Text
- Provide any Rail Fence encrypted message (without spaces)
- View all possible plaintext outputs for different rail values
- Identify the most meaningful English result

---

## 🔎 Example

```bash
Enter ciphertext: HOLELWRDLO

--- Brute Force Results ---

Rails = 2 → HWORLDELLO
Rails = 3 → HELLOWORLD
Rails = 4 → HLWLREOLDO
...
```

---

## ⚠️ Limitations
- Does not automatically score English likelihood
- Outputs all possible rail reconstructions
- Manual inspection required to identify correct plaintext
- Inefficient for very large inputs (O(n²) behavior)
- CLI-based interaction only

---

## 🌟 Future Improvements
- Rank most probable plaintext automatically
- Add English-likelihood scoring system
- Add file input support
- Integrate into a Classical Crypto Toolkit
- Convert into reusable Python module
- Add visualization of zigzag pattern

---

## ⚠️ Disclaimer

This project is created **for educational and cybersecurity learning purposes only.**
It demonstrates the inherent weakness of classical transposition ciphers such as the Rail Fence Cipher.
It must not be used for unauthorized access, malicious activity, or real-world security attacks.

---

## 🪪 Author

> **Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
