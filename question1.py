class TuitionPayment:

    def __init__(self, amount):
        self.amount = amount

    def calculate_amount(self):
        return self.amount + (self.amount * 0.05)


# Accommodation Payment
class AccommodationPayment:

    def __init__(self, amount):
        self.amount = amount

    def calculate_amount(self):
        return self.amount + (self.amount * 0.10)


# Library Fine
class LibraryFine:

    def __init__(self, amount):
        self.amount = amount

    def calculate_amount(self):
        return self.amount + (self.amount * 0.02)

# Creating payment 
payments = [TuitionPayment(1000000),AccommodationPayment(500000),LibraryFine(50000)]
    
print("STUDENT PAYMENT MANAGEMENT SYSTEM")

for payment in payments:

    final_amount = payment.calculate_amount()

    print("Payment Type:", payment.__class__.__name__)
    print("Original Amount: UGX", payment.amount)
    print("Final Amount: UGX", final_amount)