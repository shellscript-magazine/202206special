import network

SSID = 'SSID'
PASSWORD = 'パスワード'

wlan_if = network.WLAN(network.STA_IF)
wlan_if.active(True)
wlan_if.connect(SSID, PASSWORD)
