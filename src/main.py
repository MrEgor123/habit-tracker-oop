from models.habit_manager import HabitManager


class App:
    """
    Консольное меню приложения.
    """

    def __init__(self):
        self.manager = HabitManager()

    def run(self):
        print("Добро пожаловать в менеджер привычек!\n")

        while True:
            self._print_menu()
            choice = input("Выберите пункт: ").strip()

            if choice == "1":
                self._add_habit()
            elif choice == "2":
                self._mark_done()
            elif choice == "3":
                self._list_habits()
            elif choice == "4":
                print("Выход.")
                break
            else:
                print("Ошибка: неверный ввод.\n")

    @staticmethod
    def _print_menu():
        print("1 — добавить привычку")
        print("2 — отметить выполнение")
        print("3 — показать список")
        print("4 — выход")

    def _add_habit(self):
        name = input("Название: ").strip()
        description = input("Описание: ").strip()

        try:
            self.manager.add_habit(name, description)
            print("Привычка добавлена.\n")
        except ValueError as e:
            print(f"Ошибка: {e}\n")

    def _mark_done(self):
        name = input("Введите название привычки: ")

        try:
            habit = self.manager.mark_habit_done(name)
            print(f"Готово! Всего: {habit.done_count}\n")
        except ValueError as e:
            print(f"Ошибка: {e}\n")

    def _list_habits(self):
        habits = self.manager.get_all_habits()

        if not habits:
            print("Нет привычек.\n")
            return

        print("\nСписок привычек:")
        for i, h in enumerate(habits, start=1):
            print(f"{i}. {h}")
        print()


if __name__ == "__main__":
    App().run()
