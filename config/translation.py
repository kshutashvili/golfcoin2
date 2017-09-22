from modeltranslation.translator import translator, TranslationOptions

from .models import SiteConfiguration, Teammate, Advisor


class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('main_block_title',
              'main_block_subtitle',
              'main_block_timer_text',
              'about_title',
              'about_text',
              'project_plan_title',
              'project_plan_text1',
              'project_plan_text2',
              'project_plan_text3',
              'project_plan_text4',
              'project_plan_text5',
              'project_plan_text6',
              'team_block_title',
              'advisor_block_title')


# class DocumentTranslationOptions(TranslationOptions):
#     fields = ('text',)


class TeammateTranslationOptions(TranslationOptions):
    fields = ('name', 'position')


class AdvisorTranslationOptions(TranslationOptions):
    fields = ('name',)


# class ProjectTranslationOptions(TranslationOptions):
#     fields = ('title', 'text')


translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)
#translator.register(Document, DocumentTranslationOptions)
translator.register(Teammate, TeammateTranslationOptions)
translator.register(Advisor, AdvisorTranslationOptions)
#translator.register(Project, ProjectTranslationOptions)