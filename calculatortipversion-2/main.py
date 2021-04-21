print("welcome bros")
total_bill = float(input("write your total bill here\n"))
percentage = float(input("what is percentage tip you would like to give\n"))
split_people = float(input("how many people to split the bill\n"))
end_result = percentage / 100 * total_bill + total_bill
bill_per_each_person = end_result / split_people
final_result = round(bill_per_each_person, 2)
print(f"your total splited bills are {final_result}")
An