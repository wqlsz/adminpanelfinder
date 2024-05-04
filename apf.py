from colorama import Fore
import colorama
import os
import time
import socket
import requests
from optparse import OptionParser
import threading
if os.name == "nt":
    os.system("cls")
elif os.name == "posix":
    os.system("clear")
colorama.init()
parser = OptionParser()
parser.add_option("-u", "--url", dest="link", help="Enter Target URL")
(options, args) = parser.parse_args()
if options.link is None:
    print(Fore.RED + "ERROR Please Enter a Target URL (example: python apf.py --url https://targeturl.com)")
else:
    adminext = [
    '/admin1.php', '/admin1.html', '/admin2.php', '/admin2.html', '/yonetim.php', '/wp-login.php', '/yonetim.html',
    '/yonetici.php', '/yonetici.html', '/ccms/', '/ccms/login.php', '/ccms/index.php', '/maintenance/', '/webmaster/',
    '/adm/', '/configuration/', '/configure/', '/websvn/', '/admin/', '/admin/account.php', '/admin/account.html',
    '/admin/index.php', '/admin/index.html', '/admin/login.php', '/admin/login.html', '/admin/home.php',
    '/admin/controlpanel.html', '/admin/controlpanel.php', '/admin.php', '/admin.html', '/admin/cp.php', '/admin/cp.html',
    '/cp.php', '/cp.html', '/administrator/', '/administrator/index.html', '/administrator/index.php',
    '/administrator/login.html', '/administrator/login.php', '/administrator/account.html', '/administrator/account.php',
    '/administrator.php', '/administrator.html', '/login.php', '/login.html', '/modelsearch/login.php', '/moderator.php',
    '/moderator.html', '/moderator/login.php', '/moderator/login.html', '/moderator/admin.php', '/moderator/admin.html',
    '/moderator/', '/account.php', '/account.html', '/controlpanel/', '/controlpanel.php', '/controlpanel.html',
    '/admincontrol.php', '/admincontrol.html', '/adminpanel.php', '/adminpanel.html', '/admin1.asp', '/admin2.asp',
    '/yonetim.asp', '/yonetici.asp', '/admin/account.asp', '/admin/index.asp', '/admin/login.asp', '/admin/home.asp',
    '/admin/controlpanel.asp', '/admin.asp', '/admin/cp.asp', '/cp.asp', '/administrator/index.asp', '/administrator/login.asp',
    '/administrator/account.asp', '/administrator.asp', '/login.asp', '/modelsearch/login.asp', '/moderator.asp',
    '/moderator/login.asp', '/moderator/admin.asp', '/account.asp', '/controlpanel.asp', '/admincontrol.asp', '/adminpanel.asp',
    '/fileadmin/', '/fileadmin.php', '/fileadmin.asp', '/fileadmin.html', '/administration/', '/administration.php',
    '/administration.html', '/sysadmin.php', '/sysadmin.html', '/phpmyadmin/', '/myadmin/', '/sysadmin.asp', '/sysadmin/',
    '/ur-admin.asp', '/ur-admin.php', '/ur-admin.html', '/ur-admin/', '/Server.php', '/Server.html', '/Server.asp',
    '/Server/', '/wp-admin/', '/administr8.php', '/administr8.html', '/administr8/', '/administr8.asp', '/webadmin/',
    '/webadmin.php', '/webadmin.asp', '/webadmin.html', '/administratie/', '/admins/', '/admins.php', '/admins.asp',
    '/admins.html', '/administrivia/', '/Database_Administration/', '/WebAdmin/', '/useradmin/', '/sysadmins/',
    '/admin1/', '/system-administration/', '/administrators/', '/pgadmin/', '/directadmin/', '/staradmin/',
    '/ServerAdministrator/', '/SysAdmin/', '/administer/', '/LiveUser_Admin/', '/sys-admin/', '/typo3/', '/panel/',
    '/cpanel/', '/cPanel/', '/cpanel_file/', '/platz_login/', '/rcLogin/', '/blogindex/', '/formslogin/', '/autologin/',
    '/support_login/', '/meta_login/', '/manuallogin/', '/simpleLogin/', '/loginflat/', '/utility_login/', '/showlogin/',
    '/memlogin/', '/members/', '/login-redirect/', '/sub-login/', '/ogin1/', '/dir-login/', '/login_db/', '/xlogin/',
    '/smblogin/', '/customer_login/', '/UserLogin/', '/login-us/', '/acct_login/', '/admin_area/', '/bigadmin/',
    '/project-admins/', '/phppgadmin/', '/pureadmin/', '/sql-admin/', '/radmind/', '/openvpnadmin/', '/wizmysqladmin/',
    '/vadmind/', '/ezsqliteadmin/', '/hpwebjetadmin/', '/newsadmin/', '/adminpro/', '/Lotus_Domino_Admin/',
    '/admin_index.asp', '/admin_index.php', '/user.php', '/user.asp'
]
    print(f"{Fore.CYAN}------------------------THE PROCESS HAS BEEN STARTED------------------------")
    baslangic = time.time()
    semaphore = threading.Semaphore(30)
    def check_admin_path(url, admin_path):
        global baslangic
        try:
            with semaphore:
                p = url + admin_path
                getcode = requests.get(p).status_code
                if getcode == 404:
                    pass
                elif getcode == 200:
                    print(f"{Fore.GREEN}FOUND -> {p} {getcode}")
        except requests.RequestException as e:
            print(f"{Fore.RED}ERROR! Request Exception: {e}")
    threads = []
    for i in adminext:
        t = threading.Thread(target=check_admin_path, args=(options.link, i))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    print(f"{Fore.CYAN}------------------------Completed--------------------------------------------")
    bitis = time.time()
    sure = bitis - baslangic
    print(f"\n{Fore.YELLOW}The process took {sure}s")
