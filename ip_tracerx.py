import requests
from colorama import Fore, Style

banner = f"""
{Fore.CYAN}
   _____ ___      ___________                      
  |_   _/ _ \\    / /_  /_  /                      
    | || (_) |  / / / /_/ /                       
    |_| \\___/  /_/ /___/___/   IP TRACER X v2      

{Fore.YELLOW}   Developer : Cibetivist
   Team      : Garuda Cyber Team
{Style.RESET_ALL}
"""
print(banner)


def ip_api_lookup(ip):
    url = f"http://ip-api.com/json/{ip}?fields=66846719"
    return requests.get(url).json()


def ipinfo_lookup(ip):
    try:
        url = f"https://ipinfo.io/{ip}/privacy"
        return requests.get(url).json()
    except:
        return None


def display_result(ip):
    print(Fore.YELLOW + f"\nMenganalisis IP: {ip}" + Style.RESET_ALL)

    data1 = ip_api_lookup(ip)
    data2 = ipinfo_lookup(ip)

    if data1.get("status") != "success":
        print(Fore.RED + "IP tidak ditemukan / invalid." + Style.RESET_ALL)
        return

    print(Fore.GREEN + "\n=== INFORMASI DASAR IP (IP-API) ===" + Style.RESET_ALL)
    for key, val in data1.items():
        print(f"{Fore.CYAN}{key}{Style.RESET_ALL}: {val}")

    print(Fore.MAGENTA + "\n=== ADVANCED PRIVACY CHECK ===" + Style.RESET_ALL)

    proxy_basic = {
        "proxy": data1.get("proxy"),
        "mobile": data1.get("mobile"),
        "hosting": data1.get("hosting")
    }

    print(Fore.CYAN + "From IP-API:" + Style.RESET_ALL)
    print(proxy_basic)

    if data2:
        print(Fore.CYAN + "\nFrom ipinfo.io:" + Style.RESET_ALL)
        print(data2)

        is_vpn = data2.get("vpn")
        is_proxy = data2.get("proxy")
        is_tor = data2.get("tor")

        print(Fore.YELLOW + "\nKesimpulan Privasi:" + Style.RESET_ALL)
        if is_vpn or data1.get("hosting"):
            print(Fore.RED + "⚠ IP kemungkinan VPN/Hosting" + Style.RESET_ALL)
        elif is_proxy:
            print(Fore.RED + "⚠ IP kemungkinan Proxy" + Style.RESET_ALL)
        elif is_tor:
            print(Fore.RED + "⚠ IP adalah Node TOR" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "✔ IP ini tampaknya normal (tidak pakai VPN/Proxy)" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Gagal cek ipinfo.io, lanjut." + Style.RESET_ALL)

    lat = data1.get("lat")
    lon = data1.get("lon")

    print(Fore.GREEN + "\n=== MAP COORDINATE ===" + Style.RESET_ALL)
    print(f"Latitude: {lat}")
    print(f"Longitude: {lon}")

    map_link = f"https://www.google.com/maps?q={lat},{lon}"
    print(Fore.CYAN + f"\nGoogle Maps Link:\n{map_link}" + Style.RESET_ALL)

    try:
        static_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom=10&size=600x300&markers=color:red%7C{lat},{lon}"
        print(Fore.YELLOW + "\nStatic Map Link:" + Style.RESET_ALL)
        print(static_map_url)
    except:
        pass


if __name__ == "__main__":
    ip = input(Fore.YELLOW + "Masukkan IP: " + Style.RESET_ALL)
    display_result(ip)
