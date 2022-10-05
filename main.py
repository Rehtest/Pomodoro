from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

#Pomodoro time - change for testing
POMODORO_MINUTE = 60

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps

    reps += 1
    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*POMODORO_MINUTE)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*POMODORO_MINUTE)
    elif reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*POMODORO_MINUTE)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps

    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    format_time = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text, text=format_time)
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        window.attributes("-topmost", True)
        window.attributes("-topmost", False)
        start_timer()
        checks = ""
        check_icon = "✔"
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            checks += check_icon
        check_label.config(text=checks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Add Timer
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)


# Add Start and Reset butons
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Add Check Marks
check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
