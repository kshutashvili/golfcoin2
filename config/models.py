# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from solo.models import SingletonModel
from ckeditor.fields import RichTextField

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
                                             max_length=128,
                                             blank=True)
    main_block_whitepaper_link = models.FileField("Whitepaper",
                                                  upload_to='whitepapers')
    main_block_timer_text = models.CharField('Текст таймера',
                                  max_length=64,
                                  default='Pre-ICO tokens golfcoin starts through')
    show_timer = models.BooleanField('Включить таймер',
                                    default=True)
    timer_deadline = models.DateField('Дата запуска проекта',
                                      default='2017-10-30',
                                      help_text='Дата для таймера')
    # footer contacts
    main_email = models.EmailField('Email',
                                   max_length=64,
                                   default='support@golfcoin.club')
    # block about
    about_title = models.CharField("Заголовок блока 'О нас'",
                                   max_length=128,
                                   default='What is Golfcoin?')
    about_text = RichTextField("Текст блока 'О нас'",
                               blank=True)
    about_address = models.CharField("Адрес в блоке 'О нас'",
                                     max_length=128)
    about_block_html_id = models.CharField("Идентификатор HTML",
                                           max_length=16,
                                           default='about')
    # footer socials
    social_block_title = models.CharField("Заголовок блока 'Контакты'",
                                          max_length=32,
                                          default="Join Us")
    social_in = models.CharField('Ссылка Linkedin',
                                 max_length=64,
                                 blank=True,
                                 help_text='https://linkedin.com/golfco')
    social_fb = models.CharField('Ссылка Facebook',
                                       max_length=64,
                                       blank=True,
                                       help_text='https://facebook.com/golfco')
    social_insta = models.CharField('Ссылка Instagram',
                                    max_length=64,
                                    blank=True,
                                    help_text='https://instagram.com/golfco')
    social_twi = models.CharField('Ссылка Twitter',
                                      max_length=64,
                                      blank=True,
                                      help_text='https://twitter.com/golfco')
    social_telegram = models.CharField('Ссылка Telegram',
                                      max_length=64,
                                      blank=True,
                                      help_text='https://t.co/golfco')
    # block investments
    investments_eth = models.IntegerField("Инвестировано ETH",
                                          default=0)
    investments_participants = models.IntegerField("Количество инвестировавших",
                                                   default=0)
    # block project-plan
    project_plan_html_id = models.CharField("Идентификатор HTML",
                                            max_length=16,
                                            default='roadmap')
    project_plan_title = models.CharField("Заголовок блока 'Roadmap'",
                                           max_length=64,
                                           default="Roadmap")
    project_plan_date1 = models.DateField("План 1 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text1 = models.CharField("План 1 (текст)",
                                          max_length=64,
                                          blank=True)
    project_plan_date2 = models.DateField("План 2 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text2 = models.CharField("План 2 (текст)",
                                          max_length=64,
                                          blank=True)
    project_plan_date3 = models.DateField("План 3 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text3 = models.CharField("План 3 (текст)",
                                          max_length=64,
                                          blank=True)
    project_plan_date4 = models.DateField("План 4 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text4 = models.CharField("План 4 (текст)",
                                          max_length=64,
                                          blank=True)
    project_plan_date5 = models.DateField("План 5 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text5 = models.CharField("План 5 (текст)",
                                          max_length=64,
                                          blank=True)
    project_plan_date6 = models.DateField("План 6 (дата)",
                                          blank=True,
                                          null=True)
    project_plan_text6 = models.CharField("План 6 (текст)",
                                          max_length=64,
                                          blank=True)
    # block details
    details_block_html_id = models.CharField("Идентификатор HTML",
                                             max_length=16,
                                             default='details')
    details_block_title = models.CharField("Заголовок блока 'Detail'",
                                           max_length=32,
                                           default="Details")
    details_img_1 = models.ImageField("Первое изображение для блока 'Details'",
                                      upload_to='details',
                                      blank=True,
                                      null=True)
    details_img_2 = models.ImageField("Второе изображение для блока 'Details'",
                                      upload_to='details',
                                      blank=True,
                                      null=True)
    # block team
    team_block_html_id = models.CharField("Идентификатор HTML",
                                          max_length=16,
                                          default='team')
    team_block_title = models.CharField("Заголовок для блока 'Team'",
                                        max_length=64,
                                        default="Team")
    # block advisors
    advisor_block_html_id = models.CharField("Идентификатор HTML",
                                             max_length=16,
                                             default='advisor')
    advisor_block_title = models.CharField("Заголовок для блока 'Advisors'",
                                           max_length=64,
                                           default="Advisors")
    # block partners
    partners_block_html_id = models.CharField("Идентификатор HTML",
                                              max_length=16,
                                              default='partners')
    partners_block_title = models.CharField("Заголовок для блока 'Our partners'",
                                            max_length=64,
                                            default="Our partners")
    # block FAQ
    faq_block_html_id = models.CharField("Идентификатор HTML",
                                           max_length=16,
                                           default='faq-block')
    faq_block_title = models.CharField("Заголовок для блока 'FAQ'",
                                       max_length=64,
                                       default="FAQ")
    # lang settings
    enable_es = models.BooleanField("Включить Испанский язык",
                                    default=False)
    enable_de = models.BooleanField("Включить Немецкий язык",
                                    default=False)
    enable_zh = models.BooleanField("Включить Китайский язык",
                                    default=False)
    # how block
    how_block_html_id = models.CharField("Идентификатор HTML",
                                         max_length=16,
                                         default='how-it-works')
    how_block_block_title = models.CharField("Заголовок блока 'How it works'",
                                             max_length=32,
                                             default="How it works")
    how_block_video = models.URLField("Ссылка на видео для блока 'How it works'")
    # subscribe block
    subscribe_block_html_id = models.CharField("Идентификатор HTML",
                                               max_length=16,
                                               default='subscribe')
    subscribe_block_title = models.CharField("Заголовок для блока 'Subscription'",
                                             max_length=64,
                                             default="Get the most latest news")
    # dicount
    discount_block_text = models.CharField("Заголовок 'Discount'",
                                           max_length=64,
                                           default='Discount for early investors')
    # login form text
    login_form_text = models.TextField("Текст формы входа",
                                       default="To pay for other types of crypto currency (BTC, ETC, LTC etc)\n"\
                                               "Please sign up or log in to your account")

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


