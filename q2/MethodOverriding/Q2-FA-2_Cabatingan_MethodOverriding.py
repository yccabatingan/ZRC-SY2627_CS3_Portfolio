# hospital code
class Patient:
  def __init__(self, name, bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):
    return self.__name
  
  def set_name(self, name):
    self.__name = name

  def get_bill_amount(self):
    return self.__bill_amount

  def set_bill_amount(self, bill_amount):
    self.__bill_amount = bill_amount

  def calculate_bill(self):
    return (
            f"Patient Name: {self.__name} \n"
            f"Original Bill: {self.__bill_amount} \n"
            f"Final Bill: {self.__bill_amount}. \n")

class Senior_Patient(Patient):
  def calculate_bill(self):
    original_bill = self.get_bill_amount()
    final_bill = original_bill * 0.80
    return (
        f"Patient Name: {self.get_name()}\n"
        f"Original Bill: {original_bill}\n"
        f"Final Bill: {final_bill}\n")

class PhilHealth(Patient):
  def calculate_bill(self):
    original_bill = self.get_bill_amount()
    final_bill = original_bill * 0.85
    return (
        f"Patient Name: {self.get_name()}\n"
        f"Original Bill: {original_bill}\n"
        f"Final Bill: {final_bill}\n")

regular_guy = Patient("Yoanna Cabatingan", 10000.0)
philHealth = PhilHealth("The cooler Yoanna", 10000.0)
seniorcitizen = Senior_Patient("The older Yoanna", 10000.0)

print(regular_guy.calculate_bill())
print(philHealth.calculate_bill())
print(seniorcitizen.calculate_bill())