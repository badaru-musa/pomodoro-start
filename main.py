from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 1
check = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    timer_lbl.config(text="Timer", fg=PINK, bg=YELLOW)
    check_lbl.config(text="")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def timer_mech():
    global reps
    global WORK_MIN
    global SHORT_BREAK_MIN
    global LONG_BREAK_MIN

    if reps % 2 == 1:
        countdown(WORK_MIN * 60)
        timer_lbl.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    elif reps % 2 == 0 and reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        reps = 0
        timer_lbl.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_lbl.config(text="Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    global reps
    global check
    global timer
    counter_min = math.floor(count/60)
    counter_sec = count % 60
    if counter_sec < 10:
        counter_sec = f"0{counter_sec}"
    canvas.itemconfig(timer_text, text=f"{counter_min}:{counter_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        timer_mech()
        if reps % 9 == 1:
            check = ""

        if reps % 2 == 1:
            check += "✓"
            check_lbl.config(text=check)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start_btn = Button(text="Start", command=timer_mech)
start_btn.grid(column=0, row=2)

timer_lbl = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_lbl.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


check_lbl = Label(text=check, fg=GREEN, bg=YELLOW)
check_lbl.grid(column=1, row=3)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

window.mainloop()
