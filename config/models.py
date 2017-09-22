# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from solo.models import SingletonModel

from django.db import models


class SiteConfiguration(SingletonModel):
    show_site = models.BooleanField('Включить основной сайт',
                                    default=True)
    # main block
    main_block_title = models.CharField('Заголовок блока',
                                         max_length=128,
                                         default='We integrates the blockchain of 60 million golfers')
    main_block_subtitle = models.CharField('Подзаголовок блока',
                                           max_length=128,
                                           default='Discount for early investors up to 40%')
    main_block_start_link = models.CharField('Ссылка в кнопке "Start Pre-ICO"',
                                             max_length=255,
                                             blank=True)
    main_block_whitepaper_link = models.CharField("Ссылка в кнопке 'Whitepaper'",
                                                  max_length=255,
                                                  blank=True)
    main_block_timer_text = models.CharField('Текст таймера',
                                  max_length=128,
                                  default='Pre-ICO tokens golfcoin starts through')
    show_timer = models.BooleanField('Включить таймер',
                                    default=True)
    # footer contacts
    main_email = models.EmailField('Email',
                                   max_length=128,
                                   default='support@golfcoin.club')
    # block about
    about_title = models.CharField("Заголовок блока 'О нас'",
                                   max_length=128,
                                   default='What is Golfcoin?')
    about_text = models.TextField("Текст блока 'О нас'",
                                  blank=True)
    about_address = models.CharField("Адрес в блоке 'О нас'",
                                     max_length=128)
    about_block_html_id = models.CharField("Идентификатор HTML",
                                           max_length=32,
                                           default='about')
    # footer socials
    social_in = models.CharField('Ссылка Linkedin',
                                 max_length=128,
                                 blank=True,
                                 help_text='https://linkedin.com/golfco')
    social_fb = models.CharField('Ссылка Facebook',
                                       max_length=128,
                                       blank=True,
                                       help_text='https://facebook.com/golfco')
    social_insta = models.CharField('Ссылка Instagram',
                                    max_length=128,
                                    blank=True,
                                    help_text='https://instagram.com/golfco')
    social_twi = models.CharField('Ссылка Twitter',
                                      max_length=128,
                                      blank=True,
                                      help_text='https://twitter.com/golfco')
    social_telegram = models.CharField('Ссылка Telegram',
                                      max_length=128,
                                      blank=True,
                                      help_text='https://t.co/golfco')
    # block investments
    investments_eth = models.IntegerField("Инвестировано ETH",
                                          default=0)
    investments_participants = models.IntegerField("Количество инвестировавших",
                                                   default=0)
    # block project-plan
    project_plan_html_id = models.CharField("Идентификатор HTML",
                                            max_length=32,
                                            default='roadmap')
    project_plan_title = models.CharField("Заголовок блока 'Roadmap'",
                                           max_length=128,
                                           default="Roadmap")
    project_plan_date1 = models.DateField("План 1 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text1 = models.CharField("План 1 (текст)",
                                          max_length=128,
                                          blank=True)
    project_plan_date2 = models.DateField("План 2 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text2 = models.CharField("План 2 (текст)",
                                          max_length=128,
                                          blank=True)
    project_plan_date3 = models.DateField("План 3 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text3 = models.CharField("План 3 (текст)",
                                          max_length=128,
                                          blank=True)
    project_plan_date4 = models.DateField("План 4 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text4 = models.CharField("План 4 (текст)",
                                          max_length=128,
                                          blank=True)
    project_plan_date5 = models.DateField("План 5 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text5 = models.CharField("План 5 (текст)",
                                          max_length=128,
                                          blank=True)
    project_plan_date6 = models.DateField("План 6 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text6 = models.CharField("План 6 (текст)",
                                          max_length=128,
                                          blank=True)
    # block team
    team_block_title = models.CharField("Заголовок для блока 'Team'",
                                        max_length=128,
                                        default="Team")
    # block advisors
    advisor_block_title = models.CharField("Заголовок для блока 'Advisors'",
                                           max_length=128,
                                           default="Advisors")
    # block documents
    # document_block_title = models.CharField("Заголовок для блока 'Документы'",
    #                                         max_length=128,
    #                                         default="Документы")
    # block projects
    # projects_block_title = models.CharField("Заголовок для блока 'Проекты'",
    #                                         max_length=128,
    #                                         default="Проекты")

    class Meta:
        verbose_name = "Конфигурация сайта"

    def __unicode__(self):
        return "Конфигурация сайта"



class Teammate(models.Model):
    config = models.ForeignKey(SiteConfiguration,
                               verbose_name="Настройки сайта",
                               related_name="teammates")
    photo = models.ImageField("Фото",
                              upload_to="team")
    name = models.CharField("Имя",
                            max_length=128)
    position = models.CharField("Должность",
                                max_length=128)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __unicode__(self):
        return self.name


class Advisor(models.Model):
    config = models.ForeignKey(SiteConfiguration,
                               verbose_name="Настройки сайта",
                               related_name="advisors")
    photo = models.ImageField("Фото",
                              upload_to="team")
    name = models.CharField("Имя",
                            max_length=128)

    class Meta:
        verbose_name = "Советник (Advisor)"
        verbose_name_plural = "Советники (Advisors)"

    def __unicode__(self):
        return self.name