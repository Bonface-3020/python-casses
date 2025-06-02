import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")

        self.menu_items = {
            "FRIES MEAL": 2, "LUNCH MEAL": 2, "BURGER MEAL": 3,
            "PIZZA MEAL": 4, "CHEESE BURGER": 2.5, "DRINKS": 1
        }

        self.menu_quantities = {}

        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.Label(frame, text="Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, pady=10)

        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            ttk.Label(frame, text=f"{item} ($ {price}):", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            self.menu_quantities[item] = ttk.Entry(frame, width=5)
            self.menu_quantities[item].grid(row=i, column=1, padx=10, pady=5)

        ttk.Button(frame, text="Place Order", command=self.place_order).grid(row=len(self.menu_items) + 1, columnspan=3, pady=10)

    def place_order(self):
        total_cost, order_summary = 0, "Order Summary:\n"

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                cost = quantity * self.menu_items[item]
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item}: {quantity} x $ {self.menu_items[item]} = $ {cost}\n"

        if total_cost > 0:
            order_summary += f"\nTotal Cost: $ {total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()