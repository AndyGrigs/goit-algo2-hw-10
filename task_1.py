# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()
 

def create_schedule(subjects, teachers):
   uncovered_subjects = subjects.copy()  # Копія предметів, які ще не покриті
   selected_teachers = [] # Список обраних викладачів

   # Поки є непокриті предмети
   while uncovered_subjects:
       best_teacher = None
       max_covered = 0

       # Шукаємо викладача, який покриває найбільше непокритих предметів
       for teacher in teachers:
           # Скільки непокритих предметів може викладати цей викладач
           covered = len(teacher.can_teach_subjects & uncovered_subjects)
           # Якщо цей викладач покриває більше предметів
           if covered > max_covered:
               best_teacher = teacher
               max_covered = covered
       




   


    
if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    # Створення списку викладачів
    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", 
                {'Математика', 'Фізика'}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", 
                {'Хімія'}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", 
                {'Інформатика', 'Математика'}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", 
                {'Біологія', 'Хімія'}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", 
                {'Фізика', 'Інформатика'}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", 
                {'Біологія'})
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
