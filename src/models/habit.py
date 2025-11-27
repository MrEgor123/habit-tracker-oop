class Habit:
    """
    Класс, представляющий одну привычку пользователя.
    """

    def __init__(self, name: str, description: str = "") -> None:
        if not name.strip():
            raise ValueError("Название привычки не может быть пустым")

        self.name: str = name.strip()
        self.description: str = description.strip()
        self.done_count: int = 0

    def mark_done(self) -> None:
        """
        Отметить выполнение привычки ещё один раз.
        """
        self.done_count += 1

    def __str__(self) -> str:
        """
        Строковое представление привычки для вывода в консоль.
        """
        desc_part = f" — {self.description}" if self.description else ""
        return f"{self.name}{desc_part} (выполнено {self.done_count} раз)"