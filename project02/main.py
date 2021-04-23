from task04 import task04

if __name__ == "__main__":		
	
	print("\n\nTEMATYKA PROGRAMÓW:")
	print("----------------------------------------------------------------------------------------")
	print("1. Program do sprawdzania, czy dana sekwencja liczb naturalnych jest ciągiem graficznym, \n   i do konstruowania grafu prostego o stopniach wierzchołków zadanych przez ciąg graficznym.")
	print("2. Program do randomizacji grafów prostych o zadanych stopniach wierzchołków \n   (wielokrotna operacja zamieniającą losowo wybraną parę krawędzi: ab i cd na parę ad i bc).")
	print("3. Program do znajdowania największej spójnej składowej na grafie")
	print("4. Program do tworzenia losowego grafu eulerowskiego i znajdowania na nim cyklu Eulera")
	print("5. Program do generowania losowych grafów k-regularnych.")
	print("6. Program do  sprawdzania (dla małych grafów), czy graf jest hamiltonowski.")
	print("----------------------------------------------------------------------------------------")
	
	task_num = 0
	while task_num < 1 or task_num > 6:
		task_num =  int(input("\nWybierz prawidłowy numer zadania:\n"))
	

	if task_num == 1:
		# TO DO
		pass
	elif task_num == 2:
		# TO DO
		pass
	elif task_num == 3:
		# TO DO
		pass
	elif task_num == 4:
		task04()
	elif task_num == 5:
		# TO DO
		pass
	elif task_num == 6:
		# TO DO
		pass