import tkinter as tk

cards = [("Кортеж", "Неизменяемый список"), ("Список", "Набор пронумерованных значений"), ("Ткинтер", "Библиотека для создания графического интерфейса")]

current_card = 0
current_side = 0

def rotate():
  global current_card
  global current_side
  if current_side == 0:
    main_button.config(text=cards[current_card][1])
    current_side = 1
  else:
    main_button.config(text=cards[current_card][0])
    current_side = 0

def next_card():
  # ЧТОБЫ В обработчиках событий использовать глобальные переменные необходимо явно указывать на это!
  global current_card
  global current_side
  current_card += 1
  current_side = 0
  main_button.config(text=cards[current_card][0])

def back_card():
    global current_card
    global current_side
    current_card -= 1
    current_side = 0 
    main_button.config(text=cards[current_card][-1])


root = tk.Tk()
root.title("Flash Cards")
root.geometry("400x400")

# Виджет = элемент графического интерфейса, ВИртуальный гаДЖЕТ
# Первым аргументом при создании виджета всегда является родительский виджет будь то окно или что-либо другое (например область/группа)
# width и height указываются в таких единицах измерения (по умолчанию) как символы. То есть width=30 - это значит что виджет вместит 30 символов по горизонтали, то же самое и с высотой но "символ" берётся по высоте 
# ПОэтому, при ширине и высоте 30 кнопка всё равно не квадратная
main_button = tk.Button(root, text="Нажми  меня", command=rotate)
# После создания виджет необходимо расположить!
main_button.pack(fill=tk.BOTH, expand=True)

next_button = tk.Button(root, text=">", command=next_card)
next_button.pack(side=tk.RIGHT)

back_button = tk.Button(root, text='<', command=back_card)
back_button.pack(side=tk.RIGHT)

root.mainloop()
