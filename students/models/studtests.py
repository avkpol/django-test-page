# -*- coding: utf-8 -*-from django.db import models# Create your models here.class Studtest(models.Model):	'''Studexam Model'''	class Meta(object):		verbose_name= u"Іспити"		verbose_name_plural=u"Іспити"	subject = models.CharField(		max_length=256,		blank= False,		verbose_name=u"Назва предмету")	exam_time = models.CharField(		max_length=256,		blank= False,		verbose_name=u"Дата проведення")	tutor =models.CharField(		max_length=256,		blank=False,		verbose_name= u"Прізвищв викладача")	notes =models.TextField(		blank=True,		verbose_name=u"Нот")		def __unicode__(self):		return u"%s %s" % (self.first_name, self.last_name)