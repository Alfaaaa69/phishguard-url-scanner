from urllib.parse import urlparse
import re


def extract_basic_features(url):
    parsed = urlparse(url)

    hostname = parsed.hostname or ""
    path = parsed.path or ""

    features = {}

    # Panjang
    features["length_url"] = len(url)
    features["length_hostname"] = len(hostname)

    # Apakah hostname berupa IP address
    ip_pattern = r"^(?:\d{1,3}\.){3}\d{1,3}$"
    features["ip"] = 1 if re.match(ip_pattern, hostname) else 0

    # Hitung karakter tertentu
    features["nb_dots"] = url.count(".")
    features["nb_hyphens"] = url.count("-")
    features["nb_at"] = url.count("@")
    features["nb_qm"] = url.count("?")
    features["nb_and"] = url.count("&")
    features["nb_or"] = url.count("|")
    features["nb_eq"] = url.count("=")
    features["nb_underscore"] = url.count("_")
    features["nb_tilde"] = url.count("~")
    features["nb_percent"] = url.count("%")
    features["nb_slash"] = url.count("/")
    features["nb_star"] = url.count("*")
    features["nb_colon"] = url.count(":")
    features["nb_comma"] = url.count(",")
    features["nb_semicolumn"] = url.count(";")
    features["nb_dollar"] = url.count("$")
    features["nb_space"] = url.count(" ")

    # Token tertentu
    features["nb_www"] = url.lower().count("www")
    

    # Double slash setelah protocol
    temp_url = re.sub(r"^https?://", "", url.lower())
    features["nb_dslash"] = temp_url.count("//")

    # http / https token di path
    features["http_in_path"] = 1 if "http" in path.lower() else 0
    features["https_token"] = 0 if parsed.scheme.lower() == "https" else 1

    # Rasio digit
    digit_url = sum(char.isdigit() for char in url)
    features["ratio_digits_url"] = (
        digit_url / len(url) if len(url) > 0 else 0
    )

    digit_host = sum(char.isdigit() for char in hostname)
    features["ratio_digits_host"] = (
        digit_host / len(hostname) if len(hostname) > 0 else 0
    )

    # Punycode
    features["punycode"] = 1 if "xn--" in hostname.lower() else 0

    # Port eksplisit
    try:
        features["port"] = 1 if parsed.port is not None else 0
    except ValueError:
        features["port"] = 0

    # Jumlah subdomain sederhana
    parts = hostname.split(".")
    features["nb_subdomains"] = max(0, len(parts) - 2)

    # Prefix / suffix "-"
    features["prefix_suffix"] = 1 if "-" in hostname else 0

    return features


if __name__ == "__main__":
    test_url = "http://www.crestonwood.com/router.php"

    result = extract_basic_features(test_url)

    for key, value in result.items():
        print(f"{key}: {value}")