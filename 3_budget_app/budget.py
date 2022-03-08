class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        deposit_dict = {"amount": amount, "description": description}
        self.ledger.append(deposit_dict)

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            withdraw_dict = {"amount": -amount, "description": description}
            self.ledger.append(withdraw_dict)
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, destination_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {destination_category.category}')
            destination_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        final_display = self.category.center(30, '*')
        for dictionary in self.ledger:
            description23 = (dictionary['description'][:23]) if len(dictionary['description']) > 23 \
                else dictionary['description']
            amount2decimal = f"{dictionary['amount']:7.2f}"
            whitespace = 30 - len(description23) - len(amount2decimal)
            final_display += '\n' + description23 + (' ' * whitespace) + amount2decimal

        final_display += '\n' + "Total: " + "{:.2f}".format(self.get_balance())
        return final_display


def create_spend_chart(list_of_categories):
    total_spent = []
    for category in list_of_categories:
        spent = 0
        for withdrawal in category.ledger:
            if withdrawal['amount'] < 0:
                spent += (withdrawal['amount'] * -1)
        total_spent.append(spent)
    total_sum = sum(total_spent)
    percentage = [(round(i / total_sum * 100, -1)) for i in total_spent]

    chart = "Percentage spent by category"
    for i in range(100, -10, -10):
        chart += "\n" + str(i).rjust(3) + "|"
        for a in percentage:
            if a >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " "
    chart += "\n" + "    "

    for i in percentage:
        chart += "-" * 3
    chart += "-"

    cat_length = []
    for category in list_of_categories:
        cat_length.append(len(category.category))
    max_length = max(cat_length)

    for y in range(max_length):
        chart += "\n    "
        for c in range(len(list_of_categories)):
            if y < cat_length[c]:
                chart += " " + list_of_categories[c].category[y] + " "
            else:
                chart += "   "
        chart += " "

    return chart