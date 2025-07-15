#!/usr/bin/env python3
import os
import subprocess
import sys

def generate_debug_keystore(project_path):
    """为指定项目生成调试密钥库"""
    app_dir = os.path.join(project_path, 'app')
    keystore_path = os.path.join(app_dir, 'debug.keystore')
    
    # 如果密钥库已存在，跳过
    if os.path.exists(keystore_path):
        print(f"密钥库已存在: {keystore_path}")
        return
    
    # 生成调试密钥库
    cmd = [
        'keytool', '-genkey', '-v',
        '-keystore', 'debug.keystore',
        '-storepass', 'android',
        '-alias', 'androiddebugkey',
        '-keypass', 'android',
        '-keyalg', 'RSA',
        '-keysize', '2048',
        '-validity', '10000',
        '-dname', 'CN=Android Debug,O=Android,C=US'
    ]
    
    try:
        subprocess.run(cmd, cwd=app_dir, check=True)
        print(f"已生成调试密钥库: {keystore_path}")
    except subprocess.CalledProcessError as e:
        print(f"生成密钥库失败 {project_path}: {e}")
    except FileNotFoundError:
        print("未找到 keytool 命令，请确保已安装 JDK")

def main():
    """主函数"""
    android_projects = [
        'clipboard/android',
        'geolocation/android', 
        'getusermedia/android',
        'permissions/android',
        'share/android',
        'template/android'
    ]
    
    for project in android_projects:
        if os.path.exists(project):
            print(f"\n处理项目: {project}")
            generate_debug_keystore(project)

if __name__ == "__main__":
    main() 