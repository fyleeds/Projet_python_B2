import wx
from wx.core import DEFAULT_FRAME_STYLE, ID_ANY, DefaultPosition, DefaultSize, EmptyString, FrameNameStr
import get_info
from character import Character, Warrior, Mage, Thief
from adv import adversaire
from dice import Dice

class DiceWarriorsFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(DiceWarriorsFrame, self).__init__(*args, **kw)

        self.char1 : Character = None
        self.adv : Character = adversaire()
        self.SetSize((400, 600))
        
        self.menuStart = self.create_menuStart()
        self.premiermenu_panel = self.create_premiermenu_panel()
        self.secondmenu_panel = self.create_secondmenu_panel()
        self.create_char_panel = self.create_char_panel()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.menuStart, 1, wx.EXPAND)
        self.sizer.Add(self.premiermenu_panel, 1, wx.EXPAND)
        self.sizer.Add(self.secondmenu_panel, 1, wx.EXPAND)
        self.sizer.Add(self.create_char_panel, 1, wx.EXPAND)

        self.SetSizer(self.sizer)
        self.Layout()

        self.menuStart.Show()
        self.premiermenu_panel.Hide()
        self.secondmenu_panel.Hide()

    def verif(self, name):
        if name in info:
            return True
        else:
            return False

    def create_menuStart(self):
        panel = wx.Panel(self)

        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRALIGHT)
        title = wx.StaticText(panel, label="Dice Warriors", pos=(100, 20))
        title.SetFont(font)

        myButton = wx.Button(panel, label="PLAY", pos=(100, 200), size=(175, 100))
        myButton.Bind(wx.EVT_BUTTON, self.start)

        return panel

    def create_premiermenu_panel(self):
        panel = wx.Panel(self)

        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRALIGHT)
        title = wx.StaticText(panel, label="Dice Warriors", pos=(100, 20))
        title.SetFont(font)

        myButton = wx.Button(panel, label="chpan", pos=(335, 536), size=(50, 25))
        myButton.Bind(wx.EVT_BUTTON, self.action)

        i = 230
        n = 0
        texte = wx.StaticText(panel, label="Creer ou choisir un personnage :", pos=(100, 175))
        creerPersoBouton = wx.Button(panel, label="Créer un personnage", pos=(100, 200))
        creerPersoBouton.Bind(wx.EVT_BUTTON, self.CreerPerso)
        for name in info:
            n += 1
            choixPersoBouton = wx.Button(panel, label=f"{n} - {name}", pos=(100, i))
            choixPersoBouton.Bind(wx.EVT_BUTTON, self.ChoixPerso)
            i += 30

        

        return panel
    
    def create_char_panel(self):

        panel = wx.Panel(self)

        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRALIGHT)
        title = wx.StaticText(panel, label="Dice Warriors", pos=(100, 20))
        title.SetFont(font)



        return panel

    def create_secondmenu_panel(self):
        panel = wx.Panel(self)

        font = wx.Font(25, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_EXTRALIGHT)
        title = wx.StaticText(panel, label="Dice Warriors", pos=(100, 20))
        title.SetFont(font)

        # Déclarez name_label comme un attribut de classe
        self.name_label = wx.StaticText(panel, label="", pos=(100, 130))

        if self.char1 is not None and hasattr(self.char1, 'get_name'):
            self.name_label.SetLabel(f"Nom : {self.char1.get_name()}")
        advname = wx.StaticText(panel, label=f"Nom : {self.adv.get_name()}", pos=(100, 160))


        myButton = wx.Button(panel, label="chpan", pos=(335, 536), size=(50, 25))
        myButton.Bind(wx.EVT_BUTTON, self.action2)

        return panel
    
    def start(self, event):
        self.menuStart.Hide()
        self.premiermenu_panel.Show()
        self.Layout()

    def action(self, event):
        print("test")
        self.premiermenu_panel.Hide()
        self.secondmenu_panel.Show()
        self.Layout()

    def action2(self, event):
        self.premiermenu_panel.Show()
        self.secondmenu_panel.Hide()
        self.Layout()

    def CreerPerso(self, event):
        # Boîte de dialogue pour entrer le nom
        name_dialog = wx.TextEntryDialog(self, "Entrez le nom de votre personnage :", "Nom du personnage", style=wx.OK | wx.CANCEL)
        result_name_dialog = name_dialog.ShowModal()

        if result_name_dialog == wx.ID_OK:
            character_name = name_dialog.GetValue()
            print("Nom du personnage saisi :", character_name)

            # Utilisez votre fonction verif(name_char)
            if self.verif(character_name):
                wx.MessageBox(f"Le personnage '{character_name}' existe déjà. Veuillez choisir un autre nom.", "Erreur", wx.OK | wx.ICON_ERROR)
            else:
                # Boîte de dialogue pour entrer un chiffre entre 1 et 3
                number_dialog = wx.TextEntryDialog(self, "Entrez un chiffre entre 1 et 3 :", "Chiffre", style=wx.OK | wx.CANCEL)
                result_number_dialog = number_dialog.ShowModal()

                if result_number_dialog == wx.ID_OK:
                    try:
                        selected_number = int(number_dialog.GetValue())
                        if 1 <= selected_number <= 3:
                            print("Chiffre valide saisi :", selected_number)
                            # Vous pouvez maintenant utiliser le chiffre saisi selon vos besoins
                        else:
                            wx.MessageBox("Veuillez entrer un chiffre entre 1 et 3.", "Erreur", wx.OK | wx.ICON_ERROR)
                    except ValueError:
                        wx.MessageBox("Veuillez entrer un chiffre valide.", "Erreur", wx.OK | wx.ICON_ERROR)
                else:
                    # L'utilisateur a appuyé sur "Cancel" dans la boîte de dialogue du chiffre
                    print("Opération annulée.")

                number_dialog.Destroy()

        else:
            # L'utilisateur a appuyé sur "Cancel" dans la boîte de dialogue du nom
            print("Opération annulée.")

        name_dialog.Destroy()
        if selected_number == 1 : self.char1 = Warrior(character_name, 20, 8, 3, 1, Dice(6))
        elif selected_number == 2 : self.char1 = Mage(character_name, 20, 8, 3, 2, Dice(6))
        elif selected_number == 3 : self.char1 = Thief(character_name, 20, 8, 3, 3, Dice(6))
        else : self.char1 = Character(character_name, 20, 8, 3, 2, Dice(6))
        self.char1.json_save()
        self.secondmenu_panel.Show()
        self.premiermenu_panel.Hide()
        self.update_secondmenu_panel()
        self.Layout()


    def ChoixPerso(self, event):
        button = event.GetEventObject()
        label = button.GetLabel()
        name = label.split(" - ")[1]
        print(name)

    def update_secondmenu_panel(self):
        if self.char1 is not None and hasattr(self.char1, 'get_name'):
            self.name_label.SetLabel(f"Nom : {self.char1.get_name()}")
        else:
            # Si char1 n'est pas défini, mettez à jour les widgets pour indiquer qu'aucun personnage n'est créé
            self.name_label.SetLabel("Aucun personnage créé")
            # Mettez à jour d'autres widgets pour les autres données de char1

        # Assurez-vous que le panel est bien affiché
        self.secondmenu_panel.Show()
        # Assurez-vous que le sizer est mis à jour
        self.sizer.Layout()

if __name__ == '__main__':
    info = get_info.get_infos()
    app = wx.App()
    frame = DiceWarriorsFrame(None)
    frame.Center()
    frame.Show()
    app.MainLoop()