class Partner(models.Model):
    config = models.ForeignKey(SiteConfiguration,
                               verbose_name="Настройки сайта",
                               related_name="partners")
    logo = models.ImageField("Логотип",
                             upload_to="partners")
    description = models.TextField("Описание",
                                   max_length=256)
    link = models.CharField("Ссылка",
                            max_length=128,
                            blank=True)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __unicode__(self):
        return self.description


class AnswerQuestion(models.Model):
    config = models.ForeignKey(SiteConfiguration,
                               verbose_name="Настройки сайта",
                               related_name="faq")
    question = models.CharField("Вопрос",
                                max_length=128)
    answer = models.TextField("Ответ")

    class Meta:
        verbose_name = "Вопрос-Ответ"
        verbose_name_plural = "Вопросы-Ответы"

    def __unicode__(self):
        return self.question


class Discount(models.Model):
    config = models.ForeignKey(SiteConfiguration,
                               verbose_name="Настройки сайта",
                               related_name="discounts")
    discount = models.CharField("Размер скидки",
                                max_length=5,
                                default="40%")
    discount_text = models.CharField("Текст к скидке",
                                     max_length=64,
                                     default="In the first 7 days")

    class Meta:
        verbose_name = "Скидка"
        verbose_name_plural = "Скидки"

    def __unicode__(self):
        return "{}: {}".format(self.discount, self.discount_text)
