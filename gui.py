from tkinter import *
from tkinter import ttk

# --- Define Math Concepts (No OWL File) ---
math_concepts = {
    "Addition": {
        "explanation": "Addition is the process of combining two or more numbers to get their total.",
        "example": "5 + 3 = 8",
        "rule": "To add, line up the digits and sum each column from right to left."
    },
    "Subtraction": {
        "explanation": "Subtraction is taking one number away from another.",
        "example": "9 - 4 = 5",
        "rule": "Start from the rightmost digit and borrow if needed."
    },
    "Multiplication": {
        "explanation": "Multiplication is repeated addition.",
        "example": "4 × 3 = 12",
        "rule": "Multiply each digit and carry over if the result is more than 9."
    },
    "Division": {
        "explanation": "Division is splitting a number into equal parts.",
        "example": "12 ÷ 3 = 4",
        "rule": "Divide the digits starting from the left and bring down the next digit if needed."
    }
}

# --- Setup GUI Window ---
root = Tk()
root.title("🧠 Math Tutoring System")
root.geometry("700x450")
root.configure(bg="#f4f7ff")

# --- Title ---
title = Label(root, text="📘 Learn Basic Math", font=("Helvetica", 20, "bold"), fg="#004aad", bg="#f4f7ff")
title.pack(pady=15)

# --- Concept Selection ---
select_label = Label(root, text="Choose a Math Concept:", font=("Helvetica", 12), bg="#f4f7ff")
select_label.pack()

selected_concept = StringVar()
dropdown = ttk.Combobox(root, textvariable=selected_concept, state="readonly", font=("Helvetica", 11), width=30)
dropdown["values"] = list(math_concepts.keys())
dropdown.pack(pady=5)

# --- Output Frame ---
frame = Frame(root, bg="white", bd=1, relief=SOLID, padx=20, pady=15)
frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

# --- Output Labels ---
label_concept = Label(frame, text="📚 Concept: ", font=("Helvetica", 13, "bold"), bg="white", anchor="w")
label_concept.pack(fill=X)

label_explanation = Label(frame, text="💡 Explanation: ", font=("Helvetica", 12), bg="white", anchor="w", wraplength=640, justify=LEFT)
label_explanation.pack(fill=X, pady=5)

label_example = Label(frame, text="🧮 Example: ", font=("Helvetica", 12), bg="white", anchor="w", wraplength=640, justify=LEFT)
label_example.pack(fill=X, pady=5)

label_rule = Label(frame, text="✏️ Rule: ", font=("Helvetica", 12), bg="white", anchor="w", wraplength=640, justify=LEFT)
label_rule.pack(fill=X, pady=5)

# --- Function to Display Details ---
def show_concept_details(event):
    concept = selected_concept.get()
    details = math_concepts.get(concept, {})
    
    label_concept.config(text=f"📚 Concept: {concept}")
    label_explanation.config(text=f"💡 Explanation: {details.get('explanation', '')}")
    label_example.config(text=f"🧮 Example: {details.get('example', '')}")
    label_rule.config(text=f"✏️ Rule: {details.get('rule', '')}")

# --- Bind Dropdown ---
dropdown.bind("<<ComboboxSelected>>", show_concept_details)

# --- Run App ---
root.mainloop()
