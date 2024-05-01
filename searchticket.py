from behave import given
from behave import when
from behave import then



@given(u'open easyjet on the browser')
def step_impl(context):
   print("Inside - open easyjet on the browser")


@when(u'popup kapatilir')
def step_impl(context):
    print("Inside - popup kapatilir")


@when(u'kalkis havalimanı secilir')
def step_impl(context):
    print("Inside - kalkis havalimanı secilir")


@when(u'inis havalimani secilir')
def step_impl(context):
    print("Inside - inis havalimani secilir")


@when(u'seyahat tarihleri secilir')
def step_impl(context):
    print("Inside - seyahat tarihleri secilir")


@when(u'search butonuna basilir')
def step_impl(context):
    print("Inside - search butonuna basilir")


@when(u'en ucuzu secilir')
def step_impl(context):
    print("Inside - en ucuzu secilir")


@when(u'standart fare secilir')
def step_impl(context):
    print("Inside - standart fare secilir")


@when(u'gidis koltuk secimi atlanir')
def step_impl(context):
    print("Inside - gidis koltuk secimi atlanir")


@when(u'donus koltuk secimi atlanir')
def step_impl(context):
    print("Inside - donus koltuk secimi atlanir")


@when(u'bagaj secimi atlanir')
def step_impl(context):
    print("Inside - bagaj secimi atlanir")


@when(u'ekstra bagaj secimi reddedilir')
def step_impl(context):
    print("Inside - ekstra bagaj secimi reddedilir")


@when(u'bagaj secimi yeniden gecilir')
def step_impl(context):
    print("Inside - bagaj secimi yeniden gecilir")


@when(u'araba kiralama gecilir')
def step_impl(context):
    print("Inside - araba kiralama gecilir")


@when(u'kullanici girisi yapilir')
def step_impl(context):
    print("Inside -kullanici girisi yapilir")


@when(u'yolcu bilgileri girilir')
def step_impl(context):
    print("Inside - yolcu bilgileri girilir")


@when(u'ekstra hizmetler secilmeden devam edilir')
def step_impl(context):
    print("Inside - ekstra hizmetler secilmeden devam edilir")


@when(u'ucus ozeti onaylanir')
def step_impl(context):
    print("Inside - ucus ozeti onaylanir")


@then(u'odeme kismina gecilir')
def step_impl(context):
    print("Inside - odeme kismina gecilir")