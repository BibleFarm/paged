from flask import *
from time import sleep
from flask_weasyprint import HTML, render_pdf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('ressources_pedagogiques.html')

@app.route("/ressources_pedagogiques")
def arduino():
    return render_template('ressources_pedagogiques.html')

@app.route("/arduino_serie")
def serie():
    return render_template('serie.html')

@app.route('/arduino_serie.pdf')
def serie_pdf():
    html = render_template('serie.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_parallele")
def parallele():
    return render_template('parallele.html')

@app.route('/arduino_parallele.pdf')
def parallele_pdf():
    html = render_template('parallele.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_led2boutons")
def led2boutons():
    return render_template('led_2_boutons.html')

@app.route('/arduino_led2boutons.pdf')
def led2boutons_pdf():
    html = render_template('led_2_boutons.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_potentiometre_4led")
def potentiometre4led():
    return render_template('potentiometre_4led.html')

@app.route('/arduino_potentiometre_4led.pdf')
def potentiometre4led_pdf():
    html = render_template('potentiometre_4led.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_piezo_buzzer")
def piezobuzzer():
    return render_template('piezo_buzzer.html')

@app.route('/arduino_piezo_buzzer.pdf')
def piezobuzzer_pdf():
    html = render_template('piezo_buzzer.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_theremine_lumineux")
def theremine():
    return render_template('theremine_lumineux.html')

@app.route('/arduino_theremine_lumineux.pdf')
def theremine_pdf():
    html = render_template('theremine_lumineux.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_clavier_sonore")
def clavier():
    return render_template('clavier_sonore.html')

@app.route('/arduino_clavier_sonore.pdf')
def clavier_pdf():
    html = render_template('clavier_sonore.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_capteur_vibration")
def vibration():
    return render_template('capteur_vibration.html')

@app.route('/arduino_capteur_vibration.pdf')
def vibration_pdf():
    html = render_template('capteur_vibration.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_potentiometre_servo")
def pot_servo():
    return render_template('potentiometre_servo.html')

@app.route('/arduino_potentiometre_servo.pdf')
def pot_servo_pdf():
    html = render_template('potentiometre_servo.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_moteur_cc")
def moteur_cc():
    return render_template('moteur_cc.html')

@app.route('/arduino_moteur_cc.pdf')
def moteur_cc_pdf():
    html = render_template('moteur_cc.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_pontenh")
def pont_h():
    return render_template('pont_en_h.html')

@app.route('/arduino_pontenh.pdf')
def pont_h_pdf():
    html = render_template('pont_en_h.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_ecran_lcd")
def ecran_lcd():
    return render_template('ecran_lcd.html')

@app.route('/arduino_ecran_lcd.pdf')
def ecran_lcd_pdf():
    html = render_template('ecran_lcd.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_station_meteo")
def station_meteo():
    return render_template('station_meteo.html')

@app.route('/arduino_station_meteo.pdf')
def station_meteo_pdf():
    html = render_template('station_meteo.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_bmp280")
def bmp280():
    return render_template('bmp280.html')

@app.route('/arduino_bmp280.pdf')
def bmp280_pdf():
    html = render_template('bmp280.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_shield_moteur1")
def shield_moteur1():
    return render_template('shield_moteur1.html')

@app.route('/arduino_shield_moteur1.pdf')
def shield_moteur1_pdf():
    html = render_template('shield_moteur1.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_shield_moteur2")
def shield_moteur2():
    return render_template('shield_moteur2.html')

@app.route('/arduino_shield_moteur2.pdf')
def shield_moteur2_pdf():
    html = render_template('shield_moteur2.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_datalogging_shield")
def datalogging():
    return render_template('datalogging_shield.html')

@app.route('/arduino_datalogging_shield.pdf')
def datalogging_pdf():
    html = render_template('datalogging_shield.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_processing1")
def processing1():
    return render_template('processing1.html')

@app.route('/arduino_processing1.pdf')
def processing1_pdf():
    html = render_template('processing1.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_processing2")
def processing2():
    return render_template('processing2.html')

@app.route('/arduino_processing2.pdf')
def processing2_pdf():
    html = render_template('processing2.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_firmata")
def firmata():
    return render_template('firmata.html')

@app.route('/arduino_firmata.pdf')
def firmata_pdf():
    html = render_template('firmata.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_serveur_web")
def serveur_web():
    return render_template('serveur_web.html')

@app.route('/arduino_serveur_web.pdf')
def serveur_web_pdf():
    html = render_template('serveur_web.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_serveur_meteo")
def serveur_meteo():
    return render_template('serveur_meteo.html')

@app.route('/arduino_serveur_meteo.pdf')
def serveur_meteo_pdf():
    html = render_template('serveur_meteo.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_flora_temperature")
def flora_temperature():
    return render_template('flora_temperature.html')

@app.route('/arduino_flora_temperature.pdf')
def flora_temperature_pdf():
    html = render_template('flora_temperature.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_flora_neopixel")
def flora_neopixel():
    return render_template('flora_neopixel.html')

@app.route('/arduino_flora_neopixel.pdf')
def flora_neopixel_pdf():
    html = render_template('flora_neopixel.html')
    return render_pdf(HTML(string=html))

@app.route("/arduino_flora_gps")
def flora_gps():
    return render_template('flora_gps.html')

@app.route('/arduino_flora_gps.pdf')
def flora_gps_pdf():
    html = render_template('flora_gps.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_raspbian")
def rpi_raspbian():
    return render_template('raspbian.html')

@app.route('/rpi_raspbian.pdf')
def rpi_raspbian_pdf():
    html = render_template('raspbian.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_samba")
def rpi_samba():
    return render_template('samba.html')

@app.route('/rpi_samba.pdf')
def rpi_samba_pdf():
    html = render_template('samba.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_ssh")
def rpi_ssh():
    return render_template('ssh.html')

@app.route('/rpi_ssh.pdf')
def rpi_ssh_pdf():
    html = render_template('ssh.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_demarrage")
def rpi_demarrage():
    return render_template('demarrage.html')

@app.route('/rpi_demarrage.pdf')
def rpi_demarrage_pdf():
    html = render_template('demarrage.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_video")
def rpi_video():
    return render_template('video.html')

@app.route('/rpi_video.pdf')
def rpi_video_pdf():
    html = render_template('video.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_mail")
def rpi_mail():
    return render_template('mail.html')

@app.route('/rpi_mail.pdf')
def rpi_mail_pdf():
    html = render_template('mail.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_wifi")
def rpi_wifi():
    return render_template('wifi.html')

@app.route('/rpi_wifi.pdf')
def rpi_wifi_pdf():
    html = render_template('wifi.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_led")
def rpi_led():
    return render_template('rpi_led.html')

@app.route('/rpi_led.pdf')
def rpi_led_pdf():
    html = render_template('rpi_led.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_servo")
def rpi_servo():
    return render_template('rpi_servo.html')

@app.route('/rpi_servo.pdf')
def rpi_servo_pdf():
    html = render_template('rpi_servo.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_piezo")
def rpi_piezo():
    return render_template('rpi_piezo.html')

@app.route('/rpi_piezo.pdf')
def rpi_piezo_pdf():
    html = render_template('rpi_piezo.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_moteurcc")
def rpi_moteurcc():
    return render_template('rpi_moteurcc.html')

@app.route('/rpi_moteurcc.pdf')
def rpi_moteurcc_pdf():
    html = render_template('rpi_moteurcc.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_app_moteurs")
def rpi_app_moteurs():
    return render_template('rpi_app_moteurs.html')

@app.route('/rpi_app_moteurs.pdf')
def rpi_app_moteurs_pdf():
    html = render_template('rpi_app_moteurs.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_tweeter")
def rpi_tweeter():
    return render_template('tweeter.html')

@app.route('/rpi_tweeter.pdf')
def rpi_tweeter_pdf():
    html = render_template('tweeter.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_bot_led")
def rpi_bot_led():
    return render_template('rpi_bot_led.html')

@app.route('/rpi_bot_led.pdf')
def rpi_bot_led_pdf():
    html = render_template('rpi_bot_led.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_bot_retweet")
def rpi_bot_retweet():
    return render_template('rpi_bot_retweet.html')

@app.route('/rpi_bot_retweet.pdf')
def rpi_bot_retweet_pdf():
    html = render_template('rpi_bot_retweet.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_tweets_json")
def rpi_tweets_json():
    return render_template('rpi_tweets_json.html')

@app.route('/rpi_tweets_json.pdf')
def rpi_tweets_json_pdf():
    html = render_template('rpi_tweets_json.html')
    return render_pdf(HTML(string=html))

@app.route("/rpi_tweets_book")
def rpi_tweets_book():
    return render_template('rpi_tweets_book.html')

@app.route('/rpi_tweets_book.pdf')
def rpi_tweets_book_pdf():
    html = render_template('rpi_tweets_book.html')
    return render_pdf(HTML(string=html))

@app.route("/cura")
def cura():
    return render_template('cura.html')

@app.route('/cura.pdf')
def cura_pdf():
    html = render_template('cura.html')
    return render_pdf(HTML(string=html))

@app.route("/repetier_host")
def repetier_host():
    return render_template('repetier_host.html')

@app.route('/repetier_host.pdf')
def repetier_host_pdf():
    html = render_template('repetier_host.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad01")
def freecad01():
    return render_template('freecad01.html')

@app.route('/freecad01.pdf')
def freecad01_pdf():
    html = render_template('freecad01.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad02")
def freecad02():
    return render_template('freecad02.html')

@app.route('/freecad02.pdf')
def freecad02_pdf():
    html = render_template('freecad02.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad03")
def freecad03():
    return render_template('freecad03.html')

@app.route('/freecad03.pdf')
def freecad03_pdf():
    html = render_template('freecad03.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad04")
def freecad04():
    return render_template('freecad04.html')

@app.route('/freecad04.pdf')
def freecad04_pdf():
    html = render_template('freecad04.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad05")
def freecad05():
    return render_template('freecad05.html')

@app.route('/freecad05.pdf')
def freecad05_pdf():
    html = render_template('freecad05.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad06")
def freecad06():
    return render_template('freecad06.html')

@app.route('/freecad06.pdf')
def freecad06_pdf():
    html = render_template('freecad06.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad07")
def freecad07():
    return render_template('freecad07.html')

@app.route('/freecad07.pdf')
def freecad07_pdf():
    html = render_template('freecad07.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad08")
def freecad08():
    return render_template('freecad08.html')

@app.route('/freecad08.pdf')
def freecad08_pdf():
    html = render_template('freecad08.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad09")
def freecad09():
    return render_template('freecad09.html')

@app.route('/freecad09.pdf')
def freecad09_pdf():
    html = render_template('freecad09.html')
    return render_pdf(HTML(string=html))

@app.route("/freecad10")
def freecad10():
    return render_template('freecad10.html')

@app.route('/freecad10.pdf')
def freecad10_pdf():
    html = render_template('freecad10.html')
    return render_pdf(HTML(string=html))

@app.route("/inkscape01")
def inkscape01():
    return render_template('inkscape01.html')

@app.route('/inkscape01.pdf')
def inkscape01_pdf():
    html = render_template('inkscape01.html')
    return render_pdf(HTML(string=html))

@app.route("/inkscape02")
def inkscape02():
    return render_template('inkscape02.html')

@app.route('/inkscape02.pdf')
def inkscape02_pdf():
    html = render_template('inkscape02.html')
    return render_pdf(HTML(string=html))

@app.route("/inkscape03")
def inkscape03():
    return render_template('inkscape03.html')

@app.route('/inkscape03.pdf')
def inkscape03_pdf():
    html = render_template('inkscape03.html')
    return render_pdf(HTML(string=html))

@app.route("/mach3")
def mach3():
    return render_template('mach3.html')

@app.route('/mach3.pdf')
def mach3_pdf():
    html = render_template('mach3.html')
    return render_pdf(HTML(string=html))

@app.route("/typo")
def typo():
    return render_template('typo.html')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
