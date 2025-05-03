# Code taken from: https://github.com/TomSchimansky/CustomTkinter/issues/2712#issuecomment-2813737035

import darkdetect
import sv_ttk

import customtkinter as ctk

class TabbableCheckBox(ctk.CTkCheckBox):
    def __init__(self,
                 master,
                 width = 100,
                 height = 24,
                 checkbox_width = 24,
                 checkbox_height = 24,
                 corner_radius = None,
                 border_width = None,
                 bg_color = "transparent",
                 fg_color = None,
                 hover_color = None,
                 border_color = None,
                 checkmark_color = None,
                 text_color = None,
                 text_color_disabled = None,
                 text = "CTkCheckBox",
                 font = None,
                 textvariable = None,
                 state = "normal",
                 hover = True,
                 command = None,
                 onvalue = 1,
                 offvalue = 0,
                 variable = None,
                 select_color: str | tuple[str, str] = ["#a5dcff", "#155d91"],
                 **kwargs):
        """
        Modified `CTkCheckbox` to support navigation through Tab.
        On tab selection, the background of the checkbox will be highlighted as `select_color`.
        Using the space bar key or enter key, it can be toggled between the states.
        """

        super().__init__(master, width, height, checkbox_width, checkbox_height, corner_radius, border_width, bg_color, fg_color, hover_color, border_color, checkmark_color, text_color, text_color_disabled, text, font, textvariable, state, hover, command, onvalue, offvalue, variable, **kwargs)

        self._bg_color_default = bg_color
        self._select_color = select_color

        self.bind("<FocusIn>", self._on_focus)
        self.bind("<FocusOut>", self._on_focus_out)
        self.bind("<KeyRelease-space>", self._focus_action)
        self.bind("<KeyRelease-Return>", self._focus_action)

    def _on_focus(self, e=None):
        self.configure(bg_color=self._select_color)


    def _on_focus_out(self, e=None):
        self.configure(bg_color=self._bg_color_default)


    def _focus_action(self, e=None):
        if self.cget("state") == "disabled":
            return

        if self.get():
            self.deselect()
        else:
            self.select()

    def configure(self, require_redraw=False, **kwargs):
        if "select_color" in kwargs:
            self._select_color = kwargs.pop("select_color")

        if "bg_color" in kwargs:
            if kwargs["bg_color"] != self._select_color:
                self._bg_color_default = kwargs["bg_color"]

        return super().configure(require_redraw, **kwargs)

    def cget(self, attribute_name):
        if attribute_name == "select_color":
            return self._select_color

        return super().cget(attribute_name)


if __name__ == "__main__":
    root = ctk.CTk()

    sv_ttk.set_theme(darkdetect.theme())

    frame = ctk.CTkFrame(root)
    frame.grid(row=0, column=0)
    w1 = TabbableCheckBox(frame, text="check one")
    w1.grid(row=0, column=0)
    w2 = TabbableCheckBox(frame, text="check two")
    w2.grid(row=1, column=0)
    w3 = TabbableCheckBox(frame, text="check three")
    w3.grid(row=2, column=0)
    w4 = TabbableCheckBox(frame, text="check four")
    w4.grid(row=3, column=0)
    w5 = TabbableCheckBox(frame, text="check five")
    w5.grid(row=4, column=0)

    w2.configure(state="disabled")

    root.mainloop()

