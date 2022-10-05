# Pomodoro Application
#### Video Demo:  https://youtu.be/xnVwFGIfBkg
#### Description: Pomodoro application built with Python and TKInter library

#### Details: The Pomodoro application uses tkinter and the math libraries to implement a simple application with a start and reset button. The application is meant to be used to help focus using the Pomodoro technique with 25 minutes of focus work followed by 5 minutes of break - after 4 cycles of work, the short 5 minute break is replaced with a 20 minute break instead.

##### Application UI: A single window with a tomato image as the canvas background (included in the project folder). The UI consists of a timer label which counts down with each second, two buttons (one to start the timer and the other to reset it) and a final label below to update a check whenever a pomodoro is complete (25 minutes of work)

##### Start Button: The first button initiates the start timer function which in turn runs the count down function. The start timer function checks how many times a count down has reached 0 to decide if the next one should be a Short break, long break or another full 25 minute pomodoro. The Count down function measures the current minute and current second to correctly format the time label.

##### Reset Button: The reset button stops the timer and resets all labels to their default state so that the application can be used again.