import random
import string

def generate_password(length=12):
    # 指定密码中可以包含的字符，包括大小写字母、数字和特殊符号
    characters = string.ascii_letters + string.digits + string.punctuation
    # 随机选择字符并组合成密码
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 设置密码长度并生成密码
password_length = 12
random_password = generate_password(password_length)
print("生成的随机密码为:", random_password)