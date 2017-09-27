# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from solo.admin import SingletonModelAdmin

from django.contrib import admin

from .models import SiteConfiguration, Teammate, Advisor, Partner



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


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    fieldsets = ((None, {
                    "fields": ("show_site",)}),
                 ("Информация для главного блока", {
                    'classes': ('collapse',),
                    "fields": ("main_block_title",
                               "main_block_title_en",
                               "main_block_title_ru",
                               "main_block_title_zh",

                               "main_block_subtitle",
                               "main_block_subtitle_en",
                               "main_block_subtitle_ru",
                               "main_block_subtitle_zh",

                               "main_block_start_link",
                               "main_block_whitepaper_link",
                               "main_block_whitepaper_link_en",
                               "main_block_whitepaper_link_ru",
                               "main_block_whitepaper_link_zh")}),
                 ("Таймер", {
                    'classes': ('collapse',),
                    "fields": ("show_timer",
                               "main_block_timer_text",
                               "main_block_timer_text_en",
                               "main_block_timer_text_ru",
                               "main_block_timer_text_zh",
                               "timer_deadline")
                    }),
                 ("Блок 'Уже инвестировано'", {
                    'classes': ('collapse',),
                    "fields": ("investments_eth",
                               "investments_participants")}),
                 ("Блок 'О нас'", {
                    'classes': ('collapse',),
                    "fields": ("about_title",
                               "about_title_en",
                               "about_title_ru",
                               "about_title_zh",
                               "about_text",
                               "about_text_en",
                               "about_text_ru",
                               "about_text_zh",
                               "about_address",
                               "about_block_html_id")
                  }),
                 ("Блок 'План проекта'", {
                    'classes': ('collapse',),
                    "fields": ("project_plan_html_id",
                               "project_plan_title",
                               "project_plan_title_en",
                               "project_plan_title_ru",
                               "project_plan_title_zh",
                               ("project_plan_text1",
                                "project_plan_text1_en",
                                "project_plan_text1_ru",
                                "project_plan_text1_zh",
                                "project_plan_date1"),
                               ("project_plan_text2",
                                "project_plan_text2_en",
                                "project_plan_text2_ru",
                                "project_plan_text2_zh",
                                "project_plan_date2"),
                               ("project_plan_text3",
                                "project_plan_text3_en",
                                "project_plan_text3_ru",
                                "project_plan_text3_zh",
                                "project_plan_date3"),
                               ("project_plan_text4",
                                "project_plan_text4_en",
                                "project_plan_text4_ru",
                                "project_plan_text4_zh",
                                "project_plan_date4"),
                               ("project_plan_text5",
                                "project_plan_text5_en",
                                "project_plan_text5_ru",
                                "project_plan_text5_zh",
                                "project_plan_date5"),
                               ("project_plan_text6",
                                "project_plan_text6_en",
                                "project_plan_text6_ru",
                                "project_plan_text6_zh",
                                "project_plan_date6"),)
                    }),
                 ("Блок 'Команда'", {
                    'classes': ('collapse',),
                    "fields": ("team_block_title",
                               "team_block_title_en",
                               "team_block_title_ru",
                               "team_block_title_zh",)}),
                 ("Блок 'Советники'", {
                    'classes': ('collapse',),
                    "fields": ("advisor_block_title",
                               "advisor_block_title_en",
                               "advisor_block_title_ru",
                               "advisor_block_title_zh",)}),
                 ("Блок 'Партнеры'", {
                    'classes': ('collapse',),
                    "fields": ("partners_block_title",
                               "partners_block_title_en",
                               "partners_block_title_ru",
                               "partners_block_title_zh",)}),
                 ("Контакты", {
                    'classes': ('collapse',),
                    "fields": ("main_email",)
                    }),
                 ("Социальные сети", {
                    'classes': ('collapse',),
                    "fields": ("social_in",
                               "social_fb",
                               "social_insta",
                               "social_twi",
                               "social_telegram")
                    }),)
    inlines = [TeammateInline, AdvisorInline, PartnerInline]
    change_form_template = 'admin/custom/change_form.html'

