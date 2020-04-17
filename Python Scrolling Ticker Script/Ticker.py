import tkinter as tk
import time
root = tk.Tk()
# width=width chars, height=lines text
text = tk.Text(root, root.title("Ticker"), width=20, height=1, bg='yellow')
text.pack()
# use a proportional font to handle spaces correctly

text.config(font=('courier', 24, 'bold'))
s1 = "This is a scrolling ticker example. As you can see, it's quite long but can be a lot longer if necessary..."
s2 = " We can even extend the length of the ticker message by including more variables..."
s3 = " The variables are within the s-values in the code."
s4 = " Don't forget to concatenate them all before the For loop, and rename the 'spacer' s-variable too."

# pad front and end with 20 spaces
s5 = ' ' * 20
s = s5 + s1 + s2 + s3 + s4 + s5
for k in range(len(s)):
    # use string slicing to do the trick
    ticker_text = s[k:k+20]
    text.insert("1.1", ticker_text)
    root.update()
    # delay by 0.15 seconds
    time.sleep(0.15)
root.mainloop()
