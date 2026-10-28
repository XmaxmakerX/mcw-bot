from pywikibot import family


class Family(family.Family):
    name = 'mcw'
    langs = {
        'ru': 'ru.minecraft.wiki',
    }

    def scriptpath(self, code):
        return ''

    def protocol(self, code):
        return 'https'
