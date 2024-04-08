# Functions for file saving and loading
def save_notes(text):
  """
  Сохраняет текст из textedit в файл data_notes.txt.

  Args:
      text (str): Текст из textedit.

  Returns:
      bool: True, если сохранение прошло успешно, False - otherwise.
  """
  try:
    with open("data_notes.txt", "w") as f:
      f.write(text)
    return True
  except Exception as e:
    print(f"Ошибка при сохранении: {e}")
    return False
