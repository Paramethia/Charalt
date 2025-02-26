import os

from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window
from kivy.core.clipboard import Clipboard
from kivy.core.text import Label as CoreLabel
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.behaviors import HoverBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.dialog import MDDialog
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput
from kivymd.uix.button import MDRectangleFlatButton, MDRectangleFlatIconButton

Config.set('graphics', 'minimum_width', '825')
Config.set('graphics', 'minimum_height', '540')
Config.write()

logo = os.path.join(os.path.dirname(__file__), "Charalt-logo.ico")
Window.icon = logo

kv_file = os.path.join(os.path.dirname(__file__), "stylation.kv")

Builder.load_file(kv_file)

rubik_font = os.path.join(os.path.dirname(__file__), "fonts/Rubik-VariableFont_wght.ttf")

CoreLabel.register("Rubik", rubik_font)

#Passed classes from kivy file:

class Header(Label):
    pass

class InputT(MDTextField, HoverBehavior):
    def on_enter(self):
        Window.set_system_cursor('ibeam')

    def on_leave(self):
        Window.set_system_cursor('arrow')

class Error(MDLabel):
    pass

class SubmitB(MDRectangleFlatButton, HoverBehavior):
    def on_enter(self):
        self.md_bg_color = 0.54, 0.81, 0.91, 0.7
        self.line_color = 0, 0, 0, 1
        Window.set_system_cursor("hand")

    def on_leave(self):
        self.line_color = 0.68, 0.85, 0.91, 0.8
        self.md_bg_color = 0.68, 0.85, 0.91, 0.8
        Window.set_system_cursor("arrow")

class InputShow(MDRectangleFlatButton, HoverBehavior):
    def on_enter(self):
        self.line_color = (1, 1, 1, 1)
        self.text_color = (1, 1, 1, 1)
        Window.set_system_cursor("hand")

    def on_leave(self):
        self.line_color = (0.68, 0.85, 0.91, 0.8)
        self.text_color = (0.68, 0.85, 0.91, 0.8)
        Window.set_system_cursor("arrow")

class InputCon(MDDialog):
    pass

class BackB(MDRectangleFlatIconButton, HoverBehavior):
    def on_enter(self):
        self.md_bg_color = 0.8, 0.8, 0.8, 0.7
        self.line_color = 0, 0, 0, 1
        Window.set_system_cursor("hand")

    def on_leave(self):
        self.line_color = 0.68, 0.85, 0.91, 0.8
        self.md_bg_color = 0.68, 0.85, 0.91, 0.8
        Window.set_system_cursor("arrow")

class OutputCon(MDBoxLayout):
    pass

class OutputHeader(MDLabel):
    pass

class Output(MDLabel):
    pass

class InfoT(MDLabel):
    pass

class InputF(MDBoxLayout):
    pass

class AltInput(MDTextField):
    pass

class AltBCon(MDStackLayout):
    pass

class AlterB(MDRectangleFlatButton, HoverBehavior):
    def on_enter(self):
        self.md_bg_color = 0.54, 0.81, 0.91, 0.7
        self.line_color = 0, 0, 0, 1
        Window.set_system_cursor("hand")

    def on_leave(self):
        self.line_color = 0.68, 0.85, 0.91, 0.8
        self.md_bg_color = 0.68, 0.85, 0.91, 0.8
        Window.set_system_cursor("arrow")

class CopyB(MDRectangleFlatButton, HoverBehavior):
    def on_enter(self):
        self.md_bg_color = (0.68, 0.85, 0.91, 0.8)
        Window.set_system_cursor("hand")

    def on_leave(self):
        #self.md_bg_color = 0.54, 0.81, 0.91, 0.7
        self.md_bg_color = (0.17, 0.17, 0.17, 1)
        self.line_color = 0.8, 0.8, 0.8, 1
        self.text_color = 0.8, 0.8, 0.8, 1
        Window.set_system_cursor("arrow")

