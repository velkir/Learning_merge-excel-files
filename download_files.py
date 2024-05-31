import gdown

url = "https://drive.google.com/drive/folders/1J5UwgPlsUHIZ0729G9uk4HKpiJPSpMpE?usp=sharing"

gdown.download_folder(url, quiet=True, use_cookies=False)