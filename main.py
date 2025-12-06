import random
import string

def generate_password(length=12):
    """
    生成一个指定长度的强密码
    包含：大写字母、小写字母、数字、特殊符号
    """
    # 1. 定义密码可以用哪些字符
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # 2. 随机选择字符并组合
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("--- 欢迎使用强密码生成器 ---")
    
    while True:
        try:
            # 获取用户输入
            user_input = input("\n请输入你想要的密码长度 (输入 q 退出): ")
            
            # 如果输入 q 则退出程序
            if user_input.lower() == 'q':
                print("程序已退出，再见！")
                break
            
            # 转换输入为数字
            length = int(user_input)
            
            if length < 6:
                print("建议密码长度至少为 6 位哦！")
                continue
                
            # 生成并显示密码
            pwd = generate_password(length)
            print(f"✅ 你的新密码是: {pwd}")
            print("---------------------------")
            
        except ValueError:
            print("❌ 错误：请输入纯数字！")

# 运行主程序
if __name__ == "__main__":
    main()
