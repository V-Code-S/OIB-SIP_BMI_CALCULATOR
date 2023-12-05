import tkinter as tk
from tkinter import ttk, messagebox
import json
import matplotlib.pyplot as plt

class BMI_Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI CALCULATOR BY - VIRUPAKSHI")

        
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()

        
        self.create_widgets()

    def create_widgets(self):
        
        ttk.Label(self.root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        ttk.Label(self.root, text="Height (m):").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        
        ttk.Entry(self.root, textvariable=self.weight_var).grid(row=0, column=1, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.height_var).grid(row=1, column=1, padx=10, pady=10)

        
        ttk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi, style="TButton").grid(row=2, column=0, columnspan=2, pady=10)

        
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        
        style = ttk.Style()
        style.configure("TButton", foreground="blue", background="red", font=('Helvetica', 12, 'bold'))

    def calculate_bmi(self):
        try:
            
            weight = self.weight_var.get()
            height = self.height_var.get()

            
            if weight <= 0 or height <= 0:
                raise ValueError("Weight and height must be positive numbers.")

            
            bmi = weight / (height ** 2)

            category = self.get_bmi_category(bmi)

            result_text = f"BMI: {bmi:.2f} - {category}"
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    @staticmethod
    def get_bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal Weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"

if __name__ == "__main__":
    root = tk.Tk()
    app = BMI_Calculator(root)
    root.mainloop()
