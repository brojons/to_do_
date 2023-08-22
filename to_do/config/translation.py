from modeltranslation.translator import TranslationOptions,translator,register
from to_do.models import ToDoListModel

class ToDoTranslations(TranslationOptions):
    fields = ('task',)

translator.register(ToDoListModel,ToDoTranslations)
