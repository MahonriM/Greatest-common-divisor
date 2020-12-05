from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
Builder.load_string('''
<MyGrid>:
    num1:num1
    num2:num2
    res:res
    GridLayout:
        cols:1
        size:root.width,root.height
        GridLayout:
            cols:2
            Label:
                text:"Number 1"
            TextInput:
                id:num1
                multiline:False
            Label:
                text:"Number 2"
            TextInput:
                id:num2
                multiline:False
            Label:
                id:res
                text:""
        Button:
            text:"Greatest common divisor"
            on_press:root.bgc()''')
def mcd(num1,num2):
    if num2==0:
        return num1
    else:
        return mcd(num2,num1%num2)
class MyGrid(Widget):
    num1=ObjectProperty(None)
    num2=ObjectProperty(None)
    def bgc(self):
        num1=int(self.num1.text)
        num2=int(self.num2.text)
        self.res.text=("El MCD {0}".format(mcd(num1,num2)))
class MyApp(App):
     def build(self):       
         return MyGrid()
if __name__=="__main__":
    MyApp().run()
