# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from solo.admin import SingletonModelAdmin

from django.contrib import admin

from .models import (SiteConfiguration, Teammate, Advisor, Partner,
                     AnswerQuestion, Discount, DonationAddresses)


class TeammateInline(admin.StackedInline):
    model = Teammate
    extra = 1
    insert_after = 'team_block_title_zh'


class AdvisorInline(admin.StackedInline):
    model = Advisor
    extra = 1
    insert_after = 'advisor_block_title_zh'


class PartnerInline(admin.StackedInline):
    model = Partner
    extra = 1
    insert_after = 'partners_block_title_zh'


class AnswerQuestionInline(admin.StackedInline):
    model = AnswerQuestion
    extra = 1
    insert_after = 'faq_block_title_zh'


class DiscountInline(admin.StackedInline):
    model = Discount
    extra = 1
    insert_after = 'discount_block_text_zh'


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    fieldsets = ((None, {
                    "fields": ("show_site",
                               "enable_es",
                               "enable_de",
                               "enable_zh")}),
                 ("Информация для главного блока", {
                    'classes': ('collapse',),
                    "fields": ("main_block_title_en",
                               "main_block_title_ru",
                               "main_block_title_de",
                               "main_block_title_es",
                               "main_block_title_zh",

                               "main_block_subtitle_en",
                               "main_block_subtitle_ru",
                               "main_block_subtitle_de",
                               "main_block_subtitle_es",
                               "main_block_subtitle_zh",

                               "main_block_start_link",
                               "main_block_whitepaper_link_en",
                               "main_block_whitepaper_link_ru",
                               "main_block_whitepaper_link_de",
                               "main_block_whitepaper_link_es",
                               "main_block_whitepaper_link_zh")}),
                 ("Таймер", {
                    'classes': ('collapse',),
                    "fields": ("show_timer",
                               "main_block_timer_text_en",
                               "main_block_timer_text_ru",
                               "main_block_timer_text_de",
                               "main_block_timer_text_es",
                               "main_block_timer_text_zh",
                               "timer_deadline")
                    }),
                 ("Блок 'Уже инвестировано'", {
                    'classes': ('collapse',),
                    "fields": ("investments_eth",
                               "investments_participants")}),
                 ("Блок 'О нас'", {
                    'classes': ('collapse',),
                    "fields": ("about_title_en",
                               "about_title_ru",
                               "about_title_de",
                               "about_title_es",
                               "about_title_zh",
                               "about_text_en",
                               "about_text_ru",
                               "about_text_de",
                               "about_text_es",
                               "about_text_zh",
                               "about_address",
                               "about_block_html_id")
                  }),
                 ("Блок 'Discount'", {
                    'classes': ('collapse',),
                    "fields": ("discount_block_text_en",
                               "discount_block_text_ru",
                               "discount_block_text_de",
                               "discount_block_text_es",
                               "discount_block_text_zh",)}),
                 ("Текст над формой входа", {
                    'classes': ('collapse',),
                    "fields": ("login_form_text_en",
                               "login_form_text_ru",
                               "login_form_text_de",
                               "login_form_text_es",
                               "login_form_text_zh",)}),
                 ("Блок 'How it works'", {
                    'classes': ('collapse',),
                    "fields": ("how_block_block_title_en",
                               "how_block_block_title_ru",
                               "how_block_block_title_de",
                               "how_block_block_title_es",
                               "how_block_block_title_zh",
                               "how_block_video_en",
                               "how_block_video_ru",
                               "how_block_video_de",
                               "how_block_video_es",
                               "how_block_video_zh",)}),
                 ("Блок 'План проекта'", {
                    'classes': ('collapse',),
                    "fields": ("project_plan_html_id",
                               "project_plan_title_en",
                               "project_plan_title_ru",
                               "project_plan_title_de",
                               "project_plan_title_es",
                               "project_plan_title_zh",
                               ("project_plan_text1_en",
                                "project_plan_text1_ru",
                                "project_plan_text1_de",
                                "project_plan_text1_es",
                                "project_plan_text1_zh",
                                "project_plan_date1"),
                               ("project_plan_text2_en",
                                "project_plan_text2_ru",
                                "project_plan_text2_de",
                                "project_plan_text2_es",
                                "project_plan_text2_zh",
                                "project_plan_date2"),
                               ("project_plan_text3_en",
                                "project_plan_text3_ru",
                                "project_plan_text3_de",
                                "project_plan_text3_es",
                                "project_plan_text3_zh",
                                "project_plan_date3"),
                               ("project_plan_text4_en",
                                "project_plan_text4_ru",
                                "project_plan_text4_de",
                                "project_plan_text4_es",
                                "project_plan_text4_zh",
                                "project_plan_date4"),
                               ("project_plan_text5_en",
                                "project_plan_text5_ru",
                                "project_plan_text5_de",
                                "project_plan_text5_es",
                                "project_plan_text5_zh",
                                "project_plan_date5"),
                               ("project_plan_text6_en",
                                "project_plan_text6_ru",
                                "project_plan_text6_de",
                                "project_plan_text6_es",
                                "project_plan_text6_zh",
                                "project_plan_date6"),)
                    }),
                 ("Блок 'Details'", {
                    'classes': ('collapse',),
                    "fields": ("details_block_html_id",
                               "details_block_title_en",
                               "details_block_title_ru",
                               "details_block_title_de",
                               "details_block_title_es",
                               "details_block_title_zh",
                               ("details_img_1_en",
                                "details_img_1_ru",
                                "details_img_1_de",
                                "details_img_1_es",
                                "details_img_1_zh"),

                               ("details_img_2_en",
                                "details_img_2_ru",
                                "details_img_2_de",
                                "details_img_2_es",
                                "details_img_2_zh"))}),
                 ("Блок 'Команда'", {
                    'classes': ('collapse',),
                    "fields": ("team_block_html_id",
                               "team_block_title_en",
                               "team_block_title_ru",
                               "team_block_title_de",
                               "team_block_title_es",
                               "team_block_title_zh",)}),
                 ("Блок 'Советники'", {
                    'classes': ('collapse',),
                    "fields": ("advisor_block_html_id",
                               "advisor_block_title_en",
                               "advisor_block_title_ru",
                               "advisor_block_title_de",
                               "advisor_block_title_es",
                               "advisor_block_title_zh",)}),
                 ("Блок 'Партнеры'", {
                    'classes': ('collapse',),
                    "fields": ("partners_block_html_id",
                               "partners_block_title_en",
                               "partners_block_title_ru",
                               "partners_block_title_de",
                               "partners_block_title_es",
                               "partners_block_title_zh",)}),
                 ("Блок 'FAQ'", {
                    'classes': ('collapse',),
                    "fields": ("faq_block_html_id",
                               "faq_block_title_en",
                               "faq_block_title_ru",
                               "faq_block_title_de",
                               "faq_block_title_es",
                               "faq_block_title_zh",)}),
                 ("Блок 'Subscribe'", {
                    'classes': ('collapse',),
                    "fields": ("subscribe_block_html_id",
                               "subscribe_block_title_en",
                               "subscribe_block_title_ru",
                               "subscribe_block_title_de",
                               "subscribe_block_title_es",
                               "subscribe_block_title_zh",)}),
                 ("Контакты", {
                    'classes': ('collapse',),
                    "fields": ("main_email",
                               "social_block_title_en",
                               "social_block_title_ru",
                               "social_block_title_de",
                               "social_block_title_es",
                               "social_block_title_zh")
                    }),
                 ("Документы 'Terms & Condition, Privacy Policy'", {
                    'classes': ('collapse',),
                    "fields": ("terms_and_conditions_en",
                               "terms_and_conditions_ru",
                               "terms_and_conditions_de",
                               "terms_and_conditions_es",
                               "terms_and_conditions_zh",
                               "privacy_policy_en",
                               "privacy_policy_ru",
                               "privacy_policy_de",
                               "privacy_policy_es",
                               "privacy_policy_zh",)}),
                 ("Правила для загрузки документов", {
                     'classes': ('collapse',),
                     "fields": (
                         "documents_rules_en",
                         "documents_rules_ru",
                         "documents_rules_de",
                         "documents_rules_es",
                         "documents_rules_zh",)}),
                 ("Социальные сети", {
                    'classes': ('collapse',),
                    "fields": ("social_in",
                               "social_fb",
                               "social_insta",
                               "social_twi",
                               "social_telegram")}),)
    inlines = [TeammateInline,
               AdvisorInline,
               PartnerInline,
               AnswerQuestionInline,
               DiscountInline]
    change_form_template = 'admin/custom/change_form.html'


@admin.register(DonationAddresses)
class DonationAddressesAdmin(SingletonModelAdmin):
    pass
