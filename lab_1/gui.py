import customtkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import plot


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

root = customtkinter.CTk()
root.geometry("500x375")
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.wm_geometry(f'+{int(x)}+{int(y)}')
root.resizable(width=False, height=False)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill='both', expand=True)

start_label = customtkinter.CTkLabel(master=frame, text='Enter the parameter and boundaries for the φ value')
start_label.pack(pady=30, padx=10)

param_entry = customtkinter.CTkEntry(width=160, master=frame, placeholder_text='parameter')
param_entry.pack(pady=10, padx=10)
min_fi_entry = customtkinter.CTkEntry(width=160, master=frame, placeholder_text='min φ value (in degrees)')
min_fi_entry.pack(pady=10, padx=10)
max_fi_entry = customtkinter.CTkEntry(width=160, master=frame, placeholder_text='max φ value (in degrees)')
max_fi_entry.pack(pady=10, padx=10)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def error(message):
    frame.destroy()
    root.geometry("500x125")
    error_frame = customtkinter.CTkFrame(master=root)
    error_frame.pack(pady=20, padx=60, fill='both', expand=True)

    error_label = customtkinter.CTkLabel(master=error_frame, text=message)
    error_label.pack(pady=30, padx=10)


def make_plot():
    if not is_float(param_entry.get()):
        error('Invalid input: parameter!')
        return
    if not is_float(min_fi_entry.get()):
        error('Invalid input: min φ value!')
        return
    if not is_float(max_fi_entry.get()):
        error('Invalid input: max φ value!')
        return
    a = float(param_entry.get())
    min_fi = float(min_fi_entry.get())
    max_fi = float(max_fi_entry.get())
    if a <= 0.00000001:
        error('Invalid parameter: inserted parameter is less than zero!')
        return
    if min_fi <= 0.00000001 or max_fi <= 0.00000001:
        error('Invalid boundaries: one or two boundaries is less than zero!')
        return
    if max_fi < min_fi:
        error('Invalid boundaries: max bound is less than min bound!')
        return
    frame.destroy()
    canvas = FigureCanvasTkAgg(plot.func_plot(min_fi, max_fi, a))
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20, padx=60, fill='both', expand=True)


start_button = customtkinter.CTkButton(width=120, master=frame, text='Make a plot', command=make_plot)
start_button.pack(pady=30, padx=10)


if __name__ == '__main__':
    root.mainloop()
