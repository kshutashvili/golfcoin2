from modeltranslation.translator import translator, TranslationOptions

from .models import (SiteConfiguration, Teammate, Advisor, Partner,
                     AnswerQuestion, Discount)


class SiteConfigurationTranslationOptions(TranslationOptions):
    fields = ('main_block_title',
              'main_block_subtitle',
              'main_block_timer_text',
              'main_block_whitepaper_link',
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
              'advisor_block_title',
              'partners_block_title',
              'faq_block_title',
              'how_block_video',
              'details_img_1',
              'details_img_2',
              'subscribe_block_title',
              'discount_block_text',
              'login_form_text',
              'details_block_title',
              'how_block_block_title',
              'social_block_title',
              'terms_and_conditions',
              'privacy_policy',
              'documents_rules')


class TeammateTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'experience')


class AdvisorTranslationOptions(TranslationOptions):
    fields = ('name',)


class PartnerTranslationOptions(TranslationOptions):
    fields = ('description',)


class AnswerQuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


class DiscountQuestionTranslationOptions(TranslationOptions):
    fields = ('discount_text', )


translator.register(SiteConfiguration, SiteConfigurationTranslationOptions)
translator.register(Teammate, TeammateTranslationOptions)
translator.register(Advisor, AdvisorTranslationOptions)
translator.register(Partner, PartnerTranslationOptions)
translator.register(AnswerQuestion, AnswerQuestionTranslationOptions)
translator.register(Discount, DiscountQuestionTranslationOptions)
