import tkinter
import tkinter.messagebox
import customtkinter
from Code.Network import Prepare_data
from Code.Network import Network
from Code.Network import My_Vector
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.alpha = 0.0
        self.training_data = []
        self.test_data = []
        self.perceptron_list = []

        self.title("Neuron network")
        self.geometry("1100x580")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Neuron network",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.learn_button = customtkinter.CTkButton(self.sidebar_frame, text="Learn", command=self.learn_button_event)
        self.learn_button.grid(row=3, column=0, padx=10, pady=(20, 0), sticky="ew")

        self.try_button = customtkinter.CTkButton(self.sidebar_frame, text="Try", command=self.try_button_event)
        self.try_button.grid(row=4, column=0, padx=10, pady=(20, 0), sticky="ew")

        self.show_button = customtkinter.CTkButton(self.sidebar_frame, text="Show", command=self.show_button_event)
        self.show_button.grid(row=5, column=0, padx=10, pady=20, sticky="ew")

        # create sidebar settings scroll frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.sidebar_frame, label_text="Settings")
        self.scrollable_frame.grid(row=2, column=0, pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []

        manual_data_switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Add test data manually",
                                                     command=self.add_test_data_event)
        manual_data_switch.grid(row=0, column=0, padx=10, pady=(0, 20), sticky="snew")
        self.scrollable_frame_switches.append(manual_data_switch)

        switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text="Add alpha parameter",
                                         command=self.add_alpha_event)
        switch.grid(row=1, column=0, padx=10, pady=(0, 20), sticky="ew")
        self.scrollable_frame_switches.append(switch)
        for i in range(2, 5):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, rowspan=2, padx=20, pady=(20, 0), sticky="nsew")

        # create data frame
        self.data_frame = customtkinter.CTkFrame(self)
        self.data_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.data_frame.grid_columnconfigure(1, weight=1)
        self.data_frame.grid_rowconfigure(4, weight=1)

        file_image = customtkinter.CTkImage(Image.open("../Images/img.png"))

        training_label = customtkinter.CTkLabel(master=self.data_frame, text="Training data path:", width=0)
        training_label.grid(row=0, column=0, columnspan=1, padx=(20, 0), pady=10, sticky="sne")
        self.training_data_entry = customtkinter.CTkEntry(self.data_frame,
                                                          placeholder_text="Training data path")
        self.training_data_entry.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=10, sticky="snew")
        self.training_data_button = customtkinter.CTkButton(self.data_frame, text="",
                                                            command=self.open_training_file_event, width=0,
                                                            image=file_image)
        self.training_data_button.grid(row=0, column=3, columnspan=1, padx=10, pady=10, sticky="ew")
        test_label = customtkinter.CTkLabel(master=self.data_frame, text="Test data path:",
                                            width=0)
        test_label.grid(row=1, column=0, columnspan=1, padx=(20, 0), pady=10, sticky="sne")
        self.test_data_entry = customtkinter.CTkEntry(self.data_frame, placeholder_text="Test data path")
        self.test_data_entry.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=20, sticky="snew")
        self.test_data_button = customtkinter.CTkButton(self.data_frame, text="",
                                                        command=self.open_test_file_event, width=0, image=file_image)
        self.test_data_button.grid(row=1, column=3, columnspan=1, padx=10, pady=10, sticky="ew")

        aplha_label = customtkinter.CTkLabel(master=self.data_frame, text="Alpha:",
                                             width=0)
        aplha_label.grid(row=2, column=0, columnspan=1, padx=(20, 0), pady=10, sticky="sne")
        self.alpha_entry = customtkinter.CTkEntry(self.data_frame, placeholder_text="Alpha")
        self.alpha_entry.grid(row=2, column=1, columnspan=2, padx=(20, 10), pady=10, sticky="snew")

        self.save_data_button = customtkinter.CTkButton(self.data_frame, text="Save data",
                                                        command=self.save_data_button_event, width=0)
        self.save_data_button.grid(row=3, column=0, columnspan=1, padx=20, pady=10, sticky="sne")
        self.clear_data_button = customtkinter.CTkButton(self.data_frame, text="Clear data",
                                                         command=self.clear_data_button_event, width=0)
        self.clear_data_button.grid(row=3, column=1, columnspan=1, padx=20, pady=10, sticky="snw")

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Write ...")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=20, sticky="snew")

        self.execute_button = customtkinter.CTkButton(self, text="Execute", command=self.execute_button_event)
        self.execute_button.grid(row=3, column=2, columnspan=1, padx=20, pady=20, sticky="snew")

        # setting
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[1].select()
        self.appearance_mode_optionemenu.set("System")
        self.textbox.insert("0.0",
                            "Neuron network\n\n" + "Start\n\n")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def add_test_data_event(self):
        if self.entry._state == "normal":
            self.entry.configure(state="disabled")
            self.execute_button.configure(state="disabled")
        else:
            self.entry.configure(state="normal")
            self.execute_button.configure(state="normal")

    def add_alpha_event(self):
        if self.alpha_entry._state == "normal":
            self.alpha_entry.configure(state="disabled")
        else:
            self.alpha_entry.configure(state="normal")

    def open_training_file_event(self):
        path = customtkinter.filedialog.askopenfile()
        if path != None:
            self.training_data_entry.delete(0, customtkinter.END)
            self.training_data_entry.insert(0, path.name)

    def open_test_file_event(self):
        path = customtkinter.filedialog.askopenfile()
        if path != None:
            self.test_data_entry.delete(0, customtkinter.END)
            self.test_data_entry.insert(0, path.name)

    def save_data_button_event(self):
        self.textbox.insert("0.0", "\n")

        if self.training_data_entry.get() != "":
            training_response = Prepare_data.read_file(self.training_data_entry.get())
            if training_response == -1:
                error_message = "No such training file"
                self.textbox.insert("0.0", error_message + "\n\n")
                self.textbox.tag_add("err", "1.0", "1." + str(len(error_message)))
                self.textbox.tag_config("err", foreground="#FF6B68")
            else:
                self.training_data = training_response
                self.textbox.insert("0.0",
                                    "Training data is from " + self.training_data_entry.get().split("/")[-1] + "\n")

        if self.test_data_entry.get() != "":
            test_response = Prepare_data.read_file(self.test_data_entry.get())
            if test_response == -1:
                error_message = "No such training file"
                self.textbox.insert("0.0", error_message + "\n\n")
                self.textbox.tag_add("err", "1.0", "1." + str(len(error_message)))
                self.textbox.tag_config("err", foreground="#FF6B68")
            else:
                self.test_data = test_response
                self.textbox.insert("0.0", "Test data is from " + self.test_data_entry.get().split("/")[-1] + "\n")

        alpha = self.alpha_entry.get()
        if self.alpha_entry._state == "disabled":
            self.alpha = 0.01
        elif alpha != "":
            self.alpha = float(alpha)

        self.textbox.insert("0.0", "Alpha = " + str(self.alpha) + "\n\n")

    def clear_data_button_event(self):
        self.training_data_entry.delete(0, customtkinter.END)
        self.test_data_entry.delete(0, customtkinter.END)
        self.alpha_entry.delete(0, customtkinter.END)

    def learn_button_event(self):
        if len(self.training_data) == 0 or self.alpha == 0.0:
            self.textbox.insert("0.0", "Podaj właściwe dane\n\n")
            return

        self.perceptron_list = Network.generate_perceptions_list(self.training_data, float(self.alpha))
        for p in self.perceptron_list:
            p.__learn__()
            self.tabview.add(p.name)
            # print(p.name)
            self.tabview.tab(p.name).grid_columnconfigure(0, weight=1)
            label = customtkinter.CTkLabel(self.tabview.tab(p.name), text="name = " + p.name)
            label.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="snw")

            scroll_panel = customtkinter.CTkScrollableFrame(self.tabview.tab(p.name), label_text="Weights")
            scroll_panel.grid(row=1, column=0, padx=20, pady=0)

            i = 0
            for d in p.weight:
                label = customtkinter.CTkLabel(scroll_panel, text=d)
                label.grid(row=i, column=0, padx=10, pady=(2, 0), sticky="snw")
                i += 1

            label = customtkinter.CTkLabel(self.tabview.tab(p.name), text="teta = " + str(p.teta))
            label.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="snw")
            label = customtkinter.CTkLabel(self.tabview.tab(p.name), text="alpha = " + str(p.alfa))
            label.grid(row=3, column=0, padx=20, pady=(10, 0), sticky="snw")

        self.textbox.insert("0.0", "Learned\n\n")

    def try_button_event(self):
        if len(self.test_data) == 0:
            self.textbox.insert("0.0", "Enter test data\n\n")
            return

        correct_answers = Network.do(self.perceptron_list, self.test_data)
        self.textbox.insert("0.0", "Dane testowe: " + str(len(self.test_data)) + " | Dane sprawdzone: " + str(
            correct_answers) + "\n\n")

    def show_button_event(self):
        diagram_window = customtkinter.CTk()
        diagram_window.geometry("300x300")
        diagram_window.mainloop()

    def execute_button_event(self):
        if self.entry.get() == "":
            return

        data = Prepare_data.count_letters(self.entry.get())
        vector = My_Vector.My_Vector(data)
        result = Network.execute(self.perceptron_list, vector)
        self.entry.delete(0, customtkinter.END)
        self.textbox.insert("0.0", "Result = " + result + "\n\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
