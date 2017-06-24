#coding: utf-8
import urllib2
import json
import time
# 程序功能：爬百度知道上某一个用户所有的回答
# 4 * (2 - 1) 页码逻辑

uid = 'b6964069236f25705e79a626' #只有这个参数是需要填写的

p = 1
q_url = 'https://zhidao.baidu.com/question/%s'
msec = repr(time.time()).replace('.', '')

result_html  =  open('result_%s.html' % uid, 'w+')

total_cont = ''
while True:
	num = 4 * ( p - 1 )
	page_url = 'https://zhidao.baidu.com/ihome/api/myanswer?pn=%s&rn=4&t=%s&uid=%s&type=default' % (num, msec, uid)
	rep = urllib2.urlopen(page_url)
	json_cont = rep.read()
	cont = json.loads(json_cont)
	que_list = cont['data']['question']['list']

	if que_list:
		for i in que_list:
			total_cont += '<a href="%s">%s</a>' % (q_url % i['qid'], i['title']) + '<br />'
			total_cont += u'回答：%s' % i['replyContent'] + '<br />'
			total_cont += u'时间：%s' % i['finishTime'] + '<br /><br />'
	else:
		break

	p += 1

result_html.write(total_cont.encode('utf-8'))
result_html.close()