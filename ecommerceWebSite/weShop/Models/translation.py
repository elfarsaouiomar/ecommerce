from modeltranslation.translator import TranslationOptions


# Updated the following accordingly.
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class CategoryTranslationOption(TranslationOptions):
    fields = ('name',)