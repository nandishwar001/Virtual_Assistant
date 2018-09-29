import wikipedia
import wolframalpha

while True:
	x = input("Q: ")
	try:
		#wolframalpha
		app_id = "TR5875-JQ5A6EEU7H"
		client = wolframalpha.Client(app_id)
		res = client.query(x)
		answer=next(res.results).text
		print(answer)
	except:
		#wikipedia
		print(wikipedia.summary(x))

