import wikipedia 

while True:
	x = input("Question:  ")
	wikipedia.set_lang("es")
	print(wikipedia.summary(x, sentences=2))
