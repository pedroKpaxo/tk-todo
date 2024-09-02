from views import ToDoView
from controller import ToDoController


def main():
    controller = ToDoController()
    app = ToDoView(controller)
    app.mainloop()


if __name__ == "__main__":
    main()
