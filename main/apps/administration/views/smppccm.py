from django.shortcuts import render_to_response, HttpResponseRedirect, render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import user_passes_test
import json
from main.apps.core.smpp import TelnetConnection, SMPPCCM

@user_passes_test(lambda u: u.is_superuser)
def smppccm_view(request):
	args = {}
	return render(request, 'administration/smppccm.html', args)

@user_passes_test(lambda u: u.is_superuser)
def smppccm_view_manage(request):
	args = {}
	if request.POST:
		service = request.POST.get("s", None)
		if service == "list":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			args = smppccm.list()
		elif service == "add":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			smppccm.create(data={
				"cid": request.POST.get("cid"),
				"host": request.POST.get("host"),
				"port": request.POST.get("port"),
				"username": request.POST.get("username"),
				"password": request.POST.get("password"),
			})
		elif service == "edit":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			smppccm.partial_update(data={
				"cid": request.POST.get("cid"),
				"logfile": request.POST.get("logfile", "/var/log/jasmin/default-%s.log" % request.POST.get("cid")),
				"logrotate": request.POST.get("logrotate", "midnight"),
				"loglevel": request.POST.get("loglevel", "20"),
				"host": request.POST.get("host", "127.0.0.1"),
				"port": request.POST.get("port", "2775"),
				"ssl": request.POST.get("ssl", "no"),
				"username": request.POST.get("username", "smppclient"),
				"password": request.POST.get("password", "password"),
				"bind": request.POST.get("bind", "transceiver"),
				"bind_to": request.POST.get("bind_to", "30"),
				"trx_to": request.POST.get("trx_to", "300"),
				"res_to": request.POST.get("res_to", "60"),
				"pdu_red_to": request.POST.get("pdu_red_to", "10"),
				"con_loss_retry": request.POST.get("con_loss_retry", "yes"),
				"con_loss_delay": request.POST.get("con_loss_delay", "10"),
				"con_fail_retry": request.POST.get("con_fail_retry", "yes"),
				"con_fail_delay": request.POST.get("con_fail_delay", "10"),
				"src_addr": request.POST.get("src_addr", ""),
				"src_ton": request.POST.get("src_ton", "2"),
				"src_npi": request.POST.get("src_npi", "1"),
				"dst_ton": request.POST.get("dst_ton", "1"),
				"dst_npi": request.POST.get("dst_npi", "1"),
				"bind_ton": request.POST.get("bind_ton", "0"),
				"bind_npi": request.POST.get("bind_npi", "1"),
				"validity": request.POST.get("validity", ""),
				"priority": request.POST.get("priority", "0"),
				"requeue_delay": request.POST.get("requeue_delay", "120"),
				"addr_range": request.POST.get("addr_range", ""),
				"systype": request.POST.get("systype", ""),
				"dlr_expiry": request.POST.get("dlr_expiry", "86400"),
				"submit_throughput": request.POST.get("submit_throughput", "1"),
				"proto_id": request.POST.get("proto_id", ""),
				"coding": request.POST.get("coding", "0"),
				"elink_interval": request.POST.get("elink_interval", "30"),
				"def_msg_id": request.POST.get("def_msg_id", "0"),
				"ripf": request.POST.get("ripf", "0"),
				"dlr_msgid": request.POST.get("dlr_msgid", "0"),
			}, cid=request.POST.get("cid"))
		elif service == "delete":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			args = smppccm.destroy(cid=request.POST.get("cid"))
		elif service == "start":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			args = smppccm.start(cid=request.POST.get("cid"))
		elif service == "stop":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			args = smppccm.stop(cid=request.POST.get("cid"))
		elif service == "restart":
			tc = TelnetConnection()
			smppccm = SMPPCCM(telnet=tc.telnet)
			args = smppccm.stop(cid=request.POST.get("cid"))
			args = smppccm.start(cid=request.POST.get("cid"))
	return HttpResponse(json.dumps(args), content_type='application/json')