class Charalt(MDApp):
    def build(self):
        #self.theme_cls.primary_palette = 'LightBlue'

        self.root_l = MDBoxLayout(orientation="vertical", md_bg_color=(0.17, 0.17, 0.17, 1))

        header = Header(text="Charalt")
        description = MDLabel(
            text="Hello there. Welcome to Charalt! Use this to alter your text to however you would like.",
            font_style='H6', theme_text_color="Custom", text_color=(0.89, 0.89, 0.89, 1)
        )

        self.warning = Error()

        self.text_input = InputT(hint_text="Paste/type the text you want to format.")
        self.text_input.bind(text=self.limit_input)

        self.submit_b = SubmitB(text="Alter", on_press=self.change_l)

        self.output_str = ""
        
        self.root_l.add_widget(header)
        self.root_l.add_widget(description)
        self.root_l.add_widget(self.text_input)
        self.root_l.add_widget(self.warning)
        self.root_l.add_widget(self.submit_b)

        return self.root_l

    def change_l(self, instance):
        input_str = self.text_input.text
        print(f"Length of string: {len(input_str)}")
        if input_str:
            #Window.minimum_width = 925
            #Window.minimum_height = 640
            Window.size = (925, 640)
            self.warning.text = ""

            alteration_l = MDBoxLayout(orientation='vertical', spacing=22)

            show_input_b = InputShow(text="Show input", on_press=self.show_input)

            float_l = MDFloatLayout()

            back_b = BackB(text="Back", icon='arrow-left', on_press=self.back)

            float_l.add_widget(back_b)

            info_text = InfoT(text="Enter a maximum of 7 characters that you want to alter form your submitted text:")

            input_field = InputF()

            self.choice = AltInput(hint_text="Choose")
            self.replacement = AltInput(hint_text="Repacements?")

            input_field.add_widget(self.choice)
            input_field.add_widget(self.replacement)

            self.choice.bind(text=self.limit_choice)
            self.replacement.bind(text=self.limit_choice)

            self.warning2 = Error()

            alt_butts_con = AltBCon()

            replace_b = AlterB(text="Replace", on_press=self.replace)
            uppercase_b = AlterB(text="Uppercase", on_press=self.capitalize)
            lowercase_b = AlterB(text="Lowercase", on_press=self.lowercase)
            remove_b = AlterB(text="Remove", on_press=self.remove_char)
            revert_b = AlterB(text="Revert", on_press=self.revert)

            alt_butts_con.add_widget(replace_b)
            alt_butts_con.add_widget(uppercase_b)
            alt_butts_con.add_widget(lowercase_b)
            alt_butts_con.add_widget(remove_b)
            alt_butts_con.add_widget(revert_b)

            output_con = OutputCon()

            oc_head = OutputHeader(text="Your output")
            self.output = Output(text="Your output will appear here")
            copy_b = CopyB(text="Copy", on_press=self.copy)

            #output_con.add_widget(oc_head)
            output_con.add_widget(self.output)
            #output_con.add_widget(copy_b)

            alteration_l.add_widget(float_l)
            alteration_l.add_widget(show_input_b)
            alteration_l.add_widget(info_text)
            alteration_l.add_widget(input_field)
            alteration_l.add_widget(self.warning2)
            alteration_l.add_widget(alt_butts_con)
            alteration_l.add_widget(output_con)
            alteration_l.add_widget(copy_b)

            self.root_l.clear_widgets()
            self.root_l.add_widget(alteration_l)

        else:
            self.warning.text = "No text entered or the text is less than 5 characters long -_-"

    def limit_input(self, instance, value):
        max_length = 800
        if len(value) > max_length:
            instance.text = value[:max_length]

    def back(self, instance):
        self.root_l.clear_widgets()
        self.build()
        Window.add_widget(self.root_l)

    def limit_choice(self, instance, value):
        max_length = 14
        if len(value) > max_length:
            instance.text = value[:max_length]

    #Alteration functions

    def show_input(self, instance):
        #close_b = MDRectangleFlatIconButton(icon='close', icon_color=(0.68, 0.85, 0.91, 0.8))
        input_dia = InputCon(title="Your input", text=self.text_input.text)

        input_dia.open()

    def replace(self, instance):
        input_string = self.text_input.text
        chosen_str = self.choice.text
        replacement_str = self.replacement.text
        characters_not_found = 0
        if chosen_str and replacement_str and len(chosen_str) == len(replacement_str):
            print(f"String chosen to replace: {chosen_str} \n String replacement: {replacement_str}")
            chosen_characters = []
            replacement_characters = []
            for character in chosen_str:
                chosen_characters.append(character)
                if character not in input_string:
                    characters_not_found += 1
            print(chosen_characters)
            for character in replacement_str:
                replacement_characters.append(character)
            print(replacement_characters)
            if characters_not_found == 0:
                self.warning2.text = ""
                self.warning.color = (161/255, 22/255, 22/255, 1)
                print("Chosen characters are in the input string ^_^")
                if len(chosen_str) == 1:
                    self.output_str = input_string.replace(chosen_str, replacement_str)
                    self.output.text_color = (0.72, 0.71, 0.35, 1)
                    self.output.text = self.output_str
                else:
                    # Create a translation dictionary
                    translation_dict = str.maketrans(chosen_str, replacement_str)

                    # Apply translation
                    self.output_str = input_string.translate(translation_dict)
                    self.output.text = self.output_str
            elif characters_not_found == 1:
                self.warning2.text = "One of your chosen characters were not found in the input U_U"
                self.warning2.color = (161/255, 94/255, 22/255, 1)
            elif characters_not_found > 1:
                self.warning2.text = "2 or more of your chosen characters were not found in the input (remember that it is case sensitive)"
                self.warning2.color = (161/255, 94/255, 22/255, 1)
        else:
            self.warning2.text = "No chosen alterations and/or replacements entered or the lengths are not the same -_-"
            self.warning2.color = (0.78, 0.09, 0.09, 1)

    def capitalize(self, instance):
        input_string = self.text_input.text
        output_string = self.output_str
        self.output.text_color = (0.72, 0.71, 0.35, 1)
        if output_string:
            output_string = output_string.upper()
        else:
            output_string = input_string.upper()
        self.output_str = output_string
        self.output.text = output_string


    def lowercase(self, instance):
        input_string = self.text_input.text
        output_string = self.output_str
        self.output.text_color = (0.72, 0.71, 0.35, 1)
        if output_string:
            output_string = output_string.lower()
        else:
            output_string = input_string.lower()
        self.output_str = output_string
        self.output.text = output_string


    def remove_char(self, instance):
        input_string = self.text_input.text
        chosen_str = self.choice.text
        removal = ""
        if chosen_str:
            self.warning2.text = ""
            print(f"String chosen to remove: {chosen_str}")
            chosen_characters = []
            characters_not_found = 0
            for character in chosen_str:
                chosen_characters.append(character)
                if character not in input_string:
                    characters_not_found += 1
                if len(chosen_str) > 1:
                    removal += " "
            print(chosen_characters)
            if characters_not_found == 0:
                self.output.text_color = (0.72, 0.71, 0.35, 1)
                if len(chosen_str) > 1:
                    translation_dic = str.maketrans(chosen_str, removal)
                    self.output_str = input_string.translate(translation_dic)
                    #for char in chosen_characters:
                        #self.output_str = input_string.replace(char, "")
                    self.output.text = self.output_str
                else:
                    self.output_str = input_string.replace(chosen_str, "")
                    self.output.text = self.output_str
            elif characters_not_found == 1:
                self.warning2.text = "One of your chosen characters were not found in the input U_U"
                self.warning2.color = (161 / 255, 94 / 255, 22 / 255, 1)
            elif characters_not_found > 1:
                self.warning2.text = "2 or more of your chosen characters were not found in the input (remember that it is case sensitive)"
                self.warning2.color = (161 / 255, 94 / 255, 22 / 255, 1)
        else:
            self.warning2.text = "You have no chosen characters to remove -_-"
            self.warning2.color = (0.78, 0.09, 0.09, 1)

    def revert(self, instance):
        input_str = self.text_input.text
        if self.output_str:
            self.output.text_color = (0.72, 0.71, 0.35, 1)
            self.warning2.text = ""
            self.output_str = ""
            self.output.text = input_str
        else:
            self.warning2.text = "You have no output to revert -_-"
            self.warning2.color = (0.78, 0.09, 0.09, 1)

    def copy(self, instance):
        if self.output_str:
            self.warning2.text = ""
            Clipboard.copy(self.output_str)
            print("Output copied to clipboard")
        else:
            self.warning2.text = "No output to copy"

if __name__ == '__main__':
    Charalt().run()