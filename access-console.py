# import the necssary modules
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found use pip install google -y")

# To Search 
query = input("Enter the Page to want to search")

# change tld for different regions
for j in search(query, tld="co.in", num=10, stop=10, pause=3):
	print(j)
