from tkinter import *
imp
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.02
SHORT_BREAK_MIN = 0.02
LONG_BREAK_MIN = 20
reps = 1
check_mark_val = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title_label.config(text="Timer", fg=GREEN)
    global check_mark_val
    check_mark_val = ""
    check_mark.config(text="")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    reps += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    global check_mark_val
    count_min = math.floor(count/60)
    count_sec = math.floor(count % 60)

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # check if completed work session and add a check mark
        if reps % 2 != 0:
            check_mark_val += "✔"
            check_mark.config(text=f"{check_mark_val}")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=2, row=1)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

start_button = Button(text="Start", highlightthickness=0,font=(FONT_NAME, 12, "bold"), command=start_timer,)
start_button.config(padx=10, pady=4)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 12, "bold"), command=reset_timer)
reset_button.config(padx=10, pady=4)
reset_button.grid(column=3, row=3)

check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_mark.grid(column=2, row=4)


window.mainloop()
