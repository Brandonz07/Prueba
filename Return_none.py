# def is_year_leap(year):

#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     diasMeses = [31,28,31,30,31,30,31,31,30,31,30,31]   
#     if is_year_leap(year):
#         if diasMeses[month - 1] == 28:
#             return 29
#         else:
#             return diasMeses[month - 1]
#     else:
#         return diasMeses[month - 1]
#     return None

# test_years = [1900, 2000, 2016, 1987]
# test_months = [2, 2, 1, 11]
# test_results = [28, 29, 31, 30]
# for i in range(len(test_years)):
# 	yr = test_years[i]
# 	mo = test_months[i]
# 	print(yr, mo, "->", end="")
# 	result = days_in_month(yr, mo)
# 	if result == test_results[i]:
# 		print("OK")
# 	else:
# 		print("Fallido")

# def hi_everybody(my_list):
#     for name in my_list:
#         print("Hola,", name)

# hi_everybody(["Adán", "Juan", "Lucía"])

def create_list(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(create_list(5))



