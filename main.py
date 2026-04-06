from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class AppCumple(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.mensaje = Label(
            text="¡Hola Amor mio, precioso mi cuchurrumin preciosa,potra, diva empoderade, feministe" \
            "!\nTengo algo que decirte...",
            font_size='24sp',
            halign='center'
        )
        
        boton = Button(
            text="APRETELE",
            size_hint=(1, 0.3),
            background_color=(1, 0.4, 0.7, 1) # Color rosado
        )
        boton.bind(on_press=self.sorpresa)
        
        layout.add_widget(self.mensaje)
        layout.add_widget(boton)
        return layout

    def sorpresa(self, instance):
        self.mensaje.text = "¡ESTOY EMBARAZADO!\n" "¡Feliz Cumpleaños, mi amor! 🎂💖 Eres la dueña de mi corazon. 🌟 Gracias por ser mi compañera, mi mejor amiga y el amor de mi vida.🌹👩‍❤️‍💋‍👨✨"
        instance.text = "¡Te amo!"

if __name__ == "__main__":
    AppCumple().run()
