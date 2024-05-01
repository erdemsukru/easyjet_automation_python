Feature: Flight booking on Easyjet


  Scenario: Search cheapest ticket
    Given open easyjet on the browser
    When popup kapatilir
    When kalkis havalimanı secilir
    When inis havalimani secilir
    When seyahat tarihleri secilir
    When search butonuna basilir
    When en ucuzu secilir
    When standart fare secilir
    When gidis koltuk secimi atlanir
    When donus koltuk secimi atlanir
    When bagaj secimi atlanir
    When ekstra bagaj secimi reddedilir
    When bagaj secimi yeniden gecilir
    When araba kiralama gecilir
    When kullanici girisi yapilir
    When yolcu bilgileri girilir
    When ekstra hizmetler secilmeden devam edilir
    When ucus ozeti onaylanir
    Then odeme kismina gecilir
