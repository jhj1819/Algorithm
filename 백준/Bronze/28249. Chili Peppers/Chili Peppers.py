"""
CHili Peppers
"""

n = int(input())
chili = {"Poblano" : 1500, "Mirasol" : 6000, "Serrano" : 15500, "Cayenne" : 40000, "Thai" : 75000, "Habanero" : 125000}
result = 0

for i in range(n):
    result += chili[input()]

print(result)