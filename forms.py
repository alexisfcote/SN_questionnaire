# encoding: utf-8
from wtforms import Form, StringField, validators, RadioField, SelectField, BooleanField, IntegerField, SelectMultipleField, DateField, widgets, FieldList, FormField
from wtforms.widgets import TextArea
import datetime

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()



activity_list = ["Lever (nuit)",
    "Soins d’hygiène et habillage",
    "Travail en position assise",
    "Travail en position debout/accroupie",
    "Déplacements à la marche",
    "Escaliers (nombre)",
    "Période de repos en position allongée ou assise",
    "Repas (en position assise)",
    "Exercices",
    "Sortie du bateau",
    "Ménage",
    "Coucher (nuit) ",
    "Autres activités",]


class Activity(Form):
    activity_name = StringField("Nom de l'activité")
    activity_time = StringField("Heure")
    activity_type = SelectField("Type d'activité", choices=[(x,)*2 for x in activity_list])

class SNForm(Form):
    activity = FieldList(FormField(Activity), min_entries=1)
    stress = IntegerField('stress', [validators.number_range(
        0, 100, message="Évaluez votre stress")])
    workload = IntegerField('workload', [validators.number_range(
        0, 100, message="Évaluez votre effort moyen")])
    tiredness = IntegerField('tiredness', [validators.number_range(
        0, 100, message="Évaluez votre niveau de fatigue")])
    