 

input = input("Question: ")
app_id = "TR5875-JQ5A6EEU7H"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer=next(res.results).text

print(answer)
